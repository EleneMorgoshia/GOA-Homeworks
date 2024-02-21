#task4:
#Given a set of numbers, return the additive 
#inverse of each. Each positive becomes negatives,
# and the negatives become positives.
#invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
#invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
#invert([]) == []
def invert(lst):
    new_lst=[]
    if len(lst) == 0:
        return lst
    for i in range(len(lst)):
            new_lst.append( lst[i]*-1)
    return new_lst

print(invert([]))