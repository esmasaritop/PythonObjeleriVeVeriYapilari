name=('Esma')
surname='Sarıtop'
age=20
#süslü parantez yerine formatı yazıyorlar

print('My name is {}'.format(name))
#her süslü parantezin bir index numarası vardır ve o index numarasına göre yerleşir formatlar
print('My name is {} {}'.format(name,surname))

#indexe gelecek değerlerin yerini değişmek istersek
print('My name is {1} {0}'.format(name,surname))

#veya başka bir çeşit de değişken ile yapma
print('My name is {s} {n}'.format(n=name,s=surname))

print("My name is {} {} and I'm {} years old.".format(name,surname,age)) #tip dönüşümü yapmaya gerek yok

result=200/700
#noktadan sonra 3 gelmesi noktadan sonra 3 haneyi yazdırır noktadan once yazdıgımız 1 sayısı
# noktadan oncesi icin kac karakter bosluk bırakmasını söyler
print('the result is {r:1.3}'.format(r=result))

#f strinf tırnagın basına f eklemek değişen isimlerini de parantezlerin içine yazmak
print(f"My name is {name} {surname} and I'm {age} years old.")
