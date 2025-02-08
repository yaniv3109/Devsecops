
# for i in range(1,50):
#     print("*"*i)


# user_input = input("enter your fav dish: ")
# c = 0

# for n in user_input:
#     if n == ' ':
#         c+=1
   
# print(c)



# ב-python יש אפשרות של else גם ב-for, בדומה ל-if.

# correct_pin = '0140'

# for i in range(3):
#     user_pin = input("enter pin: ")
#     if user_pin == correct_pin:
#         print("welocme home")
#         break
# else:
#     print("wrong pin")


# תרוץ ללא תנאי, תצא על פי תנאי שיינתן בהמשך. אם לא יינתן תנאי זה יהיה אינסופי
# # while True
# while True:
#     password = input("enter your password: ")
#     if len(password) >= 10:
#         print("right")
#         break
#     else:
#         print("wrong")


# list = ["hello", "python", "world", "text", "code"]

# for word in list:
#     if len(word)<5:
#         break
#     print(word.upper())


# Functions
# return - עוצר את המשך הפונקציה

# *args and **kwargs
# ב-Python, *args ו-**kwargs הם דרכים מיוחדות להעביר פרמטרים לפונקציה כאשר אנחנו לא יודעים מראש את מספר הפרמטרים.

# *args
# כאשר אנחנו משתמשים ב-, כל מה שנעביר לפונקציה אחרי הכוכבית יישמר כ-"tuple". 
# המטרה היא לאפשר לפונקציה לקבל מספר משתנה של ארגומנטים מבלי להגדיר את מספרם מראש.

# def print_numbers(*args):
#     for num in args:
#         print(num)

# # קריאה לפונקציה עם מספר ארגומנטים
# print_numbers(1, 2, 3, 4)

# **kwargs
# משמש כדי לאפשר לפונקציה לקבל מספר לא מוגבל של פרמטרים במבנה של מילות מפתח, כלומר פרמטרים שהמפתחות שלהם הם מילות המפתח של הפונקציה.
# כל מה שנעביר לפונקציה אחרי ה-** יישמר כמילון, שבו כל מפתח הוא שם הפרמטר, והערך הוא הערך שהעברנו.

# def print_student_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# # קריאה לפונקציה עם פרמטרים ממילת מפתח
# print_student_info(name="John", age=20, grade="A")

# print-> end=''
# הפרמטר end של הפונקציה print() קובע מה יופיע בסוף כל קריאה. ברירת המחדל של end היא \n (מעבר לשורה חדשה), אבל אפשר לשנות אותו לערך אחר, כמו רווח, תו אחר, או אפילו להשאיר אותו ריק.

# print("Hello", end=' ')  # שים רווח בסוף
# print("world!")
