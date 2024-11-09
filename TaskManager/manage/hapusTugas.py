def hapusTugas(tasks):
    while True :
        no_urut = int(input("Pilih nomor tugas yang ingin dihapus: "))
        if 1 <= no_urut <= len(tasks):
            hapus = tasks.pop(no_urut - 1)
            print(f"Tugas '{hapus['Judul']}' berhasil dihapus!")
        else:
            print("Nomor tugas tidak valid.")
        
        ulangi = input("Apakah Anda ingin menghapus tugas lagi? (y/n): ").lower()
        if ulangi != "y" :
            print("anda kembali ke menu utama")
            break
