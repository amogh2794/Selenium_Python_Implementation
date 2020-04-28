# for loops in python

obj = [2, 3, 4, 5, 6]

for i in obj:
    print(i)

# sum of 1st 5 natural nos
summation = 0
for j in range(1,6):  #iterate from 1 to 5
    summation = summation + j
print(summation)


print("******************")

for k in range(1, 10, 2): # 2 indicates no. of iterations to be done in loop
    print(k)

print("******************")

for m in range(10): # will print till 9
    print(m)

print("*****************************While loop ***************")
# while loop in python

it = 10
while it > 1:
    if it == 9:
        it = it - 1 # to avoid infinite loop
        continue    # Skipps all the iterations after the continue
        print(" 9 is skipped")
    if it == 3:
        break   # will stop execution
    print(it)
    it = it - 1