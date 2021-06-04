
It is recommended to use custom error pages and redirect the user to the same whenever an error is occurred.
Apply following changes on your web.config file to prevent information leakage by applying custom error pages.

    <System.Web>
        <customErrors mode="On" defaultRedirect="~/error/GeneralError.aspx">
            <error statusCode="403" redirect="~/error/Forbidden.aspx" />
            <error statusCode="404" redirect="~/error/PageNotFound.aspx" />
            <error statusCode="500" redirect="~/error/InternalError.aspx" />
        </customErrors>
    </System.Web>

