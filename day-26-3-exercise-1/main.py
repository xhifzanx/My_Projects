
with open("file1.txt") as data_1:
	content = data_1.readlines()
	print(content)
with open("file2.txt") as data_2:
	content2 = data_2.readlines()
	print(content2)
result = [int(num) for num in content if num in content2]

# Write your code above 👆

print(result)


