from cx_Freeze import setup, Executable
import sys


sys.path.insert(0, "/home/demange/code/design_interface")

includes = ["os", "sys", "atexit"]
 
includefiles = [
"EditDataWindow.py", "MainWindow_ui.py", "MenuFonction.py", "EditDataWindow_ui.py", "MenuFonction_ui.py"
]
 
executables = [
Executable("MainWindow.py")
]
 
# On appelle la fonction setup
 
setup(
    install_requires=['PyQt5'],
    name = "Design App",
    version = "1",
    description = "Design application",
    options = {'build_exe' : {'include_files':includefiles, 'includes': includes}},
    executables = executables,
)
