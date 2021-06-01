#include <cassert>
#include <iostream>

class Fibonacci final {
    public:
        static int get(int n) {
            assert(n >= 0);
            if (n <= 1) {
                return n;
            }
            
            int previous = 0;
            int current = 1;
            for (int i = 2; i <= n; i++) {
                int new_current = previous + current;
                previous = current;
                current = new_current;
            }
            return current;
        }
};

int main(int argc, char *argv[]) {
    int n = atoi(argv[1]);
    // std::cout << "Input number:" << std::endl;
    // std::cin >> n;
    std::cout << Fibonacci::get(n) << std::endl;
    return 0;
}