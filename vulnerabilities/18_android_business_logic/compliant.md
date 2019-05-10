
The following should be checked and properly fixed

- Check for OTP in server side rather than in Client Side
- Use proper Authentication not same authorization token like
  Authorization: Basic aW50ZXJhY3Rpb25vbmU6bW9iaTEyMw== which
  translates to: interactionone:mobi123
- never use passwords like mobi123

