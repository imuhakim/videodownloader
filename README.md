# Video Downloader

App ringkas yang berjalan di komputer anda sendiri untuk muat turun video **YouTube** dan **Facebook** dalam format **MP3**, **MP4** atau **MPEG**.

| Format | Hasil |
|---|---|
| **MP3** | Audio sahaja (192 kbps) |
| **MP4** | Video + audio. Pilih kualiti: Terbaik / 1080p / 720p / 480p / 360p |
| **MPEG** | Video MPEG-2 (`.mpeg`) untuk pemain atau peranti lama |

---

## Panduan Langkah demi Langkah (Windows)

### Langkah 1: Pasang Python (sekali sahaja)

1. Tekan butang **Windows**, taip `cmd`, kemudian tekan **Enter**. Satu tetingkap hitam (Command Prompt) akan terbuka.
2. Salin dan tampal arahan ini (klik kanan untuk tampal), kemudian tekan **Enter**:
   ```
   winget install Python.Python.3.12
   ```
3. Tunggu sehingga siap. Jika ditanya `Do you agree...`, taip `Y` dan tekan **Enter**.

> Cara lain: muat turun dari https://www.python.org/downloads/. Semasa memasang, **WAJIB tandakan kotak "Add Python to PATH"** di skrin pertama.

### Langkah 2: Pasang ffmpeg (sekali sahaja)

ffmpeg diperlukan untuk menukar video ke MP3 dan MPEG.

1. Dalam tetingkap hitam yang sama, taip:
   ```
   winget install Gyan.FFmpeg
   ```
2. Tunggu sehingga siap.
3. **Tutup** tetingkap hitam tersebut. Ini penting supaya Windows kenal Python dan ffmpeg yang baru dipasang.

### Langkah 3: Semak pemasangan (pilihan)

Buka semula Command Prompt (lihat Langkah 1.1), kemudian taip satu demi satu:
```
python --version
```
```
ffmpeg -version
```
Jika keluar nombor versi (contoh `Python 3.12.7`), pemasangan berjaya.
Jika keluar `is not recognized`, ulang langkah pemasangan untuk program tersebut, atau restart komputer.

### Langkah 4: Muat turun app ini

1. Di bahagian atas halaman GitHub ini, klik butang hijau **`<> Code`**.
2. Klik **Download ZIP**.
3. Buka folder **Downloads**. Klik kanan fail **`videodownloader-main.zip`**, pilih **Extract All...**, kemudian klik **Extract**.
4. Folder **`videodownloader-main`** akan terbuka. Boleh pindahkan folder ini ke mana-mana (contoh: Desktop).

### Langkah 5: Jalankan app

1. Dalam folder `videodownloader-main`, klik dua kali fail **`run.bat`**.
2. Kali pertama, app akan memasang pakej yang diperlukan (1–2 minit, perlukan internet). Tunggu sahaja.
3. Browser akan terbuka secara automatik di **http://127.0.0.1:5000**.

> Jika Windows papar amaran **"Windows protected your PC"**, klik **More info**, kemudian **Run anyway**.
>
> **Jangan tutup** tetingkap hitam selagi anda masih menggunakan app.

### Langkah 6: Muat turun video

1. Salin link video dari YouTube atau Facebook (butang **Share**, kemudian **Copy link**).
2. Tampal link dalam kotak **Pautan YouTube atau Facebook**. Tajuk dan gambar video akan muncul.
3. Pilih format: **MP3**, **MP4** atau **MPEG**. Untuk MP4/MPEG, pilih juga kualiti video.
4. Klik **Muat Turun**, kemudian tunggu. Video panjang atau format MPEG mengambil masa lebih lama.
5. Fail akan disimpan dalam folder **Downloads**.

### Langkah 7: Tutup app

Pergi ke tetingkap hitam, kemudian tekan **Ctrl + C** atau klik **X** untuk menutupnya.

Untuk guna semula lain kali, ulang **Langkah 5** sahaja.

---

## Kemas kini

**Jika muat turun mula gagal** (YouTube dan Facebook kerap ubah sistem mereka):
1. Di bawah halaman app, tekan butang **Kemas Kini**.
2. Tutup app (Langkah 7), kemudian buka semula (Langkah 5).

**Untuk dapatkan versi app terbaru dari GitHub:**
1. Tutup app.
2. Ulang **Langkah 4** (muat turun ZIP baru) dan gantikan folder lama.

---

## Masalah biasa

| Masalah | Penyelesaian |
|---|---|
| `'python' is not recognized` atau Microsoft Store terbuka | Python belum dipasang dengan betul. Ulang Langkah 1, tutup dan buka semula tetingkap hitam. |
| `ffmpeg tidak dijumpai` | Ulang Langkah 2, kemudian tutup tetingkap hitam dan buka semula app. |
| Browser papar app lain / "Address already in use" | Ada app lain sedang guna port 5000. Tutup app lain itu (cari tetingkap hitamnya, atau Task Manager, kemudian **Python**, kemudian **End task**). |
| "This site can't be reached" | App belum berjalan. Klik dua kali `run.bat` dan jangan tutup tetingkap hitam. |
| Video Facebook gagal | Hanya video **awam (public)** disokong. Video private atau dari group tertutup tidak boleh dimuat turun. |
| Muat turun gagal | Tekan butang **Kemas Kini** (lihat bahagian Kemas kini). |

---

## macOS / Linux

1. Pasang Python 3.10+ dan ffmpeg:
   - macOS: `brew install python ffmpeg`
   - Ubuntu/Debian: `sudo apt install python3 python3-venv ffmpeg`
2. Muat turun dan extract ZIP (Langkah 4).
3. Dalam Terminal, masuk ke folder tersebut dan jalankan:
   ```
   ./run.sh
   ```
4. Browser akan buka http://127.0.0.1:5000.

---

## Nota

- App ini hanya berjalan di komputer anda sendiri (127.0.0.1). Orang lain tidak boleh mengaksesnya.
- Gunakan hanya untuk kandungan yang anda ada hak untuk muat turun.
