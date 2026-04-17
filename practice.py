# cdflang_675833.py

import re

# ===== CONSTANTS =====
K1 = 15
K2 = 18
K3 = 13
K4 = 13
THRESHOLD = 13
WEIGHT = 14
TAG = "voria"

# ===== SYMBOL TABLE =====
symbol_table = {}

# ===== TOKENIZER =====
def tokenize(code):
    tokens = re.findall(r'\w+|:=|<=|>=|!=|==|[()+\-*/;]', code)
    print("\nTOKENS:", tokens)
    return tokens

# ===== PARSER (VERY SIMPLE IR) =====
def parse(lines):
    ast = []
    for line in lines:
        line = line.strip()
        if line:
            ast.append(line)
    print("\nAST:")
    for node in ast:
        print(" ", node)
    return ast

# ===== EXECUTION ENGINE =====
def eval_expr(expr):
    try:
        return eval(expr, {}, symbol_table)
    except Exception:
        raise Exception(f"Runtime error in expression: {expr}")

def execute(ast):
    print("\n--- EXECUTION START ---")
    i = 0
    while i < len(ast):
        line = ast[i]

        # DECLARATION
        if line.startswith("LET"):
            _, name, _, _type = line.split()
            symbol_table[name] = None

        # ASSIGNMENT
        elif ":=" in line:
            var, expr = line.split(":=")
            var = var.strip()
            value = eval_expr(expr.strip())
            if var not in symbol_table:
                raise Exception(f"Scope error: {var} not declared")
            symbol_table[var] = value

        # REQUIRE (ERROR HANDLING)
        elif line.startswith("REQUIRE"):
            condition = line.replace("REQUIRE", "").replace("ELSE FAIL", "").strip()
            if not eval_expr(condition):
                raise Exception(f"Contract violation: {condition}")

        # IF
        elif line.startswith("IF"):
            condition = line[3:line.index("THEN")].strip()
            if eval_expr(condition):
                pass
            else:
                # skip until ENDIF
                while not ast[i].startswith("ENDIF"):
                    i += 1

        # WHILE LOOP
        elif line.startswith("WHILE"):
            condition = line[6:line.index("DO")].strip()
            loop_start = i
            loop_body = []
            i += 1
            while not ast[i].startswith("ENDWHILE"):
                loop_body.append(ast[i])
                i += 1

            while eval_expr(condition):
                execute(loop_body)

        i += 1

    print("\n--- EXECUTION END ---")

# ===== SYMBOL TABLE DISPLAY =====
def print_symbol_table():
    print("\nSYMBOL TABLE:")
    for k, v in symbol_table.items():
        print(f"{k} = {v}")

# ===== MAIN DRIVER =====
def run_program(code):
    try:
        tokens = tokenize(code)
        ast = parse(code.split("\n"))
        execute(ast)
        print_symbol_table()

        print("\nOUTPUT CONSTANTS:")
        print(K1, K2, K3, K4, THRESHOLD, WEIGHT, TAG)

        print("\nSIGNATURE:")
        print("CDF:1-0-0-1-2-2-0|REG:675833|DOMAIN:CampusMobility|TAG:voria|IMPL:Python")

    except Exception as e:
        print("\nERROR:", e)


# ===== SAMPLE PROGRAM =====
sample_program = """
LET passengers : INT
LET capacity : INT
LET trips : INT

passengers := 15
capacity := 18
trips := 0

REQUIRE passengers <= capacity ELSE FAIL

IF passengers > THRESHOLD THEN
    trips := trips + 1
ENDIF

WHILE trips < 3 DO
    trips := trips + 1
ENDWHILE
"""

if __name__ == "__main__":
    run_program(sample_program)