
Services run in the background and do not interact with the user.
Downloading a file or decompressing an archive are examples of
operations that may take place in a Service. Other components can bind
to a Service, which lets the binder invoke methods that are declared in
the target Service's interface. Intents are used to start and bind to
Services

Exported Unprotected Services can be called by any other application
installed in the phone to bind into the service leading to XAS (Cross
Application Scripting)
