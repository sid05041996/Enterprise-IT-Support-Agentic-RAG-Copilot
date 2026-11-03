2. SERVICE DESK RUNBOOK
Purpose

The Service Desk Runbook serves as an operational guide for Service Desk analysts and support engineers to resolve incidents consistently and efficiently.

Chapter 1: Incident Management Process
Ticket Lifecycle
Plain Text
New
↓
Assigned
↓
In Progress
↓
Pending User
↓
Resolved
↓
Closed
Required Ticket Fields
User Name
Contact Information
Device Name
Issue Description
Priority
Assignment Group
Resolution Notes
Chapter 2: Ticket Priority Matrix
Priority	Impact	Urgency	ExampleP1	High	High	Email outage
P2	High	Medium	VPN failure affecting multiple users
P3	Medium	Medium	Application issue
P4	Low	Low	Software request
Chapter 3: Email Troubleshooting Runbook
Common Issues
User Cannot Send Email
Diagnostic Steps
Verify internet connectivity.
Verify mailbox is active.
Check mailbox quota.
Verify SMTP settings.
Check service status dashboard.
Resolution
Clear mailbox space.
Restart email application.
Reconfigure profile.
Escalate if server-related.
User Cannot Receive Emails
Validation
Check spam folder.
Review inbox rules.
Verify mailbox quotas.
Send test email.
Resolution
Remove problematic rules.
Increase mailbox quota.
Repair mailbox profile.
Outlook Keeps Prompting for Password
Troubleshooting
Verify account lockouts.
Validate MFA status.
Check credential manager.
Rebuild Outlook profile.
Resolution
Re-create credentials.
Reconfigure Outlook.
Reset password if required.
Chapter 4: Laptop Performance Troubleshooting
Symptom: Slow Laptop
Initial Assessment

Collect:

Device model
OS version
Available disk space
Memory utilization
CPU utilization
Troubleshooting Steps
Restart device.
Review startup programs.
Verify disk space.
Run antivirus scan.
Perform OS updates.
Escalation Criteria

Escalate if:

Hardware failures detected.
Disk health critical.
Blue screen occurrences exceed threshold.
Chapter 5: VPN Troubleshooting
User Cannot Connect to VPN
Verification
Internet connectivity available
VPN client installed
MFA functioning
User account active
Resolution Steps
Restart VPN client.
Re-authenticate.
Reinstall VPN software.
Test alternate network.
Reset VPN profile.
Chapter 6: Password Reset Process
Verification Requirements

Confirm:

Employee ID
Manager verification (if required)
Secondary authentication method
Reset Procedure
Verify identity.
Reset account password.
Force password change at next login.
Verify successful logon.
Chapter 7: Printer Support Runbook
Printer Offline
Diagnostics
Verify power.
Verify network connectivity.
Check queue status.
Ping printer IP.
Resolution
Restart printer.
Clear print queue.
Reinstall printer driver.
Reconfigure printer port.
Chapter 8: Software Installation Requests
Validation

Before installation:

Verify software approval.
Check licensing availability.
Confirm compatibility.
Execution
Obtain approvals.
Download approved package.
Install software.
Verify functionality.
Update ticket.
Chapter 9: Security Incident Handling
Suspected Malware Infection
Immediate Actions
Disconnect system from network.
Inform Security Team.
Collect incident information.
Document findings.
Escalation

Mandatory escalation if:

Ransomware detected
Data exfiltration suspected
Privileged account affected
Chapter 10: Ticket Closure Standards
Resolution Documentation

Every resolved ticket must include:

Root Cause
Troubleshooting Performed
Resolution Steps
User Confirmation
Closure Notes
Sample Closure Note
Plain Text
Issue:
Outlook unable to send emails.
 
Root Cause:
Mailbox quota exceeded.
 
Resolution:
Archived emails and increased mailbox quota.
 
User Validation:
Confirmed working.
 
Status:
Resolved and closed.
Appendix A: Service Desk SLAs
Priority	Response SLA	Resolution SLAP1	15 Minutes	4 Hours
P2	30 Minutes	8 Hours
P3	4 Hours	3 Business Days
P4	1 Business Day	5 Business Days
Appendix B: Escalation Matrix
Level 1 Service Desk

Handles:

Password resets
Email issues
Basic application support
Device troubleshooting
Level 2 Support

Handles:

Advanced application issues
Network troubleshooting
System administration tasks
Level 3 Support

Handles:

Infrastructure issues
Security incidents
Vendor escalations
Complex problem management