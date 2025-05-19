file = open("student_notes.txt", "w")

file.write("This is a sample file.\n")
file.write("We are learning file handling in Python.\n")
file.write("This content is written using write() function.\n")

file.close()

print("Content written to 'student_notes.txt' successfully.")
