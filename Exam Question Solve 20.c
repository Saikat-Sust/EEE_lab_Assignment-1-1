#include<stdio.h>

float function(int a) {
    float b = a % 10;
    b *= b;
    return b;
}

int main() {
    float x, i;

    for (i = 1; i <= 20; i = i + 2) {
        x = function(i);
        printf("%f\n", x);
    }

    return 0;
}
