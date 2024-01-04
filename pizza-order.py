print("Thank you for choosing Python Pizza Deliveries!")
size = input() 
add_pepperoni = input()
extra_cheese = input() 
bill = 0
if size == "S" :
  bill+=15
  if add_pepperoni == "Y" :
      bill+=2
else:
  if size == "M" :
    bill+=20
    if add_pepperoni == "Y" :
      bill+=3
  elif size == "L" :
    bill+=25
    if add_pepperoni == "Y" :
      bill+=3
      
if extra_cheese == "Y" :
  bill+=1

print("Thank you for choosing Python Pizza Deliveries! Your final bill is: ",bill)

  
