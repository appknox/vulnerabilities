
Applications should make sure that they do not send sensitive
information to log output. If the app includes a third party library,
the developer should make sure that the library does not send sensitive
information to log output. One common solution is for an application to
declare and use a custom log class, so that log output is automatically
turned on/off based on Debug/Release. Developers can use ProGuard to
delete specific method calls. This assumes that the method contains no
side effects.

Never use HTTP URL to download data. Instead, create a valid HTTPS
request through which only sensitive data can be downloaded.
