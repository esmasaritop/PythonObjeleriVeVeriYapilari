message= ' Hello There. My name is Esma Sarıtop'

message= message.upper() # bütün karakterleri büyük harfe çevirir
print(message)
message=message.lower() # bütün karakterler küçük harf
print(message)
message= message.title() # kelimelerin ilk harfleri büyük
print(message)
message= message.capitalize() #sadece ilk kelimenin bas harfi büyük
print(message)
message=message.strip() #bastaki ve sondaki boslugu siler
# > soldan silmek için lstrip()
# > sağdan silmek icin rstrip()
print(message)
message=message.split() #cumleyi parçalara ayırır kelime kelime
print(message)
message= '--'.join(message) #parçaları birleştirir
print(message)
index= message.find('esma') # bu kelimenin cumle icinde varlıgını kontrol eder
# eğer varsa pozitif bir sayı doner yani o kelimenin basladıgı index numarasını doner
#yoksa -1 doner
print(index)
isFound= message.startswith('H') # cumle bu karakter ile mi başlar
print(isFound)
isFound= message.startswith('h') #cümle bu karakter ile mi başlar
print(isFound)
isFound= message.endswith('p') # p karakteri ile mi bitiyor
print(isFound)
message=message.replace('--', '..') # kelime veya karakter değiştirme
print(message)
message=message.center(100,'*') # örneğin 100 karakterlik bir bosluk verir ve mesajımızı bu karakter boslugunun icine ortalar
print(message)
message=message.ljust(20,'*') #soldan yıldızlayarak 100 karakteri olusturu
print(message)
message=message.rjust(100,'*')#sağdan yıldızlayarak 100 karakteri olusturur
print(message)
message=message.count('a') # kaç tane a karakteri var
print(message)

'''  daha cok method icin >>> https://www.w3schools.com/python/python_ref_string.asp
   >>> https://docs.python.org/3/library/stdtypes.html#string-methods


'''


