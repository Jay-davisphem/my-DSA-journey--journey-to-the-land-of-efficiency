#include "pow.hpp"

std::int64_t pow(int base, int exp)
{
    assert(exp > 0 && "pow: exp parameter has negative value");

    std::int64_t result{1};
    while (exp)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }

    return result;
}
