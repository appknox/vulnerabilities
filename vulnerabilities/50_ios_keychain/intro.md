
iOS provides the Keychain for secure data storage. However, in several
scenarios, the Keychain can be compromised and subsequently decrypted.

In all versions of iOS up to and including iOS 11, Keychain can be
partially compromised if attacker has access to the encrypted iTunes
backup. Due to the way iOS re-encrypts Keychain entries when creating
iTunes backups, it is possible to partially decrypt Keychain when iTunes
backup is available and password for backup encryption is known (note
that iTunes backups that are not encrypted do not allow decryption of
Keychain items).

Keychain access controls are rendered ineffective if a jailbreak has
been applied to the device. In this case any application running on the
device can potentially read every other application's Keychain items.

Lastly, for older devices, such as the iPhone 4, for which so-called
"bootrom exploits" exist, the Keychain can be compromised by an attacker
with physical access to the device.
