from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class TeacherModel(Base):
    __tablename__ = "teachers"
    teacher_id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(50))
    age = Column(INTEGER)
    subject_id = Column(ForeignKey("subjects.subject_id"))
    subjects = relationship("SubjectModel", back_populates="teachers")

    def __str__(self):
        return f"id = {self.subject_id}, title = {self.title}"