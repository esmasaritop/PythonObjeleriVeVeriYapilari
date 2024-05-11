website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1- 'course' karakter dizisinde kaç karakter bulunmaktadır?
result=len(course)
length=len(website)
print('1.',result)

#2- 'Website' icinden www karakterini alın.
result=website[7:10]
print('2.',result)

#3- 'Website' icinden com karakterini alın.
result=website[22:25]
print('3.1.',result)
result=website[length-3:length]
print('3.2.',result)

#4-'course' içinden ilk 15 ve son 15 karakterleri alın.
result=course[:15]
print('4.1',result)
result=course[-15:]
print('4.2',result)

#5- 'course' içinden karakterleri ters yazdırın.
result=course[::-1] #tüm karakterleri oldugu gibi yazdır
print('5.',result)


name, surname, age, job= 'Bora', 'Yılmaz', 32 , 'Mühendis'

#6- Yukarıda verilen değişkenler ile kerana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Bora Yılmaz. Yaşım 32 ve mesleğim mühendis.'
result='Benim adım {} {}. Yaşım {} ve mesleğim {}.'.format(name,surname,age,job)
print('6.',result)

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s='Hello world'
s=s[0:6]+'W'+ s[-4:]
print('7.1',s)
result='Hello world'
result=result.replace('w','W')
print('7.2',result)

# 8- 'abc' ifadesinin yan yana 3 defa yazdırın
result='abc'*3
print('8.',result)