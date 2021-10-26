#include <stdio.h>
#include <math.h>

int main (void) {
  unsigned int input, inputf, leninput=0;
  printf("Enter an integer: ");
  scanf("%u", &input);
  inputf=input;
  while (inputf!=0) {
    inputf/=10;
    leninput++;
  }
  unsigned int sum=0;
  for (int i=0; i<leninput; i++)
    sum += pow(input / (int)pow(10, (double)i) % 10, leninput);
  if (input == sum) {
    printf("%u is an Armstrong number\n", input);
  } else {
    printf("%u is not an Armstrong number\n", input);
  }
}
