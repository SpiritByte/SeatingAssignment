
NUM_ROWS = 18
NUM_COLS = 7
AVAIL = '-'
BOOKED = 'X'
ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

seatTable = []
Seated=[]
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

 
# Print Table (X - taken; - Available)
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

# Print Table (the newly assigned seats show O)
def printTable(seats, lastseated):
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
            # i-1, k is last seated
            if [i-1, k] in lastseated:
                print('O',end=' ') 
            else:
                print(j,end=' ')
            k += 1
        print()

# count available seats
def CountAvailSeats(seats):
    cnt=0
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if seats[i][j] == AVAIL: 
                cnt += 1
    return cnt

# last seated
def lastseated (seats):
    for i in range(NUM_ROWS-1,-1, -1):
        for j in range(NUM_COLS-1,-1,-1):
            if seats[i][j] == BOOKED: 
                return [i,j+1]
                break
    return [i,j]

# Book seats
def bookseat(seats, seated):
    for s in seated:
            seats[s[0]][s[1]] = BOOKED

# Print seat assignment
def PrintSeatAssign(seated):
    # print seat assignments
    seatassign = ""
    # s[0] row, s[1] column
    for s in Seated:
        seatassign = seatassign + str(s[0]+1) + ALPHA[s[1]] + " "

    print ("Seating Assignments: " + seatassign) 

# Find row
def findrow(seats, num, startrow):
    i = startrow
    while i < NUM_ROWS:
        count = 0
        for j in range(NUM_COLS):
            if seats[i][j] == AVAIL:
                count += 1
        if count>=num:
            return i
        i += 1
    return -1


# Find Column
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

# Find seat simply
def simplefindseat (seats, num):
    scattcolumn = []
    total = 0
    done = 0
    for i in range(NUM_ROWS):
        if done == 1:
            break
        for j in range(NUM_COLS):
            if seats[i][j] == AVAIL:
                scattcolumn.append([i,j])
                total += 1
                if total == num:
                    done =1
                    break
    return scattcolumn

# Seat
def seat(seats, num):
    if CountAvailSeats(seats) == 0:
        print ("Fully Booked - No more seats available")
        return

    if CountAvailSeats(seats) < num:
        print ("Not enough seats available")
        return
    
    # total seated
    global Seated

    if num > 7:
        seatbig(seats, num)
    else:
        seatsmall (seats, num, 0)
    

    # book seats
    # it is required to book seats in batches so that next batch can find seats properly
    bookseat(seats, Seated)

    # print seat assignments
    PrintSeatAssign (Seated)    

# Seat Small
def seatsmall(seats, num, startrow):
    global Seated
    column = []

    if CountAvailSeats(seats) < num:
        print ("No seats available")
        return

    # find row to assign
    row = findrow(seats, num, startrow)
  
    if row > -1:
        # find columns to assign
        column = findcolumn (seats, num, row)

    # update Seated
    if len(column)>0:
        for j in column:
            Seated.append([row, j])

    # find columns from next row, if no columns of the current row meet the criteria of preference contiguous block
    while len(column)==0 and row <NUM_ROWS-1:
        row = row+1
        column = findcolumn (seats, num, row)
        if len(column)>0:
            for j in column:
                Seated.append ([row, j])

    # simple seat assignment, if no contiguous block
    if len(column)==0:
        ScattedSeated = simplefindseat (seats, num)
        Seated = Seated + ScattedSeated

    return row

# Seat big 
def seatbig (seats, num):
    global Seated
    scattcolumn = []
    total = 0
    l = lastseated (seats)
    #start from latest row
    done = 0 
    for i in range(l[0],NUM_ROWS, 1):
        if done == 1: 
            break
        for j in range(NUM_COLS):
            if i == l[0] and j<l[1]:
                continue
            if seats[i][j] == AVAIL:
                scattcolumn.append([i,j])
                total += 1
                if total == num:
                    done = 1
                    break
    if total<num:
        for i in range(NUM_ROWS):
            if done == 1:
                break
            for j in range(NUM_COLS):
                if seats[i][j] == AVAIL:
                    scattcolumn.append([i,j])
                    total += 1
                    if total == num:
                        done = 1
                        break
    Seated = scattcolumn
    return scattcolumn
    
def main():
    global Seated
    print ("WELCOME TO MARS AIR SEATING")

    while 1==1:
        cnt = input("How many passengers in your group? E-Exit R-Reset P-Print: ")

        if cnt.isalpha():
            #Exit
            if cnt[0].upper()=='E':
                break
            #Reset
            if cnt[0].upper()=='R':
                resetTable(seatTable)
            #Print
            if cnt[0].upper()=='P':
                printTable(seatTable, Seated)

        if cnt.isdigit():
            # 1 find seats to assign
            # 2 assign seats
            # 3 print seat assignments
            Seated = []
            seat(seatTable, int(cnt))

main()
