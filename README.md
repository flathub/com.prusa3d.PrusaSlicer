# PrusaSlicer
This repository contains the FlatPak release of PrusaSlicer distributed on FlatHub. [Wiki](https://github.com/prusa3d/PrusaSlicer/wiki/PrusaSlicer-on-Linux---binary-distributions)

While these releases do build independantly on FlatHub's build farm, the builds are based on the excat same depencenies and versions that Prusa Research bundels and provides incling Prusa3D own patched wxWidgets.
So they are identical.

However, since these builds are running in its own container, this also gives oppertiunity for a tighter integrating in the Linux desktop for a multiplattform application. 
So there are sometimes minior differnces and fixes compared to the official AppImage or other Linux distribution builds.  
To make the experience and integration on Linux better, these builds include mime support for .gcode and .3mf files, desktop actions and support for dark theme variant.
The goal is always to get these changes back upstream without breaking PrusaSlicer's AppImage and ChromeOS builds and still keeping all platforms unified. 

The FlatHub build also includes a simlpe workaround (entrypoint script) to allow PrusaSlicer to starup when in the situation when the system locale is messed up and it recieved an exception.
In that case it will try to use youre default language or fallback to en-us.UTF8.


## Enable Dark Theme variant (since 2.4.0)

```sh 
# to enable dark mode, there is a envirioment variable that will 
# set the Adwaita:dark theme and X11 window to dark variant. 
# 
# run the following command to override and set the dark theme

flatpak override --env=PRUSA_SLICER_DARK_THEME=true com.prusa3d.PrusaSlicer

```


