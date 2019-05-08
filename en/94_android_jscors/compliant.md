
Below is an example of how to prevent the application from Javascript CORS issue:

    WebSettings settings = getSettings();
    settings.setAllowUniversalAccessFromFileURLs(false)
    settings.setAllowFileAccessFromFileURLs(false)

