
Activities provide user interfaces. Activities are started with Intents,
and they can return data to their invoking components upon completion.
All visible portions of applications are Activities.

An exported Activity contains `<intent-filter>` or `android:exported="true"` 
attribute set. If access to an exported Activity is not restricted, 
any other application installed in the phone will be able to launch 
the activity, leading to XAS (Cross Application Scripting).