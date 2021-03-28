import subprocess
import time
import random


SOURCE_ID = "1"


def mute() -> bool:
    command = f"pactl set-source-mute {SOURCE_ID} 1"

    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    p.wait()

    return p.returncode == 0


def unmute() -> bool:
    command = f"pactl set-source-mute {SOURCE_ID} 0"

    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    p.wait()

    return p.returncode == 0


def main():
    while True:
        mute()
        time.sleep(random.uniform(0.1, 0.3))
        unmute()
        time.sleep(random.uniform(0.3, 0.5))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        unmute()
        print("Unmuting and closing...")
