import requests, os, sys, socket, platform, time

# কালার কোড
R, G, Y, C, W = '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;36m', '\033[1;37m'

def banner():
    os.system('clear')
    print(f"""{C}
    ╔═══════════════════════════════════════════╗
    ║  {Y}██████╗ ██╗   ██╗██████╗  █████╗ ███████╗{C}  ║
    ║  {Y}██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔════╝{C}  ║
    ║  {Y}██████╔╝██║   ██║██████╔╝███████║█████╗  {C}  ║
    ║  {Y}██╔══██╗██║   ██║██╔══██╗██╔══██║██╔══╝  {C}  ║
    ║  {Y}██║  ██║╚██████╔╝██████╔╝██║  ██║███████╗{C}  ║
    ║  {Y}╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝{C}  ║
    ║       {G}ULTRA TOOL V4 - Rubaeat Edition{C}      ║
    ╠═══════════════════════════════════════════╣
    ║ {W}Advanced Features | Created by Rubaeat    {C}║
    ╚═══════════════════════════════════════════╝{W}""")

# ১. ইউজারনেম ট্র্যাকার (OSINT)
def username_tracker():
    user = input(f"\n{G}ইউজারনেম দিন: {W}")
    sites = {
        "Facebook": f"https://www.facebook.com/{user}",
        "Instagram": f"https://www.instagram.com/{user}",
        "GitHub": f"https://github.com/{user}",
        "Twitter": f"https://twitter.com/{user}"
    }
    print(f"{Y}চেক করা হচ্ছে...{W}")
    for name, url in sites.items():
        try:
            req = requests.get(url, timeout=5)
            if req.status_code == 200:
                print(f"{G}[+] {name}: {url} (পাওয়া গেছে!){W}")
            else:
                print(f"{R}[-] {name}: পাওয়া যায়নি।{W}")
        except: print(f"{R}[!] {name}: কানেকশন এরর।{W}")

# ২. অ্যাডমিন প্যানেল ফাইন্ডার
def admin_finder():
    site = input(f"\n{G}ওয়েবসাইট লিঙ্ক (যেমন google.com): {W}")
    paths = ['/admin', '/login', '/wp-admin', '/admin.php', '/cp']
    print(f"{Y}অ্যাডমিন পেজ খোঁজা হচ্ছে...{W}")
    for p in paths:
        url = f"http://{site}{p}"
        try:
            r = requests.get(url, timeout=3)
            if r.status_code == 200:
                print(f"{G}[FOUND] {url}{W}")
        except: pass

# ৩. ভিপিএন/প্রক্সি চেকার
def proxy_check():
    print(f"{Y}চেক করা হচ্ছে...{W}")
    res = requests.get("http://ip-api.com/json/").json()
    if res.get('proxy') or res.get('hosting'):
        print(f"{R}[!] আপনি ভিপিএন বা প্রক্সি ব্যবহার করছেন।{W}")
    else:
        print(f"{G}[+] আপনি সুরক্ষিত রিয়েল আইপিতে আছেন।{W}")

# ৪. পাসওয়ার্ড টেস্টার
def password_check():
    pwd = input(f"\n{G}আপনার পাসওয়ার্ড লিখুন: {W}")
    if len(pwd) < 8: print(f"{R}খুব দুর্বল! (৮ অক্ষরের কম){W}")
    elif pwd.isdigit() or pwd.isalpha(): print(f"{Y}মাঝারি। (অক্ষর ও সংখ্যা মিশিয়ে দিন){W}")
    else: print(f"{G}খুব শক্তিশালী পাসওয়ার্ড! 🔥{W}")

# ৫. আইপি ট্র্যাকার (আগেরটা)
def ip_tracker():
    ip = input(f"\n{G}IP দিন (ফাঁকা রাখলে নিজেরটা): {W}")
    res = requests.get(f"http://ip-api.com/json/{ip}").json()
    if res['status'] == 'success':
        print(f"{C}দেশ: {W}{res['country']}\n{C}শহর: {W}{res['city']}\n{C}আইএসপি: {W}{res['isp']}")
    else: print(f"{R}ভুল আইপি!")

def main():
    while True:
        banner()
        print(f"{Y}[1]{W} Username Tracker (সোশ্যাল মিডিয়া)")
        print(f"{Y}[2]{W} Admin Panel Finder (ওয়েবসাইট)")
        print(f"{Y}[3]{W} IP Tracker (লোকেশন)")
        print(f"{Y}[4]{W} Proxy/VPN Checker")
        print(f"{Y}[5]{W} Password Strength Checker")
        print(f"{Y}[0]{W} Exit")
        
        choice = input(f"\n{G}আপনার পছন্দ: {W}")
        if choice == '1': username_tracker()
        elif choice == '2': admin_finder()
        elif choice == '3': ip_tracker()
        elif choice == '4': proxy_check()
        elif choice == '5': password_check()
        elif choice == '0': sys.exit()
        
        input(f"\n{Y}ফিরে যেতে এন্টার দিন...")

if __name__ == "__main__":
    main()