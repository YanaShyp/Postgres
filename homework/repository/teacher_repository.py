from base_repository import BaseRepository


class TeacherRepository(BaseRepository):
    def __init__(self):
        super().__init__()

    def get_all_teachers(self):
        self.cursor.execute("SELECT * FROM teachers;")
        return self.cursor.fetchall()

    def get_teacher_by_id(self, teacher_id):
        self.cursor.execute(f"SELECT * FROM teachers WHERE teachers.teacher_id = {teacher_id};")
        return self.cursor.fetchone()

    def add_teacher(self, name, age, subject_id):
        self.cursor.execute(
            f"INSERT INTO teachers (name, age, subject_id) VALUES ('{name}', '{age}', '{subject_id}');")

    def update_teachers_subject(self, teacher_id, subject_id):
        self.cursor.execute(
            f"UPDATE teachers SET subject_id = {subject_id} WHERE teachers.teacher_id = {teacher_id};")

    def remove_by_id(self, teacher_id):
        self.cursor.execute(f"DELETE FROM teachers WHERE teacher_id={teacher_id};")


if __name__ == "__main__":
    rep = TeacherRepository()
    rep.update_teachers_subject(6, 4)
    print(rep.get_all_teachers())
