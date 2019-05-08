
ZipperDown attack launches a Man-in-the-Middle (MiTM) attack and replace the benign .zip file with malicious .zip file over the unencrypted network.

The app uses the ZipArchive or SSZipArchive library to decompress it. Since the ZipArchive and SSZipArchive libraries allow unzipping files in parent directories, malicious .zip file can be unzipped to overwrite app data or codes. Apps that dynamically load the codes, such as via JavaScript bridges, make it easier for an attacker to overwrite the codes and launch remote code execution attacks.
