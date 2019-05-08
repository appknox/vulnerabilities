
A BroadcastReceiver represents one main component of an essential
publish/subscribe messaging platform in Android. It, known as a subscriber,
can be used to receive and respond to specific messages (or broadcasts) from
the system or other components in the same application or different
applications, such as notifying Android users when cellphone power is low as
a system event-driven. This is generally achieved through the utilization of
intent filters defined in the app manifest file.

The dynamically Broadcastreceiver is in the java source code to realize the
broadcast mechanism using onReceive(). This mechanism is managed by the Activity
Manager Service (AMS) on the second framework layer in the Android architecture.
