'''
###############
#  Lab 5.03   #
###############
In this lab your job is to create a week-long to-do list using a Python dictionary. 
Each key in the dictionary is a day of the week. Each associated value is a list of items to do that day.

The program repeatedly asks the user what action they wish to take ( add or get).

If the user enters get, the program asks for a day of the week, and then returns the to-do list for that day.

If the user enters add, the program asks for a day of the week, then asks for a new item, then adds it to the 
specified list.

If a user tries to add an item that already exists on the list for that day, the program rejects the request.

At the start of the program the dictionary should be totally empty (containing no keys and no values).

---------
-Example-
---------
Here's an example. The program output is shown in bold text, the user input in regular text. (use your imagination)

>>>python3 daily_to_do_list.py
What would you like to do ('add' or 'get')?
add
What day?
Friday
What would you like to add to Fridays to-do list?
practice clarinet
What would you like to do ('add' or 'get')?
get
What day?
Friday
You have to practice clarinet.
What would you like to do('add' or 'get')?

-------
-Bonus-
-------
It's a bit tedious for the user to have to type in three different lines to add an item to a to-do list. 
Use split() to allow the user to input add Friday watch tv and relax.  Create a variation of the program 
that doesn't allow any duplicates across any of the days. Make sure when you add a to-do item that it 
doesn't exist in the to-do lists of any of the days before adding.
'''


# Basic Program
'''
# Weekly To-Do List
to_do_list = {
    "Sunday": "do homework, study for tests, and clean",
    "Monday": "go to the store and eat cookies",
    "Tuesday": "play games and walk dog",
    "Wednesday": "go to school and watch a movie",
    "Thursday": "wake up early (6:00) ",
    "Friday": "make homework list, hang out with friends, and relax",
    "Saturday": "start laundry and dishwasher"
}


# Get Function
def get_func():
    global user_choice
    while True:
        if user_choice == "get":
            day_choice = input("What day?\n")
            if day_choice in to_do_list:
                print(to_do_list[day_choice])
                break
            else:
                print("Sorry, I do not recognize that day! ")


# Add Function
def add_func():
    while True:
        if user_choice == "add":
            day_choice = input("What day?\n")
            if day_choice in to_do_list:
                add_input = input(f"What would you like to add to {day_choice}'s to-do list?\n")
                to_do_list[day_choice] = f"{add_input}, {to_do_list[day_choice]}"
                break
            else:
                print("I do not recognize that day...")
    pass

# Program (Not Bonus)
running = True
while running:
    user_choice = input("What would you like to do ('add' or 'get')?\n")
    if user_choice == "get":
        get_func()
    elif user_choice == "add":
        add_func()
    else:
        print("I'm not sure what that means, make sure you spelled everything correctly! ")
'''

# Program W/ Bonus

# Weekly To-Do List
to_do_list = {
    "Sunday": "do homework, study for tests, and clean",
    "Monday": "go to the store and eat cookies",
    "Tuesday": "play games and walk dog",
    "Wednesday": "go to school and watch a movie",
    "Thursday": "wake up early (6:00) ",
    "Friday": "make homework list, hang out with friends, and relax",
    "Saturday": "start laundry and dishwasher"
}



# Can't Be Duplicate Tasks 
def no_dupes():
        for i in task_choice:
            if i in to_do_list[day_choice]:
                print(f"{i} is already in that list, not adding!")
                break
            else:
                to_do_list[user_choice[1]] = f"{user_choice[2]}, {to_do_list[user_choice[1]]}"
                


# Get Function
def get_func():
    global user_choice
    while True:
        if user_choice[1] in to_do_list:
            print(to_do_list[user_choice[1]])
            break
        else:
            print("Sorry, I do not recognize that day! ")
            break


# Add Function
def add_func():
    while True:
            if user_choice[1] in to_do_list:
                no_dupes()
                break
            else:
                print("I do not recognize that day...")
                break

# Program (Bonus) nothing for bonus completed yet, need to figure out method of splitting users input to distinguish choice of function, day, and additions
running = True
while running:
    user_choice = input("Enter get/add, day, and task1, task2, task 3, etc (if adding):\n")
    user_choice = user_choice.split(sep= None, maxsplit= 2)
    day_choice = user_choice[1]
    for days in to_do_list:
        if user_choice[0] == "get":
            get_func()
            break
        elif user_choice[0] == "add":
            task_choice = user_choice[2].split(sep= ", ", maxsplit= -1)
            add_func()
            break
        else:
            print("I'm not sure what that means, make sure you spelled everything correctly! ")

