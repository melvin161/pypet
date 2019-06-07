print('Welcome to PyPet!')

name = 'Fluffy'
age = 5 
weight = 9.5
hungry = True,
photo = '(=^o.o^=)__'

cat = {
'name': 'fluffy',
'age': 5,
'weight': 9.5
'hungry' : True,
'photo': '(='^o.o^=)__'
}

print ('hello'+ cat['name'])
print(cat['photo'])

def feed(pet):
 if pet['hungry'] == True: 
   pet['hungry'] = False
   pet['weight'] = pet ['weight'] + 1
   else:
     print('The Pypet is not hungry')

print(cat)
feed(cat)
print(cat)
feed(cat)