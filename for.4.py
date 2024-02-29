n = int(input("enter the number: "))
estpremier =1
for i in range(2,int(n/2)+1):
    if (n % i ==0):
        estpremier=0
        break
if estpremier ==1:
    print(n,"number is premier") 
else:
    print("the number is not premier")










