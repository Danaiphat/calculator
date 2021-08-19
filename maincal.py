import one
import two
import three
import four

One_name = 1
Two_name = 2
Three_name =3
Four_name = 4
QUIT_CHOICE = 5

def main():
    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()
        choice = int(input('Enter your choice: '))
        if choice == One_name:
            num1 = int(input("Enter the fist number: "))
            num2 = int(input('Enter the second number : '))
            print('The area is',one.add(num1 , num2))
        elif choice == Two_name:
            num1 = int(input("Enter the fist number: "))
            num2 = int(input('Enter the second number : '))
            print('The circumference is',two.substract(num1 , num2))
        elif choice == Three_name:
            num1 = int(input("Enter the fist number: "))
            num2 = int(input('Enter the second number : '))
            print('The area is',three.multiply(num1 , num2))
        elif choice == Four_name:
            num1 = int(input("Enter the fist number: "))
            num2 = int(input('Enter the second number : '))
            print('The area is',four.divide(num1 , num2))
        elif choice == QUIT_CHOICE:
            print('Exiting the program...')
        else:
            print('Error: invalid selection.')
print('---------------------------------')
def display_menu():
    print(' \tMENU')
    print('1) add ')
    print('2) substract')   
    print('3) multiply')
    print('4) divide')
    print('5) Quit')
main()
print('')
print('---------------------------------')


