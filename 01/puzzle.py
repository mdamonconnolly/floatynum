import random
from collections import deque
from os import system, name

class Puzzler():

    def __init__(self):

        self.columns = []
        self.answer = 0
        self.rowsum = 0

        random.seed(50)

        for i in range(0, 7):
            self.columns.append(self.generateColumn())


        print(self.columns)
        self.shuffle()
        print(self.columns)



    def generateColumn(self):
        column = deque([])
        for i in range(0, 5):           
            column.append(random.randint(0, 9))

        self.answer += column[2]

        return column


    def shuffle(self):
        
        for column in self.columns:
            column.rotate(random.randint(-20, 20))


    def move(self, col, dir):
        
        if dir == '+':
            self.columns[col].rotate(-1)
        elif dir == '-':
            self.columns[col].rotate(1)

    def draw(self):

        '''Clear the screen first'''
        if name == 'nt': 
            system('cls') 
        else: 
            system('clear')

        print('========================================================')
        print('                      YOUR GOAL IS {0}                  '.format(self.answer))
        print('========================================================')
        for i in range (0, 5):
            row = []
            for j in self.columns:
                row.append(j[i])

            if i is 2:
                self.rowsum = sum(row)
                print('[{0}] - [{1}] - [{2}] - [{3}] - [{4}] - [{5}] - [{6}]  == [{7}]'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], sum(row)))
            else:
                print('[{0}] - [{1}] - [{2}] - [{3}] - [{4}] - [{5}] - [{6}]'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

        print('========================================================')

    def puzzleLoop(self):
        
        while self.answer != self.rowsum:

            self.draw()
            
            userIn = input('Move a column with:  columnIndex, +/-\n')

            self.move(userIn.split(',')[0], userIn.split(',')[1])
