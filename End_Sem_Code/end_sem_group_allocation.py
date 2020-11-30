import pandas as pd
import math
import csv
import re
import os

pwd = os.getcwd


def del_folder(directory=".", pwd=pwd()):
    for root, dirs, files in os.walk(directory, topdown=False):
        if (directory == '/'):
            return None
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


def open_dir(directory=".", pwd=pwd()):
    if (directory == "."):
        return
    try:
        os.chdir(directory)
    except:
        os.mkdir(os.path.join(pwd, str(directory)))
        os.chdir(directory)

    return None


filename = "Btech_2020_master_data.csv"
headers = []
raw_data = []
root_folder = pwd()

with open(filename, 'r') as input_file:
    reader = csv.DictReader(input_file)
    headers = reader.fieldnames
    for row in reader:
        raw_data.append(row)


# print(raw_data)

def append(file_name, headers, elements):
    if (os.path.exists(file_name)):
        with open(file_name, 'a', newline='') as output_file:
            writer = csv.writer(output_file, delimiter=",")
            writer.writerow(elements)
    else:
        with open(file_name, 'w', newline='') as output_file:
            writer = csv.writer(output_file, delimiter=",")
            writer.writerow(headers)
            writer.writerow(elements)

def Branch_Wise_data(row):
    open_dir(root_folder)
    open_dir("Individual" + ".csv")
    row1 = row['Roll']
    pattern = re.compile(r'\D+')
    found = re.findall(pattern, row1)
    if found:
        name = found[0]
    file_name = str(name) + ".csv"
    data = row_data(row)
    headers = ["Roll", "Name", "Email"]
    append(file_name, headers, data)

def row_data(row):
    Roll = row[headers[0]]
    Name = row[headers[1]]
    Email = row[headers[2]]

    subtitle = list((Roll, Name, Email))
    return subtitle




def Branch_Strength():
    Branch = []
    for row in raw_data:
        Branch_Wise_data(row)
        row1 = row['Roll']
        pattern = re.compile(r'\D+')
        found = re.findall(pattern, row1)
        if found:
            Branch.append(found[0])
    Branch = list(set(Branch))

    for name in Branch:
        file_name_1 = str(name) + ".csv"
        length = 0
        with open(file_name_1, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                length += 1
        length = length - 1

        file_name_2 = "branch_strength" + ".csv"
        data = list((name, length))
        print(data)
        headers = ["Branch", "Strength"]
        append(file_name_2, headers, data)


def grouping(branch, strength, number_of_groups):
    strength = int(strength)
    group_strength = strength // number_of_groups
    elements = []
    for num in range(number_of_groups):
        num = num + 1
        elements.append(group_strength)
    left = strength % num

    sublist = list((branch, strength, elements, left))
    return sublist


def group_allocation(filename, number_of_groups):
    del_folder(directory="Individual" + ".csv", pwd=pwd())

    Branch_Strength()

    List1 = []
    for num in range(number_of_groups):
        num = num + 1
        name = "G" + str(num)
        List1.append(name)
    # print(List1)

    List2 = []
    with open("branch_strength.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            List2.append(row)

    file_name = "Logics" + ".csv"
    for List in List2:
        # print(List)
        # print(List['Strength'])
        data = grouping(List['Branch'], List['Strength'], number_of_groups)
        headers = ["Branch", "Strength", List1, "Left"]
        append(file_name, headers, data)


number_of_groups = 10

group_allocation(filename, number_of_groups)

