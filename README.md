# Book Management System

## Описание проекта

Этот проект представляет собой систему управления книгами, реализованную с использованием Django (или FastAPI) для веб-API и gRPC для взаимодействия с базой данных. Система поддерживает операции создания, чтения, обновления и удаления (CRUD) книг через REST API, а также предоставляет отдельный gRPC-сервис для получения информации о книгах. Проект включает в себя аутентификацию пользователей с помощью JWT (или OAuth2), хранение данных в базе данных PostgreSQL (или MySQL), использование брокера сообщений RabbitMQ (или Kafka) для связи между веб-приложением и gRPC-сервисом, а также тестирование и контейнеризацию через Docker.

## Функциональность

1. **Веб-API (REST)**:
    - Создание новой книги
    - Получение списка всех книг
    - Получение деталей конкретной книги по ID
    - Обновление информации о книге
    - Удаление книги
2. **Аутентификация**:
    - Использование JWT для аутентификации пользователей.
    - CRUD операции доступны только аутентифицированным пользователям.
3. **База данных**:
    - Хранение данных в PostgreSQL .
    - Миграции базы данных с использованием встроенных средств Django.
4. **gRPC-сервис**:
    - Метод для получения информации о книге по ID.
    - Метод для получения списка всех книг.
    - gRPC-сервис работает с той же базой данных, что и веб-приложение.
5. **Брокер сообщений**:
    - Использование RabbitMQ для взаимодействия между веб-приложениями и gRPC-сервисом.
    - При создании, обновлении или удалении книги через REST API:
        - Соответствующее сообщение отправляется в брокер.
        - gRPC-сервис слушает эти сообщения, логирует их и выводит информацию в консоль.
6. **Docker**:
    - Контейнеризация веб-приложения, gRPC-сервиса, базы данных и брокера сообщений с использованием Docker.
7. **Тестирование**:
    - Unit-тесты для ключевых функций веб-приложения и gRPC-сервиса.
8. **Документация**:
    - Автоматическая генерация документации API через Swagger/OpenAPI для веб-приложения.
    - .proto файлы для gRPC-сервиса.

## Технологии

- **Языки программирования**: Python
- **Фреймворки**: Django 
- **База данных**: PostgreSQL
- **Брокер сообщений**: RabbitMQ
- **gRPC**: Протокол для взаимодействия сервисов
- **Аутентификация**: JWT
- **Контейнеризация**: Docker, Docker Compose
- **Кэширование**: Redis (если требуется)
- **Тестирование**: pytest (или unittest)



# Установка и запуск

## Клонирование репозитория

```
git clone https://github.com/timurxboy/abol.git
cd abol
```


## Настройка окружения

Создайте файл .env в корневой директории проекта и добавьте переменные окружения:

```
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_NAME=your-db-name
DB_PORT=5432

GRPC_SERVER_PORT=50051
```

## Docker

Соберите контейнеры и запустите проект:

```
docker-compose up --build
```

Это поднимет следующие сервисы:

- Брокер сообщений (RabbitMQ)
- Redis
- База данных (PostgreSQL)
- WEB-server (Django)
- Gateway (Django)


## Миграции базы данных

```
docker-compose exec web-server python manage.py migrate
```

## API документация
После запуска веб-приложения документация будет доступна по следующим URL:

Swagger: http://localhost:8000/api/docs/


## gRPC документация

Для работы с gRPC-сервисом используйте .proto файлы, которые находятся в директории grpc/protos.

Пример .proto файла для работы с книгами:
```
syntax = "proto3";

package book;

service Book {
    rpc GetBook (BookIdRequest) returns (BookResponseID) {}
    rpc ListBook (Empty) returns (ListBookResponse) {}
    rpc CreateBook (BookResponse) returns (BookResponseID) {}
    rpc UpdateBook (BookResponseID) returns (BookResponseID) {}
    rpc DeleteBook (BookIdRequest) returns (Empty) {}
}


message BookIdRequest {
    int32 id = 1;
}

message Empty {}

message BookResponse {
    string name = 1;
    string author = 2;
    string publication_date = 3;
}

message BookResponseID {
    int32 id = 1;
    string name = 2;
    string author = 3;
    string publication_date = 4;
}

message ListBookResponse {
    repeated BookResponseID data = 1;
}
```

## Тестирование

Для запуска тестов выполните команду:

```
docker-compose exec gateway pytest apps/main/tests.py 
```

