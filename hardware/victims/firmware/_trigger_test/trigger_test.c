
#include "hal.h"
#include <stdint.h>
#include <stdlib.h>

int main(void)
{
   __asm (
    "NOP \n\t" 
    "NOP \n\t" 
    "NOP \n\t" 

    "mov r8, r8 \n\t"
    "mov r0, r0 \n\t"
    
    "NOP \n\t" 
    "NOP \n\t" 
    "NOP \n\t" 
   );

    while(1){
     putch('h');
     putch('e');
     putch('l');
     putch('l');
     putch('o');
     putch('\n');
    }
       
}