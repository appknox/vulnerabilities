
Cordova adheres to the W3C Widget Access specification, which relies on
the `<access>` element within the app's `config.xml` file to enable
network access to specific domains. For projects that rely on the CLI
workflow described in The Command-Line Interface, this file is located
in the project's top-level directory. Otherwise for platform-specific
development paths, locations are listed in the sections below:

The following examples demonstrate whitelist syntax:

Access to google.com:

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
