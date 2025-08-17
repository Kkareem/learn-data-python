import re

def sum_numbers():

    with open("datasheet/regex_sum_2280148.txt", "r") as file:
        wiki=file.read()

    numbers=re.findall('[0-9]+',wiki)

    print(sum([int(n) for n in numbers]))

sum_numbers()