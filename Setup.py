try:
    import sys
    import os

    def OpenTelegram():
        try:
            import webbrowser
            webbrowser.open('https://discord.gg/U5XMBFUcCY')
        except: pass

    if sys.platform.startswith("win"):
        os.system("cls")
        print("Installing the python modules required for the Axiom Multi-Tool:\n")
        os.system("python -m pip install --upgrade pip")
        os.system("python -m pip install -r requirements.txt")
        OpenTelegram()
        os.system("python Axiom.py")

    elif sys.platform.startswith("linux"):
        os.system("clear")
        print("Installing the python modules required for the Axiom Multi-Tool:\n")
        os.system("pip3 install --upgrade pip")
        os.system("pip3 install -r requirements.txt")
        OpenTelegram()
        os.system("python3 Axiom.py")

except Exception as e:
    input(e)
