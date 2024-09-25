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


```
npm install
npm run serve
```

