## Домашняя работа (Урок 18. Архитектура)

Студент: Михайлов Александр

## Структура приложения:

**app.py** - *основное приложением*

**setup_db.py** - *объект SQLAlchemy, который используется в приложении*

**config.py** - *настройки конфигурации приложения*

**constants.py** - *константы приложения*

**implemented.py** - *файл для создания DAO и сервисов, чтобы импортировать их везде*

**movies.db** - *база данных с таблицами (фильмы, режиссёры и жанры)*

**requirements.txt** - *зависимости приложения*

- **Директория dao** - *Файлы для доступа к данным (DAO)*
    - **director.py** - *Data Access Object для режиссёра* <br>
    - **genre.py** - *Data Access Object для жанра* <br>
    - **movie.py** - *Data Access Object для фильма* <br>
      **Директория model** - **Модели и их схемы**
        - **director.py** - *Модель и схема для режиссера* <br>
        - **genre.py** - *Модель и схема для жанра* <br>
        - **movie.py** - *Модель и схема для фильма* <br>

- **Директория service** - *Бизнес логика приложения в виде классов*
    - **director.py** - *Класс DirectorService* <br>
    - **genre.py** - *Класс GenreService* <br>
    - **movie.py** - *Класс MovieService* <br>

- **Директория views** - *Все представления (views) приложения*
    - **directors.py** - *Представления (view) с режиссёрами* <br>
    - **genres.py** - *Представления (view) с жанрами* <br>
    - **movies.py** - *Представления (view) с фильмами* <br>