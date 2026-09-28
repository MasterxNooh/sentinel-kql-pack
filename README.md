# Sentinel KQL Pack

A collection of Microsoft Sentinel KQL detection queries for common attacker techniques across identity, endpoint, and cloud.

## Purpose

Microsoft Sentinel is one of the most widely deployed cloud SIEMs in enterprise environments. This pack gives SOC analysts and detection engineers a starting set of KQL queries mapped to MITRE ATT&CK, ready to paste into Sentinel and adapt to their environment.

Companion project: [sigma-rule-pack](https://github.com/MasterxNooh/sigma-rule-pack) — the same detections in vendor-neutral Sigma format.

## Queries

### Identity

| Query | Technique | Description |
|-------|-----------|-------------|
| `brute_force.kql` | T1110 | Failed sign-ins from a single IP |
| `password_spray.kql` | T1110.003 | Failed sign-ins across many users from one IP |
| `success_after_failures.kql` | T1078 | Successful sign-in shortly after repeated failures |
| `impossible_travel.kql` | T1078 | Successful sign-ins from distant countries in short time |
| `mfa_fatigue.kql` | T1621 | Repeated MFA prompts for one user |
| `privileged_role_assignment.kql` | T1098.003 | Addition of a user to a privileged Azure AD role |

### Endpoint

| Query | Technique | Description |
|-------|-----------|-------------|
| `suspicious_powershell.kql` | T1059.001 | PowerShell with encoded or download patterns |
| `lsass_access.kql` | T1003.001 | Process opening LSASS with credential-dump access masks |
| `anomalous_process_tree.kql` | T1204.002 | Office or PDF spawning a shell |

### Cloud

| Query | Technique | Description |
|-------|-----------|-------------|
| `inbox_rule_creation.kql` | T1114.003 | Suspicious inbox rule creation in Exchange Online |
| `mass_file_download.kql` | T1530 | Bulk file download from SharePoint or OneDrive |

## Usage

1. Open Microsoft Sentinel in the Azure portal.
2. Go to **Logs**.
3. Paste any `.kql` query from this repo.
4. Adjust the time range and any environment-specific fields.

To save a query as a scheduled analytics rule:

1. Go to **Analytics** > **Create** > **Scheduled query rule**.
2. Paste the query into the rule logic.
3. Set the schedule and alert threshold appropriate to your environment.

## Validation

```bash
python3 validate_kql.py
