
UIWebView can be susceptible to client side Javascript injection if
inputs are not properly validated. Since the code is injected on the
client side, it is possible to call native functions in the device and
perform malicious actions. Currently there are no public APIs to disable
Javascript in UIWebView.

Furthermore, UIWebView may cache loaded data into the internal database.
This means that sensitive content remains in the memory even after it
has been closed.
