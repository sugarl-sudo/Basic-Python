def list_max(l):
    return max(l)


def list_min(l):
    return min(l)


def list_sum(l):
    return sum(l)


n = int(input())
a = list(map(int, input().split()))
print(list_min(a), list_max(a), list_sum(a))
