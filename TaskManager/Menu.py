from models.operasi import TaskManager

def main_menu(tasks):
    tasks = TaskManager()
    print("=== Aplikasi Task Manager ===")
    print("1. Tambah Tugas")
    print("2. Lihat Daftar Tugas")
    print("3. Hapus Tugas")
    print("4. Update Status")
    print("5. Check Deadline")
    print("Q. Keluar")

    while True:
        pilihan = input("\nPilih menu: ")

        if pilihan == '1':
            tasks.tambah_tugas()
        elif pilihan == '2':
            tasks.lihat_tugas()
        elif pilihan == '3':
            tasks.hapus_tugas()
        elif pilihan == '4':
            tasks.update_status()
        elif pilihan == '5':
            tasks.check_deadline()
        elif pilihan.lower() == 'q':
            print("Anda Telah Keluar dari Aplikasi.")
            print("=" *25 + "Terima Kasih" + "=" *25)
            break
        else:
            print("Pilihan tidak valid, coba lagi.")
