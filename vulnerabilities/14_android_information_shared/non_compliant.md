
This non-compliant code example shows an application that creates a file
that is world readable, and hence not secure.

    openFileOutput("someFile", MODE_WORLD_READABLE);

Any application could read the file and access any data stored in it.
