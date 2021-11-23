class py_solution :
    def __init__(self,paren) :
        self.paren = paren
        self.openparen = ['(','{','[']
        self.closeparen = [')','}',']']

    def is_valid_parentheses(self) :  # รับวงเล็บเปิดเข้ามาก่อนแล้วเก็บไว้ในตัวlist พอเจอที่ไม่ใช่วงเล็บเปิดแล้วค่อยมาเช็คว่าตรงกับตัววงเล็บปิดมั้ย
        len_paren = len(self.paren)
        check = []
        for i in self.paren :
            if i in self.openparen :
                check.append(i)
            else :
                if len(check) == 0 :
                    return False
                elif check[len(check)-1] == self.openparen[self.closeparen.index(i)] :
                    check = check[:-1]
            
        if len(check) == 0 :
            return True
        else :
            return False

paren = input('input: ')
res = py_solution(paren)
# print(res.is_valid_parentheses())
if res.is_valid_parentheses() :
    print('valid parentheses')
else :
    print('invalid parentheses')