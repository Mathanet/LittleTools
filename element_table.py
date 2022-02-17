import random as rd
import sys

"""
According to the periodic table of elements 
If your answer is true, no anything will be happened.
If your answer is false, I'll tell you "No" then you can answer again until your answer is right
If you want to quit it, please type "exit"
You can find the answer in the source
"""

# A dictionarg of elements
# you can also find the answer here when you forget it.
table_of_elements = {
    1: {'name': "氢", 'symble': "H", 'valence': +1},
    2: {'name': "氦", 'symble': "He", 'valence': ''},
    3: {'name': "锂", 'symble': "Li", 'valence': ''},
    4: {'name': "铍", 'symble': "Be", 'valence': ''},
    5: {'name': "硼", 'symble': "B", 'valence': ''},
    6: {'name': "碳", 'symble': "C", 'valence': ''},
    7: {'name': "氮", 'symble': "N", 'valence': ''},
    8: {'name': "氧", 'symble': "O", 'valence': ''},
    9: {'name': "氟", 'symble': "F", 'valence': ''},
    10: {'name': "氖", 'symble': "Ne", 'valence': ''},
    11: {'name': "钠", 'symble': "Na", 'valence': +1},
    12: {'name': "镁", 'symble': "Mg", 'valence': +2},
    13: {'name': "铝", 'symble': "Al", 'valence': ''},
    14: {'name': "硅", 'symble': "Si", 'valence': ''},
    15: {'name': "磷", 'symble': "P", 'valence': ''},
    16: {'name': "硫", 'symble': "S", 'valence': -2},
    17: {'name': "氯", 'symble': "Cl", 'valence': -1},
    18: {'name': "氬", 'symble': "Ar", 'valence': ''},
    19: {'name': "钾", 'symble': "K", 'valence': +1},
    20: {'name': "钙", 'symble': "Ca", 'valence': +2},

    
}

print("""
========================================================================
                    PLEASE READ ME FIRST
========================================================================
According to the periodic table of elements to answer the question
If your answer is true, nothing will be happened.
If your answer is false, I'll tell you "No" then you can answer again until your answer is right
The question may as same as the last/next one, I'll fix it one day.
If you want to quit it, please type "exit"
You can find the answer in source

Now, let's go!

""")

while True:
    """ The Main Loop"""
    rd_num = rd.randint(1, 20)
    question = table_of_elements[rd_num]['name']
    print(question)

    while True:
        # The first question: Num
        A_num = input('num: ').strip()
        if A_num == 'exit':
            sys.exit()
        elif int(A_num) == rd_num:
            break
        else:
            print("No")

    while True:
        # The second question: Symble
        A_symble = input('symble: ').strip()
        if A_symble == 'exit':
            sys.exit()
        elif A_symble == table_of_elements[rd_num]['symble']:
            break
        else:
            print("No")
    
    
    # The third question: Valence
    if table_of_elements[rd_num]['valence']:
        while True:
            A_valence = input('valence: ').strip()
            if A_valence == 'exit':
                sys.exit()
            elif int(A_valence) == table_of_elements[rd_num]['valence']:
                break
            else:
                print("No")
