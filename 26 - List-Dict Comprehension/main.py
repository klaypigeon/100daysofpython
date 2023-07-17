# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [pow(n, 2) for n in numbers]
# print(squared_numbers)
#
# result = [n for n in numbers if n % 2 == 0]
# print(result)
#
# with open("file1.txt") as f:
#     file_1 = f.readlines()
#
# with open("file2.txt") as f:
#     file_2 = f.readlines()
#
# result = [int(item) for item in file_1 if item in file_2]
#
# print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

weather_f = {day: ((temp_c * 9/5) + 32) for (day, temp_c) in weather_c.items()}
print(weather_f)
