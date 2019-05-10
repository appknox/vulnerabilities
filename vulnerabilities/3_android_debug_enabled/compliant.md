
Ensure that the `android:debuggable` attribute is set to false before the
app is released:

    <application
        ...
        android:debuggable="false" >
        ...
    </application>

Note that some development environments (including Eclipse/ADT and Ant)
automatically set `android:debuggable` to true for incremental or
debugging builds but set it to false for release builds.
