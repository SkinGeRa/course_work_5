from src.utils import get_employers, create_db, create_tables, fill_db
from config import config
from src.db_manager import DBManager

if __name__ == '__main__':
    companies = [78638,  # Тинькофф
                 84585,  # Авито
                 3529,  # Сбер
                 147981,  # Газпром информ
                 1740,  # Яндекс
                 4934,  # Билайн
                 906557,  # СберТех
                 3144945,  # Ростелеком
                 1122462,  # Skyeng
                 15478  # VK
                 ]

    database_name = 'cw'
    params = config()

    create_db(database_name, params)
    create_tables(database_name, params)
    fill_db(get_employers(companies), database_name, params)

    db_manager = DBManager(database_name, params)

    # Необходимо раскоммитить примеры вызова созданного экземпляра класса DBManager.

    # print(db_manager.get_companies_and_vacancies_count())
    # print(db_manager.get_all_vacancies())
    # print(db_manager.get_avg_salary())
    # print(db_manager.get_vacancies_wth_highest_salary())

    # keyword = input('Введите ключевое слово для поиска вакансий: ').lower()
    # print(db_manager.get_vacancies_with_keyword(keyword))
