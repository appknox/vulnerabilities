
iOS has several mechanisms which prevent the application from being
compromised at runtime. In order to understand the security issues that
affect iOS applications, it is important to understand and to known the
security features of the platform.

- Code signing: ensures that all applications come from a approved source (using
  Apple-issued certificates)
- Address Space Layout Randomization (ASLR): Usually compiled using `-fPIE -pie`
