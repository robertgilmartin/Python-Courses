def check_zeros(*args):
    count = 0
    for arg in args:
        if arg == 0:
            count += 1
        elif count == 2:
            return True
        elif arg != 0 and count == 1:
            count = 0
        else:
            pass
    return False

print(check_zeros(5,6,1,0,0,9,3,5))
print(check_zeros(6,0,5,1,0,3,0,1))
