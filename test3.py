print("Welcome to the simple calculator program! ")


while True:
  input_a = input("Enter the first number:")
  input_b = input("Enter the second number:")
  input_c = input("Select an arithmetic operation(+, -, *, /):")

  a = float(input_a)
  b = float(input_b)

  if b==0:
    print("Error: Division by zero!")
  else:
       if input_c=="+":
	       Result=a+b
       elif input_c=="-":
	       Result=a-b
       elif input_c=="*":
	       Result=a*b
       elif input_c=="/":
	       Result=a/b
       print("Result:",Result)

  input_d=input("Do you want to perform another calculation?(yes or no):")
  d=str(input_d)
  if d=="no":
        print("Goodbye!")
        break 
