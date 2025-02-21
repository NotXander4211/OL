import cpu
import os
c = cpu.Cpu()
while (inp := input(">>> ").lower()) not in ["halt", "exit", "quit"]:
    try:
        program = inp.split(" ")
        opcode = program[0]
        pc = 1
        if opcode == "mov":
            reg = program[pc]
            val = program[pc+1]
            c.setReg(reg, cpu.Helper.hexToBin(val))
            pc += 2
        elif opcode == "prt":
            reg = program[pc]
            print(c.getReg(reg))
            pc += 1
        elif opcode == "add":
            reg = program[pc]
            reg2 = program[pc + 1]
            c.add(reg, reg2)
            pc += 2
        elif opcode == "syscall":
            c.syscall()
        elif opcode in ["clear", "cls"]:
            os.system("cls")
        elif opcode in ["reglist"]:
            print(c.enumerateReg())
        elif opcode in ["lst", "ls", "list"]:
            print("MOV <reg> <val: hex>")
            print("PRT <reg>")
            print("ADD <reg> <reg>")
            print("syscall")
            print("reglist")
            print("clear | lst | halt")
    except Exception as e:
        print(e)
