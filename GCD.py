from math import gcd
def gcdOfString(str1, str2):
    # check if str1 + str2= str2+str1
    if str1 + str2 != str2 + str1:
        return ""
    
    # find the gcd of the length of the strings
    gcd_length = gcd(len(str1), len(str2))

    # the gcd string is the prefix of str1 with length equal to gcd_length
    return str1[:gcd_length]

# usage
print(gcdOfString("ABCABC", "ABC"))
print(gcdOfString("ABABAB", "ABAB"))
print(gcdOfString("ME", "FESTUS"))
    
