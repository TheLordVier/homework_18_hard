# Импортируем фреймворк Flask и его функции
from flask import request
from flask_restx import Resource, Namespace

# Импортируем схему фильма
from dao.model.movie import MovieSchema
# Импортируем экземпляр сервиса фильм
from implemented import movie_service

# Создаём неймcпейс для представлений
movie_ns = Namespace('movies')

# Cоздаём экземпляры схем
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """"
        Получение списка всех сущностей (фильма)
        """
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        filters = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
        }
        movies = movie_service.get_all(filters)
        result = movies_schema.dump(movies)
        return result, 200

    def post(self):
        """"
        Создание определённой сущности (фильма)
        """
        request_json = request.json
        movie = movie_service.create(request_json)
        return "Movie created", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route("/<int:mid>")
class MovieView(Resource):
    def get(self, mid: int):
        """"
        Получение конкретной сущности по идентификатору (фильма)
        """
        try:
            movie = movie_service.get_one(mid)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return str(e), 404

    def put(self, mid: int):
        """"
        Обновление конкретной сущности по идентификатору (фильма)
        """
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = mid
        movie_service.update(request_json)
        return "Movie updated", 204

    def delete(self, mid):
        movie_service.delete(mid)
        return "Movie deleted", 204
