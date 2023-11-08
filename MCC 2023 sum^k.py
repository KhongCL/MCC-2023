def sum_of_scores(N, K, A):
    result = 0

    for i in range(1, 2**N):
        subset_sum = 0
        for j in range(N):
            if (i >> j) & 1:
                subset_sum += A[j]
        result += subset_sum**K

    return result % 998244353

# Read the input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Call the function and print the result
result = sum_of_scores(N, K, A)
print(result)
