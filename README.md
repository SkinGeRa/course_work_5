Основные шаги проекта

1. Получаем данные о работодателях и их вакансиях с сайта hh.ru. Для этого используем публичный API hh.ru и библиотеку requests.
2. Выбраны 10 компаний, от которых мы получаем данные о вакансиях по API.
3. Спроектированы таблицы в БД PostgreSQL для хранения полученных данных о работодателях и их вакансиях. Для работы с БД используем библиотеку psycopg2.
4. Реализован код, который заполняет созданные в БД PostgreSQL таблицы данными о работодателях и их вакансиях.
5. Создан класс DBManager для работы с данными в БД.
6. Для корректной работы необходимо создать файл database.ini в котором будет необходимо прописать данные в формате:
- [postgresql]
- host=наименование хоста (по умолчанию localhost)
- user=имя пользователя
- password=пароль пользователя
- port=номер порта (по умолчанию 5432)
