#find the multiples of n < 10
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(f"{n} equal {x} * {n//x}")
            break

for num in range(2,10):
    if num % 2 == 0:
        print(f"found an even number:{num}")
        continue
    print(f"found an odd number {num}")