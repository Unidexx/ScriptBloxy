# ScriptBloxy V1

# Imports
import time, os

# Code
print("ScriptBloxy")
time.sleep(14)
print("© 2025 Unidexx | Version: 1.0.0.0")

while True:
    navigation = input("Where do you wanna go to? (Type numbers) (1. Executor, 2. Add-ons) .. ")
    if navigation == "1":
        connectroblox = input("Please open website/microsoft Roblox and type 'Inject' to connect. ")
        print("Connected!")
        scriptName = input("Script = ")
        print("Executed!")
    elif navigation == "2":
        print("W.I.P")
        quit()
    else:
        print("Invalid")