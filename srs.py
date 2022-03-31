from time import sleep
import os, signal
import sys
import subprocess

class SRS:
    def __init__(self):
        self.ue_process = None
        self.ue_command = "sleep 100"

        self.enb_process = None
        self.enb_command = "sleep 100"
        
        self.epc_process = None
        self.epc_command = "sleep 100"

        self.topics = [
            ("ue", "Sending ue signal toggle", self.startUE),
            ("enb", "Sending enb signal toggle", self.startENB),
            ("epc", "Sending epc signal toggle", self.startEPC)
        ]

    def startUE(self, one, two, three):
        if not self.ue_process:
            print("Starting UE...")
            self.ue_process = subprocess.Popen(self.ue_command)
        else:
            print("Turning off UE...")
            self.ue_process.kill()
            self.ue_process = None

    def startENB(self, one, two, three):
        if not self.enb_process:
            print("Starting ENB...")
            self.enb_process = subprocess.Popen(self.enb_command)
        else:
            print("Turning off ENB...")
            self.enb_process.kill()
            self.enb_process = None

    def startEPC(self, one, two, three):
        if not self.epc_process:
            print("Starting EPC...")
            self.epc_process = subprocess.Popen(self.epc_command)
        else:
            print("Turning off EPC...")
            self.epc_process.kill()
            self.epc_process = None











