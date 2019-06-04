
Insecure code samples:

Example 1:

    Bundle bundle = new Bundle();
    bundle.putSerializable("exampleClass", exampleOfSerializabledClass);
    exampleOfSerializabledClass = bundle.getSerializable("exampleClass");

Example 2:

    sock = new Socket(hostname, port);
    ObjectInputStream datain = new ObjectInputStream(sock.getInputStream());
    ObjectInputStream in = new ObjectInputStream(someInputStream());
    deserializedObj = in.readObject();
