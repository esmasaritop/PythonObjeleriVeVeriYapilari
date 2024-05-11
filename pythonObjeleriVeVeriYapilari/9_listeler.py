message='hello my name is Esma Sarıtop.'.split() # listeye cevirir her bosluktan ayırır

my_list=[1,2,3]
my_list2=['bir',2,True,5.6]


list1=['one','two','there']
list2=['four','five','six']
numbers=list1+list2
print(numbers)
print(numbers[3]) #3. elemanı getirir
print(len(numbers)) #kaç elemanlı

print(message[2]) # olusturdugumuz listedeki 2. elemanı getirir


userA=['Esma',20]
userB=['Haktan',9]
users=[userA,userB] # iç içe liste oldu
print(users[1][0]) # userB listesindeki 1. indexi yaz yani userB'nin yaşı 