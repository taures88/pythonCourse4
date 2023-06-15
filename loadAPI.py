from abc import ABC, abstractmethod
import requests

SUPERJOB_API_KEY: str = 'v3.r.114177288.31012d1199b90ac1f6d3e9e080e1fe10a2d29cc2.3e405bc259c0e9aad5ba5e107cef6e21de72e5b3'


"""загрузка данных через API и сохранение в Json файл"""

class get_service_API(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(get_service_API):
    def get_vacancies(self, name_job=None):
        params = {
            'text': name_job,
            'area': 1,
            'per_page': 10
        }
        response = requests.get('https://api.hh.ru/vacancies', params)
        return response.json()


class SuperJobAPI(get_service_API):
    def get_vacancies(self, name_job=None):
        params = {
            'count': 10,
            'town': 4,
            'keyword': name_job
        }
        headers = {'X-Api-App-Id': SUPERJOB_API_KEY}
        response = requests.get('https://api.superjob.ru/2.0/vacancies/?t=4&count=100/', params, headers=headers)
        return response.json()


