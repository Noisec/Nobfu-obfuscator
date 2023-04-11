#Nobfu
import bz2
import os
import quopri
import random
import base64
import random
import platform
import traceback

def reset():
    global revcount,b64count,unifycount,comppycount,quotcount,code,strength,minran,maxran,percent,debug
    debug=False
    percent=75
    minran=5
    maxran=12

    code=""
    revcount=0
    b64count=1
    unifycount=2
    comppycount=1
    quotcount=1
reset()

if platform.system() == 'Windows':
    os.system('cls & color B')
else:
    os.system('clear')

def intro():
    global infile
    print(r'''
    __  __   ___   ____  ____  __ __
    ||\ ||  // \\  || )) ||    || ||
    ||\\|| ((   )) ||=)  ||==  || ||
    || \||  \\_//  ||_)) ||    \\_//
    by ИΘIƧƧ#6149
        
    Side notes:
    -It is recommended to always check and run your code after obfuscating!
    -By using this script, you automatically accept that this script is only for educational purposes!
    -You should eat cheese!
    
    ''')
    infile=input("    Filename:")

def debsett():
    print(f"    Do you want anti-debugger protection into your code?")
    debugc=input("    True/False:")
    if debugc=="True" or debugc=="true" or debugc=="TRUE" or debugc=="T" or debugc=="t":debug=True
    else:debug="False"
    return debug

def sett():
    global minran,maxran,percent
    print()
    print()
    print(f"Current obfuscation strength: overall[min:{minran} max:{maxran}] | filter:{percent}%")
    print("Side note:The bigger the filter is the better (max is 100), the larger is overall min an max the better, in means of obfuscation.")
    ch=input("Press enter to continue, C to change the settings:")
    if ch=="c" or ch=="C" or ch=="change" or ch=="CHANGE" or ch=="Change":
        print("Overall")
        minran=input("Min:")
        maxran=input("Max:")
        
        print("Filter")
        percent=int(input("Percentage:").replace("%",""))


def obfuscate():
    global revcount,b64count,unifycount,comppycount,quotcount,strength,debug,code
    if debsett()==True:
        dbgprot='''exec("""\nimport os\nimport ctypes\nimport platform\nprint("Checking for errors")\ndef cls():\n    if platform.system() == 'Windows':\n        os.system('cls')\n    else:\n        os.system('clear')\ndef detect_debugger_present():\n    try:\n        if ctypes.windll.kernel32.IsDebuggerPresent():\n            return True\n    except:\n        pass\n    return False\n\ndef detect_kernelmode_debugger():\n    if platform.system() == "Windows":\n        try:\n            status = os.popen('bcdedit').read()\n            if "debug on" in status.lower():\n                return True\n        except:\n            pass\n    return False\n\ndef detect_virtual_machine():\n    if platform.system() == "Windows":\n        try:\n            if os.popen('systeminfo').read().find("VMware") != -1:\n                return True\n        except:\n            pass\n    return False\n\ndef detect_sandbox():\n    if platform.system() == "Windows":\n        try:\n            if os.environ.get("SANDBOXIE") is not None:\n                return True\n        except:\n            pass\n    return False\n\ndef detect_emulation():\n    if platform.system() == "Windows":\n        try:\n            if os.popen('systeminfo').read().find("Wine") != -1:\n                return True\n        except:\n            pass\n    return False\n\ndef detect_administrator():\n    if platform.system() == "Windows":\n        try:\n            if ctypes.windll.shell32.IsUserAnAdmin():\n                return True\n        except:\n            pass\n    elif platform.system() == "Linux":\n        try:\n            if os.geteuid() == 0:\n                return True\n        except:\n            pass\n    return False\ncls()\nprint("Checking for errors")\nif detect_debugger_present() == True:\n    while True:\n        quit()\ncls()\nprint("Checking for errors.")\nif detect_kernelmode_debugger() == True:\n    while True:\n        quit()\ncls()\nprint("Checking for errors..")\nif detect_virtual_machine() == True:\n    while True:\n        quit()\ncls()\nprint("Checking for errors...")\nif detect_sandbox() == True:\n    while True:\n        quit()\ncls()\nprint("Checking for errors....")\nif detect_emulation() == True:\n    while True:\n        quit()\ncls()\n""")'''
        code=dbgprot+"\n"+code 
    code=quoted_encode(comppy(unify(b64pack(unify(remove_comments(code))))))
    for i in range(random.randint(minran,maxran)):
        exe()
        code = unify(b64pack(code))
        b64count+=1
        unifycount+=1
        
    code = "import base64\nimport base64\n"+(code)
    code=rev(code) 
    
    fl2=open(infile.replace(".py","")+"-obf.py","w")
    print(code,file=fl2)
    fl2.close()
    
    strength=quotcount+comppycount+unifycount+b64count+revcount
    print(f'    Overall obfuscation strength:{strength}')
    print(test_run(code))


''''''


def exe():
    global code,percent,revcount,quotcount,comppycount
    index=random.randint(1,3)
    if random.randint(1, 100) <= percent:

        if index==1:code=quoted_encode(code);quotcount+=1

        elif index==2:code=comppy(code);comppycount+=1

        elif index==3:code=rev(code);revcount+=1

def test_run(code):
    try:
        compile(code, "<string>", "exec")
        return "    No errors found."
    except Exception as e:
        return f"   Error found: {traceback.format_exc()}"


def rev(input_str):
    revedcode=input_str[::-1]

    xstring=f'data=r"""{revedcode}"""\nexec(data[::-1])'

    return xstring

def comppy(code):
    compressed = bz2.compress(code.encode('utf-8'))
    decompresser = "import bz2\nexec(bz2.decompress(" + repr(compressed) + "))"
    return "exec(" + repr(decompresser) + ")"

def quoted_encode(code):
    encoded = quopri.encodestring(code.encode('utf-8')).decode('ascii')
    decoder = "import quopri\nexec(quopri.decodestring(" + repr(encoded) + ").decode('utf-8'))"
    return "exec(" + repr(decoder) + ")"

def b64pack(code):
    n = random.randint(1, 3) 
    encoded = code
    for i in range(n):
        encoded = base64.b64encode(encoded.encode()).decode()
    decoding_code = f"decoded = '{encoded}'\n"
    for i in range(n):
        decoding_code += f"decoded = base64.b64decode(decoded.encode()).decode()\n"
    decoding_code += f"exec(decoded)"
    return decoding_code

def remove_comments(code):
    lines = code.split("\n")
    new_lines = []
    for line in lines:
        if "#" in line:
            line = line[:line.index("#")]
        new_lines.append(line)
    return "\n".join(new_lines)

def unify(code):
    code = code.strip()
    code = code.replace('\n', '\\n').replace('\t', '\\t')
    code = f'exec(\'\'\'{code}\'\'\')'
    return code


intro()
while True:
    reset()
    strength=0
    fl=open(infile,"r")
    code=fl.read()
    fl.close()
    obfuscate()
    ch=input("  Press enter to re-obfuscate, or S to change the setting:")
    if ch=="S" or ch=="s" or ch=="settings" or ch=="SETTINGS" or ch=="Settings":sett() 
    print()

