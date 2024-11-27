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

    def lihat_tugas(self):
        if not self.tasks:
            print("Tidak ada tugas.")
        else:
            print("=" * 25 + " DAFTAR TUGAS " + "=" * 25)
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
                
                def hapus_tugas(self):
        while True:
            if not self.tasks:
                print("\nTidak ada tugas untuk dihapus.")
                break
            else:
                self.lihat_tugas()
                try:
                    no_urut = int(input("\nPilih nomor tugas yang ingin dihapus: "))
                    if 1 <= no_urut <= len(self.tasks):
                        tugas_dihapus = self.tasks.pop(no_urut - 1)
                        print(f"Tugas '{tugas_dihapus.judul}' berhasil dihapus!")
                    else:
                        print("Nomor tugas tidak valid.")
                except ValueError:
                    print("Input tidak valid. Masukkan nomor tugas yang benar.")

                ulangi = input("Apakah Anda ingin menghapus tugas lagi? (y/n): ").lower()
                if ulangi != "y":
                    print("Anda kembali ke menu utama.")
                    break
