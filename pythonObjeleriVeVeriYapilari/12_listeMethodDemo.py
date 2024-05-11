names = ['Ali','Yağmur','Hakan','Deniz']
years=[2004,2004,2013,1973]
'''
# 1- "Cenk" ismini listenin sonuna ekleyiniz.
names.append('Cenk')
print(names)
'''

'''
# 2- "Sena değerini listenin basına ekleyiniz.
names.insert(0,'Sena')
print(names)
'''

'''
# 3- "Deniz" ismini listeden siliniz.
names.remove('Deniz') #remove ile birebir aynı değeri yazıp o değeri siliyoruz
print(names)
names.pop(2) # pop ile indexteki değeri siliyoruz
print(names)
'''

'''
# 4- "Deniz" isminin indexi nedir
index=names.index("Deniz")
print(index)
'''

# 5- "Ali" listenin bir elemanı mıdır
result ="Ali" in names
print(result)

# 6- Liste elemanlarını ters cevirin
names.reverse()
print(names)

# 7- Liste elemanlarını alfabetik olarak sıralayın
names.sort()
print(names)

# 8- years listesini rakamsal büyüklüğe göre sıralayınız
years.sort()
print(years)

# 9- str= "Chavrolet,Dacia" karakter dizisini listeye ceviriniz
str= "Chavrolet,Dacia"
result= str.split(',')
print(result)

# 10- years dizisinin en büyük ve en kücük elemanı nedir?
val=min(years)
print("min değer: ",val)

val= max(years)
print("max değer: ",val)

# 11-years dizisinde kaç tane 2004 değeri vardır?
print(years.count(2004))

# 12- years dizisinin tüm elemanlarını siliniz
years.clear()
print(years)

# 13- Kullanıcıdan alacağımız 3 tane marka bilgisini bir listede saklayınız.
markalar=[]
ilkeleman= input('1.eleman: ')
markalar.append(ilkeleman)
ikincieleman=input('2.eleman: ')
markalar.append(ikincieleman)
soneleman=input('3.eleman: ')
markalar.append(soneleman)
print(markalar)
