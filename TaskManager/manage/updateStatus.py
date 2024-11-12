def update_status(tasks):
    while True :
        no_urut = int(input("Pilih nomor tugas yang ingin diperbarui statusnya: "))
        if 1 <= no_urut <= len(tasks):
            tasks[no_urut - 1]["status"] = "Selesai"
            print(f"Tugas '{tasks[no_urut - 1]['Judul']}' telah selesai!")
        else:
            print("Nomor tugas tidak valid.")
            
        ulangi = input("Apakah Anda ingin mengubah status tugas lagi? (y/n): ").lower()
        if ulangi != "y" :
            print("anda kembali ke menu utama")
            break
