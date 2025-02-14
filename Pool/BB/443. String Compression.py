
"""
https://www.1point3acres.com/bbs/thread-1108296-1-1.html
二轮 1h 自己出的 encode number 输入1113344 输出312324 要求不能转成string做
"""


def encode_num(n):
    result = 0
    prev_digit = -1
    curr_count = 0
    while n > 0:
        curr_digit = n % 10
        n //= 10

        if curr_digit == prev_digit:
            curr_count += 1
        else:
            if prev_digit != -1:
                result = result * 100 + prev_digit * 10 + curr_count

            curr_count = 1
            prev_digit = curr_digit
    
    if prev_digit != -1:
        result = result * 100 + prev_digit * 10 + curr_count

    resvered_result = 0
    while result > 0:
        resvered_result = resvered_result * 10 + result % 10
        result //= 10
    return resvered_result

print(encode_num(1113344))
