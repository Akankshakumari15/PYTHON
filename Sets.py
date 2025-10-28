# sets::collection of unordered items(no index) 
# items aree unique and immutable(not changeable from outside the set)
# but set is mutable

nums={1,2,3,4,5,6,7,8,"hello","hello"}

# all duplicate keys will be ignored.
# we can store boolean,int,float,string,tuples ina set as they are immutable:not changeable
# but we cannot store a list and dictionary in a set as they are mutable:changeable

print(nums)
print(type(nums))   #class::set
print(len(nums))

collection=set()   #empty set syntax
print(type(collection))
# as collection={}    will give type as empty dictionary

# list[], tuple(), dictionary{}, set{}

