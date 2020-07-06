#include <stdio.h>

// gcc -Wall c.c -o c
// ./c

void hello(char name[]) {
    printf ("Hello, world!\n");
    printf ("%s!\n", name);
}

int main (void) {
    char name[] = "moose";
    hello(name);
    return 0;
}
