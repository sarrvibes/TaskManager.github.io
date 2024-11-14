from manage.tambahTugas import tambahTugas
from manage.lihatTugas import lihatTugas
from manage.hapusTugas import hapusTugas
from manage.updateStatus import update_status
from manage.check import check_deadline

def main_menu(tasks):
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
            tambahTugas(tasks)
        elif pilihan == '2':
            lihatTugas(tasks)
        elif pilihan == '3':
            hapusTugas(tasks)
        elif pilihan == '4':
            update_status(tasks)
        elif pilihan == '5':
            check_deadline(tasks)
        elif pilihan == 'q':
            print("Anda Telah Keluar dari Aplikasi.")
            print("=" *25 + "Terima Kasih" + "=" *25)
            break
        else:
            print("Pilihan tidak valid, coba lagi.")
