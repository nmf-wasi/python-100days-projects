def min_removals_to_good_sequence(n, a):
    # Step 1: Count frequencies manually
    frequency = {}
    for num in a:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Step 2: Calculate removals
    removals = 0
    for x in frequency:
        count = frequency[x]
        if count > x:
            removals += count - x  # Remove the extra occurrences
        elif count < x:
            removals += count  # Remove all occurrences since it can't be good
    
    return removals

# Input
n = int(input())  # Length of the sequence
a = list(map(int, input().split()))  # Sequence of integers

# Output
print(min_removals_to_good_sequence(n, a))
