def is_prime(num=0):
    if num <= 1:
        return False
    if num == 2:
        return True
    for I in range(2,int(num/2)+1):
        if num % I == 0:
            return False
    return True

def prinomial(num=0):
    if num <= 0:
        return None
    ctr = 1; prinomialNum = 1
    serialN = 1
    while ctr <= num:
        if is_prime(serialN):
            prinomialNum *= serialN
            ctr += 1
        serialN += 1
    return prinomialNum

message = """  A Primorial is a product of the first n prime numbers (e.g. 2 x 3 x 5 = 30). 2, 3, 5, 7, 11, 13 are prime numbers. 
If n was 3, you'd multiply 2 x 3 x 5 = 30 or Primorial = 30
"""
print(message)
pri_num = input("Enter number to find Prinomial : ")
print("Your Prinomial Number is : ",prinomial(int(pri_num)))