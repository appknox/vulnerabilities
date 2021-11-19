
圧縮、難読化、最適化を有効にするには、プロジェクトレベルの `build.gradle` ファイルに以下を含めたうえで proguard を使用してください。


    android {
        buildTypes {
            release {
                // Enables code shrinking, obfuscation, and optimization for only
                // your project's release build type.
                minifyEnabled true

                // Enables resource shrinking, which is performed by the
                // Android Gradle plugin.
                shrinkResources true

                // Includes the default ProGuard rules files that are packaged with
                // the Android Gradle plugin. To learn more, go to the section about
                // R8 configuration files.
                proguardFiles getDefaultProguardFile(
                        'proguard-android-optimize.txt'),
                        'proguard-rules.pro'
            }
        }
        ...
    }


コードを難読化する `proguard-rules.pro` の例として以下が挙げられます。


    // Basic proguard rules
    -optimizations !code/simplification/arithmetic
    -keepattributes <em>Annotation</em>
    -keepattributes InnerClasses
    -keepattributes EnclosingMethod
    -keep class *<em>.R$</em>

    -dontskipnonpubliclibraryclasses
    -forceprocessing
    -optimizationpasses 5
    -overloadaggressively

    // Removing logging code
    -assumenosideeffects class android.util.Log {
        public static *** d();
        public static *** v();
        public static *** i();
        public static *** w();
        public static *** e();
    }

    // Crashlytics code as given below which one can exclude

    -keep class com.crashlytics.** { *; }
    -keep class com.crashlytics.android.**
    -keepattributes SourceFile,LineNumberTable

