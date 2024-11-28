# models/task.py
class Task:
    def _init_(self, judul, deadline, mata_kuliah, status="Belum selesai"):
        self.judul = judul
        self.deadline = deadline
        self.mata_kuliah = mata_kuliah
        self.status = status

    def _str_(self):
        return (f"Tugas: {self.judul}, Mata Kuliah: {self.mata_kuliah}, "
                f"Deadline: {self.deadline}, Status: {self.status}")
