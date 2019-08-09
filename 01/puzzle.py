import random
from collections import deque
from os import system, name

class Puzzler():

    def __init__(self):

        self.columns = []
        self.answer = 0
        self.rowsum = 0

        random.seed(random.randint(1, 100))

        for i in range(0, 7):
            self.columns.append(self.generateColumn())
        self.rowsum = self.answer
        self.shuffle()


    def generateColumn(self):
        column = deque([])
        for i in range(0, 5):           
            column.append(random.randint(1, 9))
        
        self.answer += column[2]
        return column


    def shuffle(self):
        while self.rowsum == self.answer:
            for column in self.columns:
                column.rotate(random.randint(-20, 20))

            self.updateRowSum()


    def move(self, col, dir):
        if dir == '+':
            self.columns[col].rotate(-1)
        elif dir == '-':
            self.columns[col].rotate(1)

        self.updateRowSum()

    def draw(self):
        '''Clear the screen first'''
        if name == 'nt': 
            system('cls') 
        else: 
            system('clear')

        print('========================================================')
        print('                      YOUR GOAL IS {0}                  '.format(self.answer))
        print('========================================================')
        print('[0] - [1] - [2] - [3] - [4] - [5] - [6]')
        print(' |     |     |     |     |     |     |')
        print(' |     |     |     |     |     |     |')
        print(' V     V     V     V     V     V     V')
        for i in range (0, 5):
            row = []
            for column in self.columns:
                row.append(column[i])

            if i is 2:
                self.rowsum = sum(row)
                print('[{0}] - [{1}] - [{2}] - [{3}] - [{4}] - [{5}] - [{6}]  == [{7}]'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], self.rowsum))
            else:
                print('[{0}] - [{1}] - [{2}] - [{3}] - [{4}] - [{5}] - [{6}]'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        print('========================================================')


    def updateRowSum(self):
        row = 0
        for column in self.columns:
            self.rowsum += column[2]

    def puzzleLoop(self):

        complete = False
        while not complete:
            self.draw()

            '''TODO: Handle user input errors'''
            userIn = input('Move a column with:  columnIndex+/-\nExample: 3+\n')

            self.move(int(userIn[0]), userIn[1])

            if self.rowsum == self.answer:
                complete == True

        print("You Solved the puzzle. Yay.")


if __name__ == '__main__':

    p = Puzzler()
    p.puzzleLoop()
