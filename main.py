#Author: Jacob Noethiger jln5438@psu.edu
def digit_sum(n):
  if(n%10==n):
    return n
  else:
    return digit_sum(n//10)+n%10

def run():
  n=input("Enter an int: ")
  print("sum of digits of "+n+" is "+str(digit_sum(int(n)))+".")

if __name__=="__main__":
  run()