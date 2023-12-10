#!/usr/bin/python3

import dis
import types

if __name__ == "__main__":
    with open('hidden_4.pyc', 'rb') as file:
        code = file.read()

    code_obj = types.CodeType(
            0, 0, 0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
    code_obj = types.CodeType(*code_obj._fields,code)

    names = set()

    for instruction in dis.get_instructions(code_obj):
        if instruction.opname == 'LOAD_NAME' and not instruction.argrepr.startswith('__'):
            names.add(instruction.argrepr)

    for name in sorted(names):
        print(name)
