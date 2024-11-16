from datetime import datetime, timedelta
from models.task import Task  # Import Task class

class TaskManager:
    def __init__(self):
        self.tasks = []
def tambahTugas(self):
        while True:
            judul = input("Masukkan judul tugas: ")
            mataKuliah = input("Masukkan mata kuliah: ")
            deadline = input("Masukkan deadline tugas (YYYY-MM-DD): ")
            self.tasks.append({
                "Judul": judul,
                "Mata Kuliah": mataKuliah,
                "deadline": deadline,
                "status": "Belum selesai"
            })
            print(f"Tugas '{judul}' berhasil ditambahkan!")
            
            ulangi = input("Apakah Anda ingin menambahkan tugas lagi? (y/n): ").lower()
            if ulangi != "y":
                print("Anda kembali ke menu utama")
                break
    
def lihatTugas(self):
        if not self.tasks:
            print("Tidak ada tugas.")
        else:
            print("=" * 20 + " DAFTAR TUGAS " + "=" * 20)
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task['Judul']} - Mata Kuliah: {task['Mata Kuliah']} - Deadline: {task['deadline']} - Status: {task['status']}") 


def hapusTugas(self):
        while True:
            if not self.tasks:
                print("Tidak ada tugas untuk dihapus.")
                break
            else:
                try:
                    no_urut = int(input("Pilih nomor tugas yang ingin dihapus: "))
                    if 1 <= no_urut <= len(self.tasks):
                        hapus = self.tasks.pop(no_urut - 1)
                        print(f"Tugas '{hapus['Judul']}' berhasil dihapus!")
                    else:
                        print("Nomor tugas tidak valid.")
                except ValueError:
                    print("Input tidak valid. Masukkan nomor tugas yang benar.")

                ulangi = input("Apakah Anda ingin menghapus tugas lagi? (y/n): ").lower()
                if ulangi != "y":
                    print("Anda kembali ke menu utama")
                    break 
    
    
def update_status(self):
        while True:
            no_urut = int(input("Pilih nomor tugas yang ingin diperbarui statusnya: "))
            if 1 <= no_urut <= len(self.tasks):
                # Mengubah status tugas menjadi "Selesai"
                self.tasks[no_urut - 1]["status"] = "Selesai"
                print(f"Tugas '{self.tasks[no_urut - 1]['Judul']}' telah selesai!")
            else:
                print("Nomor tugas tidak valid.")
            
            ulangi = input("Apakah Anda ingin mengubah status tugas lagi? (y/n): ").lower()
            if ulangi != "y":
                print("Anda kembali ke menu utama")
                break
            
def check_deadline(self, days_before=2):
        today = datetime.today().date()
        pengingat = today + timedelta(days=days_before)
        
        for tugas in self.tasks:
            deadline_tugas = datetime.strptime(tugas["deadline"], "%Y-%m-%d").date()
            
            if today > deadline_tugas:
                print(f"⚠️ Tugas '{tugas['Judul']}' sudah lewat deadline ❗")
            elif today <= deadline_tugas <= pengingat:
                print(f"🔔 Tugas '{tugas['Judul']}' mendekati deadline pada {tugas['deadline']} ❗❗")
            else:
                print(f"👌 Tugas '{tugas['Judul']}' belum mendekati deadline.")
