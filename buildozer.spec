[app]
title = My Python App
package.name = mypyapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
version = 0.1

# List every library your code imports, separated by commas
requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
