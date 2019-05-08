
iOS has several mechanisms which prevent the application from being
compromised at runtime. In order to understand the security issues that
affect iOS applications, it is important to understand and to known the
security features of the platform. The main [security features of iOS](http://www.apple.com/ipad/business/docs/iOS_Security_Feb14.pdf) are:

- Code signing: ensures that all applications come from a approved source (using
  Apple-issued certificates)
- Generic exploit mitigations
    - Address Space Layout Randomization (ASLR): Usually compiled using `-fPIE -pie`
    - Non Executable Memory (ARM's Execute Never feature)
    - Stack Smashing Protections (SSP): Usually compiled with `-fstack-protector-all` flag
- Sandboxing
    - run applications as non-privileged user
    - 3rd-party apps are restricted in accessing files stored by other
      apps
- Memory Management
    - Automatic Reference Counting (ARC) protects applications
      from memory coruption issues by letting the compiler do the
      memory management stuff

