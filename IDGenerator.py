class IDGenerator:
    @staticmethod
    def generateMemberID():
        f = open("member_id", "r+")
        id = f.readline()
        id = id.strip()
        idw = int(id)
        idw += 1
        f.seek(0)
        f.write(str(idw) + "\n")
        f.truncate()
        f.close()
        return int(id)
