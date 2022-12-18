# Импортируем объект доступа к данным DirectorDAO
from dao.director import DirectorDAO


# Создаём класс DirectorService
class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        return self.dao.get_one(did)

    def get_all(self):
        return self.dao.get_all()

    def create(self, director_dict):
        return self.dao.create(director_dict)

    def update(self, director_dict):
        self.dao.update(director_dict)
        return self.dao

    def delete(self, did):
        self.dao.delete(did)
