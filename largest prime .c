#include <stdio.h>

int largestPrimeFactor(int n) {
    int factor = 2, lastFactor = 1;

    if (n <= 1) return -1;  // Invalid input

    while (n > 1) {
        if (n % factor == 0) {
            lastFactor = factor;
            n /= factor;
        } else {
            factor++;
        }
    }
    return lastFactor;
}

int main() {
    int num;
    printf("Enter a positive integer: ");
    scanf("%d", &num);

    int result = largestPrimeFactor(num);
    if (result == -1)
        printf("Invalid input. Enter a number greater than 1.\n");
    else
        printf("Largest prime factor: %d\n", result);

    return 0;
}
