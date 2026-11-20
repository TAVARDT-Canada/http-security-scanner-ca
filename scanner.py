#!/usr/bin/env python3
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

SECURITY_HEADERS = [('Strict-Transport-Security', 'Enforces HTTPS encryption and prevents downgrade vectors.'), ('Content-Security-Policy', 'Restricts resource loading to protect against XSS injections.'), ('X-Frame-Options', 'Mitigates clickjacking attacks by managing framing permissions.'), ('X-Content-Type-Options', 'Prevents client browsers from executing MIME-sniffing.'), ('Referrer-Policy', 'Protects sensitive URL query parameters from cross-domain disclosure.'), ('Permissions-Policy', 'Restricts unauthorized browser device API access.')]

def scan_target(target_url):
    print(f"\n[TAVARDT Canada] Starting HTTP security headers perimeter audit for: {target_url}\n")
    try:
        req = urllib.request.Request(
            target_url,
            headers={"User-Agent": "TAVARDT-Security-Scanner/3.0 (en-CA)"}
        )
        with urllib.request.urlopen(req, timeout=12) as response:
            headers = dict(response.headers.items())
            
            score = 0
            total = len(SECURITY_HEADERS)
            
            for header_name, desc in SECURITY_HEADERS:
                found = any(h.lower() == header_name.lower() for h in headers.keys())
                if found:
                    print(f"  [PASS] {header_name}")
                    score += 1
                else:
                    print(f"  [FAIL] {header_name}: {desc}")
                    
            print(f"\n[TAVARDT Canada] Audit Score: {score}/{total}")
            print(f"\nFull online diagnostic tool: https://tools.tavardt.com/ca/security-headers-check/")
            print(f"Corporate defense and cybersecurity consulting: https://ag.tavardt.com/ca/cybersecurity/\n")
            
    except urllib.error.URLError as e:
        print(f"[TAVARDT Canada] Error inspecting target: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1].strip()
    if not urlparse(url).scheme:
        url = "https://" + url
        
    scan_target(url)
