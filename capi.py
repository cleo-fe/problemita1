<<<<<<< HEAD
#Proyecto GitHub para windows

print("Bienvenido")
print()
=======
print("Programa para saber si un numero es o no capicua")
print()
n = int(input("Ingrese un numero: "))
print()
>>>>>>> origin/master
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
