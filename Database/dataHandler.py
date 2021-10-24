import json
import time #timestamp eklenecek

class Datahandler():
    def __init__(self):
        self.operatorSymbols = ["+", "-", "*", "/", "="]
        self.history = []
        self.currentnumber = ""

    def readFromDB(self,userInput):
        x = '{"current": null}'
        y = json.loads(x)          
        if (userInput not in self.operatorSymbols):
            self.currentnumber = (self.currentnumber)+str(userInput)
            print(self.currentnumber)
        if isinstance(userInput, str):            
            y["current"] = self.currentnumber
            self.history.append({"currentNumber":y["current"], "currentOperator": userInput})
            with open('Database/history.txt', 'w') as outfile:
                json.dump(self.history, outfile)
            print(y)
            self.currentnumber = ""
        
   
datahandler = Datahandler()

datahandler.readFromDB(3)
datahandler.readFromDB(5)
datahandler.readFromDB(5)

datahandler.readFromDB("+")

datahandler.readFromDB(4)
datahandler.readFromDB(9)
datahandler.readFromDB(0)

datahandler.readFromDB("=")

