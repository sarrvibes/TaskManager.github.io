  Plan Smart
Plan Smart adalah aplikasi berbasis Python untuk membantu manajemen tugas secara efisien. Dengan pendekatan Object-Oriented Programming (OOP), TaskMaster mempermudah pengguna dalam menambah, mengelola, dan memantau tugas mereka.

fitur utama
Tambah Tugas: Membuat tugas baru dengan judul, mata kuliah, dan deadline.
Lihat Daftar Tugas: Menampilkan semua tugas beserta detailnya.
Hapus Tugas: Menghapus tugas yang tidak diperlukan lagi.
Update Status: Menandai tugas sebagai selesai.
Cek Deadline: Memberikan pengingat untuk tugas yang mendekati atau melewati batas waktu.

Struktur Folder
TaskMaster/
├── main.py
├── menu.py
├── models/  
│   ├── task.py        # Blueprint untuk tugas individual  
│   ├── operasi.py     # Pengelolaan utama daftar tugas  
├── README.md          # Dokumentasi proyek  
└── .gitignore   

Detail Class
Task
Berfungsi untuk merepresentasikan sebuah tugas.
Atribut: judul, deadline, mata_kuliah, status.
Metode: _init, __str_.
TaskManager
Bertanggung jawab untuk pengelolaan daftar tugas.
Fitur: Tambah tugas, lihat tugas, hapus tugas, update status, cek deadline.

Alur Pengembangan
Perencanaan: Diskusi ide proyek dan pembuatan struktur awal folder.
Implementasi Kode Tahap I: Membuat kode fitur tanpa OOP.
Implementasi Kode Tahap II: Merombak kode menjadi berbasis OOP.
Debugging: Analisis dan penyederhanaan struktur untuk modularitas.
Testing: Memastikan fitur berjalan sesuai rencana.
Dokumentasi: Menyusun README dan PowerPoint presentasi.


Tim Pengembang
Group 5
- Baysarah (leader group)
- Radiah Sindikia Maharani
-Annisa
- Sultan Zaky
- Kevin Putra Zerian
