from cx_Freeze import setup, Executable 

setup(  name = "python",
        version = "1.0",
        description = "Workspace Converter",
        executables = [Executable("main.py",base="Win32GUI", icon="C:/Users/ahmad/Desktop/YOUTUBE_icon-icons.com_65487.ico")] 
)
