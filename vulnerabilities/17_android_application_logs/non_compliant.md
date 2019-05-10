
Facebook SDK for Android contained the following code which sends Facebook access tokens to log output in plain text format.

    Log.d("Facebook-authorize", "Login Success! access_token=" + getAccessToken() + " expires=" + getAccessExpires());

Here is another example. A weather report for Android sent a user's location data to the log output as follows:

    I/MyWeatherReport( 6483): Re-use MyWeatherReport data
    I/ ( 6483): GET JSON:
    http://example.com/smart/repo_piece.cgi?arc=0&lat=26.209026&lon=127.650803&rad=50&dir=-999&lim=52&category=1000

If a user is using Android OS 4.0 or before, other applications with READ\_LOGS
permission can obtain the user's location information without declaring
ACCESS\_FINE\_LOCATION permission in the manifest file.
