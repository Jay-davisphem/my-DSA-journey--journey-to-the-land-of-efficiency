#include <iostream>
#include <iomanip>

int main()
{
    std::cout << std::setprecision(4) << std::fixed;

    double num1{}, num2{}, result{};
    char op{};

    std::cout << "Enter a double value: ";
    std::cin >> num1;
    std::cout << "Enter another double value: ";
    std::cin >> num2;

    std::cout << "Enter one of the following: +. -, *, /: ";
    std::cin >> op;

    switch (op)
    {
    case '+':
        std::cout << num1 << " " << op << " " << num2 << " is " << num1 + num2;
        break;
    case '-':
        std::cout << num1 << " " << op << " " << num2 << " is " << num1 - num2;
        break;
    case '*':
        std::cout << num1 << " " << op << " " << num2 << " is " << num1 * num2;
        break;
    case '/':
        std::cout << num1 << " " << op << " " << num2 << " is " << num1 / num2;
    }
    printf("\n");
}