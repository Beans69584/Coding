#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <random>

using namespace std;

int main()
{
    int random;
    cout << "Enter a number between 1 and 10000000: ";
    cin >> random;
    int tries = 0;
    int count = 1;
    clock_t start = clock();
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 10000000);
    while (count > 0){
        int guess = dis(gen);
        if (guess == random){
            cout << "It took " << tries << " tries to guess the number " << random << endl;
            count = 0;
            clock_t end = clock();
            double elapsed_secs = double(end - start) / CLOCKS_PER_SEC;
            cout << "It took " << elapsed_secs << " seconds to guess the number." << endl;
        }
        else{
            tries++;
        }
    }
    return 0;
}