from core.lexer import Lexer
from core.parser import Parser
from core.executor import Executor
from core.ast import saveASTtoJson
import os, readline, signal, sys
from core.expander import Expander
import argparse

HISTORYFILE = os.path.expanduser("~/.rayshell_history")

LEXER:bool = False
PARSER:bool = True
EXECUTOR:bool = True
ex = Executor()

def runScript(file_path: str):
    # print(f"\n---EXECUTING SCRIPT: {file_path}---")
    try:
        with open(file_path, 'r') as f:
            # for line in f:
            line = f.read()
                
            lexer = Lexer(line=line)
                
            tokens = lexer.nextToken()
            if LEXER:
                lexerDebug(tokens)
            parser = Parser(tokens)
            ast = parser.parse()
            if PARSER:
                parserDebug(ast)
            if ast:
                exp = Expander(ex)
                ast = exp.expand(ast)
                executor(ex, ast)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: Script file not found at {file_path}")
    except Exception as e:
        raise Exception(f"Error executing script: {e}")

def repl(cmd: str = None):

    loadHistory()
    VERSION = "rayshell v1.0.0"

    parser = argparse.ArgumentParser(description="A custom shell environment.")
    parser.add_argument('-c', type=str, nargs='*', help='Execute a command string.')
    parser.add_argument('-v', '--version', action='version', version=VERSION,
                        help='Display the version and exit.')
    args = parser.parse_args(sys.argv[1:])

    if args.c:
        runOnce(" ".join(args.c))
    else:
        while True:
            try:
                line = input("rayshell> ")
                saveHistory()

            except EOFError:
                saveHistory()
                break
            except KeyboardInterrupt:
                print()
                continue

            if line.strip() in ("bye","exit"):
                print("bye-bye")
                break

            if line.startswith("./") :
                try:
                    runScript(line)
                except FileNotFoundError as e:
                    print(e)
                continue

            lexer= Lexer(line=line)
            tokens = lexer.nextToken()
            if LEXER:
                lexerDebug(tokens)

            parser = Parser(tokens)
            try:
                ast = parser.parse()
                if ast is None:
                    continue
            except SyntaxError as e:
                print(f"SyntaxError {e}")
                continue

            for job in ex.jobTable.list():
                print(job.pgid, job.status, job.cmd)
        
            exp = Expander(ex)
            ast = exp.expand(ast)
            if PARSER:
                parserDebug(ast)
                
            if EXECUTOR:
                try:
                    executor(ex, ast)
                except SyntaxError as e:
                    print(f"SyntaxError {e}")
                    continue
    saveHistory()

def executor(ex, ast):
        # print("\n---EXECUTION---")
        ex.run(ast)

def runOnce(cmd: str = None):
    if not cmd.strip():
        return None
    
    lexer = Lexer(line=cmd)
    tokens = lexer.nextToken()
    parser = Parser(tokens)
    ast = parser.parse()
    if ast is None:
        return None
    exp = Expander(ex)
    ast = exp.expand(ast)
    return executor(ex, ast)

def lexerDebug(tokens):
    print("---LEXER---")
    for token in tokens:
        print(token)

def parserDebug(ast):
    try:
        saveASTtoJson(ast, os.path.join("", "/home/venkat/rayshell/core/ast.json"))
    except Exception as e:
        pass

def loadHistory():
    if os.path.exists(HISTORYFILE):
        readline.read_history_file(HISTORYFILE)

def saveHistory():
    try:
        readline.write_history_file(HISTORYFILE)
    except Exception as e:
        print(f"error writing history {e}")

if __name__ == "__main__":
    repl()
