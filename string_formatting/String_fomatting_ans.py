def print_formatted(number):
    
    def hx(n):
        he = hex(n)[2:]
        res = [x if x.isdigit() == True else x.upper() for x in he]
        return ''.join(res)
                
    for n in range(1, 1 + number):
        dec = str(n)
        bi = bin(n)[2:]
        he = hx(n)
        oc = oct(n)[2:]
        spaces = len(bin(number)[2:])
        
        
        print(dec.rjust(spaces), end = ' ')
        print(oc.rjust(spaces), end = ' ')
        print(he.rjust(spaces), end = ' ')
        print(bi.rjust(spaces), end = ' ')
        
        print()