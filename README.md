# massh

Concurrent SSH for DevOps and NetOps (proof of concept)

massh runs one or many Linux commands across many hosts in parallel.  
On each host, commands run sequentially. Across hosts, they run concurrently (up to 200).  
It uses the existing SSH keys in `~/.ssh`, skips known_hosts verification for faster lab or POC use, and logs both successes and failures.

---

## Why massh

Ops and network engineers often need to push simple checks or fixes to many systems at once.  
massh is designed to be a small and testable tool for that: predictable, key-based authentication, no extra agents or daemons, and a clear summary of what worked and what failed.

---

## Scope for this proof of concept

- Default user: ccplayer  
- Default key: `~/.ssh/id_rsa`  
- Inventory file: `hosts.txt`, one host per line (optional `:port`)  
- Commands: one or many; run sequentially on each host  
- Concurrency limit: 200 hosts  
- Logging: written to a file and summarized on the CLI

---

## Out of scope for now

- Per-host credentials  
- sudo escalation  
- File transfer (SCP/SFTP)  
- Strict host key verification
