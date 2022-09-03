# List Comprehension
# new_numbers = [new_item for item in list]
# new_numbers = [new_item for item in list if test]# This is a sample Python script.
# Next is Dictionery Comprehension
# new_dictionery = {new_key:new_value for item in list}
# new_dictionery = {new_key:new_value for (key,value) in dict.items()}
# new_dictionery = {new_key:new_value for (key,value) in dict.items() if test}

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# Looping through dictioneries
for (key, value) in student_dict.items():pass
#   print(value)
import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
# Loop through a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":pass
        #print(row.score)
new_dict = {: for (index, row) in student_data_frame.iterrows()}
print(new_dict)