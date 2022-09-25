# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`
from operator import attrgetter, itemgetter

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def load_data_from_csv(raw_csv):
    data = []
    for line in raw_csv.split('\n'):
        name, age = line.split(';')
        data.append({'name': name, 'age': int(age)})
    return data


def asc_sort_data_by_age(data):
    return sorted(data, key=itemgetter("age"))


def filter_data_by_age_ge_than(age, data):
    data = filter(
        lambda user: user["age"] >= age,
        data
    )
    return data


def get_users_list():
    data = load_data_from_csv(csv)
    data = asc_sort_data_by_age(data)
    data = filter_data_by_age_ge_than(10, data)

    return [*data]


if __name__ == '__main__':
    print(get_users_list())
