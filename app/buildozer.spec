[app]
android.gradle_dependencies = com.android.tools.build:gradle:7.0.4
android.gradle_distribution_url = https\://services.gradle.org/distributions/gradle-7.4.2-all.zip
log_level = 2
title = SquidBot
package.name = squidbot
package.domain = org.topquark2025
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = kivy,requests
android.permissions = INTERNET,ACCESS_FINE_LOCATION
android.ndk = 25b
android.ndk_path = /root/.buildozer/android/platform/android-ndk-r25b

fullscreen = 1
orientation = portrait