# Day 30
# try, except, else, finally

try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["nonexistentkey"])
except FileNotFoundError:  # Must relate to error type
    print("There was an error, file has been created")
    open("a_file.txt", "w")  # Will create the file
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("code has ended")

"""notes 2"""

# Day 30
# try, except, else, finally

height = float(input("Height:"))
weight = float(input("Weight:"))

if height > 3:
    raise ValueError("Height should not be over 3 metres")

    bmi = weight/height ** 2
    print(bmi)

"""notes 3"""

fruits = ["Apple", "Pear", "Orange"]

# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit + " pie")


make_pie(4)

"""notes 4"""
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},  # Some will have no likes so originally fails
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        total_likes += 0

print(total_likes)

"""notes 5"""

else:
    with open("data.json", "r") as data_file:  # with closes file automatically
        # json.dump(new_data, data_file, indent=4)
        data = json.load(data_file)
        print(type(data))


"""notes 6"""

else:
    with open("data.json", "w") as data_file:  # with closes file automatically
        json.dump(new_data, data_file, indent=4)