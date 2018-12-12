from collections import Counter
from statistics import mean


def average_age_under(people, maxage):
    youngests = [one_preson['age'] for one_preson in people if one_preson['age'] <= maxage]
    return float(sum(youngests))/max(len(youngests), 1)


def get_all_hobbies_list(people):
    return [one_hobbie
            for person in people
            for one_hobbie in person['hobbies']]


def all_hobbies(people):
    return set(get_all_hobbies_list(people))


def hobby_counter(people):
    return Counter(get_all_hobbies_list(people))


def n_most_common(people, n):
    return [key for key, val in hobby_counter(people).most_common(n)]
