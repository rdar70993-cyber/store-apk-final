[app]
# نام اپلیکیشن
title = Store AP
# نام پکیج
package.name = storeap
# دامنه پکیج
package.domain = org.reza
# مسیر سورس
source.dir = .
# فایل‌هایی که باید شامل شوند
source.include_exts = py,kv,png,jpg,atlas
# نسخه اپلیکیشن
version = 1.0
# نیازمندی‌ها
requirements = python3,kivy
# حالت نمایش
orientation = portrait
fullscreen = 1

[buildozer]
# سطح لاگ برای دیباگ
log_level = 2

[android]
# نسخه API هدف
android.api = 33
# حداقل نسخه API
android.minapi = 21
# نسخه SDK
android.sdk = 33
# نسخه NDK
android.ndk = 21b
# نسخه Build-tools
android.build_tools_version = 30.0.3
# معماری
android.arch = armeabi-v7a
# دسترسی‌ها
android.permissions = INTERNET
# مسیر SDK (خیلی مهم برای رفع ارورهای sdkmanager)
android.sdk_path = $HOME/.buildozer/android/platform/android-sdk
