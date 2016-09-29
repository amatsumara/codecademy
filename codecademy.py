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
    f *= x
    return f


def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        # for x==3 this loop doesn't executes
        for n in range(2, x - 1):
            if x % n == 0:
                print "false"
                return False
        else:
            print "true"
            return True


def reverse(text):
    rtext = ""
    # rtext.append('t')
    for rchar in range(len(text)-1,-1,-1):
         rtext += (text[rchar])
    return rtext


def anti_vowel(text):
    s = ""
    for c in text:
        if c not in "aeiouAEIOU":
            print c,
            s += c
    return s
            

def count(sequence, item):
    found = 0
    for c in range(0, len(sequence)):
        if sequence[c] == item:
            found += 1
    return found


def purify(plist):
    plisted = []
    for c in range(0, len(plist)):
        if plist[c] % 2 == 0:
            plisted.append(plist[c])
    return plisted


def median(somelist):
    m = 0.0
    sll = len(somelist)
    somelist_s = sorted(somelist)
    if sll % 2 == 0:
        index = sll / 2 - 1
        print index, somelist_s[index], somelist_s[index + 1]
        m = float(somelist_s[index] + somelist_s[index + 1]) / 2
    else:
        index = int(sll / 2)
        m = somelist_s[index]
    return m


def main():
    x = 15
    text = "Python!"
    # print digit_sum(x)
    # print factorial(x)
    # print is_prime(x)
    # print reverse(text)
    # print anti_vowel(text)
    # print count(sequence=[1,2,1,1],item=1)
    # print purify([1, 2, 3])
    print median([4, 5, 5, 4])

if __name__ == "__main__":
    main()


