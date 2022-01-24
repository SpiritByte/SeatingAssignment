NUM_ROWS = 18
NUM_COLS = 7
AVAIL = '-'
BOOKED = 'X'
ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

seatTable = []
lastrow=0
lastcolumn=[]
# Build seatTable
for i in range(NUM_ROWS):
    column = []
    for j in range(NUM_COLS):
        column.append(AVAIL)
    seatTable.append(column)

 
# Reset Table
def resetTable(seats):
    global lastcolumn
    lastcolumn = []
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            seats[i][j] = AVAIL

 
# Print Table
def printTable1(seats):
    i=1
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print('Row', end=' ')

    for num in range(NUM_COLS):
        print(f'{alpha[num]:2s}'.format(alpha),end='')
    print()

    for num in seats:
        print(f'{str(i):3s}'.format(str(i)), end=' ')
        i+=1
        for j in num:
            print(j,end=' ')
        print()

def printTable(seats, row, column):
    i=0
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print('Row', end=' ')

    for num in range(NUM_COLS):
        print(f'{alpha[num]:2s}'.format(alpha),end='')
    print()

    for num in seats:
        i+=1

        print(f'{str(i):3s}'.format(str(i)), end=' ')
        k=0
        for j in num:
            if i == row+1 and k in column:
                print('O',end=' ') 
            else:
                print(j,end=' ')
            k += 1
        print()

def printTable3(seats):
    i=1
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print('Row', end=' ')

    for num in range(NUM_COLS):
        print(f'{alpha[num]:2s}'.format(alpha),end='')

    print()

    for num in seats:
        print(f'{str(i):3s}'.format(str(i)), end=' ')
        i+=1
        k=0
        for j in num:
            if j == AVAIL:
                print(alpha[k],end=' ')
            else:
                print(j,end=' ')
            k+=1
        print()

def bookseat(seats, row, column):
    for j in column:
        seats[row][j]=BOOKED

def findrow(seats, num):
    for i in range(NUM_ROWS):
        count =0 
        for j in range(NUM_COLS):
            if seats[i][j] == AVAIL:
                count += 1
        if count>=num:
            return i
    return 0


def findcolumn (seats, num, row):
    column=[]
    if num == 1:
        for j in range(NUM_COLS):
            if seats[row][j] == AVAIL:
                column.append (j)
                return column

    elif num == 2:
        if seats[row][0] == AVAIL and seats[row][1] == AVAIL:
            column = column + [0,1]
            return column
        if seats[row][5] == AVAIL and seats[row][6] == AVAIL:
            column = column + [5,6]
            return column
        if seats[row][2] == AVAIL and seats[row][3] == AVAIL:
            column = column + [2,3]
            return column
        if seats[row][3] == AVAIL and seats[row][4] == AVAIL:
            column = column + [3,4]
            return column

    elif num == 3:
        if seats[row][2] == AVAIL and seats[row][3] == AVAIL and seats[row][4] == AVAIL:
            column = column + [2,3,4]
            return column

    elif num >=4 and num<=7:
        index = 0
        start = index
        total = 0
        while index < NUM_COLS and total < num:
            if seats[row][index] != AVAIL:
                index += 1
                start = index
                total = 0
            else:
                index += 1
                total += 1
        if total == num:
            for i in range(num):
                column.append(start+i)
        return column
    return column       
""" 


        for j in range(NUM_COLS-num+1):
            found = j
            for k in range(num):
                if seats[row][j+k] != AVAIL:
                    found ==0
                    break
            if found != 0:
                break
        print(found)
        print (seats[row][found])
        if found != 0:
            for l in range(num):
                column.append(found+l)
            print(column)
            return column
        print(column) 
"""
    

def seat(seats, num):
    column = []

    # 1 find row to assign
    row = findrow(seats, num)

    #2 find columns to assign
    column = findcolumn (seats, num, row)

    while len(column)==0 and row <NUM_ROWS:
        row = row+1
        column = findcolumn (seats, num, row)

    if len(column)==0:
        print ("No seats available")
        return

    # book seats
    bookseat(seats, row, column)
    global lastrow
    global lastcolumn
    lastrow = row
    lastcolumn = column

    # 3 print seat assignments
    seatassign = ""
    for j in column:
        seatassign = seatassign + str(row+1) + ALPHA[j] + " "

    print ("Seating Assignments: " + seatassign)


print ("WELCOME TO MARS AIR SEATING")

while 1==1:
    cnt = input("How many passengers in your group? E-Exit R-Reset P-Print: ")

    if cnt.isalpha():
        if cnt[0].upper()=='E':
            break

        if cnt[0].upper()=='R':
            resetTable(seatTable)

        if cnt[0].upper()=='P':
            printTable(seatTable, lastrow, lastcolumn)

    if cnt.isdigit():
        # 1 find seats to assign
        # 2 assign seats
        # 3 print seat assignments
        seat(seatTable, int(cnt))

