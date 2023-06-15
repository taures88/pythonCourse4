import json
import sys

"""основной класс вакансий"""


class Vacancy:
    all_vacancy = {'AllVacancy': []}
    del_vacancy = 0

    def __init__(self, name_profession: str, salary: int, url: str, requirement: str):
        self.vacancy = None
        self.name_profession = name_profession
        if salary == 0:
            self.salary = "З/П не указана"
        else:
            self.salary = salary
        self.url = url
        self.requirement = requirement

    @classmethod
    def file_vacancies_clean(cls):
        try:
            with open('all_vacancy.json', 'w', encoding='utf-8') as file:
                pass
        except FileNotFoundError:
            pass

    def file_vacancy_save(self):

        self.vacancy = {'Профессия': self.name_profession,
                        'Заработная плата': self.salary,
                        'Ссылка на вакансию': self.url,
                        'Требования к работе': self.requirement
                        }
        Vacancy.all_vacancy['AllVacancy'].append(self.vacancy)

    @classmethod
    def json_file_vacancy(cls):
        with open('all_vacancy.json', 'a', encoding='utf-8') as file:
            json.dump(Vacancy.all_vacancy, file, indent=2, ensure_ascii=False)

    """метод для сохранения вакансий в json файл"""
    @classmethod
    def save_all_vacancy_file(cls, All_VACANCY):
        Vacancy.file_vacancies_clean()
        for vacancy in All_VACANCY:
            vacancy.file_vacancy_save()
        Vacancy.json_file_vacancy()

    @classmethod
    def del_vacancy_in_file(cls, data_all_vacancy):

        """Метод для удаления вакансии из файла"""

        with open('all_vacancy.json', 'w', encoding='utf-8') as file:
            json.dump(data_all_vacancy, file, ensure_ascii=False)

    @classmethod
    def filter_vacancy(cls, salary, keyword):
        """Метод для фильтрации вакансий"""

        with open('all_vacancy.json', 'r', encoding='utf-8') as file:
            data_all_vacancy = json.load(file)
            try:
                while True:
                    for vacancy in data_all_vacancy['AllVacancy']:
                        info_vacancy = f"\nНазвания вакансии — {vacancy['Профессия']}\n" \
                                       f"Заработная плата — {vacancy['Заработная плата']}\n" \
                                       f"Требования — {vacancy['Требования к работе']}\n" \
                                       f"Ссылка на вакансию: {vacancy['Ссылка на вакансию']}\n"
                        try:
                            if keyword.lower() in vacancy['Требования к работе'].lower():
                                try:
                                    if vacancy['Заработная плата'] >= salary:
                                        data_all_vacancy['AllVacancy'].pop(Vacancy.del_vacancy)
                                        Vacancy.del_vacancy_in_file(data_all_vacancy)
                                        Vacancy.del_vacancy += 1
                                        return info_vacancy
                                except TypeError:
                                    print('\nЭта вакансия, не попадает под критерий указанной ЗП.')
                                    return info_vacancy
                            else:
                                data_all_vacancy['AllVacancy'].pop(Vacancy.del_vacancy)
                                Vacancy.del_vacancy_in_file(data_all_vacancy)
                                Vacancy.del_vacancy += 1
                        except AttributeError:
                            pass
            except IndexError:
                print('Нету подходящих. Попробуйте загрузить больше вакансий или снизить требования.')
                sys.exit()
