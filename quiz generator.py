import random

# Sample question sets with options for each subject
questions = {
    'python': [
        ("What is the output of print(2 ** 3)?", "8", ["6", "8", "9", "10"]),
        ("Which of these is a mutable data type in Python?", "list", ["int", "tuple", "list", "string"]),
        ("How do you define a function in Python?", "def", ["function", "fun", "define", "def"]),
        ("What is the purpose of 'self' in a Python class?", "refers to the instance", 
            ["refers to the instance", "refers to the class", "refers to a method", "refers to a variable"]),
        ("Which module is used to generate random numbers in Python?", "random", ["math", "random", "os", "sys"]),
        ("What is the output of print(len('Python'))?", "6", ["5", "6", "7", "8"]),
        ("Which data type is used to store multiple values in a single variable?", "list", ["int", "str", "list", "float"]),
        ("What keyword is used to create a class in Python?", "class", ["class", "def", "method", "function"]),
        ("What does '==' operator do in Python?", "checks equality", ["checks equality", "assigns value", "compares memory", "checks type"]),
        ("Which method is used to convert a string to uppercase?", "upper", ["capitalize", "upper", "toUpper", "uppercase"]),
        ("What is the output of print(10 // 3)?", "3", ["3", "3.3", "4", "10"]),
        ("How do you write an infinite loop in Python?", "while True:", ["for i in range()", "while i != 0", "while True:", "while 1:"]),
        ("Which keyword is used to handle exceptions in Python?", "try", ["catch", "except", "try", "error"]),
        ("What is the default value returned by a Python function?", "None", ["0", "None", "Null", "undefined"]),
        ("Which Python function is used to open a file?", "open", ["read", "write", "file", "open"]),
        ("What is the purpose of the 'break' statement in Python?", "exit the loop", 
            ["exit the loop", "skip iteration", "restart loop", "end the program"]),
        ("How do you comment a single line in Python?", "#", ["//", "#", "--", "/* */"]),
        ("What is the output of print(3 + 4 * 2)?", "11", ["14", "11", "10", "16"]),
        ("How do you install an external Python package?", "pip install", ["install", "get", "download", "pip install"])
    ],
    'java': [
        ("What is the size of int in Java?", "4 bytes", ["1 byte", "2 bytes", "4 bytes", "8 bytes"]),
        ("Which keyword is used to inherit a class in Java?", "extends", ["inherits", "extends", "super", "this"]),
        ("How do you define a method in Java?", "returnType methodName()", 
            ["methodName returnType()", "define methodName()", "returnType methodName()", "method returnType()"]),
        ("Which of these is the entry point for Java programs?", "main method", 
            ["start method", "init method", "main method", "execute method"]),
        ("How do you define a constant in Java?", "final", ["static", "final", "constant", "def"]),
        ("Which keyword is used to create a new object in Java?", "new", ["new", "create", "make", "build"]),
        ("What is the default value of a boolean in Java?", "false", ["true", "false", "0", "null"]),
        ("Which method is used to compare two strings?", "equals", ["==", "equals", "compareTo", "isEqual"]),
        ("Which loop is used when the number of iterations is known?", "for", ["while", "for", "do-while", "switch"]),
        ("How do you declare an array in Java?", "dataType[] arrayName", 
            ["array dataType arrayName", "dataType arrayName[]", "dataType[] arrayName", "dataType{} arrayName"]),
        ("What does JVM stand for?", "Java Virtual Machine", 
            ["Java Variable Machine", "Java Virtual Machine", "Java Versatile Machine", "Java Version Manager"]),
        ("What is the output of System.out.println(3 + 4 * 2)?", "11", ["10", "11", "14", "16"]),
        ("Which access modifier allows access within the same package?", "default", 
            ["private", "protected", "default", "public"]),
        ("What is the return type of the main method?", "void", ["int", "String", "void", "null"]),
        ("How do you implement an interface in Java?", "implements", ["extends", "implements", "inherits", "interfaces"]),
        ("Which package is automatically imported in every Java program?", "java.lang", 
            ["java.io", "java.util", "java.lang", "java.net"]),
        ("What is the superclass of all classes in Java?", "Object", ["Class", "Main", "Object", "Base"]),
        ("Which keyword is used to terminate a loop?", "break", ["break", "end", "stop", "return"]),
        ("What is the size of a char in Java?", "2 bytes", ["1 byte", "2 bytes", "4 bytes", "8 bytes"]),
        ("What is a constructor in Java?", "initializes objects", 
            ["destroys objects", "initializes objects", "compiles code", "manages memory"]),
        ("Which method is used to find the length of a string?", "length()", 
            ["size()", "length", "count()", "length()"]),
        ("Which keyword is used to refer to the current object?", "this", ["self", "this", "current", "object"])
    ],
    'cpp': [
        ("What is the size of int in C++?", "4 bytes", ["1 byte", "2 bytes", "4 bytes", "8 bytes"]),
        ("Which keyword is used to define a class in C++?", "class", ["define", "class", "struct", "object"]),
        ("How do you define a method in C++?", "returnType methodName()", 
            ["methodName returnType()", "define methodName()", "returnType methodName()", "method returnType()"]),
        ("What is the default access modifier in C++ classes?", "private", ["public", "private", "protected", "internal"]),
        ("How do you write a comment in C++?", "// or /* */", ["// or /* */", "#", "--", "//"]),
        ("Which operator is used for accessing members of a class?", ".", ["::", ".", "->", ":"]),
        ("Which header file is used for input/output in C++?", "iostream", ["iostream", "stdio.h", "stream", "io.h"]),
        ("What is a constructor in C++?", "initializes objects", 
            ["destroys objects", "initializes objects", "compiles code", "manages memory"]),
        ("Which function is used to allocate memory dynamically?", "new", 
            ["malloc", "allocate", "new", "create"]),
        ("What is the return type of the main function?", "int", ["void", "main", "int", "return"]),
        ("How do you define a constant in C++?", "const", ["final", "static", "const", "immutable"]),
        ("What is a pointer in C++?", "stores memory address", 
            ["stores data", "stores memory address", "points to a variable", "is a reference"]),
        ("Which keyword is used to inherit a class in C++?", "public", ["inherits", "public", "extends", "this"]),
        ("What is the output of cout << 5 + 2 * 3?", "11", ["7", "11", "13", "16"]),
        ("What is a destructor in C++?", "destroys objects", 
            ["destroys objects", "initializes objects", "compiles code", "manages memory"]),
        ("How do you declare a template in C++?", "template<typename T>", 
            ["template<T>", "template<class T>", "template<typename T>", "template T"]),
        ("Which loop is guaranteed to execute at least once?", "do-while", ["for", "while", "do-while", "switch"]),
        ("How do you define a string in C++?", "std::string", 
            ["std::string", "string", "char[]", "str"]),
        ("Which library is used for mathematical functions?", "cmath", ["math", "cmath", "mathlib", "math.h"]),
        ("What is the output of cout << 'A' + 1?", "66", ["A1", "66", "B", "Error"]),
        ("How do you handle exceptions in C++?", "try-catch", ["try-catch", "throw-catch", "error-handle", "catch-exception"]),
        ("Which operator is used to access a member of a pointer?", "->", 
            [".", "::", "->", ":"]),
        ("Which keyword is used to define a namespace?", "namespace", 
            ["space", "namespace", "define", "static"])
    ]
}


# User data and progress
users = {}
answered_questions = {'python': [], 'java': [], 'cpp': []}

# Registration
def register():
    print("Register a new user:")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    if username in users:
        print("Username already exists! Try logging in.")
        return False
    users[username] = password
    print("Registration successful!")
    return username

# Login
def login(username):
    print("\nLogin required")
    for _ in range(3):  # allow 3 login attempts
        password = input(f"Enter your password, {username}: ")
        if users.get(username) == password:
            print("Login successful!")
            return True
        else:
            print("Incorrect password. Try again.")
    return False

# Ask questions from a subject
def ask_questions(subject):
    available_questions = [q for q in questions[subject] if q not in answered_questions[subject]]
    
    selected_questions = random.sample(available_questions, 5)
    for question, answer, options in selected_questions:
        print(f"\n{question}")
        # Display options as A, B, C, D
        option_labels = ['A', 'B', 'C', 'D']
        for i, opt in enumerate(options):
            print(f"{option_labels[i]}. {opt}")
        
        user_choice = input("Choose an option (A, B, C, or D): ").upper()
        
        # Map user input to the corresponding option and check if it's correct
        if options[option_labels.index(user_choice)].lower() == answer.lower():
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is {answer}.")
        
        answered_questions[subject].append((question, answer, options))

# Main quiz logic
def main():
    print("Welcome to the Quiz Application!")
    
    # Registration and login process
    username = register()
    if not username:
        return
    
    if not login(username):
        print("Failed to login. Exiting...")
        return
    
    # Quiz selection loop
    while True:
        print("\nChoose a subject:")
        print("1. Python")
        print("2. Java")
        print("3. C++")
        print("4. Exit")
        subject_choice = input("Enter choice: ")
        
        if subject_choice == '1':
            ask_questions('python')
        elif subject_choice == '2':
            ask_questions('java')
        elif subject_choice == '3':
            ask_questions('cpp')
        elif subject_choice == '4':
            print("Exiting the quiz. Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
