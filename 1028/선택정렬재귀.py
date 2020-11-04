def sel_sort(arr):
    if arr != []:
        x = min(arr)
        arr.remove(x)
        return [x] + sel_sort(arr)
    else:
        return []



test = [1,2,5,1,8,0]

print(sel_sort(test))