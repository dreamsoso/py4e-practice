def chop(t):
    t.remove(t[0])
    t.remove(t[-1])

def middle(t):
    return t[1:-1]

def main():
    t = ['a', 'b', 'c', 'd', 'e', 'f']
    chop(t)
    print(t)    
    z = middle(t)
    print(z)
    print(t)




if __name__ == "__main__":
    main()