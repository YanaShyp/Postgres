from sqlalchemy import Column, INTEGER, VARCHAR
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class SubjectModel(Base):
    __tablename__ = "subjects"
    subject_id = Column(INTEGER, primary_key=True)
    title = Column(VARCHAR(50))
    teachers = relationship("TeacherModel", back_populates="subjects")

    def __str__(self):
        return f"id = {self.subject_id}, title = {self.title}"