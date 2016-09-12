#

# Using recursion instead of strings
def digit_sum(x):
    summ = 0
    if x // 10 <> 0:
        print "Going deeper..."
        summ = digit_sum(x // 10)
    print "Going out",
    summ += x % 10
    print summ
    return summ

# Recursion instead of loop
def factorial(x):
    f = 1
    if x > 1:
        f = factorial(x-1)
    elif x == 0:
        f = 1
        return f
    f = f * x
    return f

def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        # for x==3 this loop doesn't executes
        for n in range(2, x - 1):
            if (x % n == 0):
                print "false"
                return False
        else:
            print "true"
            return True

def reverse(text):
    rtext = ""
    #rtext.append('t')
    for rchar in range(len(text)-1,-1,-1):
         rtext += (text[rchar])
    return rtext

def main():
    x = 3
    text = "Python!"
    #print digit_sum(x)
    #print factorial(x)
    #print is_prime(x)
    #print reverse(text)


if __name__ == "__main__":
    main()


