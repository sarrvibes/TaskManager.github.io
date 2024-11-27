from datetime import datetime, timedelta
from models.task import Task  # Import Task class

class TaskManager:
    def __init__(self):
        self.tasks = []  # Menyimpan daftar objek Task

    def tambah_tugas(self):
        while True:
            judul = input("Masukkan judul tugas: ")
            mata_kuliah = input("Masukkan mata kuliah: ")
            
            # Validasi input deadline
            while True:
                deadline = input("Masukkan deadline tugas (YYYY-MM-DD): ")
                try:
                    deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print("Format tanggal salah. Harap masukkan dalam format YYYY-MM-DD.")
            
            # Membuat objek Task dan menambahkannya ke daftar
            tugas_baru = Task(judul, deadline, mata_kuliah)
            self.tasks.append(tugas_baru)
            print(f"Tugas '{judul}' berhasil ditambahkan!")

            ulangi = input("Apakah Anda ingin menambahkan tugas lagi? (y/n): ").lower()
            if ulangi != "y":
                print("Anda kembali ke menu utama.")
                break
