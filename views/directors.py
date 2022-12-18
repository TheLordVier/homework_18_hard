# Импортируем фреймворк Flask и его функции
from flask import request
from flask_restx import Resource, Namespace

# Импортируем схему директора
from dao.model.director import DirectorSchema
# Импортируем экземпляр сервиса директор
from implemented import director_service

# Создаём неймcпейс для представлений
director_ns = Namespace('directors')

# Cоздаём экземпляры схем
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        """"
        Получение списка всех сущностей (режиссёра)
        """
        directors = director_service.get_all()
        result = directors_schema.dump(directors)
        return result, 200

    def post(self):
        """"
        Создание определённой сущности (режиссёра)
        """
        request_json = request.json
        director = director_service.create(request_json)
        return "Director created", 201, {"location": f"/directors/{director.id}"}


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        """"
        Получение конкретной сущности по идентификатору (режиссёра)
        """
        try:
            director = director_service.get_one(did)
            return director_schema.dump(director), 200
        except Exception as e:
            return str(e), 404

    def put(self, did: int):
        """"
            Обновление конкретной сущности по идентификатору (режиссёра)
            """
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = did
        director_service.update(request_json)
        return "Director updated", 204

    def delete(self, did):
        """"
            Удаление конкретной сущности по идентификатору (режиссёра)
            """
        director_service.delete(did)
        return "Director deleted", 204
