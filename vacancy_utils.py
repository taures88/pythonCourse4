from vacancy import Vacancy

from loadAPI import SuperJobAPI, HeadHunterAPI

All_VACANCY = []

"""функция делает запрос через API и собирает вакансии HH"""


def vacancies_hh():
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies('Python')
    for info in hh_vacancies['items']:
        name_profession = info['name']
        if info['salary'] is None:
            salary = 0
        else:
            salary = info['salary']['from']
        url = info['alternate_url']
        requirement = info['snippet']['requirement']
        vacancy = Vacancy(name_profession, salary, url, requirement)
        All_VACANCY.append(vacancy)
    return All_VACANCY


"""функция делает запрос через API и собирает вакансии SJ"""


def vacancies_superjob():
    superjob_api = SuperJobAPI()
    superjob_vacancies = superjob_api.get_vacancies('Python')
    for info in superjob_vacancies['objects']:
        name_profession = info['profession']
        salary = info['payment_from']
        url = info['link']
        requirement = info['candidat']
        vacancy = Vacancy(name_profession, salary, url, requirement)
        All_VACANCY.append(vacancy)
    return All_VACANCY


def user_interaction():
    """Функция для ввода пользователем"""

    user_input = input('Hello! Эта программа покажет тебе нужные вакансии \n'
                       'Для продолжения, нажми Enter\n')
    if user_input == '':
        while True:
            user_choice_platform = input('Вы хотите посмотреть вакансии с сайта HeadHunter или SuperJob? \n'
                                         'Чтобы появились с HeadHunter наберите «HH», если хотите с SuperJob наберите - «SJ»\n').lower()
            if user_choice_platform in ['sj']:
                vacancies_superjob()
                break
            elif user_choice_platform in ['hh', 'нн']:
                vacancies_hh()
                break
            else:
                print('Некорректный ввод, попробуйте ещё раз!\n')
        Vacancy.save_all_vacancy_file(All_VACANCY)
        user_salary = input('Укажите минимальную ЗП или просто нажмите Enter.\n')
        user_keyword = input('Введите для удобного поиска дополнительные слова\n'
                             'Пример: «MySQL», «SQL», «Oracle», «PHP» и т.д.\n')
        if user_salary == '':
            user_salary = 0
            print(Vacancy.filter_vacancy(int(user_salary), user_keyword))
        else:
            print(Vacancy.filter_vacancy(int(user_salary), user_keyword))
        while True:

            user_answer = input('Смотреть ещё вакансии?\n'
                                'Чтобы продолжить введите _ Да _\n'
                                'Чтобы выйти введите _ Нет _\n').lower()
            if user_answer in ['да']:
                print(Vacancy.filter_vacancy(int(user_salary), user_keyword))
            elif user_answer in ['нет']:
                print('Досвидания!')
                break
            else:
                print('Некорректный ввод, попробуйте ещё раз!\n')

    elif user_input is not None:
        print('Ошибка ввода.')
