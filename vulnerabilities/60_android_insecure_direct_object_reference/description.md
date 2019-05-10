
To test for this vulnerability, all locations in the application need to be mapped where user input is used to reference objects directly.
For example, locations where user input is used to access a database row, a file or even an application page.
Next, the value of the parameter used to reference objects is modified and assessed whether it is possible to
retrieve objects belonging to other users or otherwise bypass authorisation.
