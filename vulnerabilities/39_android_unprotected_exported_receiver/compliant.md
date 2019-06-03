
When using Receivers it is important to set restrictions on which all 
entities it can receive intent broadcasts from.

#### Only current app:

If the only messages the broadcast receiver can receive are those sent 
by components of the same application or applications with the same 
user ID, then remove Intent-Filters or set `android:exported="false"`.

#### Apps with same signature:

If you want to receive intent broadcasts from only your own apps which 
are signed with the same key, then set permission with 
`android:protectionLevel="signature"`.
Signature permissions do not require user confirmation, so 
they provide a better user experience and more controlled access to 
the Broadcast Receiver.

`android:permission` can be set on `<application>` which applies to all 
of the application's components, or can be set on individual components.

Example:

App 1 manifest:

    <manifest package="com.company.app1" ...>
        <permission
            android:name="com.company.permission.CUSTOM"
            android:label="custom_permission"
            android:protectionLevel="signature" />
 
        <application android:permission="com.company.permission.CUSTOM" ...>
            <receiver 
                android:name=".Receiver1">
                <intent-filter>...</intent-filter>
            </receiver>
            <receiver 
                android:name=".Receiver2"
                android:export="true">
            </receiver>
        </application>
    </manifest>

App 2 manifest:

    <manifest package="com.company.app2" ...>
        <uses-permission 
            android:name="com.company.permission.CUSTOM" />
        ...
    </manifest>

**App1** can now receive broadcasts from **App2**.


#### Any app having required receiver permission:

Receiver permission with `protectionLevel` set to `dangerous` or `normal` 
based on nature of data or resource exposed by the receiver.
`normal` is used for permissions that don't pose much risk to the 
user's privacy or the device's operation, the system automatically 
grants those permissions to your app.
`dangerous` is used for permissions that could potentially affect 
the user's privacy or the device's normal operation, the user must 
explicitly agree to grant those permissions.

Example: 

App 1 manifest:

    <manifest package="com.company1.app1" ...>
        <permission
            android:name="com.company1.permission.CUSTOM1"
            android:label="custom_permission"
            android:protectionLevel="dangerous" />
        <permission
            android:name="com.company1.permission.CUSTOM2"
            android:label="custom_permission"
            android:protectionLevel="dangerous" />
 
        <application ...>
            <receiver
                android:name=".Receiver1"
                android:permission="com.company1.permission.CUSTOM1">
                <intent-filter>...</intent-filter>
            </receiver>
            <receiver 
                android:name=".Receiver2" 
                android:permission="com.company1.permission.CUSTOM1"
                android:export="true">
            </receiver>
            <receiver 
                android:name=".Receiver3" 
                android:permission="com.company1.permission.CUSTOM2"
                android:export="true">
            </receiver>
            ...
        </application>
    </manifest>

App 2 manifest:

    <manifest package="com.company2.app2" ...>
        <uses-permission 
            android:name="com.company1.permission.CUSTOM1" />
        ...
    </manifest>

**App2** can now send broadcasts to both `Receiver1` and `Receiver2`, 
but not to `Receiver3`.
