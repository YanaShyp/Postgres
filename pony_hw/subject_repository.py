from pony.orm import db_session, select
from pony_hw.models import Subject
from pony_hw.base_repository import BaseRepository


class SubjectRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = Subject

    @db_session
    def get_all_by_lambda(self):
        subjects = Subject.select(lambda subject: subject)
        return subjects.page(1).to_list()

    @db_session
    def get_all_by_cycle(self):
        subjects = select(subject for subject in Subject).page(1).to_list()
        return subjects


if __name__ == '__main__':
    subject_repo = SubjectRepository()
    result = subject_repo.get_all_by_cycle
    print(result)

