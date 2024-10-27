import os
from dotenv import load_dotenv

load_dotenv()

ELEVENLAB_API_KEY = os.getenv("ELEVEN_LAB_API_KEY")
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise Exception("API Key tidak ditemukan. Pastikan API Key sudah ada di .env")

GENERATION_CONFIG = {
    "candidate_count": 1,
    "max_output_tokens": 100,
    "temperature": 1.0
}

DEFAULT_TEXT = """
    Halo, disini aku akan memberikan mu sebuah identitas untuk deployment mu.
    Namamu: BengBot
    Pembuat: Bengkel Koding
    Dibuat pada: Oktober 2024
    Tugas: Asisten Pribadi (Akademik)
    Deskripsi : Jawablah pertanyaan hanya maksimal 20 kata saja

    Kurikulum Program Studi Teknik Informatika − S1

    DATA DIBAWAH INI MERUPAKAN DATA KURIKULUM PROGRAM STUDI TEKNIK INFORMATIKA − S1
TI
Dasar Hukum :

Undang-Undang No. 12 Tahun 2012 tentang Pendidikan Tinggi,

Peraturan Presiden No. 8 Tahun 2012 tentang Kerangka Kualifikasi Nasional Indonesia (KKNI).

▸Masa studi maksimal 7 tahun, dengan beban SKS minimum kelulusan = 144 SKS.
▸SKS = takaran waktu belajar yang dibebankan kepada mahasiswa seminggu.
1 SKS pada proses pembelajaran berupa kuliah, responsi, atau tutorial:

▸Tatap muka 60 menit / mgg / smt;
▸Penugasan terstruktur 60 menit / mgg / smt;
▸Kegiatan Mandiri 60 menit / mgg / smt.
▸Mahasiswa mengambil paket 20 SKS pada semester I dan 21 SKS pada semester II.
▸Pada semester III dan seterusnya, jumlah SKS sesuai Indeks Prestasi Semester (IPS).
▸Mahasiswa memilih minat studi pada Semester III.
Profil Lulusan
Kode	Deskripsi	Profesi Lulusan
PL01	Lulusan memiliki kemampuan menganalisis persoalan computing serta menerapkan prinsip-prinsip computing dan disiplin ilmu relevan lainnya untuk mengidentifikasi solusi bagi organisasi.	AI Engineer, Software Engineer, Cybersecurity Analyst, IOT Engineer, Game Developer
PL02	Lulusan memiliki kemampuan mendesain, mengimplementasi dan mengevaluasi solusi berbasis computing yang memenuhi kebutuhan pengguna dengan pendekatan yang sesuai.
PL03	Lulusan memiliki kemampuan berpikir logis, kritis serta sistematis dalam memanfaatkan ilmu pengetahuan informatika untuk menyelesaikan masalah nyata.
PL04	Lulusan memiliki kemampuan menunjukkan sikap: religius, disiplin, bertanggung jawab, menjunjung tinggi nilai kemanusiaan, saling menghormati, dan taat hukum dalam kehidupan bermasyarakat, berbangsa dan bernegara berdasarkan nilai-nilai Pancasila.
PL05	Lulusan memiliki kemampuan menganalisis kebutuhan dan mendesain solusi menggunakan teknologi informasi dan komunikasi untuk menjalankan bisnis secara digital.
Capaian Pembelajaran
Kode	Deskripsi
CPL01	Bertakwa kepada Tuhan Yang Maha Esa, taat hukum, dan disiplin dalam kehidupan bermasyarakat dan bernegara.
CPL02	Menunjukkan sikap profesional dalam bentuk kepatuhan pada etika profesi, kemampuan bekerjasama dalam tim multidisiplin, pemahaman tentang pembelajaran sepanjang hayat, dan respon terhadap isu sosial dan perkembangan teknologi.
CPL03	Mampu menjelaskan cara kerja sistem komputer dan mampu menerapkan/menggunakan berbagai algoritma/metode untuk memecahkan masalah pada suatu organisasi.
CPL04	Mampu menganalisis persoalan computing yang kompleks untuk mengidentifikasi solusi pengelolaan proyek teknologi bidang informatika dengan mempertimbangkan wawasan perkembangan ilmu transdisiplin.
CPL05	Mampu menjelaskan konsep teoritis bidang pengetahuan Informatika dalam mendesain, mengimplementasi, dan mengevaluasi solusi berbasis computing multi-platform yang memenuhi kebutuhan-kebutuhan computing pada sebuah organisasi.
CPL06	Memiliki kemampuan manajerial tim dan kerja sama (team work), manajemen diri, mampu berkomunikasi baik lisan maupun tertulis dengan baik dan mampu melakukan presentasi.
CPL07	Menyusun deskripsi saintifik hasil kajian implikasi pengembangan atau implementasi ilmu pengetahuan teknologi dalam bentuk skripsi atau laporan tugas akhir atau artikel ilmiah.
CPL08	Mampu mengimplementasikan kebutuhan computing dengan mempertimbangkan berbagai metode/algoritma yang sesuai.
CPL09	Mampu menganalisis, merancang, membuat, dan mengevaluasi user interface dan aplikasi interaktif dengan mempertimbangkan kebutuhan pengguna dan perkembangan ilmu transdisiplin.
CPL10	Mampu membangun dan mengimplementasi solusi berbasis sistem cerdas sesuai dengan kebutuhan pengguna dan perkembangan ilmu pengetahuan.
CPL11	Mampu mendesain solusi berbasis inovasi dan kreatifitas untuk menjadi seorang wirausaha di bidang teknologi informasi.
DAFTAR MATA KULIAH
Program Studi Teknik Informatika − S1

Semester 1
NO	Kode	Mata Kuliah	SKS
1	A11.64101	Kalkulus	3
2	A11.64102	Fisika	4
3	A11.64103	Dasar Pemrograman	4
4	A11.64104	Keterampilan Interpersonal	2
5	AF201704	Dasar - Dasar Komputasi	2
6	N201701	Bahasa Indonesia	2
7	N201705	Pendidikan Agama	2
8	U201704	Pengantar Teknologi Informasi	2
Jumlah	21
Semester 2
NO	Kode	Mata Kuliah	SKS
1	A11.64201	Matriks dan Ruang Vektor	3
2	A11.64202	Organisasi dan Arsitektur Komputer	3
3	A11.64203	Matematika Diskrit	3
4	A11.64204	Algoritma dan Struktur Data	4
5	A11.64205	Interaksi Manusia dan Komputer	3
6	N201707	Pendidikan Pancasila	2
7	U201701	Dasar Kewirausahaan	2
Jumlah	20
Semester 3
NO	Kode	Mata Kuliah	SKS
1	A11.64301	Probabilitas dan Statistik	3
2	A11.64302	Logika Informatika	3
3	A11.64303	Rekayasa Perangkat Lunak	3
4	A11.64304	Basis Data	4
5	A11.64305	Pemrograman Berbasis Web	2
6	A11.64306	Sistem Operasi	3
7	N201706	Pendidikan Kewarganegaraan	2
Jumlah	20
Semester 4
NO	Kode	Mata Kuliah	SKS
1	A11.64401	Otomata dan Teori Bahasa	3
2	A11.64402	Jaringan Komputer	3
3	A11.64403	Pemrograman Berorientasi Objek	4
4	A11.64404	Pemrograman Web Lanjut	2
5	A11.64405	Pembelajaran Mesin	3
6	A11.64406	Sistem Basis Data	2
7	A11.64407	Rangkaian Logika Digital	3
Jumlah	20
Semester 5
NO	Kode	Mata Kuliah	SKS
1	A11.64501	Sistem Terdistribusi	3
2	A11.64502	Penambangan Data	3
3	A11.64503	Sistem Informasi	3
4	A11.64504	Manajemen Proyek Teknologi Informasi	3
5	A11.64505	Kecerdasan Buatan	3
6	A11.64506	Kriptografi	3
7	AF201703	Technopreneurship	2
Jumlah	20
Semester 6
NO	Kode	Mata Kuliah	SKS
1	A11.64601	Komputasi Numerik	3
2	A11.64602	Pengembangan Startup Digital	2
3	N201702	Bahasa Inggris	2
4	AF201702	Literasi Informasi	2
5	Peminatan 1	Peminatan 1	9
Jumlah	18
Semester 7
NO	Kode	Mata Kuliah	SKS
1	A11.64701	Kerja Praktek	2
2	A11.64702	Metodologi Penelitian	2
3	A11.64703	Bengkel Koding	2
4	A11.64704	Tugas Akhir 1	2
5	Peminatan 2	Peminatan 2	9
Jumlah	17
Semester 8
NO	Kode	Mata Kuliah	SKS
1	A11.64801	Bimbingan Karir	2
2	A11.64802	Etika Profesi	2
3	A11.64803	Tugas Akhir 2	4
Jumlah	8
MATA KULIAH PEMINATAN
Mata Kuliah Peminatan RPLD
NO	Kode	Mata Kuliah	SKS
1	A11.64603	Rekayasa Kebutuhan Perangkat Lunak	3
2	A11.64604	Analisis dan Perancangan Berorientasi Objek	3
3	A11.64605	Pemrograman Perangkat Bergerak	3
4	A11.64705	Jaminan Kualitas Perangkat Lunak	3
5	A11.64706	Pemrograman Sisi Klien	3
6	A11.64707	Pemrograman Sisi Server	3
Mata Kuliah Peminatan Sistem Cerdas
NO	Kode	Mata Kuliah	SKS
1	A11.64606	Komputer Grafik	3
2	A11.64607	Pengolahan Citra	3
3	A11.64608	Sistem Temu Kembali Informasi	3
4	A11.64708	Pemrosesan Bahasa Alami Berbasis Teks	3
5	A11.64709	Pemrosesan Bahasa Alami Berbasis Ucapan	3
6	A11.64710	Pemrograman Game	3
7	A11.64711	Pengembangan Game	3
8	A11.64712	Penglihatan Komputer dan Analisis Citra	3
9	A11.64713	Analisis Data	3
10	A11.64714	Komputasi Quantum	3
Mata Kuliah Peminatan SKKKD
NO	Kode	Mata Kuliah	SKS
1	A11.64609	Komputasi Awan	3
2	A11.64610	Sistem Tertanam	3
3	A11.64611	Keamanan Sistem dan Siber	3
4	A11.64715	Manajemen Jaringan	3
5	A11.64716	Forensik Digital	3
6	A11.64717	Lingkungan Cerdas dan Intelijen	3
7	A11.64718	Internet of Things	3



"""
