input_amount = input("Enter the shopping amount: ")
input_level = input("Enter the shopping level(Regular or Gold): ")

A=float(input_amount)
L=str(input_level)

if L == "Regular":
  if A<1000:
    print("Regular $",A)
  elif 2000>A>1000:
    print(A*0.9)
  elif 3000>A>2000:
    print(A*0.85)
  elif A>3000:
    print(A*0.80)

elif L == "Gold":
  if A<1000:
    print("Gold $",A)
  elif 2000>A>1000: 
    print(A*0.85)
  elif 3000>A>2000:
    print(A*0.80)
  elif A>3000:
    print(A*0.75)

else:
  print("Invalid member level. Please enter \"Regular\" or \"Gold\" ")
