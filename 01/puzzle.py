import random
from collections import deque
from os import system, name

class Puzzler():

    def __init__(self):

        self.columns = []
        self.answer_a = 0
        self.answer_b = 0
        self.answer_c = 0
        self.attempts = 0

        random.seed(random.randint(1, 100))

        for i in range(0, 7):
            self.columns.append(self.generateColumn())
        
        self.rowsum_a = self.answer_a
        self.rowsum_b = self.answer_b
        self.rowsum_c = self.answer_c
        self.shuffle()


    def generateColumn(self):
        column = deque([])
        for i in range(0, 5):           
            column.append(random.randint(1, 9))
        self.answer_a += column[0]
        self.answer_b += column[2]
        self.answer_c += column[4]
        return column


    def shuffle(self):
        while self.rowsum_b == self.answer_b:
            for column in self.columns:
                column.rotate(random.randint(-20, 20))

            self.updateRowSum()


    def move(self, col=0, dir='+'):
        if dir == '+':
            self.columns[col].rotate(-1)
        elif dir == '-':
            self.columns[col].rotate(1)

        self.updateRowSum()
        self.attempts += 1

    def draw(self):
        '''Clear the screen first'''
        self.clearscr()

        print('========================================================')
        print('                      YOUR GOAL IS {0}.{1}.{2}                  '.format(self.answer_a, self.answer_b, self.answer_c))
        print('========================================================')
        print('[0] - [1] - [2] - [3] - [4] - [5] - [6]')
        print(' |     |     |     |     |     |     |')
        print(' |     |     |     |     |     |     |')
        print(' V     V     V     V     V     V     V')
        for i in range (0, 5):
            row = []
            for column in self.columns:
                row.append(column[i])

            if i is 0:
                self.rowsum_a = sum(row)
                print('[{0}] - [{1}] - [{2}] - [{3}] - [{4}] - [{5}] - [{6}]  == [{7}]'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], self.rowsum_a))
            elif i is 2:
                self.rowsum_b = sum(row)
                print('[{0}] - [{1}] - [{2}] - [{3}] - [{4}] - [{5}] - [{6}]  == [{7}]'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], self.rowsum_b))
            elif i is 4:
                self.rowsum_c = sum(row)
                print('[{0}] - [{1}] - [{2}] - [{3}] - [{4}] - [{5}] - [{6}]  == [{7}]'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], self.rowsum_c))
            else:
                print('[{0}] - [{1}] - [{2}] - [{3}] - [{4}] - [{5}] - [{6}]'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        print('========================================================')


    def updateRowSum(self):
        self.rowsum_a = 0
        self.rowsum_b = 0
        self.rowsum_c = 0
        for column in self.columns:
            self.rowsum_a += column[0]
            self.rowsum_b += column[2]
            self.rowsum_c += column[4]

    def clearscr(self):
        if name == 'nt': 
            system('cls') 
        else: 
            system('clear')


    def puzzleLoop(self):
        self.attempts = 0
        complete = False
        while not complete:
            self.draw()

            '''TODO: Handle user input errors'''
            userIn = input('Move a column with:  columnIndex+/-\nExample: 3+\n')

            if int(userIn[0]) > -1 and int(userIn[0]) < 7:
                self.move(int(userIn[0]), userIn[1])

            if self.rowsum_a == self.answer_a and self.rowsum_b == self.answer_b and self.rowsum_c == self.answer_c:
                complete = True
        
        self.clearscr()
        print("You Solved the puzzle in {0} attempts".format(self.attempts))


if __name__ == '__main__':

    p = Puzzler()
    p.puzzleLoop()
