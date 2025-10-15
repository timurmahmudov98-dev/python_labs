def min_max(nums):
    if not nums:
        raise ValueError
    
    return (min(nums), max(nums))
#тест кейсы
#print(min_max([3, -1, 5, 5, 0]))
#print(min_max([42]))
#print(min_max([-5, -2, -9]))
#print(min_max([1.5, 2, 2.0, -3.1]))
#print(min_max([]))

def unique_sorted(n):
    n = set(n)
    return sorted(n)
#print(unique_sorted([3, 1, 2, 1, 3]))
#print(unique_sorted([]))
#print(unique_sorted([-1, -1, 0, 2, 2]))
#print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))