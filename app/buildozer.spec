# buildozer.spec 예시

[app]
title = SquidBot
package.name = squidbot
package.domain = org.topquark2025
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = kivy,requests
android.permissions = INTERNET,ACCESS_FINE_LOCATION

# NDK 관련 항목은 반드시 삭제하거나 주석 처리하세요!
# android.ndk_path = ...
# android.ndk = ...

# 최소 SDK 및 아키텍처 명시 (안정성을 위해 추가)
android.minapi = 21
android.ndk_api = 21
android.arch = arm64-v8a,armeabi-v7a