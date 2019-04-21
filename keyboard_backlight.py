#! Python3
#/sys/devices/platform/thinkpad_acpi/leds/tpacpi::kbd_backlight

try:
    file = open("/sys/devices/platform/thinkpad_acpi/leds/tpacpi::kbd_backlight/brightness","w+")
    val = file.read()
    print(val)
    v = int(val[:-1])
    v= (v+1)%3
    file.write(str(v))
    file.close()

except:
    import os
    os.system("gnome-terminal -e \"sudo chmod 777 /sys/devices/platform/thinkpad_acpi/leds/tpacpi::kbd_backlight/brightness\"")
