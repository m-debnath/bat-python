str = "hixxhi"
last_two = str[-2:]
print(last_two)
count = 0
for i in range(len(str)):
    if str[i:i+2] == last_two:
        count = count + 1
else:
    count = count - 1
print(count)