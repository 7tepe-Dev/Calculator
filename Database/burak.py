import json

class Datahandler():
    def __init__(self):
        self.history = []
        self.currentnumber = ""

    def readFromDatabase(self,firstnumber):
        x = '{"current": null}'
        y = json.loads(x)    
        
        if (firstnumber!="+" and firstnumber!="-" and firstnumber!="*" and firstnumber!="/"):
            self.currentnumber = (self.currentnumber)+str(firstnumber)
            print(self.currentnumber)
        if isinstance(firstnumber, str):
            
            y["current"] = self.currentnumber
            # self.history.append(y["current"])
            # self.history.append(firstnumber)
            self.history.append({"currentNumber":y["current"], "currentOperator": firstnumber})
            with open('history.txt', 'w') as outfile:
                json.dump(self.history, outfile)
            print(y)
            self.currentnumber = ""
        

        


datahandler = Datahandler()

datahandler.readFromDatabase(3)

datahandler.readFromDatabase(5)
datahandler.readFromDatabase(5)

datahandler.readFromDatabase("+")

datahandler.readFromDatabase(4)
datahandler.readFromDatabase(9)
datahandler.readFromDatabase(0)
datahandler.readFromDatabase("-")