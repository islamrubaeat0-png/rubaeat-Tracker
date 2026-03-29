import requests, os, sys, hashlib, socket, time, platform
from datetime import datetime

# কালার কোড (ইউনিক কম্বিনেশন)
R, G, Y, C, M, W = '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;36m', '\033[1;35m', '\033[1;37m'

def banner():
    os.system('clear')
    print(f"""{C}
    ╔═════════════════════════════════════════════════╗
    ║   {Y}██████╗ ██╗   ██╗██████╗  █████╗ ███████╗{C}     ║
    ║   {Y}██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔════╝{C}     ║
    ║   {Y}██████╔╝██║   ██║██████╔╝███████║█████╗  {C}     ║
    ║   {Y}██╔══██╗██║   ██║██╔══██╗██╔══██║██╔══╝  {C}     ║
    ║   {Y}██║  ██║╚██████╔╝██████╔╝██║  ██║███████╗{C}     ║
    ║   {Y}╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝{C}     ║
    ║             {G}RUBAEAT VS-8 EDITION{C}                ║
    ╠═════════════════════════════════════════════════╣
    ║ {W}Advanced Hacking Suite | Secure Recon | V-Audit {C}║
    ║ {M}Developer: Rubaeat Islam (Top 9 Specialist)     {C}║
    ╚═════════════════════════════════════════════════╝{W}""")

# ১. নিওরাল এনক্রিপশন (ডাটা গোপন করা)
def neural_encryptor():
    print(f"\n{Y}[!] ডাটা এনক্রিপ্ট করুন (Advanced SHA-256 Vault)")
    msg = input(f"{G}গোপন মেসেজ লিখুন: {W}")
    salt = "RUBAEAT_SECURE_8"
    hashed = hashlib.sha256((msg + salt).encode()).hexdigest()
    print(f"{C}আপনার এনক্রিপ্টেড কী: {G}{hashed}{W}")
    with open("vault_vs8.txt", "a") as f:
        f.write(f"Date: {datetime.now()} | Text: {msg} | Key: {hashed}\n")
    print(f"{Y}[+] ডাটা ভল্টে সেভ করা হয়েছে।{W}")

# ২. সিকিউরিটি অডিটর (ওয়েবসাইট দুর্বলতা বের করা)
def security_auditor():
    domain = input(f"\n{G}ওয়েবসাইট লিঙ্ক দিন (যেমন google.com): {W}")
    if "://" not in domain: domain = "http://" + domain
    try:
        print(f"{Y}[*] অডিট শুরু হচ্ছে...{W}")
        r = requests.get(domain, timeout=7)
        headers = r.headers
        print(f"\n{C}─── [ RUBAEAT VS-8 SECURITY REPORT ] ───{W}")
        
        vulnerabilities = {
            "X-Frame-Options": ("Clickjacking", "পাওয়াই যায়নি! এটি একটি বড় ঝুঁকি।"),
            "Content-Security-Policy": ("XSS Attack", "নিরাপত্তা স্তর পাওয়া যায়নি।"),
            "Strict-Transport-Security": ("HSTS Header", "ওয়েবসাইট এনক্রিপশন দুর্বল।")
        }
        
        for h, (risk, info) in vulnerabilities.items():
            if h in headers:
                print(f"{G}[✔] {h}: সুরক্ষিত{W}")
            else:
                print(f"{R}[✘] {h}: {risk} ({info}){W}")
        
        print(f"{C}সার্ভার সফটওয়্যার: {W}{headers.get('Server', 'Unknown')}")
        print(f"{C}রেসপন্স টাইম: {W}{r.elapsed.total_seconds()} seconds")
        print(f"{C}────────────────────────────────────────{W}")
    except Exception as e:
        print(f"{R}[!] এরর: {e}{W}")

# ৩. নেটওয়ার্ক ওয়াচডগ (টার্গেট মনিটরিং)
def network_watchdog():
    target = input(f"{G}টার্গেট আইপি বা হোস্ট দিন: {W}")
    print(f"{Y}[*] লাইভ মনিটরিং শুরু... (বন্ধ করতে Ctrl+C চাপুন){W}")
    try:
        while True:
            response = os.system(f"ping -c 1 {target} > /dev/null")
            status = f"{G}ONLINE" if response == 0 else f"{R}OFFLINE"
            print(f"{C}[{datetime.now().strftime('%H:%M:%S')}] {W}Target: {target} | Status: {status}{W}")
            time.sleep(3)
    except KeyboardInterrupt:
        print(f"\n{Y}[!] মনিটরিং বন্ধ করা হয়েছে।{W}")

# ৪. টার্মাক্স অপ্টিমাইজার (সিস্টেম বুস্ট)
def optimizer():
    print(f"{Y}[*] টার্মাক্স জাঙ্ক ফাইল পরিষ্কার করা হচ্ছে...{W}")
    os.system("rm -rf ~/.cache/*")
    os.system("apt autoremove -y && apt clean")
    print(f"{G}[+] Rubaeat vs8 এখন সুপার ফাস্ট!{W}")

def main():
    while True:
        banner()
        print(f"{Y}[1]{W} Neural Encryptor (গোপন ডাটা লক)")
        print(f"{Y}[2]{W} Web Security Auditor (দুর্বলতা খোঁজা)")
        print(f"{Y}[3]{W} Network Watchdog (লাইভ ট্র্যাকিং)")
        print(f"{Y}[4]{W} System Optimizer (টার্মাক্স বুস্ট)")
        print(f"{Y}[5]{W} View Security Vault (সংরক্ষিত ডাটা)")
        print(f"{Y}[0]{W} Exit")
        
        choice = input(f"\n{G}কমান্ড দিন >> {W}")
        
        if choice == '1':
            neural_encryptor()
        elif choice == '2':
            security_auditor()
        elif choice == '3':
            network_watchdog()
        elif choice == '4':
            optimizer()
        elif choice == '5':
            if os.path.exists("vault_vs8.txt"):
                print(f"\n{G}--- সংরক্ষিত ভল্ট ডাটা ---{W}")
                print(open("vault_vs8.txt").read())
            else:
                print(f"{R}[!] ভল্ট এখন খালি।{W}")
        elif choice == '0':
            print(f"{G}Rubaeat vs8 বন্ধ হচ্ছে... বিদায় বন্ধু!{W}")
            sys.exit()
        else:
            print(f"{R}[!] ভুল অপশন সিলেক্ট করেছেন।{W}")
            
        input(f"\n{C}ফিরে যেতে এন্টার দিন...{W}")

if __name__ == "__main__":
    main()