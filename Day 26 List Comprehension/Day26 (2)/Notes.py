numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]
name = 'Angela'
letters_list = [letter for letter in name]
range_list = [num * 2 for num in range(1,5)]
names = ['Alex', 'Beth', 'Caroline', 'Dave']
print(names)

short_names = [name for name in names if len(name) < 5]
print(short_names)

#long_names = [new_item for item in list if test]
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

"""notes 2"""
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

#New item for item in list
squared_numbers = [numbers*numbers for numbers in numbers]

print(squared_numbers)

"""notes 3"""

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

#New item for item in list if test
squared_numbers = [numbers*numbers for numbers in numbers if (numbers % 2 ==0)]

print(squared_numbers)

"""notes 4"""

with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()

#result = [new_item for item in list if test]
result = [int(num) for num in file_1_data if num in file_2_data]

print(result)

"""notes 5"""

#new_dict = {new_key:new_value for item in list}

#new_dict = {new_key:new_value for (key,value) in dict.items()}

#new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor']

student_scores = {student:random.randint(1,100) for student in names}

print(student_scores)

passed_students = {student:score for (student,score) in student_scores.items() if (score > 70)}

print(passed_students)


"""notes 6"""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

#How to convert string into list of words
sentence_split =sentence.split()

print(sentence_split)

#new_dict = {new_key:new_value for item in list}
result = {word:len(word) for word in sentence_split}

print(result)

"""notes 7"""

weather_c = {
    "Monday" : 12,
    "Tuesday" : 10,
    "Wednesday" : 15,
    "Thursday" : 21,
    "Friday" : 10

}

weather_f = {day:(temp_c*9/5) + 32 for (day,temp_c) in weather_c.items()}

print(weather_f)

"""Notes 8"""

import pandas

student_dict = {
 "student":  ["Angela" , "James" ,"Lily"],
    "score": [56,76,98]
}

student_df = pandas.DataFrame(student_dict)
print(student_df)

#Loop through a data frame
for (key, value) in student_df.items():
    print(key)

#Loop through rows of a data frame
for (index, row) in student_df.iterrows():
    #print(index)
    #print(key)
    print(row.student)

"""notes 9"""
