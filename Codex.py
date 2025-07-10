import os
import subprocess
import distro  # مكتبة لاكتشاف توزيعة النظام
import time
from termcolor import colored  # مكتبة لإضافة ألوان للنصوص في الطرفية

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

# Function to detect the system distribution
def detect_system():
    distro_name = distro.id().lower()  # استخدام مكتبة distro لاكتشاف التوزيعة
    if "kali" in distro_name:
        return "Kali Linux"
    elif "ubuntu" in distro_name:
        return "Ubuntu"
    elif "debian" in distro_name:
        return "Debian"
    else:
        return "Other Linux"

# Loading effect function
def loading(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.05)  # simulate typing effect
    print()

# Function to update Kali Linux
def update_kali():
    print(colored("[*] Starting Kali Linux update process...", "yellow"))
    
    try:
        # Display the contents of /etc/apt/sources.list
        loading(colored("[*] Displaying /etc/apt/sources.list...", "cyan"))
        subprocess.run(["cat", "/etc/apt/sources.list"], check=True)
        
        # Update the package list
        loading(colored("[*] Running 'sudo apt update'...", "cyan"))
        subprocess.run(["sudo", "apt", "update"], check=True)
        
        # Upgrade installed packages
        loading(colored("[*] Running 'sudo apt upgrade -y'...", "cyan"))
        subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
        
        # Perform a full upgrade
        loading(colored("[*] Running 'sudo apt full-upgrade -y'...", "cyan"))
        subprocess.run(["sudo", "apt", "full-upgrade", "-y"], check=True)
        
        # Perform a distribution upgrade
        loading(colored("[*] Running 'sudo apt dist-upgrade -y'...", "cyan"))
        subprocess.run(["sudo", "apt", "dist-upgrade", "-y"], check=True)
        
        # Remove unused packages
        loading(colored("[*] Running 'sudo apt autoremove -y'...", "cyan"))
        subprocess.run(["sudo", "apt", "autoremove", "-y"], check=True)
        
        # Clean up package cache
        loading(colored("[*] Running 'sudo apt clean -y'...", "cyan"))
        subprocess.run(["sudo", "apt", "clean", "-y"], check=True)
        
        print(colored("[+] Kali Linux update completed successfully!", "green"))
    except subprocess.CalledProcessError as e:
        print(colored(f"[-] Error during update process: {e}", "red"))

# Function to display a box with text
def print_box(message):
    print(colored("+" + "-"*(len(message)+2) + "+", "magenta"))
    print(colored("| " + message + " |", "magenta"))
    print(colored("+" + "-"*(len(message)+2) + "+", "magenta"))

# Main function
def main():
    # عرض Banner عند بداية تشغيل الأداة
    print(colored(BANNER, "magenta"))

    # كشف نوع النظام قبل البدء
    system_type = detect_system()
    print_box(f"[+] Detected system: {system_type}")  # عرض نوع النظام داخل صندوق جميل
    print("="*50)  # خط فاصل لتنسيق المخرجات

    # البدء في تحديث النظام
    update_kali()

if __name__ == "__main__":
    main()
