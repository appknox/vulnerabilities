
Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious
scripts are injected into otherwise benign and trusted web sites. XSS attacks
occur when an attacker uses a web application to send malicious code, generally
in the form of a browser side script, to a different end user. Flaws that allow
these attacks to succeed are quite widespread and occur anywhere a web application
uses input from a user within the output it generates without validating or encoding it.

An attacker can use XSS to send a malicious script to an unsuspecting user. The
end user's browser has no way to know that the script should not be trusted,
and will execute the script. Because it thinks the script came from a trusted
source, the malicious script can access any cookies, session tokens, or other
sensitive information retained by the browser and used with that site.
These scripts can even rewrite the content of the HTML page.

The impace of XSS attacks may range from a petty nuisance to a significant
security risk, depending on the sensitivity of the data handled by the
vulnerable site and the nature of any security mitigation implemented by the
site's owner.
