n = int(input("Ingrese un numero: "))
s=0
k=n;
while(n!=0):
    r=n%10;
    s=s*10+r;
    n=n/10;
if(s==k):
    print("Es capicua ");
else:
    print("No es capicua ")
