
It is often convenient to serialize objects for convenient communication or to save them for later use. However, deserialized data or code can often be modified without using the provided accessor functions if it does not use cryptography to protect itself. Furthermore, any cryptography would still be client-side security - which is of course a dangerous security assumption.

An attempt to serialize and then deserialize a class containing transient fields will result in NULLs where the non-transient data should be. This is an excellent way to prevent time, environment-based, or sensitive variables from being carried over and used improperly.

In Android <5.0, java.io.ObjectInputStream did not check whether the Object that is being deserialized is actually serializable. This means that ObjectInputStream is used on untrusted inputs allows attackers to execute arbitrary code via a crafted finalize method for a serialized object.