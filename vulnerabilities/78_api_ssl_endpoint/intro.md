
When a response is served over HTTPS, the connection with the web server
is encrypted with TLS and is therefore safeguarded from sniffers and man-in-the-middle
attacks. If the HTTPS response includes links to content that is
retrieved through regular, cleartext HTTP, then the connection is only partially
encrypted; the unencrypted content is accessible to sniffers and can be modified
by man-in-the-middle attackers, so the connection is not safeguarded.
