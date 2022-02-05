print("*********Calculate my score*********")
a=int(input("Assiment"))
b=int(input("Project"))
c=int(input("Major exam"))
g=int(input("Quiz"))
m=int(input("Exam"))
sum=a+b+c+m
print("The result:")
if 90 <= sum <= 100:
    print("A")
elif 80 <= sum <=89:
    print("B")
elif 70<= sum <=79:
    print("C")
elif 60 <= sum <=69:
    print("D")
else:
    print("F")
