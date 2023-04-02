REGISTERS = {
    "R0": 0,
    "R1": 0,
    "R2": 0,
    "R3": 0
}
STACK = []

def decode_instruction(instruction):
    table = {
        10: MOVR,
        11: MOVV, 
        20: ADD,
        21: SUB,
        30: PUSH,
        31: POP,
        
    }
    
def decode_register(encoded):
    table = {
        0: "R0",
        1: "R1",
        2: "R2",
        3: "R3"
    }
    
    return table[encoded]


def MOVR(src, dst):
    REGISTERS[decode_register(dst)] = REGISTERS[decode_register(src)]    
    
def MOVV(dst, val):
    REGISTERS[decode_register(dst)] = val
    
def ADD(src, dst):
    REGISTERS[decode_register(dst)] = REGISTERS[decode_register(dst)] + REGISTERS[decode_register(src)]
    
def SUB(src, dst):
    REGISTERS[decode_register(dst)] = REGISTERS[decode_register(dst)] - REGISTERS[decode_register(src)]
    
def PUSH(src):
    STACK.append(REGISTERS[decode_register(src)])
    
def POP(dst):
    REGISTERS[decode_register(dst)] = STACK.pop()


#if __name__ == "__main__":
#    main()
