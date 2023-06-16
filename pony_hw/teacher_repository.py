from pony.orm import db_session, select
from pony_hw.models import Teacher
from pony_hw.base_repository import BaseRepository


class TeacherRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = Teacher

    @db_session
    def get_all_by_lambda(self):
        teachers = Teacher.select(lambda teacher: teacher)
        return teachers.page(1).to_list()

    @db_session
    def get_all_by_cycle(self):
        teachers = select(teacher for teacher in Teacher).page(1).to_list()
        return teachers


if __name__ == '__main__':
    teacher_repo = TeacherRepository()
    result = teacher_repo.get_all_by_cycle
    print(result)
