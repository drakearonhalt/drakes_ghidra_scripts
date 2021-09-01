# ghidra-scripts

## radare2_import_functions.py

Imports and renames functions based on input from a json file created by `aflj > file.json` in radare2. Originally developed to support recovering function names in stripped golang binaries with the excellent [redress project](https://github.com/goretk/redress) and importing those into ghidra. 

1. `r2 stripped-golang-binary`
2. `#!pipe redress`
3. `aa`
4. `aflj > funcs.json`
5. Import stripped-golang-binary into Ghidra
6. Run radare2_import_functions.py and select funcs.json as your input. 

Note: The script accepts any output from `aflj`. Does not need to be modified with redress. 
