import subprocess
# import time
from pynput import keyboard
# from pynput.keyboard import HotKey
# from pynput.keyboard import Key

MAC_ADDRESS_C1 = 'ENTER MAC TV1 HERE'
MAC_ADDRESS_C2 = 'ENTER MAC TV2 HERE'
TV_IP_C1 = 'ENTER IP TV1 HERE'
TV_IP_C2 = 'ENTER IP TV2 HERE'
SECRET_C1 = 'ENTER SECRET TV1 HERE'
SECRET_C2 = 'ENTER SECRET TV2 HERE'


GLOBAL_MUTE_C1 = "off" #LEAVE THOSE ALONE.
GLOBAL_MUTE_C2 = "off" #LEAVE THOSE ALONE.

# Find the key number of the keyboard.
# for key in Key:
#     if isinstance(key, Key):
#         print(f"Key code: {key.value}, Key name: {key.name}")

#TURN MONITOR OFF FUNCTION.
def monitor_off(tv):
    if tv == "C1":
        command = ["bin/lgtv-ip-control-cli-win.exe", "-o", TV_IP_C1, "-m", MAC_ADDRESS_C1, "-k", SECRET_C1,
                   "power", "off"]
        process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)
    elif tv == "C2":
        command = ["bin/lgtv-ip-control-cli-win.exe", "-o", TV_IP_C2, "-m", MAC_ADDRESS_C2, "-k", SECRET_C2,
                   "power", "off"]
        process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)

#TURN MONITOR ON FUNCTION.
def monitor_on(tv):
    if tv == "C1":
        command = [r"bin\lgtv-ip-control-cli-win.exe", "-o", TV_IP_C1, "-m", MAC_ADDRESS_C1, "-k", SECRET_C1,
                   "power", "on"]
        process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)
    elif tv == "C2":
        command = [r"bin\lgtv-ip-control-cli-win.exe", "-o", TV_IP_C2, "-m", MAC_ADDRESS_C2, "-k", SECRET_C2,
                   "power", "on"]
        process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)
    # Debug output messages.
    # print("STDOUT:", process.stdout)
    # print("STDERR:", process.stderr)

#SWITCH TO INPUT 3 ON TV 1 AND INPUT 2 ON TV2.
def hdmi_2(tv):
    if tv == "C1":
        command = ["bin/lgtv-ip-control-cli-win.exe", "-o", TV_IP_C1, "-m", MAC_ADDRESS_C1, "-k", SECRET_C1,
                   "input", "3"]
        process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)
    elif tv == "C2":
        command = ["bin/lgtv-ip-control-cli-win.exe", "-o", TV_IP_C2, "-m", MAC_ADDRESS_C2, "-k", SECRET_C2,
                   "input", "2"]
        process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)

#SWITCH TO INPUT 2 ON TV 1 AND INPUT 1 ON TV2
def hdmi_1(tv):
    if tv == "C1":
        command = ["bin/lgtv-ip-control-cli-win.exe", "-o", TV_IP_C1, "-m", MAC_ADDRESS_C1, "-k", SECRET_C1,
                   "input", "2"]
        process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)
    elif tv == "C2":
        command = ["bin/lgtv-ip-control-cli-win.exe", "-o", TV_IP_C2, "-m", MAC_ADDRESS_C2, "-k", SECRET_C2,
                   "input", "1"]
        process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)

#SET VOLUME PERCENTAGE TO 40.
def volume_40(tv):
    if tv == "C1":
        command = ["bin/lgtv-ip-control-cli-win.exe", "-o", TV_IP_C1, "-m", MAC_ADDRESS_C1, "-k", SECRET_C1,
                   "volume", "40"]
        process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)
    elif tv == "C2":
        command = ["bin/lgtv-ip-control-cli-win.exe", "-o", TV_IP_C2, "-m", MAC_ADDRESS_C2, "-k", SECRET_C2,
                   "volume", "40"]
        process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)

#SET VOLUME PERCENTAGE TO 30.
def volume_30(tv):
    if tv == "C1":
        command = ["bin/lgtv-ip-control-cli-win.exe", "-o", TV_IP_C1, "-m", MAC_ADDRESS_C1, "-k", SECRET_C1,
                   "volume", "30"]
        process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)
    elif tv == "C2":
        command = ["bin/lgtv-ip-control-cli-win.exe", "-o", TV_IP_C2, "-m", MAC_ADDRESS_C2, "-k", SECRET_C2,
                   "volume", "30"]
        process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)

#SET VOLUME PERCENTAGE TO 20.
def volume_20(tv):
    if tv == "C1":
        command = ["bin/lgtv-ip-control-cli-win.exe", "-o", TV_IP_C1, "-m", MAC_ADDRESS_C1, "-k", SECRET_C1,
                   "volume", "20"]
        process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)
    elif tv == "C2":
        command = ["bin/lgtv-ip-control-cli-win.exe", "-o", TV_IP_C2, "-m", MAC_ADDRESS_C2, "-k", SECRET_C2,
                   "volume", "20"]
        process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)

#SET VOLUME PERCENTAGE TO 10.
def volume_10(tv):
    if tv == "C1":
        command = ["bin/lgtv-ip-control-cli-win.exe", "-o", TV_IP_C1, "-m", MAC_ADDRESS_C1, "-k", SECRET_C1,
                   "volume", "10"]
        process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)
    elif tv == "C2":
        command = ["bin/lgtv-ip-control-cli-win.exe", "-o", TV_IP_C2, "-m", MAC_ADDRESS_C2, "-k", SECRET_C2,
                   "volume", "10"]
        process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)

#MUTE TV FUNCTION.
def mute_btn(tv):
    global GLOBAL_MUTE_C1, GLOBAL_MUTE_C2
    if tv == "C1":
        if GLOBAL_MUTE_C1 == "on":
            command = ["bin/lgtv-ip-control-cli-win.exe", "-o", TV_IP_C1, "-m", MAC_ADDRESS_C1, "-k", SECRET_C1,
                       "mute", "off"]
            process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)
            GLOBAL_MUTE_C1 = "off"
        elif GLOBAL_MUTE_C1 == "off":
            command = ["bin/lgtv-ip-control-cli-win.exe", "-o", TV_IP_C1, "-m", MAC_ADDRESS_C1, "-k", SECRET_C1,
                       "mute", "on"]
            process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)
            GLOBAL_MUTE_C1 = "on"

    elif tv == "C2":
        if GLOBAL_MUTE_C2 == "on":
            command = ["bin/lgtv-ip-control-cli-win.exe", "-o", TV_IP_C2, "-m", MAC_ADDRESS_C2, "-k", SECRET_C2,
                       "mute", "off"]
            process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)
            GLOBAL_MUTE_C2 = "off"
        elif GLOBAL_MUTE_C2 == "off":
            command = ["bin/lgtv-ip-control-cli-win.exe", "-o", TV_IP_C2, "-m", MAC_ADDRESS_C2, "-k", SECRET_C2,
                       "mute", "on"]
            process = subprocess.Popen(command, creationflags=subprocess.CREATE_NO_WINDOW)
            GLOBAL_MUTE_C2 = "on"

#PRESSED HOTKEYS WILL ACTIVATE FUNCTIONS.
hotkeys_actions = {
    '<ctrl>+<shift>+<123>': lambda: monitor_off(tv="C1"),  # CTRL+SHIFT+F12
    '<ctrl>+<shift>+<122>': lambda: monitor_on(tv="C1"),  # CTRL+SHIFT+F11
    '<ctrl>+<shift>+<121>': lambda: hdmi_2(tv="C1"),  # CTRL+SHIFT+F10
    '<ctrl>+<shift>+<120>': lambda: hdmi_1(tv="C1"),  # CTRL+SHIFT+F9
    '<ctrl>+<shift>+<119>': lambda: volume_40(tv="C1"),  # CTRL+SHIFT+F8
    '<ctrl>+<shift>+<118>': lambda: volume_30(tv="C1"),  # CTRL+SHIFT+F7
    '<ctrl>+<shift>+<117>': lambda: volume_20(tv="C1"),  # CTRL+SHIFT+F6
    '<ctrl>+<shift>+<116>': lambda: volume_10(tv="C1"),  # CTRL+SHIFT+F5
    '<ctrl>+<shift>+<115>': lambda: mute_btn(tv="C1"),  # CTRL+SHIFT+F4
    '<ctrl>+<alt>+<123>': lambda: monitor_off(tv="C2"),  # CTRL+ALT+F12
    '<ctrl>+<alt>+<122>': lambda: monitor_on(tv="C2"),  # CTRL+ALT+F11
    '<ctrl>+<alt>+<121>': lambda: hdmi_2(tv="C2"),  # CTRL+ALT+F10
    '<ctrl>+<alt>+<120>': lambda: hdmi_1(tv="C2"),  # CTRL+ALT+F9
    '<ctrl>+<alt>+<119>': lambda: volume_40(tv="C2"),  # CTRL+ALT+F8
    '<ctrl>+<alt>+<118>': lambda: volume_30(tv="C2"),  # CTRL+ALT+F7
    '<ctrl>+<alt>+<117>': lambda: volume_20(tv="C2"),  # CTRL+ALT+F6
    '<ctrl>+<alt>+<116>': lambda: volume_10(tv="C2"),  # CTRL+ALT+F5
    '<ctrl>+<alt>+<115>': lambda: mute_btn(tv="C2")  # CTRL+ALT+F4
}

#LISTEN FOR PRESSED HOTKEYS.
with keyboard.GlobalHotKeys(hotkeys_actions) as h:
    h.join()
