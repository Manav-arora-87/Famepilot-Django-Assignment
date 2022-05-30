'''1. Implement a group_by_owners function that:
      accepts a dict containing the file owner name for each file name.
      Returns a dict containig a list of file names for each owner name, in any order.
For eg: {
 'Input.txt': 'Randy',
 'Code.py': 'Stan',
 'Output.txt': 'Randy'
 }
the group_by_owners function should return {“randy”: [“input.txt”, “output.txt”], “stan”: [“code.py”]}
'''

def group_by_owners(mydict):
    res={}                # dict to hold the result
    for key,value in mydict.items():   # traverse the key and value in dictionary
        if value not in res.keys(): 
            res[value]=[key]
        else:
            res[value].append(key)
    return res

print(group_by_owners({
 'Input.txt': 'Randy',
 'Code.py': 'Stan',
 'Output.txt': 'Randy'
 }))