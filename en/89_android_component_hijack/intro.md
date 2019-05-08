
Android app can have four types of components:
- Activity
- Broadcast Receiver
- Content Provider
- Service App

They have their own entry points and can be activated individually.
These components can be exposed to other apps for flexible code and data
sharing. Android (mainly) uses Manifest XML file to define component exposure.
Intents come into play here because they are the main mechanism for
communication between components. Intents are used to start activities and
services, bind to services, and convey notifications to broadcast receivers.
By default, a component can only receive intents from other components
in the same application, but it can be configured to accept intents from
outside applications by setting the `android:exported` attribute in the
manifest.

An intent can be classified as one of two types based on how it is addressed.

- Implicit Intent
- Explicit Intent

There are two main ways that the security of intents can be compromised:

- **Intent interception** involves a malicious app receiving an
  intent that was not intended for it. This can cause a leak of sensitive
  information, but more importantly, it can result in the malicious component
  being activated instead of the legitimate component. For example, if a
  malicious activity intercepted an intent then it would appear on the screen
  instead of the legitimate activity.
- **Intent spoofing** is an attack where a malicious application
  induces undesired behavior by forging an intent.

