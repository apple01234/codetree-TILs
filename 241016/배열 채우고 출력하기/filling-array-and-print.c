#include <stdio.h>

int main() {
    char val[10];
    for (int i = 0; i < 10; i++) {
    scanf("%c", &val[i]);
    }
    for (int i = 9; i >= 0; i--) {
        printf("%c ", val[i]);
    }
    return 0;
}