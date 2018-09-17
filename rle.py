

def rle_encoder(txt):
    """ RLE encoder modetager en streng og returner en streng
        med saa gentagne bogstaver bilver erstattet med bogstavet og
         antallet af gentagelser

         "bbbkkk" bliver "b3k3"
         """
    if not txt:
        return ''
    if txt == '\0':
        return '\0'
    old = txt[0]
    i = 0
    res = []
    for c in txt:
        if c == old:
           i += 1
        else:
            res.append('%c%d' % (old,i))
            old = c
            i = 1
    res.append('%c%d' % (old,i))
    return ''.join(res)

def rle_decoder(txt):
    if not txt:
        return ''
    if txt == '\0':
        return '\0'
    i = 0
    res = []
    for c in txt:
        if i % 2 == 0:
            new = c
            i += 1
        else:
            for a in range(int(c)):
                res.append('%c' % (new))
            i += 1
    return ''.join(res)


if __name__ == "__main__":
    import sys
    args = sys.argv
    print(args)
    if len(args)==3:
        dat = args[2]
    elif len(args)==2:
        dat = sys.stdin.read()
    else:
        print("Error")
        exit(0)
    if args[1]=='-d':
        print(rle_decoder(dat))
    else:
        print(rle_encoder(dat))
