def add_to_list():
  shopping_list = []
  q = input("would you like to continue  y/n ") 
  while q == "y" :
    x = userinput8()
    shopping_list.append (x)
    q = input("would you like to continue y/n ")
  print (shopping_list)
  return shopping_list

def userinput8():
  x = input("please enter your item ")
  return x 

def delete(shopping_list):
  print(shopping_list)
  print("which item would you like to delete ? ")
  i = int(input("please enter the number of that item"))
  del shopping_list [i]
  print (shopping_list)
  return shopping_list

def view(shopping_list):
  print(shopping_list)


  
def main8():
  stop = False 
  while stop == False:
    z = int(input("what would you like to do ? 1. add to list,  2.   remove item, 3. view list  "))
    if z == 1 :
      listA = add_to_list()
    elif z == 2 :
      delete(listA)
    elif 3 :
      view(listA) 
    else:
      print("invalid input")
    q2 = input("would you like to continue?  y/n ")
    if q2 == "y":
      stop == False 
    else :
      break
main8()
