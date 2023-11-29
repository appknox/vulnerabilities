
The application is publicly exposing a feature that uses an externally provided intent to
start a new component. This allows an attacker to control the contents of an intent used
to launch the new component, thus giving the attacker the ability to access private
components of the application. Depending on the features privately exposed, this can lead to
further exploitations, sensitive data disclosure, or even persistent code execution.
