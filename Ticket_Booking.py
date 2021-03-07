
x = 10
Seats_Booked = 0 #variable to store no. of seats to be booked
Ticket_Cost = 0 # variable to store the cost of ticket
Total_Income =0 # to store total income
Row = int(input('Enter number of rows = \n')) # to store no.of rows
Columns = int(input('Enter number of columns  = \n')) #to store no.of colmns
Total_Seats = Row * Columns # total no.of seats
# Total booked persons details in list
Booked_person = [[None for k in range(Columns)] for i in range (Row)]


class availability:
# static method  to display the seats
    @staticmethod
    def seats_avail():
        vacant_seats ={}
        for i in range(Row):
            seats_in_row = {}
            for j in range(Columns):
                seats_in_row[str(j+1)] = 'S'
            vacant_seats[str(i)] = seats_in_row
        return vacant_seats
    #static method for calculating the percentage of tickets booked
    @staticmethod
    def find_stat():
        percent = (Seats_Booked/Total_Seats) * 100
        return percent
#function calling
class_calling = availability
availability_list = class_calling.seats_avail()
# checking with the conditions
while x != 0:
    print('1. show the Seats \n')
    print('2. Buy a Ticket \n')
    print('3. show Statistics \n')
    print('4. show booked tickets user information \n')
    print('0. for exit')

    x = int(input('choose option -'))
    if x == 1:
        if Columns < 10:
            for col in range(Columns):
                print(col, end = '  ')
            print(Columns)
        else:
            for col in range(10):
                print(col, end=' ')
            for col in range(10, Columns):
                print(col, end=' ')
            print(Columns)

        if Columns < 10 :
            for num in availability_list.keys():
                print(int(num)+1, end = ' ')
                for num1 in availability_list[num].values():
                    print(num1, end= ' ')
                print()
        else:
            count = 0
            for num in availability_list.keys():
                if int(list(availability_list.keys())[count]) < 9:
                    print(int(num)+1, end= ' ')
                else:
                    print(int(num)+1, end=' ')
                count_no = 0
                for no in availability_list[num].values():
                    if int(list(availability_list[num].keys())[count_no]) <= 10:
                        print(no, end=' ')
                    else:
                        print(no, end=' ')
                    count_no +=1
                count += 1
                print()
        print('seats are vacant = ', Total_Seats - Seats_Booked)
    # if we select for buying a ticket execute the below condition
    elif x == 2:
        row_num = int(input('enter row number= \n'))
        col_num = int(input('enter column number = \n'))
        if row_num in range(1, Row+1) and col_num in range(1, Columns+1):
            if availability_list[str(row_num -1)][str(col_num)] == 'S':
                if Row * Columns <= 60:
                    Ticket_Cost = 10
                elif row_num <= int(Row/2):
                    Ticket_Cost = 10
                else:
                    Ticket_Cost = 8
                print('Ticket cost is = ', '$',Ticket_Cost)
                print(" Wanted to book a Ticket")
                option ={
                    "1" : "Yes",
                    "2" : "no"
                }
                print(option)
                choice = int(input( "choose your option:"))
                Information ={} # information filled by the user while booking ticket will store ina dictionary
                if choice == 1:
                    Information['f_Name'] = input('Enter First name - \n')
                    Information['l_Name'] = input('Enter Last name -\n')
                    Information['Gender'] = input('Enter your gender - \n')
                    Information['Phone_Num'] = input('Enter mobile number - \n')
                    Information['Ticket_Cost'] =  Ticket_Cost
                    availability_list[str(row_num -1)][str(col_num)] = 'B' # after boooking a ticket is successfull the solt is replaced with 'B'
                    Seats_Booked += 1
                    Total_Income += Ticket_Cost
                else:
                    continue
                Booked_person[row_num - 1][col_num-1]= Information
                print("Booked succesfully")
            else:
                print("Slot is already booked try with another seat....")
    #Executes when we select a call with Statistics
    elif x == 3:
        print('No. of ticket purchased = ', Seats_Booked) # it is initially zero but updated whne a user booked ticket
        print('percentage -', class_calling.find_stat()) # called from class availability
        print('Current Income- ', '$', Ticket_Cost)# initally set to zero it count varies when ticked is booked
        print('total income-','$',Total_Income)# price is added of the tickets booked
    # executes when select for user information details
    elif x == 4:
        enter_row = int(input('enter row number - \n'))
        enter_col = int(input('Enter column number =\n'))
        if enter_row in range(1, Row+1) and enter_col in range(1, Columns+1):
            if availability_list[str(enter_row-1)][str(enter_col)] == 'B':
                user = Booked_person[enter_row-1][enter_col-1]
                print('fname-',user['f_Name'])
                print('lname-',user['l_Name'])
                print('Gender-',user['Gender'])
                print('phonenum-',user['Phone_Num'])
            else:
                print(" vacancy seats available")
        else:
            print("invalid input")
    else:
        print("invalid input")




