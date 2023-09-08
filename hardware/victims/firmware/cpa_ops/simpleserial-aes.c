/*
    This file is part of the ChipWhisperer Example Targets
    Copyright (C) 2012-2017 NewAE Technology Inc.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#include "hal.h"
#include "simpleserial.h"
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

#define SEND_REPONSE // SEND_REPONSE
#define MEMORY_PT  0x20000000u
#define MEMORY_SEC 0x20000004u
#define mem_address_pt ((volatile uint8_t *)MEMORY_PT) // Endereço de memória desejado, como eu coloquei o * antes ele vai estar sempre trabalhando com o valor
#define mem_address_sec ((volatile uint8_t *)MEMORY_SEC)

static char hex_lookup[16] = {
	'0', '1', '2', '3', '4', '5', '6', '7',
	'8', '9', 'A', 'B', 'C', 'D', 'E', 'F'
};


uint8_t get_pt(uint8_t* pt, uint8_t len) {
    // Context
    *mem_address_pt = 0;
    //*mem_address_sec = 0;
    __asm__ (
        "mov    r0, #0                      \n" //Moving value const to R0
        "mov    r1, #0                      \n" //Moving value const to R1
        "strb	r0, [%[_mem_address_pt_], #0]  \n" // 0 to 0x20000000
        "strb	r0, [%[_mem_address_sec_], #0]  \n"
        : 	               
        : [_mem_address_pt_] "r" (mem_address_pt), [_mem_address_sec_] "r" (mem_address_sec)
        :  "memory", "r0", "r1" 
    );

    #ifdef CLASSIC_EOR // Benchmark 1
    // Init memory values with M and S
    *mem_address_pt = pt[0];
    *mem_address_sec = 0xBE;
      
    //uint8_t volatile seg =  0xBE;
    trigger_high();

    //pt[0]  =  pt[0] ^ (seg);
    
       __asm__ (
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "ldrb   r0, [%[_mem_address_pt_], #0]      \n"
        "ldrb   r1, [%[_mem_address_sec_], #0]                   \n" //Salvar o resultado da operação no endereço de memória
        "eor    r0, r1                      \n" //Operação EOR entre o valor carregado e R1
        "strb	r0, [%[_mem_address_pt_], #0]      \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        : 	               
        : [_mem_address_pt_] "r" (mem_address_pt), [_mem_address_sec_] "r" (mem_address_sec)
        : "memory", "cc", "r0", "r1"
    );

    #endif

    #ifdef SECRET_MOV_EOR // Benchmark 2
    *mem_address_pt = pt[0];

    __asm__ (
        "mov    r0, #0                      \n" //Moving value const to R0 (PT)
        "mov    r1, #0                      \n" //Moving value const to R1 (Sec)
        : 	               
        : 
        :  
    );
    trigger_high();
    __asm__ (
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "ldrb   r0, [%[_mem_address_pt_]]   \n"
        "mov    r1, #0xBE                   \n" //Salvar o resultado da operação no endereço de memória
        "eor    r0, r1                      \n" //Operação EOR entre o valor carregado e R1
        "strb	r0, [%[_mem_address_pt_]]   \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        : 	               
        : [_mem_address_pt_] "r" (mem_address_pt)
        :  "memory", "r0", "r1"
    );
    #endif

    #ifdef CURRENT
    trigger_high();
    __asm__ (
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "ldrb   r0, [%[_mem_address_pt_]]      \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "mov    r1, #0xBE                   \n" //Salvar o resultado da operação no endereço de memória
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "eor    r0, r1                      \n" //Operação EOR entre o valor carregado e R1
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "strb	r0, [%[_mem_address_pt_]]      \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "strb	r0, [%[_mem_address_pt_], #4]      \n" 
        : 	               
        : [_mem_address_pt_] "r" (mem_address_pt)
        :  "memory", "r0", "r1", "r2"
    );
    #endif

    #ifdef ALL_SEPARATE
       *mem_address_pt = pt[0];
    __asm__ (
        "mov    r0, #0                      \n" //Moving value const to R1
        "mov    r1, #0                      \n" //Moving value const to R1
        : 	               
        : 
        :  
    );
    trigger_high();
    __asm__ (
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "ldrb   r0, [%[_mem_address_pt_]]      \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "mov    r1, #0xBE                   \n" //Salvar o resultado da operação no endereço de memória
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "eor    r0, r1                     \n" //Operação EOR entre o valor carregado e R1
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "strb	r0, [%[_mem_address_pt_]]      \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        "NOP \n"
        : 	               
        : [_mem_address_pt_] "r" (mem_address_pt)
        :  "memory", "r0", "r1"
    );
    #endif

    trigger_low();

    #ifdef SEND_REPONSE
    simpleserial_put('r', 16, mem_address_pt);
    #endif 

	return 0x00;
}

int main(void)
{

    platform_init();
    init_uart();
    trigger_setup();

    putch('\n');
    putch('m');
    putch('a');
    putch('i');
    putch('n');
    putch('\n');

	simpleserial_init();
    simpleserial_addcmd('p', 16,  get_pt);

    while(1)
        simpleserial_get();
        
}
