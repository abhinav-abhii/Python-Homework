Frontend={"Abhinav","Afsal","Azar"}
Backend={"Abhinav","Aromal","Abdu","Anandhu"}
Backend.add("Alfin")
Frontend.remove("Azar")

intersection=Frontend.intersection(Backend)
print("Frontend and Backend both:",intersection)

only_backend=Backend.difference(Frontend)
print("Only Backend students:",only_backend)

unique=Frontend.union(Backend)
count=len(unique)
print("Total unique students:",count)


dict={
    "Frontend":len(Frontend),
    "Backend":len(Backend)
}

for course, students in dict.items():
    print(f"Course: {course}, Students: {students}")

courses_with_fullstack = {**dict, "Fullstack": sum(dict.values())}
print("Courses with Fullstack added:", courses_with_fullstack)



