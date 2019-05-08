
Java の場合,

    <session-config>
    <cookie-config>
    <secure>false</secure>
    </cookie-config>
    </session-config>

ASP.Net の場合,

    <httpCookies requireSSL="false" />
PHP の場合,

    session.cookie_secure = false

