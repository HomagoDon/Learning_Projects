# this checks if both numbers are even
# if both are then it returns the lower number, if not, it returns the bigger number

def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:

        return min(a,b)

    else:

        return max(a,b)


print(lesser_of_two_evens(2,6))
