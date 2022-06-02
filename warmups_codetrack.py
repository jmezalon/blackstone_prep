# check for factors

def check_for_factor(base, factor):
    return base % factor == 0


# print(check_for_factor(9, 2))


# total number of goals from Messi

def goals(la_liga_goals, copa_del_rey_goals, champion_league_goals):
    return la_liga_goals + copa_del_rey_goals + champion_league_goals


# print(goals(43, 10, 5))


# count up to a given number

def summation(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total


# print(summation(1))


def create_phone_numbers(numbers):
    phone_str = "".join(map(str, numbers))

    area_code, first_three, last_four = phone_str[:3], phone_str[3:6], phone_str[6:]

    return '(' + area_code + ')' + first_three + '-' + last_four


# print(create_phone_numbers([9, 1, 7, 6, 0, 0, 5, 8, 0, 3]))