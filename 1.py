# x=5
# y=6.2
# z="hello"
# r=3+5j
# print(type(x))
# print(type(y))
# print(type(z))
# a=(1,2,3)
# b={1,2,3}
# c=[1,2,3]
# d={1:"mon",2:"tues"}
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(r))
# print(id(x))
# print(id(y))
# print(id(z))
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))
# print(id(r))
 
 
# #operation
# m=56
# n=2
# print(m+n)
# print(m-n)
# print(m*n)
# print(m/n)
# print(m%n)
# print(m**n)
# print(m//n) #int value return
# print(type(m+n))
# print(type(m-n))
# print(type(m/n))
# print(type(m%n))
# print(type(m*n))
# print(type(m**n))
# print(type(m//n))

# a=13
# b=12
# c=int(a/b)
# print(c)


# a=12.4
# b=20
# c='123.25'
# print(int(a),complex(b),float(c))

# a=int(input())
# b=int(input())
# c=a+b
# print(c)

# a=12
# b=23.5
# c='ABESEC'

# # print(a,b,c,sep='\n')
# print(c,sep='\n')
# print("Hello "+ "World")
# a=input()
# b=input()
# c=a+b
# print(c)
# print("3"*5)
# print(3*5)
# a=10.0
# b= for i in b:
    
# print(a==b)
# h=9
# i=3
# print(h<i)
# print(h<=i)
# print(h==i)
# print(h!=i)
# print(h&i)
# print(h|i)
# print(i^h)
# print(h>>1)#right shift
# print(h<<1)#left shift

# h+=5
# i-=2
# print(h)
# print(i)

# 
# Lt=[1,2,5,7,9]
# print(4 in Lt)
# print(7 in Lt)
# print(4  not in Lt)
# print(7  not in Lt)


#  Python Calculator 

# operator = input("Enter the Operator(+ _ * /)")
# num1 = float(input("Enter the num1"))
# num2= float(input("Enter the num2"))

# if operator=="+":
#     sum=num1+num2
#     print(sum)
# elif operator=="-":
#     sum=num1-num2
#     print(sum)
# elif operator=="*":
#     sum=num1*num2
#     print(sum)
# elif operator=="/":
#     sum=num1/num2
#     print(sum)
 
    
#  Write a program to mention the movie ticket price as per the age
# age = int(input("Enter Your age"))
# if (age>=18):
#     ticket_price = 150
#     print(ticket_price)
# elif (age>=100):
#     ticket_price = 50
#     print(ticket_price)
# elif (age>=5 and age<=18):
#     ticket_price = 100
#     print(ticket_price)
# else:
  
#     print("You are not human Being")
    
#     #  WAP to Check the balance in ATM and to Withdraw the amount in Atm
#     accountNumber=input(" Enter Your Account  Number")
#     PIN=int(input("Enter Your PIN Number"))
    
#     if (PIN == 1234):
#         balance=1000
#         print(balance)
#     else:
#         print("Insufficient Balance")
# Leap Year
year=int(input("Enter the Year: "))

if (year%4==0 and year%100 !=0) or (year%400==0):
    print(f"{year} is a LEap YEar")
else:
    print(f"{year} is a not a LEap YEar")
    