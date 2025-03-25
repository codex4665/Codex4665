# WARNING: This script is for educational purposes only. Do not use it for malicious activities.

import os
import subprocess

# CODEX Banner
BANNER = """
 ██████╗ ██████╗ ██████╗ ███████╗██╗  ██╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝╚██╗██╔╝
██║     ██║   ██║██║  ██║█████╗   ╚███╔╝ 
██║     ██║   ██║██║  ██║██╔══╝   ██╔██╗ 
╚██████╗╚██████╔╝██████╔╝███████╗██╔╝ ██╗
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
  Kali Linux Updater & System Maintenance Tool
"""

print(BANNER)

# Function to update Kali Linux
def update_kali():
    print("[*] Starting Kali Linux update process...")
    
    try:
        # Display the contents of /etc/apt/sources.list
        print("[*] Displaying /etc/apt/sources.list...")
        subprocess.run(["cat", "/etc/apt/sources.list"], check=True)
        
        # Update the package list
        print("[*] Running 'sudo apt update'...")
        subprocess.run(["sudo", "apt", "update"], check=True)
        
        # Upgrade installed packages
        print("[*] Running 'sudo apt upgrade -y'...")
        subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
        
        # Perform a full upgrade
        print("[*] Running 'sudo apt full-upgrade -y'...")
        subprocess.run(["sudo", "apt", "full-upgrade", "-y"], check=True)
        
        # Perform a distribution upgrade
        print("[*] Running 'sudo apt dist-upgrade -y'...")
        subprocess.run(["sudo", "apt", "dist-upgrade", "-y"], check=True)
        
        # Remove unused packages
        print("[*] Running 'sudo apt autoremove -y'...")
        subprocess.run(["sudo", "apt", "autoremove", "-y"], check=True)
        
        # Clean up package cache
        print("[*] Running 'sudo apt clean -y'...")
        subprocess.run(["sudo", "apt", "clean", "-y"], check=True)
        
        print("[+] Kali Linux update completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"[-] Error during update process: {e}")

# Main function
def main():
    update_kali()

if __name__ == "__main__":
    main()
