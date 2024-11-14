#phone_book = {'Den': [892711111,892722],'Max': 892722222}
#print(phone_book)
#phone_book.update({'Sasha': 892733333,
                   #'Alex': 892744444})
#print(phone_book)
#print(phone_book.get('Kamila','такого ключа нет'))
#list_=[1,2,3]
#list_.pop(0)
#print(list_)
#print(phone_book.keys())
#print(phone_book.values())
#print(phone_book.items())
#set_={1,2,3,4,5,1,2,3,4,'string',True,(1,2,3)}
#list_=[1,1,1,2,2,2,3,3,3,2]
#list_=set(list_)
#print(list_)
#print(list_.add(4))
#print(list_)
my_dict = {'Vasya': 1975,'Egor': 1999, 'Masha':2002}
print('Dic:', my_dict)
print('Existing value: ',my_dict['Masha'])
print('Not existing value: ',my_dict.get('Petya'))
print('Deleted value:',my_dict.pop("Egor"))
my_dict.update({'Kamila':1981,'Artem':1915})
print('Modifield dictionary: ',my_dict)
my_set = {1,1,1,1,'Яблоко','Яблоко',42.314,42.314,42.314}
print('Set: ',set(my_set))
my_set.remove(1)
my_set.add((13))
my_set.add((5,6,1.6))
print("Modifield set: ",my_set)

















