# Import function names from radare2 json
#@author https://github.com/drakearonhalt
#@category Data


import json

class R2Func:
    def __init__(self, name, address):
        self.name = name
        self.address = toAddr(address)


def parse_r2(data):
    r2 = []
    for d in data:
        r2.append(R2Func(d['name'],d['offset']))

    return r2


if __name__=='__main__':
    r2 = askFile('Choose File:', 'Choose File:')
    data = ''
    with open(r2.absolutePath, 'r') as fd:
        data = fd.read()

    
    data = json.loads(data)
    r2funcs = parse_r2(data)
    fm = currentProgram.getFunctionManager()
    for r in r2funcs:
        func = fm.getFunctionAt(r.address)
        if func:
            func.setName(r.name, ghidra.program.model.symbol.SourceType.DEFAULT)

