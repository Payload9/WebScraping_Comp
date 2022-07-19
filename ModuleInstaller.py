import os
import platform
from importlib.util import find_spec


required_modules = ['bs4', 'colorama', 'PyInquirer', 'prettytable']
missing_modules = []

for module in required_modules:
    moduleInstalled = find_spec(module)
    if moduleInstalled == None:
        missing_modules.append(module)

if len(missing_modules) != 0:
    print("The following Python modules are required for the program to run, but are not installed: ")
    for modules in missing_modules:
        print("- "+str(modules))
    print("Would you like to install them?")
    userSelection = input("(Y/N): ")
    
    
    if userSelection.lower() == 'y':
        if platform.system() == 'Windows':
            for mod in missing_modules:
                print("Detected OS: Windows")
                os.system("py -m pip install "+ mod)
            print("Installation successful! Run `main.py` from the command line to start the program.")
            input("Press [ENTER] to exit . . .")
            exit()
                
        if platform.system() == 'Linux':
            for mod in missing_modules:
                print("Detected OS: Linux")
                os.system("python3 -m pip install "+ mod)
            print("Installation successful! Run `main.py` from the command line to start the program.")
            input("Press [ENTER] to exit . . .")
            exit()
        
        else:
            print(f"Installation failed: Unsupported OS: {platform.system()}")
            input("Press any key to exit . . .")
            exit()
    else:
        print("The program cannot run without the missing modules. If you need further help, @ Payload9.")
        exit()
else:
    print("No missing modules found. No further action required.")
    input("Press [ENTER] to exit . . .")
    exit()