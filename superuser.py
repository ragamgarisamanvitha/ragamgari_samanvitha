class GymManager:
    def __init__(self):
        self.members = dict()
    def addMember(self, customer):
        self.members[customer.getname()] = customer

    

    def save(self):
        GymManager.dump(self, open("gym_manager.bin", "wb"))

