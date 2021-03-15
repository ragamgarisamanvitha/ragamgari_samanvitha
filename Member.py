
class Member:
    def __init__(self, name='', age='', gender='', mobNo='', joiningDate=''):
        self.__fname = fname
        self.__mobNo = mobNo
        self.__age = age
        self.__gender = gender
        self.__email = email
        self.__bmi = bmi
        self.__duration = duration
        self.__memberId = IDGenerator.generateMemberID()

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setPhoneNo(self, phoneNo):
        self.__mobNo = mobNo

    def getmobNo(self):
        return self.__mobNo

    def setage(self, age):
        self.__age = age

    def getage(self):
        return self.__age
    
    def setgender(self, gender):
        self.__gender = gender

    def getgender(self):
        return self.__gender

    def setemail(self, email):
        self.__email = email

    def getemail(self):
        return self.__email

    def getbmi(self):
        return BMT.bmi

    def setduration(self,duration):
        self.__duration = duration

    def getduration(self):
        return self.__duration

    def getMemberId(self):
        return self.__memberId

    def __str__(self):
        return self.getName()+" "+self.mobNo()+" "+self.getage()+" "+self.getgender()+" "+self.getemail()+" "+self.getbmi()+" "+self.getduration()+" "+str(self.getMemberId())
    
