from click._compat import raw_input
from GymManager import GymManager
from Member import Member 

gymManager = GymManager()
print ("\n")
print ("   *****The Body Shop Fitness Center*****")
print ("Select the Option from Menu")


def menu():
    print ("1. New member")
    print ("2. Existing Member")
    print('3. Super User')
    print ("\nEnter You Choice: ")

menu()

while(True):
    input = int(raw_input())
    if input == 1:
        name = str(raw_input("Enter Member's name - "))
        phoneNo = str(raw_input("Enter member's phone no. - "))
        joinDate = str(raw_input("Enter duration - "))
        customer = Customer(name, phoneNo, duration)
        gymManager.addCustomer(customer)

    elif input == 2:
        print ("CustomerID\tName\tPhone\tduration")
        for memId in gymManager.members.keys():
            member = gymManager.members[memId]
            memberId = memId
            name = member.getName()
            mobNo = member.getmobNo()
            duration = member.getduration()
            print (str(memberId) + "\t" + name + "\t" + phoneNo + "\t" + duration)



    elif input == 3:
        GymManager()
    
