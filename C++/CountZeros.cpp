#include<iostream>
using namespace std;
int main() {

    int n, count = 0;

    cout << "Enter a number: "; cin >> n;

    while (n != 0) { // loop until the last digit is zero. 
        if (n % 10 == 0) count++; // increment the counter when we find a zero. 
        n /= 10; // remove the last digit from our number. 
    }

    cout << "The number of zeros in your entered number is: " << count << endl;

	return 0;
}
