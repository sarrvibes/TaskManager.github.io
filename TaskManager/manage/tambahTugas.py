def tambahTugas(tasks):
    while True:
        judul = input("Masukkan judul tugas: ")
        mataKuliah = input("Masukkan mata kuliah : ")
        deadline = input("Masukkan deadline tugas (YYYY-MM-DD): ")
        tasks.append({"Judul": judul, "Mata Kuliah": mataKuliah, "deadline": deadline, "status": "Belum selesai"})
        print(f"Tugas '{judul}' berhasil ditambahkan!")
        
        ulangi = input("Apakah Anda ingin menambahkan tugas lagi? (y/n): ").lower()
        if ulangi != "y" :
            print("anda kembali ke menu utama")
            break
