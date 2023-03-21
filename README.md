[![foodgram_deploy](https://github.com/STI-xa/foodgram-project-react/actions/workflows/foodgram_deploy.yml/badge.svg)](https://github.com/STI-xa/foodgram-project-react/actions/workflows/foodgram_deploy.yml)

**Foodgram_project** - Продуктовый помощник или сайт, на котором пользователи могут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «Список покупок» позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд, с возможностью скачать файл .txt со списком продуктов.
___
**Проект доступен по [здесь](158.160.55.121)**

___
## **Что внутри**:
* Одностраничное приложение на фреймворке React
* API и он-лайн сервис
* Djoser аутентификация по токенам
___
## **Как запустить проект**:

### **Для Windows, локально:**

* Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/STI-xa/foodgram-project-react

cd backend
```

* Cоздать и активировать виртуальное окружение:
```
python -m venv venv

source venv/Scripts/activate
```

* Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip

pip install -r requirements.txt
```

* Выполнить миграции:
```
python manage.py migrate
```

* Запустить проект:
```
python manage.py runserver
```

### **Запуск из контейнера:**
* Клонировать репозиторий и перейти в папку infra в командной строке:
```
git clone https://github.com/STI-xa/foodgram-project-react

cd infra
```

* Создание и запуск контейнеров:
```
docker-compose up -d --build
```

* Выполняем миграции, создаем суперпользователя, собираем статику и создаем дамп БД:
```
docker-compose exec backend python manage.py migrate

docker-compose exec backend python manage.py createsuperuser

docker-compose exec backend python manage.py collectstatic --no-input

docker-compose exec backend python manage.py dumpdata > fixtures.json
```

## Шаблон наполнения env-файла:
```
DB_ENGINE=django.db.backends.postgresql # указывает, с какой БД работать
DB_NAME=postgres # имя БД
POSTGRES_USER=postgres # логин для подключения к БД
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

### **Образ доступен на** [DockerHub](https://hub.docker.com/repository/docker/stixaxa/foodgram_backend/general)
___
## **Примеры запросов**:
* GET-запрос возвращает список рецептов:
```
http://127.0.0.1:8000/api/recipe/
```
```
{
  "count": 123,
  "next": "http://foodgram.example.org/api/recipes/?page=4",
  "previous": "http://foodgram.example.org/api/recipes/?page=2",
  "results": [
    {
      "id": 0,
      "tags": [
        {
          "id": 0,
          "name": "Завтрак",
          "color": "#E26C2D",
          "slug": "breakfast"
        }
      ],
      "author": {
        "email": "user@example.com",
        "id": 0,
        "username": "string",
        "first_name": "Вася",
        "last_name": "Пупкин",
        "is_subscribed": false
      },
      "ingredients": [
        {
          "id": 0,
          "name": "Картофель отварной",
          "measurement_unit": "г",
          "amount": 1
        }
      ],
      "is_favorited": true,
      "is_in_shopping_cart": true,
      "name": "string",
      "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
      "text": "string",
      "cooking_time": 1
    }
  ]
}
```
* POST-запрос для создания рецепта:
```
* http://127.0.0.1:8000/api/recipes/
```
```
{
  "ingredients": [
    {
      "id": 1123,
      "amount": 10
    }
  ],
  "tags": [
    1,
    2
  ],
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
  "name": "string",
  "text": "string",
  "cooking_time": 1
}
```
* Примеры запросов можно посмотреть по [ссылке](http://127.0.0.1:8000/redoc/) после запуска проекта.
___
## **Стэк технологий**:
* ![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
* ![image](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
* ![image](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
* ![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
* ![image](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
* ![image](https://img.shields.io/badge/Djoser-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)
* ![image](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
* ![image](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
* ![image] https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
