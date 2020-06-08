# imports
import json


# global variables
path = "./files/my_folder"
filename = "info.txt"
json_filename = "info.json"
# functions definitions

def testing_csv_1():
    print("Hello, this is my new program.")
    f = open(path + '/' + filename, 'r')
    print(f.closed)
    lines = f.readlines()
    print(type(lines))
    for line in lines:
        print(line)
    # a = f.readline()
    # print(a)
    f.flush()
    f.close()
    print(f.closed)

    f = open(path + '/' + filename, 'a')
    f.write('I added this line programatically!')
    f.flush()
    f.close()


def testing_csv_2():
    with open(path + '/' + filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line)
    print(f.closed)


def write_json(my_object):
    with open("/".join([path, json_filename]), 'w') as f:
        json.dump(my_object, f)

def read_json(path, filename):
    with open("/".join([path, filename]), 'r') as d:
        my_file = json.load(d)
        return my_file


def main():

    testing_csv_1()

    testing_csv_2()

    a = [1, 2, 3, 4, 5]

    b = {
        "first_color": "blue",
        "second_color": "red",
        "third_color": "green"
    }

    print(a)
    print(b)

    b["fourth_color"] = "yellow"

    b["my_list_of_numbers"] = [2, 4, 6, 8, "nine"]

    print(b)

    print(b["my_list_of_numbers"][0])

    for k, v in b.items():
        print(f"The key {k} points to the value {v}.")

    s1 = "I like to read"
    s2 = "books."

    s3 = s1 + " " + s2

    s4 = " ".join([s1, s2, "I mean really, a lot."])

    print(s4)

    write_json(b)

    r1 = read_json(path, json_filename)

    print(r1 == b)

    print(r1)

if __name__ == "__main__":
    main()