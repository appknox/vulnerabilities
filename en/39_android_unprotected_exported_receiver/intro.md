
Broadcast Receivers receive Intents sent to multiple applications.
Receivers are triggered by the receipt of an appropriate Intent and then
run in the background to handle the event. Receivers are typically
short-lived; they often relay messages to Activities or Services. There
are three types of broadcast Intents: normal, sticky, and ordered.
Normal broadcasts are sent to all registered Receivers at once, and then
they disappear. Ordered broadcasts are delivered to one Receiver at a
time; also, any Receiver in the delivery chain of an ordered broadcast
can stop its propagation. Broadcast Receivers have the ability to set
their priority level for receiving ordered broadcasts. Sticky broadcasts
remain accessible after they have been delivered and are re-broadcast to
future Receivers.

Exported Broadcast Receiver can be called by any other malicious
application installed in the phone to invoke the Broadcast Receiver
leading to XAS (Cross Application Scripting)
