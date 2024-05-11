#value types >>> string, number
x = 5
y = 25
x=y
y=10
print(x,y) #x etkilenmez x=25 y=10


#referance types>>> list
a=["apple","banana"]
b=["apple","banana"]
a=b
b[0]= "grape"
print("a:",a,'\n'"b:",b)  #b'de yaptıgım değşiklik a'yı etkiler
