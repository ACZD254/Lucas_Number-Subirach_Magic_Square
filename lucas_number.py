"""
Lucas Number
L(0) = 2
L(1) = 1
L(n) = L(n-1)+L(n-2) for n>1
"""
# Okay, so how am I going to do this? 
# let's do this scheme style
def main():
    def get_n():
        try:
            n = int(input("Please enter n "))
        except ValueError:
            print("Please enter a number, sir.")
            get_n()
        else:
            print(lucas(n))
    get_n()

def lucas(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

main()