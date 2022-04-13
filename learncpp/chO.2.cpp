#include <iostream>
#include <bitset>

std::bitset<4> rotl(std::bitset<4> bits)
{
    if (bits.test(3))
    {
        bits <<= 1;
        bits.set(0);
    }
    else
        bits <<= 1;
    return bits;
}
std::bitset<4> rotl2(std::bitset<4> bits)
{
    std::bitset<4> mask0{0b0001};
    std::bitset<4> mask3{0b1000};
    std::bitset<4> bit3{bits & mask3};

    bits <<= 1;
    if (bit3.any())
        bits |= mask0;
    return bits;
}
int main()
{
    std::bitset<4> bits{0b1010};
    std::cout << rotl2(bits) << '\n';
}