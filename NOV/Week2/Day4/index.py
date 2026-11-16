# non primitivr data types
# main difference


              # List            tuples              set               dictionary
# ordering      ordered           ordered           un ordered         ordered
# indexing      indexed           indexed           not indexed         keyed
# mutability    mutable           imutable          mutable             mutable
# Duplicates
# allowed       yes               yes                no                  yes
# type allowed  mutable
#             and imutable



# list=[1,2,3,4]
# print(list)
# print(list[0])
# a=tuple.append(50)
# print(list)



# tuple=(1,2,3,4)
# print(tuple)
# print(tuple[2])
# a=tuple.append(50)
# print(list)


# set=(1,2,3,4)
# print(set)


# dic={"name":"adya"}
# print(dic)



# list
# Method	          Use
# append()	List ke end mein element add karta hai
# insert()	Specific position par element add karta hai
# extend()	Dusri list ke elements add karta hai
# remove()	Given element remove karta hai
# pop()	    Element ko index se remove karta hai
# clear()   Puri list empty karta hai
# sort()    List ko ascending order mein arrange karta hai
# reverse() List ko reverse karta hai
# index()   Element ka index batata hai
# count()   Element kitni baar hai batata hai
# copy()	List ki copy banata hai



# list=[10,20,30,40]
# list.append(50)
# list.extend([50,60,70])
# list.insert(60,6)
# list.remove(20)
# list.pop()
# list.pop(2)
# list.clear()
# list.index(30)
# print(a)

# print(list)

# Tuple

# Method	Use
# count()	Element kitni baar present hai count karta hai
# index()	Element ka index position batata hai


# tuple=(1,2,3,3,3,3,3,3,4,4,4,5,6,7)
# print(tuple.count(3))
# print(tuple.index(3))

# set
# set_A={1,2,3,4}
# set_B={4,5,6,7}
# set_A.add(5)
# set_A.update([9,6])
# set_A.remove(2) if any value in not in the set it will show the error
# set_A.discard(2)  if any value in not in the set it will show the set
# U_set=set_A.union(set_B)
# U_set=set_A.intersection(set_B)
# U_set={5,4}.issubset(set_B)

# print(U_set)

# print(set_A)

# dic

# dic={
#     "name" :"Adya" ,
#     "age" :"20"
# }
# print(dict.get("name"))
# print(dict.get("hii"))
# print(dict.keys())
# print(dict.values())
# dict.update({"name":"Adya","age":"20"})
# dict.clear()
# a=dict.copy()
# print(dict)