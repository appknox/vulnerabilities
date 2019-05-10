
Domain whitelisting is a security model that controls access to external
domains over which you application has no control. Cordova's default
security policy allows access to any site. Before moving your
application to production, you should formulate a whitelist and allow
access to specific network domains and subdomains.

Cordova adheres to the W3C Widget Access specification, which relies on
the `<access>` element within the app's `config.xml` file to enable
network access to specific domains. For projects that rely on the CLI
workflow described in The Command-Line Interface, this file is located
in the project's top-level directory. Otherwise for platform-specific
development paths, locations are listed in the sections below:

The following examples demonstrate whitelist syntax:

Access to google.com

    <access origin="http://google.com" />

Access to the secure google.com:

    <access origin="https://google.com" />

Access to the subdomain maps.google.com:

    <access origin="http://maps.google.com" />

Access to all the subdomains on google.com, for example, mail.google.com and docs.google.com:

    <access origin="http://*.google.com" />

Access to all domains, for example, google.com and developer.mozilla.org:

    <access origin="*" />

This is the default value for newly created CLI projects which not secured.

Also upgrade your PhoneGap or Apache Cordova application to the latest version
