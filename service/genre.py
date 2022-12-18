# Импортируем объект доступа к данным GenreDAO
from dao.genre import GenreDAO


# Создаём класс GenreService
class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, genre_dict):
        return self.dao.create(genre_dict)

    def update(self, genre_dict):
        self.dao.update(genre_dict)
        return self.dao

    def delete(self, gid):
        self.dao.delete(gid)
