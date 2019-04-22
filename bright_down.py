#!Python3

try:
    file = open("/sys/class/backlight/intel_backlight/brightness","w+")
    val = file.read()
    v = int(val[:-1])
    v= v-20
    if v >0:
        file.write(str(v))
    else:
        file.write("0")
    file.close()

except:
    import os
    os.system("gnome-terminal -e \"sudo chmod 777 /sys/class/backlight/intel_backlight/brightness\"")
