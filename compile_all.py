import os
import py_compile

def compile_all_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    py_compile.compile(file_path, doraise=True)
                    print(f"Compiled successfully: {file_path}")
                except py_compile.PyCompileError as e:
                    print(f"Failed to compile: {file_path}")
                    print(e)

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    compile_all_files(current_directory)
