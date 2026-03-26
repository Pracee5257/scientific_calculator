import math
import matplotlib.pyplot as plt
import numpy as np


# base class

class ScientificCalculator:
  def __init__(self):
    self.a=0
    self.b=0
    self.mode="DEG"

    #mode conversion

  def set_mode(self, mode):
    self.mode=mode
  def to_radians(self,angle):
    return math.radians(angle) if self.mode =="DEG" else angle

  def set_values(self, a, b):
    self.a=a
    self.b=b

  def set_a(self, value):
    self.a= value

  def get_a(self):
    return self.a
  def get_b(self):
    return self.b

  def add(self):
    return self.a + self.b

  def subtract(self):
    return self.a - self.b

  def multiply(self):
    return self.a * self.b

  def divide(self):
    if self.b==0:
      return "Error: Devided by zero!"

    return self.a / self.b
  
  #scientific calculator class


  def power(self):
    return self.a ** self.b

  def square_root(self):
    if self.a < 0:
      return "Error. Negative number"
    return math.sqrt(self.a)

  def sin(self):
    return math.sin(math.radians(self.a))
  
  def cosec(self):
    if math.sin(math. radians(self.a))==0:
     return"Error:Undefined"
    return 1/ math.sin(math.radians(self.a))
  
  def cos(self):
    return math.cos(math.radians(self.a))
  
  def sec(self):
    if math.cos(math. radians(self.a))==90:
     return"Error:Undefined"
    return 1/ math.cos(math.radians(self.a))
  
  def tan(self):
    angle= self.a % 180
    if angle == 90:
      return "Error: tan 90 is undefined"
    return math.tan(math.radians(self.a))
  
  def cot(self):
    if math.tan(math. radians(self.a))==0:
     return"Error:Undefined"
    return 1/ math.tan(math.radians(self.a))
  
  def log(self):
    if self.a <= 0:
      return "Error:Invalid input for log!!! Please enter number which is <=0"
    return math.log10(self.a)
  
  def ln(self):
    if self.a <= 0:
      return "Error:Invalid input for ln!!! Please enter number which is <=0"
    return math.log(self.a)
  
 #graph plotting 

def plot_graph(mode):
  while True: 
    eqn= input("Enter your function(e.g, sin(x),x^3,or type 'back' to return):")
    if eqn.lower() == "back":
      break
    try:
       functions= eqn.split(",")
       plt.figure
       for func in functions:
         eqn= func.strip()
       x= np.linspace(-360,360,2000)
       eqn= eqn.replace("^","**")
       eqn= eqn.replace("sin","np.sin")
       eqn= eqn.replace("cos","np.cos")
       eqn= eqn.replace("tan","np.tan")
       eqn= eqn.replace("1/sin","1/np.sin")
       eqn= eqn.replace("1/cos","1/np.cos")
       eqn= eqn.replace("1/tan","1/np.tan")
       eqn= eqn.replace("log","np.log10")
      
       if "log" in eqn:
         x= np.linspace(0.1,10,1000)

       if mode =="DEG":
         x = np.radians(x)
       else:
         x=x

       y=eval(eqn,{"np":np,"x":x})
       y[np.isnan(y)]= np.nan
       y[np.isinf(y)]= np.nan
       y[np.abs(y)>10]=np.nan
       plt.plot(x,y,label= func.strip())
       plt.xlabel("x axis")
       plt.ylabel("y axis")
       plt.title(f"Graph({mode}mode)")
       plt.grid()
       plt.legend()
       plt.show()
    except  Exception as e:
     print("Invalid Input",e)
  

#programs
scientificCalculator=ScientificCalculator()

history=[]

while True:
  print("\n--- Scientific Calculator ---")
  print(f"Mode:{scientificCalculator.mode}")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Power")
  print("6. Square Root")
  print("7. Sin")
  print("8. Cos")
  print("9. Tan")
  print("10. Log")
  print("11. Cosec")
  print("12. Sec")
  print("13. Cot")
  print("14. ln")
  print("15. Plot Graph")
  print("16. Switch mode")
  print("17. Show History")
  print("18. Exit")

  choice=input("Choose an option: ")

  if choice =='18':
    break

  if choice in ['1', '2', '3', '4', '5']:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    scientificCalculator.set_values(a, b)


  elif choice in ['6', '7','8','9','10','11','12','13','14']:
    a=float(input("Enter a number: "))
    scientificCalculator.set_a(a)

       #operations

  if choice=='1':
    result= scientificCalculator.add() 
    history.append(f"{a}+{b}={result}")
  elif choice=='2':
    result= scientificCalculator.subtract() 
    history.append(f"{a}-{b}={result}")
    
  elif choice=='3':
    result= scientificCalculator.multiply() 
    history.append(f"{a}*{b}={result}")
    
  elif choice=='4':
    result= scientificCalculator.divide() 
    history.append(f"{a} / {b}={result}")
    
  elif choice == '5':
    result= scientificCalculator.power() 
    history.append(f"{a}^{b}={result}")
    
  elif choice == '6':
    result= scientificCalculator.square_root() 
    history.append(f"√{a}={result}")
    
  elif choice == '7':
    result= scientificCalculator.sin() 
    history.append(f"sin{a}={result}")

  elif choice == '8':
    result= scientificCalculator.cos() 
    history.append(f"cos{a}={result}")


  elif choice == '9':
    result= scientificCalculator.tan() 
    history.append(f"tan{a}={result}")

  elif choice == '10':
    result= scientificCalculator.log() 
    history.append(f"log{a}={result}")


  elif choice == '11':
    result= scientificCalculator.cosec() 
    history.append(f"cosec{a}={result}")

  elif choice == '12':
    result= scientificCalculator.sec() 
    history.append(f"sec{a}={result}")

  elif choice == '13':
    result= scientificCalculator.cot() 
    history.append(f"cot{a}={result}")

  elif choice == '14':
    result= scientificCalculator.ln() 
    history.append(f"log{a}={result}")

  
  elif choice == '15':
    print("Plotting Graph......")
    plot_graph(scientificCalculator.mode)
    continue
    

  elif choice =='16':
    if scientificCalculator.mode =="DEG":
      scientificCalculator.set_mode("RAD")
    else:
      scientificCalculator.set_mode("DEG")
    print("Mode Switched")
    continue

  elif choice == '17':
    print("\n--- Recent Histories---")
    for item in history:
      print(item)
    continue
    
  else:
    print("Invalid Choice ")
    continue

  print("Result:", result)






