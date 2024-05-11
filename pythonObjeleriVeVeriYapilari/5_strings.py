name='Esma'
surname='Sarıtop'
age=20
#String
greeting='My name is '+ name + ' '+surname+ ' '+ 'and \n I am '+ str(age)+ ' years old.'
length=len(greeting) # kaç karakter oldugunu gosteriri

print(greeting )
print(greeting[0]) #0.indexteki karakteri yazzdırıyor
print(length-1) # sağdan
print(greeting[3:9])
print(greeting[3:]) # üçten sona doğru
print(greeting[:16]) # bastan basla 16 ya kadar
print(greeting[2:40:2]) # 2 den 40a 2şer 2şer

if 5>4:
  print("hello")


