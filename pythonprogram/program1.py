
# reduce() function is not a built-in function anymore ,and it can be found in the functools module

from functools import reduce
def add(x,y):
      return x+y

list =[2,3,4,5,6]
print(reduce(add,list))


# map() function -The map() function iterates through all items in the given iterable
#  and execute the function we passes as an argument on each of them
def starts_with_A(s):
      return s[0]=="A"

fruit =["Apple","Banana","pear","mango","Apricot"]
map_object =map(starts_with_A,fruit)
print(list(map_object))

#another example
def sq(a):
      return a*a
num =[2,3,4,5,6,7,8,9,]
square = list(map(sq,num))
print(square)



#filter() function forms a new list that contains only elements that satisfy a certain condition

def starts_with_A(s):
      return s[0]=="A"

fruit =["Apple","Banana","pear","mango","Apricot"]
filter_object =filter(starts_with_A,fruit)
print(list(filter_object))



from array import*

# vals = array('i',[1,2,3,4,5,])
#
# for i in range(5):
#    print(vals[i])

# val =array('i',[2,3,4,5,])
# for i in range(4):
#    print(val[i])
val=array('i',[2,3,4,5,6,7])



val.reverse()
print(val)

i =int(input("enter a number"))
rev =0
while (i>0):
    rev =(rev*10)+i%10
    i =i//10
print("Reverse=",rev)


def all_total(*args):
    total =0
    for num in args:
        total+=num
    return total
print (all_total(1,2,3,))


