# 入力
n = int(input())
nums = list(map(int, input().split()))
# -------------------------------
# n = 4
# num_str = "3 2 1 1 2 4 4 4 4 3 1 3 2 1 3"
# nums = list(map(int, num_str.split()))
# -------------------------------
# １枚抜いた状態
ans_a = sum(nums)

# 抜く前
arr_b = list(range(n+1))
sum_b = sum(arr_b)
ans_b = sum_b*4

# 差分
diff = ans_b - ans_a
print(diff)
