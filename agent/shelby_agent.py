import json
import time

class ShelbyAgent:

    def __init__(self, config):
        self.wallet = config["wallet"]
        self.platforms = config["platforms"]

    def scan_platforms(self):
        for platform in self.platforms:
            print(f"Scanning {platform}")

    def run(self):
        while True:
            self.scan_platforms()
            time.sleep(10)

print("Shelby agent running")
