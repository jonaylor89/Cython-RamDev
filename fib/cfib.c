
#include <stdio.h>

int fib(int n){

  int a = 1, b = 0;

  for(int i = 0; i < n; i++){
    int temp = a;
    a = a + b;
    b = temp;
  }

  return a;
}

int main(){

  printf("%d\n", fib(50));

  return 0;
}
