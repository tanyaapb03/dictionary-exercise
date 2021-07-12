# Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}



def con(dict1,dict2,dict3):
    for k,v in dict1.items():
        dict3[k]=v
    for k,v in dict2.items():
        dict3[k]=v
    for k,v in dict3.items():
        dict3[k]=v
    
    
    
    print(dict3)
    return dict3
con({1:10, 2:20},{3:30, 4:40},{5:50,6:60})

# Write a Python script to check whether a given key already exists in a dictionary.
def check(key):
    dict1={1:10, 2:20}
    # for k, v in dict1.items():
    #     if k == key :
    #         return True 
    #     else:
    #         return False 
    if key in dict1.keys():
        return True
    else:
         return False
print(check(2))

# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Go to the editor
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def dbl(n):
    dictd={}
    key=1
    while key<=n:

        value=key*key
        dictd[key]= value
        key+=1
    print(dictd)
    return dictd
print(dbl(6))

# # Write a Python program to sum all the items in a dictionary.

def sumi(dict1):
    x=0
    for k, v in dict1.items():
        print(k,v)
        x+=k
        x+=v
    return x
print(sumi({1:10, 2:20}))

# Write a Python program to remove a key from a dictionary

def remove(key):
    dict1={1:10, 2:20}
    if key in dict1.keys():
        dict1.__delitem__(key)
    return dict1
print(remove(2))


# Write a Python program to combine two dictionary adding values for common keys. Go to the editor
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

def add2(dict1,dict2):
    dict3={}
    for k,v in dict1.items(): 
        for key,value in dict2.items():
            if k in dict2.keys():
                v=dict1[k]+dict2[k]
                dict3[k]=v
        else:
            dict3[k]=v
            dict3[key]=value
    return dict3
print(add2({'a': 100, 'b': 200, 'c':300},{'a': 300, 'b': 200, 'd':400}))


# Write a Python program to print all unique values in a dictionary. Go to the editor
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

def unique():
    sample_data=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    unique=[]
    output=[]
    for x in sample_data:
        for k,v in x.items():
            unique.append(v)
   
    dict2={}
    for x in unique:
        if x in dict2:
            dict2[x]+=1
        else:
            dict2[x]=1
    print(dict2)
    for k,v in dict2.items():
        if dict2[k]==1:
            output.append(k)
    
    return output
   
print(unique())

# # Write a Python program to check if a specific Key and a value exist in a dictionary. Go to the editor
# Original dictionary:
# [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
# Check if a specific Key and a value exist in the said dictionary:
# True
# True
# True
# False
# False
# False

def check1(key,value):
    record=[{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
    for dict1 in record:
        if key in dict1.keys() and value== dict1[key]:
            return True
        else:
            return False
print(check1('class','V'))

# # Write a Python program to convert a given list of lists to a dictionary. Go to the editor
# Original list of lists:
# [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# Convert the said list of lists to a dictionary:
            

def Ltodict(llist):
    dict1={}
    for x in llist:
        key=x[0]
        value=[x[1],x[2]]
        dict1[key]=value
    return dict1
print(Ltodict([[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]))