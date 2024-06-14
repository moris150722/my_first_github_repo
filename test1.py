input_R = input("Please input a Richter scale value: ")
R=float(input_R)
print("Richter scale value:",R)


e=10**((1.5*R)+4.8)
print("Equivalence in Joules:",e)

T=float(e/(4.184*(10**9)))
print("Equivalence in tons of TNT:",T)

lunch=float(e/2930200)
print("Equivalence in the number of nutritious lunches:",lunch)
