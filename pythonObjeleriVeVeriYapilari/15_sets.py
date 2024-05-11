fruits={'orange','apple','banana'}
#print(fruits[0]) indexlenemez

for x in fruits:
    print(x)

fruits.add('cherry') # listeye eleman ekleme
print(fruits)
fruits.update(['mango','grape']) #liste üstüne liste ekleme
print(fruits)
fruits.update(['mango','grape','apple']) # liste icinde bir elemandan bir tane olur tekrar eklenemez
print(fruits)
myList= [1,2,5,2,2,2]
print(set(myList)) #set metodu fazla elemanı siler

fruits.remove('mango') #silmek
print(fruits)

fruits.pop() #ilk eleman silinir
print(fruits)



