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
#include <stdint.h>
#include <stdlib.h>

#include "simpleserial.h"

uint8_t get_pt(uint8_t* pt, uint8_t len)
{

    // My secret
    __asm volatile (
    "mov r1, #0 \n" 
    "add r1, r1, #0xBE \n" 
   );

   __asm volatile (
    "ADD %[result], %[input_i], r1 \n"
    : [result] "=r" (pt[0])
    : [input_i] "r" (pt[0])
    );

	/* End user-specific code here. *
	********************************/
	simpleserial_put('r', 16,  pt);
	return 0x00;
}


int main(void)
{
    platform_init();
	init_uart();

	simpleserial_init();

	simpleserial_addcmd('p', 16, get_pt);

	while(1)
		simpleserial_get();
}
