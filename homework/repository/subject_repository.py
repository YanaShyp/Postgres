from homework.models.subject_model import SubjectModel
from homework.session import session
from sqlalchemy import update


class SubjectRepository:
    def __init__(self):
        self.__session = session
        self.__model = SubjectModel

    def get_all(self):
        return self.__session.query(self.__model).all()

    def get_by_id(self, subject_id):
        subject = self.__session.get(self.__model, {'subject_id': subject_id})
        return subject

    def add_subject(self, subject: SubjectModel):
        self.__session.add(subject)

    # def update_subject(self, subject: SubjectModel, title, subject_id):
        # updated = update(self.__model).where({'subject_id': subject_id}).values({'title' = title})

    def remove_subject_by_id(self, subject_id):
        subject = self.__session.get(self.__model, {'subject_id': subject_id})
        self.__session.delete(subject)



if __name__ == "__main__":
    subject_repo = SubjectRepository()
    result = subject_repo.update_subject()
