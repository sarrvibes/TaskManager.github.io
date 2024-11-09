def lihatTugas(tasks):
    if not tasks:
        print("Tidak ada tugas.")
    else:
        print("=" * 20 + " DAFTAR TUGAS " + "=" * 20)
        for i, tugas in enumerate(tasks, start=1):
            print(f"{i}. {tugas['Judul']} - Deadline: {tugas['deadline']} - Status: {tugas['status']}")
            print("=" * 54)
