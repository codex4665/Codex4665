import os
import subprocess
import psutil
import distro
import socket
import getpass
from InquirerPy import inquirer
from termcolor import colored

# 🟣 Banner
BANNER = """
 ██████╗ ██████╗ ██████╗ ███████╗██╗  ██╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝╚██╗██╔╝
██║     ██║   ██║██║  ██║█████╗   ╚███╔╝ 
██║     ██║   ██║██║  ██║██╔══╝   ██╔██╗ 
╚██████╗╚██████╔╝██████╔╝███████╗██╔╝ ██╗
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
   CODEX v3 – Terminal Linux Maintainer
"""

# 🔁 Reset screen
def reset_screen():
    os.system("clear")
    print(colored(BANNER, "magenta"))

# 🟢 Detect Distro
def detect_system():
    name = distro.id().lower()
    if "kali" in name:
        return "Kali Linux"
    elif "ubuntu" in name:
        return "Ubuntu"
    elif "debian" in name:
        return "Debian"
    else:
        return "Other"

# 🔐 Root Check
def is_root():
    return os.geteuid() == 0

# 🌐 Internet Check
def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except:
        return False

# 📊 System Info
def system_info():
    print(colored("\n📋 System Information:", "cyan"))
    print(colored(f"🖥️  User: {getpass.getuser()}", "green"))
    print(colored(f"🧠 RAM Usage: {psutil.virtual_memory().percent}%", "green"))
    print(colored(f"💾 Disk Usage: {psutil.disk_usage('/').percent}%", "green"))
    print(colored(f"🌐 Internet: {'Connected' if check_internet() else 'Disconnected'}", "green"))
    print(colored(f"📦 OS: {detect_system()}", "green"))
    input(colored("\n🔁 Press Enter to return to main menu...", "cyan"))
    reset_screen()

# 🔄 Update System
def update_system():
    print(colored("\n🔄 Updating system...\n", "yellow"))
    cmds = [
        ["sudo", "apt", "update"],
        ["sudo", "apt", "upgrade", "-y"],
        ["sudo", "apt", "full-upgrade", "-y"],
        ["sudo", "apt", "dist-upgrade", "-y"]
    ]
    for cmd in cmds:
        print(colored(f"[+] {' '.join(cmd)}", "cyan"))
        subprocess.run(cmd)
    input(colored("\n✅ Update complete. Press Enter to return to menu...", "cyan"))
    reset_screen()

# 🧹 Clean System
def clean_system():
    print(colored("\n🧹 Cleaning system...\n", "yellow"))
    cmds = [
        ["sudo", "apt", "autoremove", "-y"],
        ["sudo", "apt", "clean", "-y"]
    ]
    for cmd in cmds:
        print(colored(f"[+] {' '.join(cmd)}", "cyan"))
        subprocess.run(cmd)
    input(colored("\n✅ Clean complete. Press Enter to return to menu...", "cyan"))
    reset_screen()

# 📄 Show sources.list
def show_sources():
    print(colored("\n📄 /etc/apt/sources.list:\n", "yellow"))
    subprocess.run(["cat", "/etc/apt/sources.list"])
    input(colored("\n🔁 Press Enter to return to main menu...", "cyan"))
    reset_screen()

# 📌 Check installed tools
def check_tools():
    tools = ["nmap", "wireshark", "metasploit-framework", "john", "hydra"]
    print(colored("\n📌 Checking common tools...\n", "yellow"))
    for tool in tools:
        found = subprocess.call(["which", tool], stdout=subprocess.DEVNULL) == 0
        status = "✅ Installed" if found else "❌ Not Found"
        print(f"{tool:<25} → {status}")
    input(colored("\n🔁 Press Enter to return to main menu...", "cyan"))
    reset_screen()

# 🧠 Main Menu
def main():
    reset_screen()
    
    if not is_root():
        print(colored("⚠️  Please run this script as root (sudo).", "red"))
        return

    while True:
        choice = inquirer.select(
            message="🛠️ What do you want to do?",
            choices=[
                "🔄 Update System",
                "🧹 Clean System",
                "📋 System Info",
                "📄 Show sources.list",
                "📌 Check Installed Tools",
                "❌ Exit"
            ],
            default=None,
        ).execute()

        if choice == "🔄 Update System":
            update_system()
        elif choice == "🧹 Clean System":
            clean_system()
        elif choice == "📋 System Info":
            system_info()
        elif choice == "📄 Show sources.list":
            show_sources()
        elif choice == "📌 Check Installed Tools":
            check_tools()
        elif choice == "❌ Exit":
            print(colored("\nوداعًا يا صديقي ❤️", "green"))
            break

if __name__ == "__main__":
    main()
