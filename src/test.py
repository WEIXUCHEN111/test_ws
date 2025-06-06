#!/usr/bin/env python3
import subprocess

# Run C++ executable 3 times
print("Running C++ program 3 times...")
for i in range(3):
    subprocess.run(["src/cpp_demo/main"])

# Run Python script 2 times
print("Running Python script 2 times...")
for i in range(2):
    subprocess.run(["python3", "src/python_demo/hello.py"])
