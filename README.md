# H1D023099-PraktikumKB-Pertemuan4

# Sistem Pakar Rekomendasi Outfit Harian 👗🧥👕

Aplikasi sistem pakar yang memberikan rekomendasi outfit harian berdasarkan cuaca, agenda kegiatan, dan preferensi pengguna.

## 📌 Deskripsi

Proyek ini menggabungkan kecerdasan buatan berbasis aturan (rule-based expert system) dengan antarmuka pengguna untuk membantu pengguna memilih pakaian yang sesuai kondisi harian. Sistem ini mempertimbangkan faktor-faktor seperti kondisi cuaca, jenis agenda (formal/non-formal), dan preferensi gaya pengguna.

## 📁 Struktur File

sistem-pakar-outfit/
├── main.py                  # File utama untuk menjalankan aplikasi
├── knowledge_base.py        # Basis pengetahuan dalam Python
├── outfit_kb.pl             # Basis pengetahuan dalam format Prolog
├── recommendation_engine.py # Mesin inferensi dan logika rekomendasi
├── ui_components.py         # Komponen antarmuka pengguna
├── prolog_bridge.py         # Penghubung antara Python dan Prolog (jika digunakan)
└── README.md                # Dokumentasi proyek ini

## 🚀 Fitur Utama

- Rekomendasi outfit berdasarkan cuaca (panas, hangat, dingin, hujan)
- Rekomendasi sesuai agenda (formal, casual, olahraga)
- Preferensi style (maskulin, feminin, atau netral)
- Pertimbangan khusus (modest/tertutup)
- Rekomendasi warna sesuai musim
- Tips khusus berdasarkan cuaca dan agenda

## Cara Menjalankan

1. Pastikan semua file berada dalam satu direktori
2. Jalankan file utama:
```bash
python main.py
```

## Struktur Sistem Pakar

Sistem ini mengikuti struktur sistem pakar dengan:
1. Basis Pengetahuan - Data tentang pakaian dan aturan pencocokan
2. Mesin Inferensi - Logika yang menentukan rekomendasi berdasarkan input
3. Antarmuka Pengguna - Tampilan untuk berinteraksi dengan sistem

## Lisensi

Aplikasi ini tersedia secara bebas untuk tujuan pendidikan dan pengembangan pribadi.
