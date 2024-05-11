'''
list=[1,2,3]

tuple= (1,'iki', 3)

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])
'''

list=['ali','veli']
tuple=('damla','ayşe')
names=('damla','ayşe','demet')+tuple


#list[0]='ahmet'
#tuple[0]='deniz' # elemaman değişikliği yapılmasına tuple izin vermiyor

print(tuple.count('ayşe'))
print(tuple.index('ayşe'))

print(list)
print(tuple)
print(names)