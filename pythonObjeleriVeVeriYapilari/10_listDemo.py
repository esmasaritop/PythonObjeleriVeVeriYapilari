
#1- "Bmw,Opel,Mazda,Mercedes" elemanlarına sahip bir liste oluşturunuz.
arabalar=['Bmw','Opel','Mazda','Mercedes']


'''
#2- Liste kaç elemanlıdır?
result=len(arabalar)
print(result)
'''

'''
#3-Listenin ilk ve son elemanı nedir
result=arabalar[0]
print(result)
result=arabalar[-1]
print(result) '''

'''
#4- Mazda değerini Toyota ile değiştirin
arabalar[3]='Toyota'
result=arabalar
print(result)
'''

'''
#5-Mercedes listenin bir eleanı mıdır ?
result ='Mercedes' in arabalar
print(result)
'''

'''
#6-Listenin -2 indexindeki değer nedir?
result=arabalar[-2]
print(result)
'''

'''
#7-Listenin ilk üç elemanını alın 
result=arabalar[:3]
print(result)
'''

'''
#8-Listenin son iki elemanının yerine "toyota" ve "Renault" değerlerini ekleyin
arabalar[-2:]=['Toyota','Renault']
result=arabalar
print(result)
'''

'''
#9-Listelerin üzerine 'Nissan' ve 'Audi' değerlerini ekleyin.
result= arabalar +['Audi','Nissan']
print(result)
'''

'''
#10- Listenin son elemanını silin.
del arabalar[-1]
result=arabalar
print(result)
'''

'''
#11- Liste elemanlarını tersten yazdırın
result=arabalar[::-1]
print(result)
'''

'''
#12- Aşağıdaki verileri bir liste içinde saklayınız.

    #studentA= Esma Sarıtop 2004, (70,60,70)
    #studentB= Haktan Sarıtop 2013, (80,80,90)
    #studentC= Emre Sarıtop 2003, (85,97,100)

studentA=['Esma','Sarıtop',2004,[70,60,70]]
studentB=['Haktan','Sarıtop',2013,[80,80,90]]
studentC=['Emre','Sarıtop',2003,[85,97,100]]
students=studentA+studentB+studentC
print(students)
print(students[7][2])
print(students[4][3])
'''














