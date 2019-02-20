
カスタムエラーページを使用して、エラーが発生したときにユーザをリダイレクトすることを推奨しています。
カスタムエラーページを適用して情報漏れを防ぐには、 web.config に以下のような変更を適用してください。

    <System.Web>
        <customErrors mode="On" defaultRedirect="~/error/GeneralError.aspx">
            <error statusCode="403" redirect="~/error/Forbidden.aspx" />
            <error statusCode="404" redirect="~/error/PageNotFound.aspx" />
            <error statusCode="500" redirect="~/error/InternalError.aspx" />
        </customErrors>
    </System.Web>

