Disable the TRACE method on your Webserver.

Following are the configurations you can do depending on what kind of server is used:

Apache
======
To disable these methods, add the following lines for each virtual host in your configuration file :

    RewriteEngine on
    RewriteCond %{REQUEST_METHOD} ^(TRACE|TRACK)
    RewriteRule .* – [F]

Alternatively, note that Apache versions 1.3.34, 2.0.55, and 2.2 support disabling the TRACE method natively via the ‘TraceEnable’ directive.

Microsoft IIS
==============
The TRACK method can be added to Microsoft’s URLScan DenyVerbs section. It should not be in the AllowVerbs section in the urlscan.ini file.

Use the URL Scan Tool to deny HTTP TRACE requests or to permit only the methods needed to meet site requirements and policy. The default configurations of Urlscan 2.5 (both baseline and SRP) only permit GET and HEAD methods.

NGINX
======
The majority of web sites only require the GET, HEAD & POST HTTP methods. Enabling the TRACE or DELETE method can pose a risk to your server leaving it vulnerable to a Cross-Site Tracking attack.

Modify the default.conf file and add the following under “server block” to mitigate the risk of a Cross-Site Tracking attack.

    if ($request_method !~ ^(GET|HEAD|POST)$ )
    {
        return 405;
    }

Modifying the code will return a “405 – Not Allowed” if anyone attempts to use the DELETE, TRACE, PUT or OPTIONS method.
