# 🔐 Network Audit Automation with n8n + Python

Automate **network checks** and send results to **Google Sheets** using **n8n** + lightweight **Python** scripts.

## ✨ Features
- Ping host + check TCP **22/SSH** reachability (from your n8n environment).
- Daily schedule or manual trigger.
- Append structured results to **Google Sheets**: Date, Host, Ping, SSH, Status.

## 🧩 Contents
```
network-audit-automation/
├─ README.md
├─ n8n-workflow.json        # import into n8n
└─ scripts/
   ├─ ssh_audit.py          # sample local test for SSH port
   └─ firewall_audit.py     # sample local firewall info (optional)
```

## 🚀 Quick Start
1) **Import** `n8n-workflow.json` into your n8n instance.
2) In node **Set Hosts**, change the array to your target hosts.
3) Create a Google Sheet with sheet name **Audit** and header row:
   `Date | Host | Ping | SSH | Status`
4) In node **Google Sheets: Append** set:
   - **Credentials** (Google API)  
   - **Document ID** (from your Google Sheets URL)
5) **Run Once** or wait for the daily schedule (00:00 UTC).

> Note: The connectivity checks run **from the n8n host/container**. Make sure `ping` and `nc` are available. For Debian/Ubuntu-based images:
> `apt-get update && apt-get install -y iputils-ping netcat-openbsd`

## 🧪 Local quick tests
Run the sample Python script locally:

```bash
python3 scripts/ssh_audit.py 8.8.8.8
python3 scripts/firewall_audit.py
```

## 📄 License
AGPL v3.0
