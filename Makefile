ANTLR_JAR ?= /usr/local/lib/antlr-4.8-complete.jar
i ?= i.c
o ?= o.s
CC = riscv64-unknown-elf-gcc  -march=rv32im -mabi=ilp32
QEMU = qemu-riscv32


RUNMD = python3 -m minidecaf 

CLASSPATH = $(ANTLR_JAR):generated

all: run

run: asm
	$(CC) $(o)
	$(QEMU) a.out ; echo $$?


justrun:
	$(CC) $(o)
	$(QEMU) a.out ; echo $$?

asm: grammar-py
	$(RUNMD) $(i) $(o)


usage: grammar-py
	$(RUNMD) -h

grammar-py:
	cd minidecaf && java -jar $(ANTLR_JAR) -Dlanguage=Python3 -visitor -o generated MiniDecaf.g4

clean:
	rm -rf generated minidecaf/generated
	rm -rf minidecaf/**__pycache__

.PHONY: all clean run justrun usage  grammar-py 
