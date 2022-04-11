#include <iostream>
#include <iomanip>

int getHeight()
{
    int h{};
    std::cout << "Enter the height of the tower in meters: ";
    std::cin >> h;
    return h;
};

void printResult(int h)
{
    std::cout << std::setprecision(1) << std::fixed;

    constexpr float g{9.8};
    int x_seconds{0};
    while (x_seconds <= 5)
    {
        float g_h{g * (x_seconds * x_seconds) / 2};
        if (g_h >= h)
            std::cout << "At " << x_seconds << "seconds, the ball is on the ground\n";
        else
            std::cout << "At " << x_seconds << " seconds, the ball is at height: " << h - g_h << " meters\n";
        ++x_seconds;
    }
};

int main()
{

    int h{};
    h = getHeight();
    printResult(h);
}