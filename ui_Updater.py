import subprocess
import os


python_dir = os.path.expandvars("%LOCALAPPDATA%/Programs/Python/Python310")
pyside6_uic = python_dir + "/Scripts/pyside6-uic.exe"
target_uipy = "ui_BlenderAddonManager.py"
target_ui = "BlenderAddonManager.ui"


def UpdateUI():
    try:
        cmd = " ".join([pyside6_uic, "-o " + target_uipy, target_ui])
        subprocess.call(cmd, shell=True)
        print("success")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    UpdateUI()
