
The Network Security Configuration feature lets apps customize their network security
settings in a safe, declarative configuration file without modifying app code. These
settings can be configured for specific domains and for a specific app. The key
capabilities of this feature are as follows:
- **Custom trust anchors**: Customize which Certificate Authorities (CA) are trusted for an app's secure connections. For example, trusting particular self-signed certificates or restricting the set of public CAs that the app trusts.
- **Debug-only overrides**: Safely debug secure connections in an app without added risk to the installed base.
- **Cleartext traffic opt-out**: Protect apps from accidental usage of cleartext traffic.
- **Certificate pinning**: Restrict an app's secure connection to particular certificates.
