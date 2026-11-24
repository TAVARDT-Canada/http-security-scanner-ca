# HTTP Security Headers Scanner

[![Scope of Perimeter Verification](https://img.shields.io/badge/TAVARDT-Technical%20Audit-5b3cf5.svg)](https://tools.tavardt.com/ca/security-headers-check/)
Automated technical audit of HTTP security headers aligned with Canadian Centre for Cyber Security guidelines, PIPEDA, and Bill C-27 standards.

Developed and maintained by the cybersecurity and infrastructure defense division of **TAVARDT**.

***

## 1. Scope of Perimeter Verification

This command-line utility audits essential browser security controls and transport layer configurations:

* **Strict-Transport-Security (HSTS):** Enforces HTTPS encryption and prevents downgrade vectors.
* **Content-Security-Policy (CSP):** Restricts resource loading to protect against XSS injections.
* **X-Frame-Options:** Mitigates clickjacking attacks by managing framing permissions.
* **X-Content-Type-Options:** Prevents client browsers from executing MIME-sniffing.
* **Referrer-Policy:** Protects sensitive URL query parameters from cross-domain disclosure.
* **Permissions-Policy:** Restricts unauthorized browser device API access.

***

## 2. Quick Start Guide

Run this tool directly via Python without installing third-party packages:

```bash
python scanner.py example.ca
```

***

## 3. Online Diagnostic Tools (Canada)

Audit the public perimeter of your systems using the TAVARDT technical verification suite:

* HTTP Security Headers Checker
* [Consent Mode v2 & PIPEDA Validator](https://tools.tavardt.com/ca/consent-mode-v2-checker/)
* [DMARC & Anti-Spoofing Verifier](https://tools.tavardt.com/ca/dmarc-checker/)
* [Exposed Credentials & Secret Scanner](https://tools.tavardt.com/ca/exposed-files-scanner/)
* [Full Canadian Tools Portal](https://tools.tavardt.com/ca/)

***

## 4. Technical Advisory & Remediation

For enterprise cyber defence consulting, data governance alignment, and security audits in Canada, contact **TAVARDT**.

***

© 2026 TAVARDT. All rights reserved.
