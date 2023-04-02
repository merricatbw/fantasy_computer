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
    REGISTERS[decode_register(src)] = 0


#if __name__ == "__main__":
#    main()