[app]
title = Store AP
package.name = storeap
package.domain = org.reza
source.dir = .
source.include_exts = py,kv,png,jpg,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2

[android]
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 21b
android.build_tools_version = 30.0.3
android.arch = armeabi-v7a
android.permissions = INTERNET
android.sdk_path = $HOME/.buildozer/android/platform/android-sdk
