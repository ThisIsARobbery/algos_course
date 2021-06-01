#include <iostream>
#include <cassert>
#include <utility>
#include <cstdint>

template <class Int>
Int gcd(Int a, Int b) {
    assert(a > 0);

    if (b > 0) {
        return gcd(b, a % b);
    }
    return a;
}

int main(int argc, char *argv[]) {
    std::int64_t a, b;
    a = _atoi64(argv[1]);
    b = _atoi64(argv[2]);
    const int RUNS_COUNT = 1000000;
    for (int i = 0; i < RUNS_COUNT; i++) {
        gcd(a, b);
    }
    std::cout << gcd(a, b) << std::endl;
    return 0;
}