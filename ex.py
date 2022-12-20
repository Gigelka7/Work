arr = ["Hello", "2", "world", ":-)"]
arr0 = []
for i in range(len(arr)):
    if len(arr[i]) <= 3:
        arr0 += [arr[i]]
print(arr0)