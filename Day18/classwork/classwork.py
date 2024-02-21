#group102
#-----------------
#abs function
print(abs(-7)) #მანძილი რიცხვიდან ნულამდე(მოდული)
print(abs(2.5))
#------------------
#dictionaries
my_arr = ["nika", "saba", "luka" , "sandro"]
my_students ={ #Dictionaries are used to store data values in key:value pairs.
    "luka" : 18, #"luka"- key 18 - value  key : value
    "nika" : 24,
    "sandro": 30,
    "mzia": 46
}

print(my_students["nika"]) #"nika"- key
my_dict = {
    0 : "a",
    1 : "b",
    5 : "c",
    3 : "d"
}
print(my_dict[5]) # დაიპრინტება  c 
# ---------------------
#ელემენტის ჩამატება 
my_students ={ #Dictionaries are used to store data values in key:value pairs.
    "luka" : 18, #"luka"- key 18 - value  key : value
    "nika" : 24,
    "sandro": 30,
    "mzia": 46
}
my_students["erekle"] = 32 #ბოლოში ემატება
print(my_students)
my_students["nika"] = 5 # ნიკას მნიშვნელობა დააბდეითდა
print(my_students)
#-----------------------------
#get
my_students ={ #Dictionaries are used to store data values in key:value pairs.
    "luka" : 18, #"luka"- key 18 - value  key : value
    "nika" : 24,
    "sandro": 30,
    "mzia": 46
}
print(my_students.get("mzia"))
#----------------------------------
#გალისთვა
my_students ={ #Dictionaries are used to store data values in key:value pairs.
    "luka" : 18, #"luka"- key 18 - value  key : value
    "nika" : 24,
    "sandro": 30,
    "mzia": 46
}
print(list(my_students.items())) 
print(list(my_students.items())[0][1]) 
print(list(my_students.keys())) 
print(list(my_students.values()))
#---------------------
#list as  a value
my_students ={ #Dictionaries are used to store data values in key:value pairs.
    "luka" : 18, #"luka"- key 18 - value  key : value
    "nika" : 24,
    "sandro": 30,
    "mzia": [56,15]
}
print(my_students)
#----------------
#pop- გაგდება
my_students ={ #Dictionaries are used to store data values in key:value pairs.
    "luka" : 18, #"luka"- key 18 - value  key : value
    "nika" : 24,
    "sandro": 30,
    "shako_rou": [46,15]
}
my_students.pop("shako_rou") #shajo_rou გავარდება
print(my_students)
#--------------------
list = [[1, 1], [2,3], [5, 8, 2]]
print(list[list[2][list[1][0]]]) #5,8,2
