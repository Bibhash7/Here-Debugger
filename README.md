# Here-Debugger
This user-friendly debugger simplifies the debugging process by accepting any number of variables and printing their names, values, and line numbers. It also offers options to add search text and include variable type information for enhanced clarity.

## Features:
- Prints variable names and values
- Displays line number of the variables
- Option to add search text
- Option to include variable type information

## Installation
To install the debugger, use:
```pip install here_debugger```

## Usage
1. Print variable names and values.
   ```
   from here_debugger.debug import here_debugger
   a = 2
   b = "Bibhash"
   here_debugger(a, b)
   ```
   Output:
   ```Line-4: a = 2, | b = Bibhash, |```

2. Add search text:
    ```
   from here_debugger.debug import here_debugger
   a = 2
   b = "Bibhash"
   here_debugger(a,b, custom_arguments="Debug-")
   ```
   Output:
   ```Debug-:Line-4: a = 2, | b = Bibhash, |```

3. Print variable type information:
   ```
   from here_debugger.debug import here_debugger
   a = 2
   b = "Bibhash"
   c = [2,2]
   d = {}
   here_debugger(a,b,c,d, custom_arguments="Debug-", include_types=True)
   ```
   Output: ```Debug-:Line-6: a = 2, type=<class 'int'> | b = Bibhash, type=<class 'str'> | c = [2, 2], type=<class 'list'> | d = {}, type=<class 'dict'> | ```
