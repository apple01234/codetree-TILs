#include <stdio.h>

int main() {
    string val[10];
    for (int i = 0; i < 10; i++) {
    scanf("%d", &val[i]);
    }
    for (int i = 0; i >= 0; i--) {
        printf("%d ", val[i]);
    }
    return 0;
}