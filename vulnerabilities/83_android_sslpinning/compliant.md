
Certificate pinning is done by providing a set of certificates by hash of 
the public key (`SubjectPublicKeyInfo` of the X.509 certificate). 
A certificate chain is then valid only if the certificate chain contains 
at least one of the pinned public keys.

#### Pinning Using Network security configuration (preferred):

Since Android N, the preferred way for implementing pinning is by 
leveraging Android's Network Security Configuration feature, which lets 
apps customize their network security settings in a safe, declarative 
configuration file without modifying app code.

*res/xml/network_security_config.xml:*

    <?xml version="1.0" encoding="utf-8"?>
    <network-security-config>
        <domain-config>
            <domain includeSubdomains="true">example.com</domain>
            <pin-set expiration="2025-01-01">
                <pin digest="SHA-256">7HIpactkIAq2Y49orFOOQKurWxmmSFZhBCoQYcRhJ3Y=</pin>
                <pin digest="SHA-256">fwza0LRMXouZHRC8Ei+4PyuldPDcf3UKgO/04cDM1oE=</pin>
            </pin-set>
        </domain-config>
    </network-security-config>

TrustKit acts as a polyfill for old Android versions that not support Network Security Configuration. 

#### Pinning with OkHttp:

OkHttp provides a mechanism that makes implementing certificate pinning easy, 
as it only requires creating an instance of CertificatePinner.

    import com.squareup.okhttp.CertificatePinner;

&nbsp;

    CertificatePinner certPinner = new CertificatePinner.Builder()
        .add("example.com", "sha256/7HIpactkIAq2Y49orFOOQKurWxmmSFZhBCoQYcRhJ3Y=")
        .add("example.com", "sha256/fwza0LRMXouZHRC8Ei+4PyuldPDcf3UKgO/04cDM1oE=")
        .build();

    OkHttpClient okHttpClient = new OkHttpClient();
    okHttpClient.setCertificatePinner(certPinner);

&nbsp;

    Request request = new Request.Builder()
        .url("https://" + hostname)
        .build();
    okHttpClient.newCall(request).execute();


#### Pinning with Retrofit:

With Retrofit being built on top of OkHttp, configuring it for pinning is as simple as setting up an OkHttpClient as shown above and supplying that to Retrofit.Builder.

    Retrofit retrofit = new Retrofit.Builder()
        .baseUrl("https://example.com")
        .client(okHttpClient)
        .build();
