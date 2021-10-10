print('Ընտրեք գործողությունը։')
print('1.Գումար')
print('2.Տարբերություն')
print('3.Արտադրյալ')
print('4.Քանորդ')

choice = input('Գրեք գործողության համարը։ ')

num1 = float(input('Գրեք առաջին թիվը։ '))
print("a:" , num1)
num2 = float(input('Գրեք երկրորդ թիվը։ '))
print("b:" , num2)

print('/////Արդյունք/////')

if choice == '1':
    print(num1, "-" , num2 , "=" , num1 + num2)

elif choice == '2':
    print(num1, "-" , num2 , "=" , num1 - num2 )


elif choice == '3':
    print(num1, "*" , num2 , "=" , num1 * num2 )


elif choice == '4':
    print(num1, "/" , num2 , "=" , num1 / num2 )









