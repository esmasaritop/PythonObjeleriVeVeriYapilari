# key - value seklinde calısır

# 34> istanbul   23>Elazığ
'''
sehirler=['Elazığ','İstanbul']
plakalar=[23,34]
print(plakalar[sehirler.index('Elazığ')])

# print(plakalar['elazıg'])=> 23 olması lazım

plakalar= {'Elazığ':23, 'İstanbul':34}
print(plakalar['Elazığ'])

plakalar['Ankara']=6 # var olmayan bir varlıgı ekler ama
print(plakalar)
plakalar['Elazığ']=233 # var olana yeni değer atar
print(plakalar)
'''

users= {
    'esmasarıtop':20,
    'hasansarıtop':52,
    'emresarıtop':21
}

print(users['hasansarıtop'])

users= {
    'esmasarıtop':{
        'roles':['admin','user'],
        'age':20,
        'emailadresi':'esmasaritop@gmail.com',
        'addresss':'güneykent mah',
        'phone':'12232'
        },
    'hasansarıtop':{
        'roles':['user'],
        'age':51,
        'emailadresi':'hasansaritop@gmail.com',
        'addresss':'güneykent mah',
        'phone':'93232'
    },
    'emresarıtop':{
        'roles':['user'],
        'age':21,
        'emailadresi':'emresaritop@gmail.com',
        'addresss':'yemislik mah',
        'phone':'12267'
    }
}
print(users['esmasarıtop'])
print(users['esmasarıtop']['age'])
print(users['esmasarıtop']['emailadresi'])
print(users['esmasarıtop']['roles'])
print(users['esmasarıtop']['roles'][0])






