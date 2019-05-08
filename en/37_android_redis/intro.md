
Redis framework should be used strictly in server to server
communication. Using Redis in the client side compromises security
because the credentials can be read in plain text.
