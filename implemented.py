# Файл для создания DAO и сервисов, чтобы импортировать их везде

# Импортируем классы DAO из директории dao
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
# Импортируем классы сервисов с бизнес-логикой из директории service
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
# Импортируем db из файла setup_db.py
from setup_db import db


# Создаём экземпляры DAO
director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)

# Создаём экземпляры для сервисов
director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)