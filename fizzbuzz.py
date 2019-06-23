def fizz(num):
    return 'fizz' if num % 3 == 0 else ""

def buzz(num):
    return 'buzz' if num % 5 == 0 else ""

def fizzbuzz(num):
    tmp = fizz(num) + buzz(num)
    print(tmp if tmp != "" else num)

def fizz_plus(num, flag):
    return 'fizz' if (num % 3 == 0) ^ flag ^ (num <0) else ""

def buzz_plus(num, flag):
    return 'buzz' if (num % 5 == 0) ^ flag ^ (num < 0) else ""

def fizzbuzz_plus(num, flag):
    tmp = fizz_plus(num,flag) + buzz_plus(num,flag)
    print(tmp if tmp != "" else num)

print("==== fizzbuzz ====")
for i in range(1, 31):
    fizzbuzz(i)

print("==== fizzbuzz plus_True ====")
for i in range(-30, 31):
    fizzbuzz_plus(i, True)

print("==== fizzbuzz plus_False ====")
for i in range(-30, 31):
    fizzbuzz_plus(i, False)

