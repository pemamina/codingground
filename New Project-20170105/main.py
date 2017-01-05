# Hello World program in Python
    
print "Hello World!\n"
def reverse(input):    
    size = len(input)
    result = []
    for i in range(0,size):
        result.append(input[size-i-1])
        continue
    return result
    
    
print (reverse("92489014")) 