para="""     Python is a high-level, easy-to-learn programming language known for its simplicity and readability. It supports multiple programming styles, including procedural, object-oriented, and functional programming."""
print(len(para))
print("First character=",para[0])
print("Last character=",para[-1])
print("\nShort Preview=",para[:50])
print(para.replace("Python","PYTHON"))
print(para.lower())
print(para.strip())
print(para.split(" "))

if "course" in para:
    print("Word Found")
else:
    print("Word Not Found")

desc="The course description is {} characters long and has {} words".format(len(para),len(para.split(" ")))
print(desc)