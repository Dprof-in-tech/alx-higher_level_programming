#!/usr/bin/python3

import dis
import types

if __name__ == "__main__":
    with open('hidden_4.pyc', 'rb') as file:
        code = file.read()

        code_obj = compile(code, '<string>', 'exec')
        names = set()

    for instruction in dis.get_instructions(code_obj):
        if instruction.opname == 'LOAD_NAME' and not instruction.argrepr.startswith('__'):
            names.add(instruction.argrepr)

    for name in sorted(names):
        print(name)
