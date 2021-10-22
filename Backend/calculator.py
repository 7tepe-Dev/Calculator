import math


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False


def EnterNumber(self, num):
    self.result = False
    firstnum = txtResult.get()
    secondnum = str(num)(0, END)
    if self.input_value:
        self.current = secondnum
        self.input_value = False
    else:
        if secondnum == '.':
            if secondnum in firstnum:
                return
            self.current = firstnum + secondnum
            self.display(self.current)


def sumOfTotal(self):
    self.result = True
    self.current = float(self.current)
    if self.check_sum == True:
        self.validFunction()
    else:
        self.total = float(txtResult.get())


def display(self, value):
    txtResult.delete(0, END)
    txtResult.insert(0, value)


def validFunction(self):
    if self.op == "add":
        self.total += self.current
    if self.op == "sub":
        self.total -= self.current
    if self.op == "mult":
        self.total *= self.current
    if self.op == "divide":
        self.total /= self.current
    if self.op == "mod":
        self.total %= self.current
    self.input_value = True
    self.check_sum = False
    self.display(self.total)


def operation(self, op):
    self.current = float(self.current)
    if self.check_sum:
        self.validFunction()
    elif not self.result:
        self.total = self.current
        self.input_calue = True
    self.check_sum = True
    self.op = op
    self.result = False


def Clear_Entry(self):
    self.result = False
    self.current = "0"
    self.display(0)
    self.input_value = True


def all_Clear_Entry(self):
    self.Clear_Entry
    self.total = 0


def mathsPM(self):
    self.result = False
    self.current = -(float(txtReslut.get()))
    self.display(self.current)


def cos(self):
    self.result = False
    self.current = math.cos(math.radians(float(txtResuly.get())))
    self.display(self.current)


def cosh(self):
    self.result = False
    self.current = math.cosh(math.radians(float(txtResuly.get())))
    self.display(self.current)


def tan(self):
    self.result = False
    self.current = math.tan(math.radians(float(txtResuly.get())))
    self.display(self.current)


def tanh(self):
    self.result = False
    self.current = math.tanh(math.radians(float(txtResuly.get())))
    self.display(self.current)


def sin(self):
    self.result = False
    self.current = math.sin(math.radians(float(txtResuly.get())))
    self.display(self.current)


def sinh(self):
    self.result = False
    self.current = math.sinh(math.radians(float(txtResuly.get())))
    self.display(self.current)


def log(self):
    self.result = False
    self.current = math.exp(float(txtResuly.get()))
    self.display(self.current)


def pi(self):
    self.result = False
    self.current = math.pi
    self.display(self.current)


def tau(self):
    self.result = False
    self.current = math.tau
    self.display(self.current)


def e(self):
    self.result = False
    self.current = math.e
    self.display(self.current)


def acosh(self):
    self.result = False
    self.current = math.acosh(math.radians(float(txtResuly.get())))
    self.display(self.current)


def asinh(self):
    self.result = False
    self.current = math.asinh(float(txtResult.get()))
    self.display(self.current)


def expm1(self):
    self.result = False
    self.current = math.expm1(float(txtResult.get()))
    self.display(self.current)


def lgamma(self):
    self.result = False
    self.current = math.lgamma(float(txtResult.get()))
    self.display(self.current)


def degrees(self):
    self.result = False
    self.current = math.degrees(float(txtResult.get()))
    self.display(self.current)


def log2(self):
    self.result = False
    self.current = math.log2(float(txtResult.get()))
    self.display(self.current)


def log10(self):
    self.result = False
    self.current = math.log10(float(txtResult.get()))
    self.display(self.current)


def log1p(self):
    self.result = False
    self.current = math.log1p(float(txtResult.get()))
    self.display(self.current)


def backspace(self):
    numLen = len(txtResult.get())
    txtResult.delete(numLen - 1, 'end')
    if numLen == 1:
        txtResult.insert(0, "0")

