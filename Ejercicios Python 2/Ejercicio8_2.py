############ EJERCICIO 8
lista=range(0,1000,1)

prime=[]

for i in lista:
   c=0
   for j in range(1,i):
      if i%j==0:
         c+=1
   if c==1:
      prime.append(i)

print(prime)

   





    



