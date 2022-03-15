numlist = []
while True:
    inp = input("enter a number: ")
    if inp.lower() == 'done':
        break
    numlist.append(float(inp))
average = sum(numlist)/len(numlist)

print(f"average : {average}")
