import re


def is_positive_less_than_300(value):
    if re.search(r"[0-9]{1,3}", value):
        return int(value) < 300 and int(value) > 0
    return False

print(is_positive_less_than_300("292"))
print(is_positive_less_than_300("0"))
print(is_positive_less_than_300("-5"))
# print(is_positive_less_than_300("3.14"))
print("========================================")
#2
def is_number_from_1_to_255(value):
    if not re.fullmatch(r"[1-9][0-9]{1,3}", value):
        return False
    return int(value) <= 255 and int(value) >= 1
print(is_number_from_1_to_255("255"))
print(is_number_from_1_to_255("256"))
print(is_number_from_1_to_255("0"))
print(is_number_from_1_to_255("-1"))
print(is_number_from_1_to_255("025"))

#3
print("========================================")
# def is_israel_mobile(phone):
#     clean_phone = phone.replace("-", "")
#     if  re.fullmatch(r"05[0-9]{8}", clean_phone):
#         return True
#     if  re.search(r"\+9725[0-9]{8}", clean_phone):
#         return True
#
#     return False
#
# print(is_israel_mobile("0501234567"))
# print(is_israel_mobile("+972501234567"))
# print(is_israel_mobile("050-123--4567"))


def is_israel_mobile(phone):

    # pattern = r"^(05|-?\+972-?5)[0-9]{1}-?([0-9]{3}-?|[0-9]{2}-?)([0-9]{4}|[0-9]{3})$"
    pattern = r"^(?!.*--)(?:05|\+972-?5)\d(?:-?\d){7}$"
    return bool(re.fullmatch(pattern, phone))


print(is_israel_mobile("0501234567"))
print(is_israel_mobile("+972501234567"))
print(is_israel_mobile("050-123-45-67"))
print(is_israel_mobile("050-123--45-67"))
print(is_israel_mobile("050-1-3-45-67"))

print("========================================")
#4
IS_VALID_TIME_PATTERN = r"([0-1][0-9]|2[0-3]):[0-5][0-9]"
def is_valid_time(time):
    return bool(re.fullmatch(IS_VALID_TIME_PATTERN, time))
print(is_valid_time("12:34"))
print(is_valid_time("23:59"))
print(is_valid_time("24:00"))
print(is_valid_time("00:00"))
print(is_valid_time("00:60"))
print("=========")
#5
IS_ISRAEL_CAR_NUMBER = r"\d{2}-\d{3}-\d{2}|\d{3}-\d{2}-\d{3}"
def is_israel_car_number(car_number):
    return bool(re.fullmatch(IS_ISRAEL_CAR_NUMBER, car_number))

print(is_israel_car_number("12-345-78"))
print(is_israel_car_number("123-56-789"))





