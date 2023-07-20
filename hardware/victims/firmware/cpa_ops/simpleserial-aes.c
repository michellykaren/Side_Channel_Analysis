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

#define NO_SEND_REPONSE // SEND_REPONSE
#define MEMORY_TARGET 0x20000000
volatile uint8_t *mem_address = (volatile uint8_t *)MEMORY_TARGET;  // Endereço de memória desejado
typedef struct {
    uint8_t registers[4];
} Context;

static char hex_lookup[16] = {
	'0', '1', '2', '3', '4', '5', '6', '7',
	'8', '9', 'A', 'B', 'C', 'D', 'E', 'F'
};

void context_puts(Context *cont) {
    uint8_t *reg_ptr = cont->registers;

    for (int i = 0; i < 4; i++) {
        putch('i');
        putch(hex_lookup[*reg_ptr >> 4 ]);
        putch(hex_lookup[*reg_ptr & 0xF]);
        reg_ptr++;
    }

    // Seding UART MEMORY_TARGET value
    uint32_t target = MEMORY_TARGET;
    putch('m');
    putch(hex_lookup[(target >> 28) & 0xF ]);
    putch(hex_lookup[(target >> 24) & 0xF ]);
    putch(hex_lookup[(target >> 20) & 0xF ]);
    putch(hex_lookup[(target >> 16) & 0xF ]);
    putch(hex_lookup[(target >> 12) & 0xF ]);
    putch(hex_lookup[(target >>  8) & 0xF ]);
    putch(hex_lookup[(target >>  4) & 0xF ]);
    putch(hex_lookup[(target & 0xF) ]);

}

void init_contexto(Context *cont) {
    *mem_address = 0;
    for (int i = 0; i < 4; i++) {
        cont->registers[i] = 0x00;  // Valor padrão: 0
    }
}


uint8_t get_pt(uint8_t* pt, uint8_t len) {
    Context myContext;
    init_contexto(&myContext);
    //context_puts(&myContext);

    #ifdef MEMORY_SELECTED
    *mem_address = pt[0];
    trigger_high();
    __asm__ volatile (
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
        "mov    r1, #0xBE               \n" //Moving value const to R1
        "ldrb   r0, [%[mem_address]]    \n" //Moving address to R6
        "eor    r0, r1                  \n" //Operação EOR entre o valor carregado e R1
        "strb   r0, [%[mem_address]]    \n" //Salvar o resultado da operação no endereço de memória
        :   		                        // Sem operandos de saída
        : [mem_address] "r" (mem_address)
        : "memory", "r0", "r1", "r6"
    );
    #endif

    #ifdef NORMAL_EOR
    uint8_t volatile seg =  0xBE;
    #endif

    #ifdef NORMAL_ADD
    uint8_t volatile seg =  0xBE;
    #endif

    #ifdef EOR
    uint8_t volatile seg =  0xBE;
    __asm__ volatile (
        "LDRB %[s], =0xBE                   \n"
        : [s] "=r" (seg)
        : 
    );
    #endif

    #ifdef CURRENT
    trigger_high();

    __asm__ __volatile__ (
        "mov    r0, #0                      \n" //Moving value const to R1
        "mov    r1, #0                      \n" //Moving value const to R1
        "mov    r1, #0xBE                   \n" //Salvar o resultado da operação no endereço de memória
        "mov    r0, %[_pt_]                 \n" //Salvar o resultado da operação no endereço de memória
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
        "mov    %[_pt_], r0                 \n" //Salvar o resultado da operação no endereço de memória
        : [_pt_] "+r" (pt[0])	                        // Sem operandos de saída
        : 
        : "memory", "cc", "r0", "r1"
    );
    #endif

    #ifdef MOV_PIPELINE_INFLUENCE
        __asm__ volatile (
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
        "EOR %[output], %[input1]           \n"
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
        : [output] "+r" (*pt)
        : [input1] "r" (0xBE)
    );
    #endif

    #ifdef EOR
   __asm__ volatile (
        "EOR %[output], %[s]                \n" 
        : [output] "+r" (pt[0])
        : [s] "r" (seg)
        : 
    ); 
    #endif

    #ifdef NORMAL_EOR
    pt[0] =  pt[0] ^ seg;
    #endif

    #ifdef NORMAL_ADD
    pt[0] =  (pt[0] + seg) &0xFF;
    #endif

    __asm__ volatile (
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
    );
    trigger_low();

    #ifdef MEMORY_SELECTED
    pt[0] = *mem_address;
    #endif

    #ifdef SEND_REPONSE
    simpleserial_put('r', 16, pt);
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
