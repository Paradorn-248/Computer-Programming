def my_function() :
    n = 1
    while True:
        n = int(input('Input Decimal: '))
        if n != -1 :
            print(f'Hex: {n:x}')
        else:
            break
        
    print('Good bye.')

def my_dec_to_hex() :
    
    n = 1
    while True :
        n = int(input('Input Decimal: '))
        hex_list = []
        if n != -1 : 
            char = list('abcdefghijklmnopqrstuvwxyz')
            while n > 0 :
                remain = n % 16
                if remain >= 10 :
                    hex_list.append(char[remain-10])
                else :
                    hex_list.append(remain)
                n = n // 16
        else :
            print('Good bye!!')
            break
        hex_list.reverse()
        for i in range(len(hex_list)) :
            print(hex_list[i],end = '')
        print()
            
# my_function()
my_dec_to_hex()