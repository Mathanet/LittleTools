import random as rd
import sys


"""
========================================================================
            PLEASE READ ME FIRST
========================================================================
According to the periodic table of elements to answer the question
If your answer is right, nothing will be happened.
If your answer is wrong, I'll tell you "No" then you can answer again until your answer is right
The question may as same as the last/next one, I'll fix it one day.
Type "skip" to skip
Type "exit" to quit
You can find the answer in source

Now, let's go!

"""


class Element_table:
    def __init__(self):
        self.table_of_elements = {
            1: {'name': "氢", 'symble': "H", 'valence': +1},
            2: {'name': "氦", 'symble': "He", 'valence': ''},
            3: {'name': "锂", 'symble': "Li", 'valence': ''},
            4: {'name': "铍", 'symble': "Be", 'valence': ''},
            5: {'name': "硼", 'symble': "B", 'valence': ''},
            6: {'name': "碳", 'symble': "C", 'valence': ''},
            7: {'name': "氮", 'symble': "N", 'valence': ''},
            8: {'name': "氧", 'symble': "O", 'valence': -2},
            9: {'name': "氟", 'symble': "F", 'valence': ''},
            10: {'name': "氖", 'symble': "Ne", 'valence': ''},
            11: {'name': "钠", 'symble': "Na", 'valence': +1},
            12: {'name': "镁", 'symble': "Mg", 'valence': +2},
            13: {'name': "铝", 'symble': "Al", 'valence': +3},
            14: {'name': "硅", 'symble': "Si", 'valence': ''},
            15: {'name': "磷", 'symble': "P", 'valence': ''},
            16: {'name': "硫", 'symble': "S", 'valence': -2},
            17: {'name': "氯", 'symble': "Cl", 'valence': -1},
            18: {'name': "氩", 'symble': "Ar", 'valence': ''},
            19: {'name': "钾", 'symble': "K", 'valence': +1},
            20: {'name': "钙", 'symble': "Ca", 'valence': +2},

        
            26: {'name': "铁", 'symble': "Fe", 'valence': +3},
            29: {'name': "铜", 'symble': "Cu", 'valence': +2},
            30: {'name': "锌", 'symble': "Zn", 'valence': +2},
            47: {'name': "银", 'symble': "Ag", 'valence': +1},
            56: {'name': "钡", 'symble': "Ba", 'valence': +2},

            119: {'name': "亚铁离子", 'symble': "Fe^(2+)", 'valence': ''},
            120: {'name': "氢氧根离子", 'symble': "OH^(-)", 'valence': ''},
            121: {'name': "硝酸根离子", 'symble': "NO_3^(-)", 'valence': ''},
            122: {'name': "硫酸根离子", 'symble': "SO_4^(2-)", 'valence': ''},
            123: {'name': "碳酸根离子", 'symble': "CO_3^(2-)", 'valence': ''},
            124: {'name': "铵根离子", 'symble': "NH_4^(+)", 'valence': ''},
            125: {'name': "磷酸根离子", 'symble': "PO_4^(3-)", 'valence': ''},
            126: {'name': "锰酸根离子", 'symble': "MnO_4^(2-)", 'valence': ''},
            127: {'name': "高锰酸根离子", 'symble': "MnO_4^(-)", 'valence': ''},
            128: {'name': "氯酸根离子", 'symble': "ClO_3^(-)", 'valence': ''},
        
        }
        self.q_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
            26, 29, 30, 47, 56, 119, 120, 121, 122,
             123, 124, 125, 126, 127, 128]
        self.q_num = 0

    def main(self):
        # a.get_q_list()
        while True:
            a.get_and_show_question()
            a.first_question()
            a.second_question()
            a.third_question()

    # def get_q_list(self):
    #     for i in self.table_of_elements.keys():
    #         self.q_list.append(i)

    # def show_q_list(self):
    #     a.get_q_list()
    #     print(self.q_list)

    def get_and_show_question(self):
        self.q_num = rd.choice(self.q_list)
        question = self.table_of_elements[self.q_num]['name']
        print(question)

    def first_question(self):
        if self.q_num < 119:
            while True:
                # The first question: Num
                A_num = input('num: ').strip()
                if A_num == 'exit':
                    sys.exit()
                elif A_num == 'skip':
                    break
                elif A_num == 'answer':
                    print(self.q_num)
                elif A_num == str(self.q_num):
                    break
                else:
                    print("No")

        else:
            while True:
                # The first question: Symble
                # only for elements which are NOT in elements table
                A_symble = input('symble: ').strip()
                if A_symble == 'exit':
                    sys.exit()
                elif A_symble == 'skip':
                    break
                elif A_symble == 'answer':
                    print(self.table_of_elements[self.q_num]['symble'])
                elif A_symble == self.table_of_elements[self.q_num]['symble']:
                    break
                else:
                    print("No")

    def second_question(self):
        # The third question: Symble
        # only for elements which are in elements table
        if self.q_num < 119:
            while True:
                A_symble = input('symble: ').strip()
                if A_symble == 'exit':
                    sys.exit()
                elif A_symble == 'skip':
                    break
                elif A_symble == 'answer':
                    self.table_of_elements[self.q_num]['symble']
                elif A_symble == self.table_of_elements[self.q_num]['symble']:
                    break
                else:
                    print("No")

    def third_question(self):
        # The third question: Valence
        # only for elements which are in elements table
        if self.table_of_elements[self.q_num]['valence'] and self.q_num < 119:
            while True:
                while True:
                    A_valence = input('valence: ').strip()
                    try:
                        int(A_valence)
                    except ValueError:
                        print("Please input a integer")
                    else:
                        break
                if A_valence == 'exit':
                    sys.exit()
                elif A_valence == 'skip':
                    break
                elif A_valence == 'answer':
                    print(self.table_of_elements[self.q_num]['valence'])
                elif int(A_valence) == self.table_of_elements[self.q_num]['valence']:
                    break
                else:
                    print("No")


if __name__=='__main__':
    a = Element_table()
    # a.show_q_list()
    a.main()
