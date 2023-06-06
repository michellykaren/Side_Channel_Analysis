
#include "hal.h"
#include <stdint.h>
#include <stdlib.h>

int main(void)
{
    int s __attribute__((aligned (16)));
    s = 0xBEBACA00;
    __asm volatile (
    "mov r1, #0 \n" 
    "mov r1, #0x00FE \n" 
   );

   __asm volatile (
    "ADD %[result], %[input_i], r1 \n"
    : [result] "=r" (s)
    : [input_i] "r" (s)
    );  
    return 0;
}

/*
- Idx: Indica o índice da seção na tabela de seções. Os índices são números sequenciais atribuídos a cada seção.
- Name: É o nome da seção, que é uma identificação única para a seção.
- Size: É o tamanho da seção em bytes, indicando a quantidade de espaço ocupado pela seção na memória.
- VMA (Virtual Memory Address): É o endereço virtual inicial da seção. O endereço virtual é o endereço lógico usado pelo programa durante a execução, que pode ser mapeado para um endereço físico específico pela unidade de gerenciamento de memória do sistema operacional.
- LMA (Load Memory Address): É o endereço de carga inicial da seção. O endereço de carga é o endereço físico onde a seção é carregada na memória.
- File off: É o deslocamento (offset) do início da seção no arquivo binário. Ele indica a posição da seção no arquivo.
- Algn (Alignment): Indica o alinhamento da seção, ou seja, a restrição no endereço inicial da seção. É o valor de alinhamento em potência de 2 que especifica como a seção deve ser alinhada na memória.
*/