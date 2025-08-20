#!/usr/bin/env python3
import shutil
import subprocess

def run(cmd):
    try:
        out = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True, timeout=5)
        return out.strip()
    except Exception as e:
        return f"error: {e}"

if shutil.which("ufw"):
    print("UFW status:")
    print(run("ufw status"))
elif shutil.which("iptables"):
    print("iptables (filter) rules:")
    print(run("iptables -S"))
else:
    print("No ufw/iptables found. This script is optional for local info only.")