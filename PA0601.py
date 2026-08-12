import random

def creatingStudentid() :
 Studentid = ""
 for i in range(1, 6):
  num = str(random.randint(11, 100))
  
  Studentid = Studentid+num

 return Studentid

ID = creatingStudentid()
print(f'StudentNumber: {ID}')

def creatingCode():
 Verifycode = ""
 for i in range (1, 10):
  num = str(random.randint(100, 1000))

 Verifycode = Verifycode + num

 return Verifycode
Code = creatingCode()
print(f'Verification Code: {Code}')