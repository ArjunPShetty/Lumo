# Security Policy

## LUMO – An AI-Powered Voice Assistant Using Arduino

Security is important for LUMO because it connects hardware, Wi-Fi, and a Python backend to control real-world devices. This file explains how to report security issues and what is considered a security concern.

## Supported Versions

Only the latest version available in the main branch is supported for security updates. Older versions may not receive fixes.

## Reporting Security Issues

If you discover a security issue, please do not report it publicly using GitHub issues.

Report the issue privately to the project maintainer.

Include the following information if possible:

* Description of the issue
* Affected component (Python backend, NodeMCU firmware, Arduino code, network communication, etc.)
* Steps to reproduce the issue
* Possible impact (unauthorized access, device control, data exposure, crashes, etc.)
* Logs, screenshots, or test details if available

Contact:
Maintainer: Arjun
Method: GitHub private message or other private communication

## What Is Considered a Security Issue

Examples:

* Unauthorized control of appliances or relays
* Wi-Fi or network vulnerabilities
* Exposed credentials or insecure data storage
* Remote command execution or injection
* Voice command spoofing that leads to unsafe actions

Not considered security issues:

* Hardware damage due to incorrect wiring
* Electrical safety mistakes
* Issues caused only by third-party libraries

## Hardware and Electrical Safety

LUMO interacts with real electrical appliances.

* Follow proper electrical safety practices
* Use insulated wiring and certified components
* Test high-voltage devices with caution
* Avoid exposing devices directly to the public internet without security measures

The project maintainer is not responsible for damage or injury caused by improper use.

## Responsible Disclosure

Please allow reasonable time for the issue to be reviewed and fixed before making it public. Responsible disclosure helps keep the project safe for everyone.

## Security Updates

Security fixes will be applied to the main branch. Users are encouraged to keep their local setup updated.

## Acknowledgment
Thank you to everyone who helps improve the security of the LUMO project.