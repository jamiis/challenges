#include <iostream>
#include <string>

using namespace std;

int get_chocolates(int& bill, int& price, int& exchange) {
    int chocolates = bill / price;
    // exchange wrappers for bonus chocolates
    int wrappers = chocolates;
    int bonus = wrappers / exchange;
    while (bonus) {
        chocolates += bonus;
        // colculate number of new wrappers
        wrappers = bonus + wrappers % exchange;
        // exchange wrappers again
        bonus = wrappers / exchange;
    }
    return chocolates;
}

int main() {
    int N;
    cin >> N;
    int bill, price, exchange;
    for (int i = 0; i < N; ++i) {
        cin >> bill;
        cin >> price;
        cin >> exchange;
        cout << get_chocolates(bill, price, exchange) << endl;
    }
}
