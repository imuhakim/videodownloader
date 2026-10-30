"""Video Downloader - muat turun video YouTube dan Facebook sebagai MP3, MP4 atau MPEG."""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import webbrowser
from urllib.parse import urlparse

from flask import Flask, after_this_request, jsonify, render_template, request, send_file
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from yt_dlp.version import __version__ as ENGINE_VERSION

app = Flask(__name__)

FORMATS = {"mp3", "mp4", "mpeg"}
MP4_QUALITIES = {"best", "1080", "720", "480", "360"}
SUPPORTED_HOSTS = (
    "youtube.com", "youtu.be",                     # YouTube
    "facebook.com", "fb.watch", "fb.com", "fb.gg",  # Facebook
)
INVALID_URL = "Sila masukkan pautan YouTube atau Facebook yang sah."


def is_supported_url(url: str) -> bool:
    if not re.match(r"^https?://", url, re.I):
        url = "https://" + url
    try:
        parsed = urlparse(url)
    except ValueError:
        return False
    host = (parsed.hostname or "").lower()
    return any(host == h or host.endswith("." + h) for h in SUPPORTED_HOSTS)


def safe_name(title: str) -> str:
    name = re.sub(r'[\\/:*?"<>|\r\n]+', "", title).strip()
    return name[:120] or "video"


def ydl_opts(fmt: str, quality: str, outdir: str) -> dict:
    opts = {
        "outtmpl": os.path.join(outdir, "%(id)s.%(ext)s"),
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
    }
    if fmt == "mp3":
        opts["format"] = "bestaudio/best"
        opts["postprocessors"] = [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
    else:
        height = "" if quality == "best" else f"[height<={quality}]"
        opts["format"] = (
            f"bestvideo{height}[ext=mp4]+bestaudio[ext=m4a]/"
            f"bestvideo{height}+bestaudio/best{height}/best"
        )
        opts["merge_output_format"] = "mp4"
    return opts


def to_mpeg(src: str, dst: str) -> None:
    """Tukar fail video ke MPEG-2 (.mpeg) menggunakan ffmpeg."""
    subprocess.run(
        ["ffmpeg", "-y", "-i", src,
         "-c:v", "mpeg2video", "-q:v", "3",
         "-c:a", "mp2", "-b:a", "192k",
         "-f", "mpeg", dst],
        check=True, capture_output=True,
    )


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/version")
def version():
    return jsonify(version=ENGINE_VERSION)


@app.post("/api/update")
def update():
    """Kemas kini enjin muat turun ke versi terbaru."""
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-U", "yt-dlp"],
            check=True, capture_output=True, timeout=300,
        )
        out = subprocess.run(
            [sys.executable, "-c", "from yt_dlp.version import __version__; print(__version__)"],
            check=True, capture_output=True, text=True,
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return jsonify(error="Kemas kini gagal. Pastikan internet berfungsi dan cuba lagi."), 500
    new_version = out.stdout.strip()
    return jsonify(old=ENGINE_VERSION, new=new_version, restart=new_version != ENGINE_VERSION)


@app.post("/api/info")
def info():
    url = (request.json or {}).get("url", "").strip()
    if not is_supported_url(url):
        return jsonify(error=INVALID_URL), 400
    try:
        with YoutubeDL({"quiet": True, "noplaylist": True, "skip_download": True}) as ydl:
            data = ydl.extract_info(url, download=False)
    except DownloadError as e:
        return jsonify(error=f"Gagal dapatkan maklumat video: {e}"), 400
    return jsonify(
        title=data.get("title"),
        channel=data.get("uploader"),
        duration=data.get("duration"),
        thumbnail=data.get("thumbnail"),
    )


@app.post("/api/download")
def download():
    url = request.form.get("url", "").strip()
    fmt = request.form.get("format", "mp4").lower()
    quality = request.form.get("quality", "best")

    if not is_supported_url(url):
        return jsonify(error=INVALID_URL), 400
    if fmt not in FORMATS:
        return jsonify(error="Format tidak disokong."), 400
    if quality not in MP4_QUALITIES:
        quality = "best"

    workdir = tempfile.mkdtemp(prefix="ytdl-")

    @after_this_request
    def cleanup(response):
        response.call_on_close(lambda: shutil.rmtree(workdir, ignore_errors=True))
        return response

    try:
        with YoutubeDL(ydl_opts(fmt, quality, workdir)) as ydl:
            data = ydl.extract_info(url, download=True)
    except DownloadError as e:
        shutil.rmtree(workdir, ignore_errors=True)
        return jsonify(error=f"Muat turun gagal: {e}"), 500

    vid = data["id"]
    if fmt == "mp3":
        path = os.path.join(workdir, f"{vid}.mp3")
    else:
        path = os.path.join(workdir, f"{vid}.mp4")
        if fmt == "mpeg":
            mpeg_path = os.path.join(workdir, f"{vid}.mpeg")
            try:
                to_mpeg(path, mpeg_path)
            except subprocess.CalledProcessError:
                return jsonify(error="Gagal tukar ke format MPEG."), 500
            path = mpeg_path

    if not os.path.exists(path):
        return jsonify(error="Fail output tidak dijumpai."), 500

    mimetypes = {"mp3": "audio/mpeg", "mp4": "video/mp4", "mpeg": "video/mpeg"}
    return send_file(
        path,
        mimetype=mimetypes[fmt],
        as_attachment=True,
        download_name=f"{safe_name(data.get('title', vid))}.{fmt}",
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    url = f"http://127.0.0.1:{port}"
    if not shutil.which("ffmpeg"):
        print("AMARAN: ffmpeg tidak dijumpai. MP3 dan MPEG perlukan ffmpeg.")
    print(f"Video Downloader berjalan di {url}  (tekan Ctrl+C untuk berhenti)")
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    app.run(host="127.0.0.1", port=port, debug=False)
