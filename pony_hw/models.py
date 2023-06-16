from pony.orm import Database, PrimaryKey, Required, Set

db = Database()
db.bind(provider='postgres', user='postgres', password='postgres', host='127.0.0.1', database='teachers_subjects')


class Subject(db.Entity):
    _table_ = "subjects"
    subject_id = PrimaryKey(int, auto=True)
    title = Required(str, 50)
    teachers = Set("Teacher")

    def __str__(self):
        return f"subject_id = {self.subject_id}; title = {self.title}"

    def __repr__(self):
        return f"subject_id = {self.subject_id}; title = {self.title}"


class Teacher(db.Entity):
    _table_ = "teachers"
    teacher_id = PrimaryKey(int, auto=True)
    name = Required(str, 50)
    age = Required(int)
    subject = Required(Subject, column="subject_id")

    def __str__(self):
        return f"teacher_id = {self.teacher_id}; name = {self.name}"

    def __repr__(self):
        return f"{self.name} || {self.subject.title}"


db.generate_mapping(create_tables=False)
