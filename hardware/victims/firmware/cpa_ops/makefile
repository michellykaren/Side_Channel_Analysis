# Hey Emacs, this is a -*- makefile -*-
#----------------------------------------------------------------------------
#
# Makefile for ChipWhisperer SimpleSerial-AES Program
#
#----------------------------------------------------------------------------
# On command line:
#
# make all = Make software.
#
# make clean = Clean out built project files.
#
# make coff = Convert ELF to AVR COFF.
#
# make extcoff = Convert ELF to AVR Extended COFF.
#
# make program = Download the hex file to the device, using avrdude.
#                Please customize the avrdude settings below first!
#
# make debug = Start either simulavr or avarice as specified for debugging,
#              with avr-gdb or avr-insight as the front end for debugging.
#
# make filename.s = Just compile filename.c into the assembler code only.
#
# make filename.i = Create a preprocessed source file for use in submitting
#                   bug reports to the GCC project.
#
# To rebuild project do "make clean" then "make all".
#----------------------------------------------------------------------------

# Target file name (without extension).
# This is the base name of the compiled .hex file.
TARGET = simpleserial-aes

# List C source files here.
# Header files (.h) are automatically pulled in.
SRC += simpleserial-aes.c

# -----------------------------------------------------------------------------

OPERATIONS_ALLOWED = CURRENT EOR_CLASSIC EOR_SECRET_LDR EOR_SECRET_MOV EOR_ISOLATED

define OPERATIONS_LIST

  +------------------+----------------+
  | Operation        | Description    |
  +------------------+----------------+------------
  | CURRENT          | It is your current test 
  | EOR_CLASSIC      | pt[0] =  pt[0] ^ secret    
  | EOR_SECRET_LDR   | secret charged with ldr     
  | EOR_SECRET_MOV   | secret charged with mov   
  | EOR_ISOLATED     |
  +------------------+----------------+------------

endef

ifeq ($(OPERATION),)
  OPERATION = EOR_classic
else ifeq ($(filter $(OPERATION),$(OPERATIONS_ALLOWED)),)
  $(error Invalid OPERATION : $(OPERATION); Allowed : $(OPERATIONS_LIST))
endif

# -----------------------------------------------------------------------------
EXTRA_OPTS = NO_EXTRA_OPTS
CFLAGS += -D$(OPERATION)

ifeq ($(CRYPTO_TARGET),)
  ${info No CRYPTO_TARGET passed - defaulting to TINYAES128C}
  CRYPTO_TARGET = TINYAES128C
endif

${info Building for platform ${PLATFORM} with CRYPTO_TARGET=$(CRYPTO_TARGET) and OPERATION=$(OPERATION)}

#Add simpleserial project to build
include ../simpleserial/Makefile.simpleserial

FIRMWAREPATH = ../.
include $(FIRMWAREPATH)/Makefile.inc

