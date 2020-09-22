# 데이터 타입

v_str1 = "Nicewoman"
v_bool = True # 1
v_str2 = "Goodgirl"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "choi",
    "age" : 25
}
v_list = [3,5,7]
v_tuple = 3, 5, 7
v_set = {7,8,9}


print(type(v_tuple))
print(type(v_set))
print(type(v_float))
print(type(v_list))
print(type(v_dict))
print(type(v_int))
print(type(v_bool))
print(type(v_str1))
print(type(v_str2))

i1 = 39
i2 = 939
big_int1 = 9999999999999999999999
big_int2 = 7777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5  # 0.5
f4 = 10. # 10.0 

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2) # 지수(제곱)
print(f3 + i2)

result = f3 +i2
print(result, type(result))

a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a + b
print(result2)

# 형변환
# int, float, complex(복소수)

print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))

y = 100
y *= 100
print(y)


# 2진수 변환
print(bin(50)) #0b로 시작



# 수치 연산 함수
print(abs(-7))
n, m = divmod(100,8) # 몫과 나머지 각가 n,m에
print(n, m)

import math

print(math.ceil(5.1)) # 5.1보다 큰수중에 가까운 수
print(math.floor(3.874)) # 3.874보다 작은수중에 가까운 수
