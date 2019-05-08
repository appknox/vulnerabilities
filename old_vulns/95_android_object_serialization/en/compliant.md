
Use only serialization when you have the control over data. Use the following pointers to figure out if serialization is necessary

- Does the deserialization take place before authentication?
- Does the deserialization limit which types can be deserialized?
- Does the deserialization host have types available which can be repurposed towards malicious ends?

