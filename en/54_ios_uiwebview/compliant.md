
When using UIWebView, make sure the data is loaded over HTTPS. Avoid
using it to load content that depends on user input. Validate the
contents of the URL by using `dataWithContentsOfURL` from NSData. Never
use loadRequest to render local file resource as this causes a universal
Cross-Site Scripting vulnerability. Instead, use `loadHTMLString:baseURL:`.
Finally, disable caching when sensitive content is loaded.
