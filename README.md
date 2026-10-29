# YT Downloader

App ringkas yang berjalan di komputer anda sendiri untuk muat turun video YouTube dalam format **MP3**, **MP4** atau **MPEG**.

- **MP3**: audio sahaja, 192 kbps
- **MP4**: video + audio, pilih kualiti (Terbaik / 1080p / 720p / 480p / 360p)
- **MPEG**: video ditukar ke MPEG-2 (`.mpeg`)

## Keperluan (pasang sekali sahaja)

1. **Python 3.10+**: https://www.python.org/downloads/ (Windows: tandakan "Add Python to PATH")
2. **ffmpeg**:
   - Windows: `winget install ffmpeg`
   - macOS: `brew install ffmpeg`
   - Linux: `sudo apt install ffmpeg`

## Cara guna

- **Windows**: klik dua kali `run.bat`
- **macOS / Linux**: jalankan `./run.sh` dalam Terminal

Kali pertama ia akan pasang pakej yang diperlukan. Lepas tu browser akan buka http://127.0.0.1:5000 secara automatik. Tampal pautan YouTube, pilih format dan tekan **Muat Turun**.

App ni hanya boleh diakses dari komputer anda sendiri (127.0.0.1). Untuk berhenti, tutup tetingkap terminal atau tekan Ctrl+C.

## Masalah?

- Muat turun gagal: tekan butang **Kemas Kini** di bawah halaman app, kemudian tutup dan buka semula app. YouTube kerap ubah sistemnya, jadi app perlu dikemas kini sekali-sekala.
- "ffmpeg tidak dijumpai": pasang ffmpeg (lihat di atas), kemudian buka semula terminal.

Gunakan hanya untuk kandungan yang anda ada hak untuk muat turun.
