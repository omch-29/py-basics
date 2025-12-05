# print("hello")
# a=int(input("Enter your age:"))

# if(a<18):
#     print("INELIGIBLE")
# else:
#     print("ELIGIBLE")

#sum of first n numbers
# n=int(input("Enter number:"))
# sum=0
# for i in range(1, n+1):
#     sum+=i
# print(sum)
#LAMBDA FUNCTION, it is a inline function
sum = lambda a,b: a+b
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print(sum(a,b))