
Domain whitelisting is a security model that controls access to external domains
over which the app has no control. The default security policy allows access to
any site. Before moving your application to production, you should formulate
a whitelist and allow access to specific network domains and subdomains.

Application Transport Security (ATS) is a new feature in iOS 9 that acts as
a whitelist for the app. All the `<access>` and `<allow-navigation>` tags
automatically get converted to the appropriate ATS directives.
