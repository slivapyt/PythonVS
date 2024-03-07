import json


def load_students(stud_lst="students.json"):
    '''Получаем данные о студенте из json'''
    with open(stud_lst, "r") as file:
        data = json.load(file)
        return data


def load_prof(prof_lst="professions.json"):
    '''Получаем данные о профессии из json'''
    with open(prof_lst, "r") as file:
        data = json.load(file)
        return data


def get_student_by_pk(inp_pk: int, students: list):
    '''Распаковка данных о студенте'''
    for stu in students:
        if stu['pk'] == inp_pk:
            return (stu['pk'], stu["full_name"], stu["skills"])
        else:
            print("У нас нет такого студента"), quit()


def get_profession_by_title(inp_title: str, title: list):
    '''Распаковка данных о профессии'''
    for num_title in title:
        if num_title["title"] == inp_title:
            return (num_title["pk"], num_title["title"], num_title["skills"])
        else:
            print("У нас нет такой специальности"), quit()


def check_fitness(student: tuple, profession: tuple):
    '''Сравнение скила студента с требованиями, процент пригодности студента'''
    has = [f for f in profession[2] if f in student[2]]
    lacks = [f for f in profession[2] if not f in student[2]]
    summ = len(has)+len(lacks)
    proc_has = (len(has) / summ)*100
    return {"has": has, "lacks": lacks, "fit_percent": int(proc_has)}
