# Импортируем фреймворк Flask и его функции
from flask import request
from flask_restx import Resource, Namespace

# Импортируем схему жанра
from dao.model.genre import GenreSchema
# Импортируем экземпляр сервиса жанр
from implemented import genre_service

# Создаём неймcпейс для представлений
genre_ns = Namespace('genres')

# Cоздаём экземпляры схем
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route("/")
class GenresView(Resource):
    def get(self):
        """"
        Получение списка всех сущностей (жанра)
        """
        genres = genre_service.get_all()
        result = genres_schema.dump(genres)
        return result, 200

    def post(self):
        """"
        Создание определённой сущности (жанра)
        """
        request_json = request.json
        genre = genre_service.create(request_json)
        return "Genre created", 201, {"location": f"/genres/{genre.id}"}


@genre_ns.route("/<int:gid>")
class GenreView(Resource):
    def get(self, gid: int):
        """"
        Получение конкретной сущности по идентификатору (жанра)
        """
        try:
            genre = genre_service.get_one(gid)
            return genre_schema.dump(genre), 200
        except Exception as e:
            return str(e), 404

    def put(self, gid: int):
        """"
        Обновление конкретной сущности по идентификатору (жанра)
        """
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = gid
        genre_service.update(request_json)
        return "Genre updated", 204

    def delete(self, gid: int):
        """"
        Удаление конкретной сущности по идентификатору (жанра)
        """
        genre_service.delete(gid)
        return "Genre deleted", 204

