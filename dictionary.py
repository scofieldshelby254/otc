def main():
    student = {
        "name": "Alice",
        "age": 25,
        "major": "Computer Science",
        "gpa": 3.8,
    }

    print(student["name"])
    print(student["age"])
    print(student["major"])
    print(student["gpa"])

    student = {"name": "Alice", "age": 25}
    student["major"] = "Computer Science"
    student["gpa"] = 3.8

    print(student)
    # {"name": "Alice", "age": 25, "major": "Computer Science", "gpa": 3.8}

    student = {
        "name": "Alice",
        "age": 25,
        "major": "Computer Science",
    }

    student["age"] = 26
    student["major"] = "Data Science"

    print(student)
    # {"name": "Alice", "age": 26, "major": "Data Science"}

    student = {
        "name": "Alice",
        "age": 25,
        "major": "Computer Science",
    }

    del student["age"]

    print(student)
    # {"name": "Alice", "major": "Computer Science"}

    student = {"name": "Alice", "age": 25}

    if "name" in student:
        print("Has name:", student["name"])

    if "major" in student:
        print("Has major")
    else:
        print("No major yet")

    student = {
        "name": "Alice",
        "age": 25,
        "major": "Computer Science",
        "gpa": 3.8,
    }

    for key in student:
        print(key, ":", student[key])

    for key, value in student.items():
        print(key, ":", value)

    student = {"name": "Alice", "age": 25, "major": "Computer Science"}

    keys = student.keys()
    print(keys)

    values = student.values()
    print(values)

    items = student.items()
    print(items)

    major = student.get("major")
    hometown = student.get("hometown", "Unknown")
    print(major)
    print(hometown)

    students = [
        {"name": "Alice", "age": 25, "gpa": 3.8},
        {"name": "Bob", "age": 22, "gpa": 3.5},
        {"name": "Charlie", "age": 23, "gpa": 3.9},
        {"name": "Diana", "age": 24, "gpa": 3.6},
    ]

    for student in students:
        print(student["name"], "has GPA", student["gpa"])

    # Sets
    colors = {"red", "green", "blue", "yellow"}
    numbers = {1, 3, 5, 7, 9}

    colors = {"red", "green", "blue"}
    repeated_numbers = [1, 2, 2, 3, 3, 3, 4, 5]
    unique_numbers = set(repeated_numbers)
    print(unique_numbers)
    empty_set = set()

    colors.add("yellow")
    colors.remove("green")
    print(colors)

    if "red" in colors:
        print("We have red")

    if "yellow" in colors:
        print("We have yellow")
    else:
        print("No yellow")

    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    union = set_a | set_b
    intersection = set_a & set_b
    difference = set_a - set_b
    print(union)
    print(intersection)
    print(difference)

    for color in colors:
        print(color)

    # Choosing a collection
    class_names = ["Alice", "Bob", "Charlie", "Diana"]
    student_info = {
        "name": "Alice",
        "student_id": 12345,
        "major": "Computer Science",
        "gpa": 3.8,
    }
    majors = {
        "Computer Science",
        "Data Science",
        "Computer Science",
        "Mathematics",
    }
    print(majors)

    # A grade book using nested dictionaries and lists
    gradebook_students = [
        {
            "name": "Alice",
            "id": 101,
            "grades": {"math": 95, "english": 88, "science": 92},
        },
        {
            "name": "Bob",
            "id": 102,
            "grades": {"math": 87, "english": 91, "science": 85},
        },
        {
            "name": "Charlie",
            "id": 103,
            "grades": {"math": 92, "english": 86, "science": 94},
        },
    ]


    def get_student_average(students, student_name):
        for student in students:
            if student["name"] == student_name:
                grades = list(student["grades"].values())
                if grades:
                    return sum(grades) / len(grades)
                return 0
        return None


    def add_grade(students, student_name, subject, grade):
        for student in students:
            if student["name"] == student_name:
                student["grades"][subject] = grade
                return True
        return False


    def display_all_students(students):
        for student in students:
            print("\nStudent:", student["name"])
            print("ID:", student["id"])
            for subject, grade in student["grades"].items():
                print(subject, ":", grade)


    alice_average = get_student_average(gradebook_students, "Alice")
    print("Alice's average:", round(alice_average, 2))
    add_grade(gradebook_students, "Alice", "history", 90)
    display_all_students(gradebook_students)

    # Nested collections
    person = {
        "name": "Alice",
        "hobbies": ["reading", "coding", "gaming"],
        "scores": [95, 87, 92, 88],
    }
    print(person["name"])
    print(person["hobbies"])
    print(person["hobbies"][0])
    print(person["scores"][2])

    courses = [
        {"name": "Python", "credits": 3, "grade": "A"},
        {"name": "JavaScript", "credits": 4, "grade": "B"},
        {"name": "SQL", "credits": 3, "grade": "A"},
    ]
    for course in courses:
        print(course["name"], "-", course["grade"])

    school = {
        "name": "Central University",
        "departments": [
            {
                "name": "Computer Science",
                "head": "Dr. Smith",
                "courses": ["Python", "JavaScript", "Database Design"],
            },
            {
                "name": "Mathematics",
                "head": "Dr. Johnson",
                "courses": ["Calculus", "Linear Algebra", "Statistics"],
            },
        ],
    }
    first_department = school["departments"][0]
    print(first_department["name"])
    first_course = school["departments"][0]["courses"][0]
    print(first_course)

    # Filtering, transforming, aggregating, and sorting
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    print(even_numbers)

    numbers_to_double = [1, 2, 3, 4, 5]
    doubled = []
    for number in numbers_to_double:
        doubled.append(number * 2)
    print(doubled)

    total = 0
    for number in numbers_to_double:
        total += number
    print(total)
    print(sum(numbers_to_double))
    print(max(numbers_to_double))
    print(min(numbers_to_double))

    numbers_to_sort = [5, 2, 8, 1, 9, 3]
    print(sorted(numbers_to_sort))
    print(sorted(numbers_to_sort, reverse=True))

    students_by_gpa = [
        {"name": "Alice", "gpa": 3.8},
        {"name": "Bob", "gpa": 3.5},
        {"name": "Charlie", "gpa": 3.9},
    ]
    sorted_by_gpa = sorted(
        students_by_gpa, key=lambda student: student["gpa"], reverse=True
    )
    for student in sorted_by_gpa:
        print(student["name"], student["gpa"])

    # List comprehensions
    numbers = [1, 2, 3, 4, 5]
    doubled = [number * 2 for number in numbers]
    print(doubled)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = [number for number in numbers if number % 2 == 0]
    odd_squares = [number**2 for number in numbers if number % 2 == 1]
    print(even_numbers)
    print(odd_squares)

    student_grades = {"Alice": 95, "Bob": 87, "Charlie": 92}
    names = [name for name in student_grades]
    grades = [grade for grade in student_grades.values()]
    print(names)
    print(grades)

    # Grade-book project functions
    def find_student(students, name):
        for student in students:
            if student["name"].lower() == name.lower():
                return student
        return None


    def add_student(students, name, student_id):
        if find_student(students, name):
            return False
        students.append({"name": name, "id": student_id, "grades": {}})
        return True


    def record_grade(students, student_name, subject, grade):
        student = find_student(students, student_name)
        if student is None:
            return False
        student["grades"][subject] = grade
        return True


    def calculate_average(grades):
        if not grades:
            return 0
        return sum(grades) / len(grades)


    def student_average(students, student_name):
        student = find_student(students, student_name)
        if student is None:
            return None
        return calculate_average(list(student["grades"].values()))


    def display_student_report(students, student_name):
        student = find_student(students, student_name)
        if student is None:
            print("Student", student_name, "not found")
            return

        print("\nStudent:", student["name"])
        print("ID:", student["id"])
        for subject, grade in student["grades"].items():
            print(subject + ":", grade)
        print("Average:", format(student_average(students, student_name), ".2f"))


    def display_gradebook(students):
        if not students:
            print("No students in the grade book")
            return

        for student in students:
            average = student_average(students, student["name"])
            print(
                student["name"],
                "(ID:",
                student["id"],
                ")- Average:",
                format(average, ".2f"),
            )


    def find_top_student(students):
        if not students:
            return None
        return max(
            students,
            key=lambda student: calculate_average(list(student["grades"].values())),
        )


    def find_bottom_student(students):
        if not students:
            return None
        return min(
            students,
            key=lambda student: calculate_average(list(student["grades"].values())),
        )


    def remove_student(students, student_name):
        student = find_student(students, student_name)
        if student is None:
            return False
        students.remove(student)
        return True


    def run_gradebook():
        students = []

        while True:
            print("\nStudent Grade Book")
            print("1. Add a student")
            print("2. Add a grade")
            print("3. View one student's report")
            print("4. View all students")
            print("5. Find the top student")
            print("6. Find the bottom student")
            print("7. Remove a student")
            print("8. Exit")

            choice = input("Choose an option (1-8): ")

            if choice == "1":
                name = input("Student name: ")
                student_id = input("Student ID: ")
                if add_student(students, name, student_id):
                    print("Student added")
                else:
                    print("A student with that name already exists")
            elif choice == "2":
                name = input("Student name: ")
                subject = input("Subject: ")
                try:
                    grade = float(input("Grade: "))
                except ValueError:
                    print("Grade must be a number")
                    continue
                if record_grade(students, name, subject, grade):
                    print("Grade added")
                else:
                    print("Student not found")
            elif choice == "3":
                display_student_report(students, input("Student name: "))
            elif choice == "4":
                display_gradebook(students)
            elif choice == "5":
                student = find_top_student(students)
                if student is None:
                    print("No students in the grade book")
                else:
                    print("Top student:", student["name"])
            elif choice == "6":
                student = find_bottom_student(students)
                if student is None:
                    print("No students in the grade book")
                else:
                    print("Lowest student:", student["name"])
            elif choice == "7":
                if remove_student(students, input("Student name to remove: ")):
                    print("Student removed")
                else:
                    print("Student not found")
            elif choice == "8":
                break
            else:
                print("Invalid choice")

    # Call run_gradebook() to start the interactive grade-book menu.

    # Common collection mistakes and their corrected forms
    student_names = ["Alice", "Bob", "Charlie"]
    print(student_names[0])
    print(student_names[1])

    numbers = [1, 2, 3, 4, 5]
    numbers_without_three = [number for number in numbers if number != 3]
    print(numbers_without_three)

    student = {"name": "Alice"}
    print(student["name"])
    print(student['name'])

    student = {"name": "Alice", "age": 25, "major": "CS"}
    for key in student:
        print(key, ":", student[key])

    numbers = {1, 2, 3, 4, 5}
    numbers_list = list(numbers)
    print(numbers_list[0])

    empty_dictionary = {}
    empty_set = set()
    print(type(empty_dictionary))
    print(type(empty_set))

    # Debugging collections
    debug_students = [
        {"name": "Alice", "gpa": 3.8},
        {"name": "Bob", "gpa": 3.5},
    ]
    print("Students:", debug_students)
    print("First student:", debug_students[0])
    print("First student's name:", debug_students[0]["name"])
    print("Type of students:", type(debug_students))
    print("Type of first student:", type(debug_students[0]))

    student_names = ["Alice", "Bob", "Charlie"]
    print(len(student_names))
    if "Diana" in student_names:
        print(student_names.index("Diana"))
    else:
        print("Diana is not in the list")

    try:
        print(student_names[5])
    except IndexError:
        print("Index does not exist")

    # Collection best practices
    user_tags = {"python", "coding", "programming"}
    student_records = [
        {
            "name": "Alice",
            "id": 101,
            "grades": {"math": 95, "english": 88},
        }
    ]

    sample_data = [
        {
            "departments": [
                {
                    "courses": [
                        {"assignments": [{"grade": 95}]},
                    ],
                },
            ],
        },
    ]
    department = sample_data[0]["departments"][0]
    course = department["courses"][0]
    assignment = course["assignments"][0]
    grade = assignment["grade"]
    print(grade)

    # Real-world collection examples
    users = [
        {
            "id": 1,
            "username": "alice",
            "email": "alice@example.com",
            "posts": ["First post", "Second post"],
            "followers": {"bob", "charlie", "diana"},
        },
        {
            "id": 2,
            "username": "bob",
            "email": "bob@example.com",
            "posts": ["My first post"],
            "followers": {"alice", "diana"},
        },
    ]


    def find_user(users, username):
        for user in users:
            if user["username"] == username:
                return user
        return None


    def get_followers(users, username):
        user = find_user(users, username)
        if user:
            return user["followers"]
        return set()


    def get_posts(users, username):
        user = find_user(users, username)
        if user:
            return user["posts"]
        return []


    shopping_cart = [
        {"product": "Laptop", "price": 999.99, "quantity": 1},
        {"product": "Mouse", "price": 29.99, "quantity": 2},
        {"product": "Keyboard", "price": 79.99, "quantity": 1},
    ]


    def calculate_cart_total(cart):
        total = 0
        for item in cart:
            total += item["price"] * item["quantity"]
        return total


    def find_cart_item(cart, product_name):
        for item in cart:
            if item["product"] == product_name:
                return item
        return None


    def remove_cart_item(cart, product_name):
        for index, item in enumerate(cart):
            if item["product"] == product_name:
                cart.pop(index)
                return True
        return False


    print("Cart total: ${:.2f}".format(calculate_cart_total(shopping_cart)))

    # Common collection patterns
    def search_by_name(items, name):
        for item in items:
            if item["name"] == name:
                return item
        return None


    def get_students_above_grade(students, minimum):
        result = []
        for student in students:
            if student["grade"] >= minimum:
                result.append(student)
        return result


    def group_students_by_major(students):
        groups = {}
        for student in students:
            major = student["major"]
            if major not in groups:
                groups[major] = []
            groups[major].append(student)
        return groups


    def count_occurrences(items):
        counts = {}
        for item in items:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1
        return counts


    def find_statistics(numbers):
        if not numbers:
            return None
        return {
            "total": sum(numbers),
            "count": len(numbers),
            "average": sum(numbers) / len(numbers),
            "maximum": max(numbers),
            "minimum": min(numbers),
        }

if __name__ == "__main__":
    main()
