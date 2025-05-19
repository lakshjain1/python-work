file = open("student_notes.txt", "r")

content = file.read()

print("File Content:\n")
print(content)

file.close()
