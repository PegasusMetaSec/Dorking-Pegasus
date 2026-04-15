import requests
from bs4 import BeautifulSoup
import time
import random
from urllib.parse import urlparse
from colorama import Fore, Style, init
import os

os.system("cls" if os.name == "nt" else "clear")

init(autoreset=True)

if not os.path.exists('results'):
    os.makedirs('results')

def print_banner():
    banner = """
          ██████╗ ███████╗ ██████╗  █████╗ ███████╗██╗   ██╗███████╗
          ██╔══██╗██╔════╝██╔════╝ ██╔══██╗██╔════╝██║   ██║██╔════╝
          ██████╔╝█████╗  ██║  ███╗███████║███████╗██║   ██║███████╗
          ██╔═══╝ ██╔══╝  ██║   ██║██╔══██║╚════██║██║   ██║╚════██║
          ██║     ███████╗╚██████╔╝██║  ██║███████║╚██████╔╝███████║
          ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝
                                                               DORK
    """
    print(Fore.CYAN + banner)
    print(Fore.LIGHTYELLOW_EX + "\n[+] Pegasus Dork - Advanced Google Dorking Tool")
    print(Fore.LIGHTYELLOW_EX + "[+] Created by Pegasus Team\n")

def search_google(dork, max_results=50):
    """Search Google with dork and return websites"""
    websites = []
    start = 0
    
    try:
        while start < max_results:
            url = f"https://www.google.com/search?q={dork}&start={start}"
            headers = {
                "User-Agent": random.choice([
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
                ]),
                "Accept-Language": "en-US,en;q=0.9"
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all links
            for link in soup.find_all('a'):
                href = link.get('href', '')
                if '/url?q=' in href:
                    website = href.split('/url?q=')[1].split('&')[0]
                    if website.startswith('http') and 'google.com' not in website:
                        websites.append(website)
            
            start += 10
            time.sleep(random.uniform(1, 3))  # Delay to avoid blocking
            
    except Exception as e:
        print(Fore.RED + f"[ERROR] {str(e)}")
    
    return websites

def extract_domains(websites):
    """Extract main domains from websites"""
    domains = set()
    for website in websites:
        try:
            domain = urlparse(website).netloc
            if domain:
                domains.add(f"https://{domain}")
        except:
            continue
    return list(domains)

def save_results(results, dork_name):
    """Save results to file"""
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"results/pegasus_{dork_name[:30]}_{timestamp}.txt"
    
    with open(filename, 'w') as f:
        for result in results:
            f.write(result + "\n")
    
    print(Fore.GREEN + f"[✓] Saved {len(results)} results to {filename}")
    return filename

def main():
    print_banner()
    
    print(Fore.CYAN + "="*60)
    print(Fore.LIGHTWHITE_EX + "PEGASUS DORK - GOOGLE DORKING TOOL")
    print(Fore.CYAN + "="*60 + "\n")
    
    # Menu pilihan
    print(Fore.YELLOW + "[1] Single Dork Search")
    print(Fore.YELLOW + "[2] Multiple Dorks from List")
    print(Fore.YELLOW + "[3] Use Predefined Dorks")
    print(Fore.CYAN + "-"*40)
    
    choice = input(Fore.WHITE + "\n[?] Choose option (1/2/3) --> ")
    
    dorks = []
    
    if choice == "1":
        # Single dork
        dork = input(Fore.CYAN + "[?] Enter your dork query --> ")
        dorks = [dork]
        
    elif choice == "2":
        # Multiple dorks from file
        filename = input(Fore.CYAN + "[?] Enter filename (e.g., dorks.txt) --> ")
        try:
            with open(filename, 'r') as f:
                dorks = [line.strip() for line in f if line.strip()]
            print(Fore.GREEN + f"[✓] Loaded {len(dorks)} dorks from {filename}")
        except:
            print(Fore.RED + f"[✗] File {filename} not found!")
            return
            
    elif choice == "3":
        # Predefined dorks for Indonesian sites
        print(Fore.YELLOW + "\n[!] Using predefined dorks for .ac.id domains\n")
        dorks = [
            "inurl:index of site:ac.id",
            "intitle:index.of \"parent directory\" site:ac.id",
            "inurl:login site:ac.id",
            "inurl:admin site:ac.id",
            "inurl:config site:ac.id",
            "filetype:pdf site:ac.id",
            "filetype:doc site:ac.id",
            "inurl:database site:ac.id",
            "intitle:\"dashboard\" site:ac.id",
            "inurl:phpmyadmin site:ac.id"
        ]
        print(Fore.GREEN + f"[✓] Loaded {len(dorks)} predefined dorks")
    
    else:
        print(Fore.RED + "[✗] Invalid choice!")
        return
    
    if not dorks:
        print(Fore.RED + "[✗] No dorks to process!")
        return
    
    # Input parameters
    print(Fore.CYAN + "\n" + "-"*40)
    pages = int(input(Fore.CYAN + "[?] Pages per dork (1-5) --> "))
    delay = float(input(Fore.CYAN + "[?] Delay between requests (1-5 sec) --> "))
    
    print(Fore.LIGHTYELLOW_EX + f"\n[!] Starting Pegasus Dork with {len(dorks)} dorks...\n")
    
    start_time = time.time()
    all_results = {}
    
    for i, dork in enumerate(dorks, 1):
        print(Fore.LIGHTYELLOW_EX + f"\n[{i}/{len(dorks)}] Processing: {dork}")
        
        # Search Google
        websites = []
        for page in range(pages):
            print(Fore.WHITE + f"  → Page {page+1}...", end=" ")
            results = search_google(dork, max_results=(page+1)*10)
            
            if results:
                websites.extend(results)
                print(Fore.GREEN + f"Found {len(results)} URLs")
            else:
                print(Fore.RED + "No results")
            
            time.sleep(delay)
        
        if websites:
            # Extract unique domains
            domains = extract_domains(websites)
            print(Fore.GREEN + f"  ✓ Total unique domains: {len(domains)}")
            
            # Save results
            dork_name = dork.replace(' ', '_').replace(':', '_')[:30]
            filename = save_results(domains, dork_name)
            all_results[dork] = filename
        else:
            print(Fore.RED + f"  ✗ No results found for: {dork}")
    
    # Summary
    elapsed = time.time() - start_time
    print(Fore.CYAN + "\n" + "="*60)
    print(Fore.LIGHTGREEN_EX + f"\n[✓] PEGASUS DORK COMPLETED!")
    print(Fore.LIGHTGREEN_EX + f"[✓] Time elapsed: {elapsed:.2f} seconds")
    print(Fore.LIGHTGREEN_EX + f"[✓] Dorks processed: {len(dorks)}")
    print(Fore.LIGHTGREEN_EX + f"[✓] Successful dorks: {len(all_results)}")
    print(Fore.LIGHTGREEN_EX + f"[✓] Results saved in 'results' folder")
    print(Fore.CYAN + "="*60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\n[!] Dorking interrupted by user")
    except Exception as e:
        print(Fore.RED + f"\n[ERROR] {str(e)}")