from datetime import datetime, timedelta
from models.task import Task  # Import Task class

class TaskManager:
    def __init__(self):
        self.tasks = []

    

    

    
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