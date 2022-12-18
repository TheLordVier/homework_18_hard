# Импортируем модель Genre
from dao.model.genre import Genre


# Создаём класс GenreDAO
class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, genre_dict):
        entity = Genre(**genre_dict)
        self.session.add(entity)
        self.session.commit()
        return entity

    def update(self, genre_dict):
        genre = self.get_one(genre_dict.get("id"))
        genre.name = genre_dict.get("name")
        self.session.add(genre)
        self.session.commit()

    def delete(self, gid):
        genre = self.get_one(gid)
        self.session.delete(genre)
        self.session.commit()

