# Thanks To : ZEECK, RISKY, LATIP, ZEE, GULL, DLL
import os

if __name__ == "__main__":
   try:
       os.system("git pull")
       __import__("shinzy24.c").Main()
   except Exception as e:
       exit(str(e))
