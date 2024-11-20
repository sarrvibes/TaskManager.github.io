class Task:
    def _init_(self, judul, deadline, status="Belum selesai"):
        self.judul = judul
        self.deadline = deadline
        self.status = status

    def _str_(self):
        return f"{self.judul} - Deadline: {self.deadline} - Status: {self.status}"
