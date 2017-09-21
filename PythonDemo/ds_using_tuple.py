#元组是不可变的
zoo = ('python','elephant','penguin')
print('number of animals in the zoo is',len(zoo))

new_zoo = 'monkey' ,'camel',zoo

print('number of cages in the new zoo is',len(new_zoo))
print('all animal in new zoo are',new_zoo)

print(new_zoo[2])

print(new_zoo[2][2])

print(len(new_zoo)-1+len(new_zoo[2]))
