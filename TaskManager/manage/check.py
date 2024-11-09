from datetime import datetime, timedelta

# Fungsi untuk menampilkan tugas yang mendekati deadline
def check_deadline(tasks, days_before=2):
    today = datetime.today().date()
    pengingat = today + timedelta(days=days_before)
    
    for tugas in tasks:
        deadlineTugas = datetime.strptime(tugas["deadline"], "%Y-%m-%d").date()
        
        if today > deadlineTugas:
            print(f"⚠️ Tugas '{tugas['Judul']}' sudah lewat deadline ❗")
        elif today <= deadlineTugas <= pengingat:
            print(f"🔔 Tugas '{tugas['Judul']}' mendekati deadline pada {tugas['deadline']}❗❗")
        else:
            print(f"👌 Tugas '{tugas['Judul']}' belum mendekati deadline.")

