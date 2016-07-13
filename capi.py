#Proyecto GitHub para windows

print("Bienvenido")
print()
print("Este programa dira si el numero ingresado es capicua o no")
print()

n = int(input("Por favor ingrese un numero: "))
s=0
k=n;

while(n!=0):
    r=n%10;
    s=s*10+r;
    n=n/10;
    
if(s==k):
    print("El numero ingresado es capicua ");
    
else:
    print("El numero ingresado no es capicua ")

#Fin del programa
