numbers=[1,10,5,16,4,9,10]
letters=['a','g','s','b','y','a','s']
print(numbers)
print(letters)

val = min(numbers)
print(val)
val = max(numbers)
print(val)
val=max(letters)
print(val)
val=min(letters)
print(val)


# 3. indexten 6ya kadar olanları yazdır
val=numbers[3:6]
print(val)
val=numbers[:3] # baştan 3e kadar
print(val)
val=numbers[4:] #4ten sona kadar
print(val)

numbers[4]=40 # eleman güncelleme/değiştirme
print(numbers)

numbers.append(49) # listeye eleman ekleme
print(numbers)

numbers.insert(3,78) #3. indexin önüne ekler 78 i
print(numbers)

numbers.insert(-1,52) #en sondaki elemanın onune ekledik
print(numbers)

numbers.pop(0) # elemanı siler
print(numbers)

numbers.pop(-1) # elemanı siler
print(numbers)

numbers.remove(16) # 16 elemanını arar bulur ve siler
print(numbers)

numbers.sort() #sayısal olarak sıralanır
print(numbers)

letters.sort() #alfabetik olarak sıralanır
print(letters)

numbers.reverse() #listeyi ters cevir
print(numbers)

letters.reverse() #listeyi ters cevirir
print(letters)

print(len(numbers))
print(len(letters))

print(numbers.count(10)) # kaç tane var oldugunu sorar
print(letters.count('a')) # kaç tane var oldugunu sorar

numbers.clear() #elemanları temizledik
print(numbers)

''' daha fazlası icin >>> https://www.w3schools.com/python/python_ref_list.asp
                      >>>https://docs.python.org/3/tutorial/datastructures.html'''




