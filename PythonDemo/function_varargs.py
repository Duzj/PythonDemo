#用* 来表示可变参数(就是元组),** 表示字典(字典)
def total(a=5,*number,**phonebook):
    print('a',a)

    for single_item in number:
        print('single_item',single_item)


    for [first_part, second_part] in phonebook.items():
        print(first_part,second_part)


print(total(10,1,2,3,jack=1123,john=2231,inge=1560))
