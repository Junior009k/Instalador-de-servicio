#include <stdio.h>
 
unsigned long long factorial(unsigned int n);
 
int main() 
{
    unsigned int num;
 
    printf("Ingrese un número entero no negativo: ");
    scanf("%u", &num);

    unsigned long long fact = factorial(num);
 
    printf("El factorial de %u es %llu\n", num, fact); 
 
    return 0;
}

 

unsigned long long factorial(unsigned int n) {
    if (n == 0 || n == 1)   
    {     
        return 1;
    } 
    else 
    {
        return n * factorial(n - 1);
    }
}