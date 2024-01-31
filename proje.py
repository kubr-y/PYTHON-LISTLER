def duzlist (liste):
    flat_liste=[]
    for i in liste:
     if  isinstance(i, list):
        flat_liste.extend(duzlist(i))
     else:
        flat_liste.append(i)
    return flat_liste

l=[[1, "a", ["cat"],2], [[[3]],"dog"],4,5]       
yenilist=duzlist(l)
print(yenilist)

def reverse_nested_list(lst):
    reversed_list = []
    for item in lst:
        if isinstance(item, list):
            reversed_item = reverse_nested_list(item)
            reversed_item=lst.reverse()
            reversed_list.append(reversed_item)
        else:
            reversed_list.append(item)
    return reversed_list

nested_list = [[1, 2], [3, 4], [5, 6, 7]]
reverse_nested_list(nested_list)
print(nested_list)

 
      