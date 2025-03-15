def main():
#Find the largest number among three numbers
 l = []
 num1 = eval(input("Enter the first number:"))
 l.append(num1)
 num2 = eval(input("Enter the second number:"))
 l.append(num2)
 num3 = eval(input("Enter the third number:"))
 l.append(num3)

 print("The largest number among the three is:",str(max(l)))
main()
