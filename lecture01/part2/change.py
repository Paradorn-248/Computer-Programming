money = int(input())
print(f'1000 => {money//1000}')
print(f'500 => {(money%1000) // 500}')
print(f'100 => {((money%1000)%500) // 100}')
print(f'50 => {(((money%1000)%500)%100) // 50}')
print(f'20 => {((((money%1000)%500)%100)%50) // 20}')
print(f'10 => {(((((money%1000)%500)%100)%50)%20) // 10}')
print(f'5 => {((((((money%1000)%500)%100)%50)%20)%10) // 5}')
print(f'1 => {(((((((money%1000)%500)%100)%50)%20)%10)%5) // 1}')
