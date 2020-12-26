#include <bits/stdc++.h>
using namespace std;

void print(int *x) {
    cout << *x << *(x + 1) << endl;
}

int main() {
    
    int a[5] = {1,2,3,4,5};
    print(a);
    return 0;
}
