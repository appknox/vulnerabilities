
Activity export should be done based on the required restriction level.

#### Only current app:

If the activity is called within the same app, then don't export or 
use Intent-Filter.


#### Apps with same signature:

If you are using an Activity for sharing between only your own apps, it
is preferable to use permission with `android:protectionLevel` attribute 
set to `signature` protection. Signature permissions do not require 
user confirmation, so they provide a better user experience and more 
controlled access to the application. 

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
            <activity 
                android:name=".Activity1">
                <intent-filter>...</intent-filter>
            </activity>
            <activity 
                android:name=".Activity2"
                android:export="true">
            </activity>
        </application>
    </manifest>

App 2 manifest:

    <manifest package="com.company.app2" ...>
        <uses-permission 
            android:name="com.company.permission.CUSTOM" />
        ...
    </manifest>

**App2** can now access both `Activity1` and `Activity2 .


#### Any app having required activity permission:

Set Activity permission with `protectionLevel` set to `dangerous` or 
`normal` based on nature of data or resource exposed by the activity. 
`normal` is used for permissions that don't pose much risk to the 
user's privacy or the device's operation, the system automatically 
grants those permissions to your app.
`dangerous` is used for permissions that could potentially affect 
the user's privacy or the device's normal operation, the user must 
explicitly agree to grant those permissions.

Example: 

App 1 manifest:

    <manifest package="com.company1.app" ...>
        <permission
            android:name="com.company1.permission.CUSTOM1"
            android:label="custom_permission"
            android:protectionLevel="dangerous" />
        <permission
            android:name="com.company1.permission.CUSTOM2"
            android:label="custom_permission"
            android:protectionLevel="dangerous" />
 
        <application ...>
            <activity
                android:name=".Activity1"
                android:permission="com.company1.permission.CUSTOM1">
                <intent-filter>...</intent-filter>
            </activity>
            <activity 
                android:name=".Activity2" 
                android:permission="com.company1.permission.CUSTOM1"
                android:export="true">
            </activity>
            <activity 
                android:name=".Activity3" 
                android:permission="com.company1.permission.CUSTOM2"
                android:export="true">
            </activity>
            ...
        </application>
    </manifest>

App 2 manifest:

    <manifest package="com.company2.app" ...>
        <uses-permission 
            android:name="com.company1.permission.CUSTOM1" />
        ...
    </manifest>

**App2** can now access both `Activity1` and `Activity2`, but not `Activity3`.