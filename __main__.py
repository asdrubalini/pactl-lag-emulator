import subprocess
import time
import random


SOURCE_ID = "1"


class Microphone:
    def __init__(self, source_id: str):
        self.source_id = source_id

    def mute(self) -> bool:
        command = f"pactl set-source-mute {self.source_id} 1"

        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        p.wait()

        return p.returncode == 0

    def unmute(self) -> bool:
        command = f"pactl set-source-mute {self.source_id} 0"

        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        p.wait()

        return p.returncode == 0


def run(microphone: Microphone):
    while True:
        microphone.mute()
        time.sleep(random.uniform(0.1, 0.3))
        microphone.unmute()
        time.sleep(random.uniform(0.3, 0.5))


if __name__ == "__main__":
    microphone = Microphone(source_id=SOURCE_ID)

    try:
        run(microphone)

    except KeyboardInterrupt:
        microphone.unmute()
        print("Unmuting and closing...")
