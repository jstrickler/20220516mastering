
LIMIT = 1000

is_prime = [True] * (LIMIT + 1)

for n in range(2, LIMIT + 1):
    if is_prime[n]:
        print(n, end=' ')
        for multiple in range(n * 2, LIMIT + 1, n):
            is_prime[multiple] = False

print('\n')
