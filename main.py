import random
import os
from capstone import *
import pandas as pd
import pefile

# Assuming you have your executables in a directory
EXECUTABLES_DIR = 'executables'
OUTPUT_CSV = 'disassembly_results.csv'


# Function to read the binary content of a file
def read_executable(file_path):
    with open(file_path, 'rb') as f:
        return f.read()


# Function to determine the architecture of an executable using pefile
def determine_architecture(file_path):
    pe = pefile.PE(file_path)
    if pe.FILE_HEADER.Machine == 0x14c:  # IMAGE_FILE_MACHINE_I386
        return 32
    elif pe.FILE_HEADER.Machine == 0x8664:  # IMAGE_FILE_MACHINE_AMD64
        return 64
    else:
        print('hhhh')
        raise ValueError("Unsupported architecture")


# Function to initialize the disassembler
def get_disassembler(arch):
    if arch == 32:
        return Cs(CS_ARCH_X86, CS_MODE_32)
    elif arch == 64:
        return Cs(CS_ARCH_X86, CS_MODE_64)
    else:
        raise ValueError("Unsupported architecture")


# Function to disassemble from a given offset
def disassemble_from_offset(disassembler, code, offset):
    code_slice = code[offset:]
    instructions = []
    for i in disassembler.disasm(code_slice, offset):
        instructions.append(i)
    return instructions


# Main function to process all executables
def process_executables():
    results = []
    for file_name in os.listdir(EXECUTABLES_DIR):
        if not file_name.endswith(('.exe', '.bin')):
            continue
        file_path = os.path.join(EXECUTABLES_DIR, file_name)
        print(f"Processing {file_path}")
        code = read_executable(file_path)

        try:
            arch = determine_architecture(file_path)
        except ValueError as e:
            print(f"Skipping {file_path}: {e}")
            continue

        disassembler = get_disassembler(arch)

        # Choose 1000 random offsets
        code_length = len(code)
        random_offsets = random.sample(range(code_length), 1000)

        for offset in random_offsets:
            try:
                instructions = disassemble_from_offset(disassembler, code, offset)
                if not instructions:
                    continue

                valid_instructions_count = 0
                for instr in instructions:
                    if instr.mnemonic == 'invalid':  # Capstone-specific check for invalid instructions
                        break
                    valid_instructions_count += 1

                results.append({
                    'file': file_name,
                    'offset': offset,
                    'valid_instructions_count': valid_instructions_count,
                    'arch': arch
                })
            except CsError as e:
                print(f"Error disassembling {file_path} at offset {offset}: {e}")
                continue

    df = pd.DataFrame(results)
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"Results saved to {OUTPUT_CSV}")


if __name__ == '__main__':
    process_executables()
