#problem 1

def equation(x):
    num_seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1
    # Added line
       num_seq.append(x)    
    return num_seq

print(equation(5))
print(equation(15))

# problem 2

lst = []
for i in range(100,1000): 
    for n in range(2,i) : 
        lst.append (i* n) 
        lst.append(i*i)

lst2=[]
for i in lst: 
    if str(i) == str(i)[::-1]:
        lst2.append(i)
print max(lst2) 

#problem 3
check = range(10,21)
a = 21
b = False

while b == False:
    if a % 2520 == 0:
        if all(a % n ==0 for n in check):
            b = True
        else:
            a = a + 2520
    else:
        a = a + 1
print(a)

#or
# check_list = [11, 13, 14, 16, 17, 18, 19, 20]

# def find_solution(step):
#     for num in xrange(step, 999999999, step):
#         if all(num % n == 0 for n in check_list):
#             return num
#     return None

# if __name__ == '__main__':
#     solution = find_solution(20)
#     if solution is None:
#         print "No answer found"
#     else:
#         print solution