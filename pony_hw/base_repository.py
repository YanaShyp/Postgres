from pony.orm import db_session


class BaseRepository:
    def __init__(self):
        self.model = None

    @db_session
    def get_by_id(self, id):
        entity = self.model.get(lambda r: r.id == id)
        return entity

    @db_session
    def delete_by_id(self, id):
        entity = self.get_by_id(id)
        entity.delete()