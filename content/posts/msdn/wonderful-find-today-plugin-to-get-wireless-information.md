---
title: "Wonderful Find : Today Plugin to get Wireless information"
platform: "msdn"
era: "microsoft"
source_url: "https://learn.microsoft.com/en-us/archive/blogs/frankarr/wonderful-find-today-plugin-to-get-wireless-information"
date: "2006-05-04"
---

Wonderful Find : Today Plugin to get Wireless information I've been looking at registry tweaks for the K-Jam and found a wonderful one recently. Just add the keys below to the registry. (I use the Mobile Registry Editor , which allows me to do this via my PC) [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Today\Items\"Wireless"] "DLL"="netui.dll" "Order"=dword:00000000 "Enabled"=dword:00000001 "Type"=dword:00000004 Select the new Wireless setting on the Today Plugin page and you will see the network carrier name and status, the active WiFi Access point, and the Bluetooth status on the Today screen. It works with all AKU2 Roms , so it's not limited to the K-Jam. Here's where I found this and other tweaks: https://wiki.xda-developers.com/index.php?pagename=WM5_Tweaks_Other This is what it looks like on my phone - it's the 3rd entry on the page. [ Currently Playing : Let Me Try - Luminita Anghel & Sistem - Eurovision Song Contest 2005 K (03:02) ]
