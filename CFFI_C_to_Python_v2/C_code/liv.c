#include <stdio.h>
int factorial(int n) {
   printf("Print on C \n n=%i \n", n);
   return (n > 1) ? (n * factorial(n - 1)) : 1;
}
