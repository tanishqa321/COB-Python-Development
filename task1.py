import random
questions = [
    {"question": "Which symbol is used to comment a single line in Python? A) //  B) --  C) #  D) /* */", "answer": "C"},
    {"question": "Which of the following is NOT a Python data type? A) Integer  B) Float  C) Character  D) Boolean", "answer": "C"},
    {"question": "In Python, how do you declare a variable? A) var x = 5  B) int x = 5  C) x = 5  D) $x = 5", "answer": "C"},
    {"question": "What does the len() function return? A) Maximum length of a list  B) Number of elements in a sequence  C) Length of a string  D) Length of a tuple", "answer": "C"},
    {"question": "Which keyword is used to define a function in Python? A) func  B) function  C) define  D) def", "answer": "D"},
    {"question": "Which data structure in Python is ordered and mutable? A) List  B) Tuple  C) Set  D) Dictionary", "answer": "A"},
    {"question": "What is the output of print('''Hello''' + '''World''')? A) HelloWorld  B) Hello World  C) Hello+World  D) Error", "answer": ""},
    {"question": "What is the purpose of the elif statement in Python? A) To handle exceptions  B) To define a class  C) To check multiple conditions  D) To declare a variable", "answer": "C"},
    {"question": "Which operator is used for exponentiation in Python? A) ^  B) **  C) //  D) **", "answer": "B"},
    {"question": "What is the output of 3 * 3.0 in Python? A) 9  B) 9.0  C) 6.0  D) Error", "answer": "B"},
    {"question": "Which of the following is not a valid variable name in Python? A) my_var  B) 123_var  C) _var  D) var123", "answer": "B"},
    {"question": "What does the import statement do in Python? A) Imports a Python script  B) Imports external modules and libraries  C) Imports data from a file  D) Imports a class", "answer": "B"},
    {"question": "Which of the following is a mutable data type in Python? A) Integer  B) String  C) List  D) Tuple", "answer": "C"},
    {"question": "What is the purpose of a try...except block in Python? A) To define a function  B) To handle exceptions  C) To create a loop  D) To import a module", "answer": "B"},
    {"question": "What is a virtual environment used for in Python? A) To create a new Python interpreter  B) To install Python packages globally  C) To isolate project dependencies  D) To run Python in a virtual reality environment", "answer": "C"},
    {"question": "Which of the following statements is true about Python's indentation? A) Python doesn't require indentation  B) Indentation is only for aesthetics  C) Indentation is used to define code blocks  D) Indentation is optional", "answer": "C"},
    {"question": "What is a lambda function in Python? A) A function that takes no arguments  B) A built-in Python function  C) An anonymous, inline function  D) A function with a large number of arguments", "answer": "C"},
    {"question": "Which operator is used to check if a value is present in a list or tuple in Python? A) &&  B) ||  C) in  D) not", "answer": "C"},
    {"question": "What is the purpose of the break statement in a loop? A) To continue to the next iteration of the loop  B) To exit the loop immediately  C) To skip the current iteration  D) To restart the loop", "answer": "B"},
    {"question": "What does the pop() method do in Python? A) Adds an element to a list  B) Removes the last element from a list  C) Removes the first element from a list  D) Removes an element at a specific index from a list", "answer": "D"},
    {"question": "What is the output of print('''Python'''[::-1])? A) Python  B) nohtyP  C) Error  D) 1", "answer": "B"},
    {"question": "Which of the following is an example of a Python framework for web development? A) Django  B) Jupyter  C) Flask  D) NumPy", "answer": "A"},
    {"question": "What is the purpose of the with statement in Python? A) To declare a variable  B) To create a context manager  C) To define a class  D) To import a module", "answer": "B"},
    {"question": "What is the result of 10 / 3 in Python? A) 3.3333333333333335  B) 3.333333333333333  C) 3.0  D) 3", "answer": "A"},
    {"question": "Which library is commonly used for data analysis and manipulation in Python? A) pandas  B) matplotlib  C) scipy  D) requests", "answer": "A"},
    {"question": "What does the __init__ method in a class do in Python? A) Initializes class attributes  B) Imports a module  C) Defines a class method  D) Calls the constructor", "answer": "A"},
    {"question": "What does the ord() function in Python return? A) The ordinal value of a character  B) The number of characters in a string  C) The position of a character in a string  D) The binary representation of a character", "answer": "A"},
    {"question": "What is the purpose of the format() method in Python strings? A) To remove whitespace from strings  B) To format numbers as currency  C) To concatenate strings  D) To create formatted strings with placeholders", "answer": "D"},
    {"question": "Which statement is used to terminate the current loop iteration and continue to the next one in Python? A) break  B) return  C) continue  D) exit", "answer": "C"},
    {"question": "Which of the following is an example of a Python framework for web development? A) Django  B) Jupyter  C) Flask  D) NumPy", "answer": "A"},
    {"question": "What is the purpose of the with statement in Python? A) To declare a variable  B) To create a context manager  C) To define a class  D) To import a module", "answer": "B"},

]
def select_random_question():
    return random.choice(questions)

def quiz_1():
    score = 0
    num_questions = 5  # You can change the number of questions in the quiz.
    
    for _ in range(num_questions):
        question = select_random_question()
        print(question["question"])
        user_answer = input("Your answer: ").strip().capitalize()  # Convert user input to uppercase.
        
        if user_answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"OOPS Wrong! The correct answer is {question['answer']}.\n")
    
    print(f"HOORAY! Quiz complete! You got {score}/{num_questions} questions correct.")

if __name__ == "__main__":
    print("Welcome to the Random Quiz!")
    quiz_1()
