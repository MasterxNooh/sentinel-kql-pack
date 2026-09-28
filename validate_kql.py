#!/usr/bin/env python3
"""Basic structural validator for KQL query files."""
import os
import sys

QUERIES_DIR = "queries"
VALID_TABLES = [
    "SigninLogs", "AuditLogs", "OfficeActivity", "DeviceProcessEvents",
    "DeviceEvents", "DeviceNetworkEvents", "SecurityEvent", "Syslog",
    "AADSignInEventsBeta", "AADNonInteractiveUserSignInLogs",
    "AzureActivity", "CommonSecurityLog", "Heartbeat",
]


def validate_file(path):
    errors = []
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.strip():
        return ["file is empty"]

    lines = [l for l in content.splitlines() if l.strip() and not l.strip().startswith("//")]
    if not lines:
        return ["file contains only comments"]

    first_line = lines[0].strip()
    first_token = first_line.split()[0] if first_line.split() else ""
    if first_token not in VALID_TABLES and not first_token.lower().startswith("let"):
        errors.append(f"first token '{first_token}' is not a recognized Sentinel table or 'let' statement")

    if "|" not in content:
        errors.append("no pipe (|) found - this doesn't look like KQL")

    return errors


def main():
    if not os.path.isdir(QUERIES_DIR):
        print(f"[!] Directory '{QUERIES_DIR}' not found.")
        sys.exit(1)

    total = 0
    failed = 0
    for root, _, files in os.walk(QUERIES_DIR):
        for name in sorted(files):
            if name.endswith(".kql"):
                total += 1
                path = os.path.join(root, name)
                errs = validate_file(path)
                if errs:
                    failed += 1
                    print(f"[FAIL] {path}")
                    for e in errs:
                        print(f"       - {e}")
                else:
                    print(f"[ OK ] {path}")

    print(f"\n{total - failed}/{total} queries passed.")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
