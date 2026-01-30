# 1.1-misol
numbers = [10,20,30,40,50,]
print(numbers)

# 1
a = len(numbers)
print(f"royhat uzunligi {a} ga teng")
# 2
print(numbers[2])
# 3
if 30 in numbers:
    print("royhatda 30 elementi bor ")
else:
    print("royhatda 30 elementi yoq")
# 4
b = numbers[-2:]
print(b)
# 5
summa = sum(numbers)
print(summa)

# 1.2-misol
meva = ['apple','banana','cherry']
print(meva)

# 1
a = meva.append('kiwi')
print(meva)

# 2
meva.remove("banana")
print(meva)

# 3
meva.insert(1, 'peach')
print(meva)

# 4
meva.sort()
print(meva)

# 5
print(f"yakuniy royhat: {meva}")

