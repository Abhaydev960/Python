import os
import platform
import shutil

print("----- FILE SYSTEM INFORMATION -----")
print("Operating system :", platform.system())
print("OS release :", platform.release())
print("Current folder :", os.getcwd())

total, used, free = shutil.disk_usage(os.getcwd())
print(f"Disk total : {total // (1024**3)} GB")
print(f"Disk used : {used // (1024**3)} GB")
print(f"Disk free : {free // (1024**3)} GB")

print("\nItems in current folder:")
for item in os.listdir(".")[:10]:
    print("-", item)
