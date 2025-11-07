Rayshell — Command Execution and Scripting Language
=

Rayshell is a shell scripting language built for command execution, and system scripting.<br>
It combines a simple syntax and native system integration to deliver a fast, reliable scripting environment.

## Features
 - Basic command execution
 - Pipelines
 - Redirections
 - Basic job control
 - Basic Signal handling
 - Control statements (if and while)
 - Builtins (hi, history, cd, jump, echo, print, jobs, fg, bg)
 - Script files execution

## Installation

1. Download the given executable.
2. Move them to a location like `/usr/bin`. If you've downloaded the file to Downloads, run the command

   ```
   sudo mv ~/Downloads/rayshell /usr/bin/
   ```
3. Open your terminal and type `rayshell -v` and ensure it's working.

## Syntax
### All unix commands will work fine. 
### If block
   ```
    if (ls something | grep something) -> {
        print done
    }
    elif (false) -> {
        print not done
    }
    else {
        print hahaa
    }
    ls -l
   ```
   This syntax is for script files. Type this in the same when you're running it in a terminal.
### While loop
   ```
    while (ls | grep core) -> {
        print looping.
    }
   ```
### Script files
1. You can create script files with .rsh extension. And execute them by running them normally. For example, if you have a script named `morpheus' in the current directory. You can run
   ```
    chmod +x morpheus.rsh
    ./morpheus.rsh
   ```

### Single commands
1. You can run a single command without the repl.
   ```
   rayshell -c hi
   rayshell -c ls
   ```

### Making it the default shell
1. If you want to make it the default shell, you can edit your terminal app's .config or modify /bin/sh.

<img width="2880" height="1800" alt="screenshot-20251016-192340" src="https://github.com/user-attachments/assets/dd3bed40-91a0-4bf5-b3be-6b1ba22eaf53" />


