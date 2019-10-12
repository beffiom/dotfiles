# darkstar | linux-dotfiles

## system information

**distribution:** arch linux
**window manager:** bspwm
**panel:** polybar
**keybinding daemon:** sxhkd
**notification daemon:** dunst

## universal keybindings
### programs

keybinding | function | description
---------- | -------- | -----------
super+enter | st | terminal emulator
super+shift+enter | vifm | file browser
super+w | qutebrowser | web browser
super+d | dmenu (key programs) | program launcher
super+shift+d | dmenu (all programs) | program launcher
super+n | ncmpcpp | music client
super+t | youtube | opens invidio.us in qutebrowser
super+shift+t | transmission-cli | torrent client
super+s | htop | system processes
super+a | pulsemixer | audio mixer

### system processes
keybinding | description
---------- | -----------
super+? | help (opens this document)
super+F1 | reloads bspwm
super+F2 | lockscreen (i3lock-color)
super+F3 | prompt logout
super+F4 | prompt reboot
super+F5 | prompt shutdown
super+F6 | passmenu
super+F7 | configure multi-monitor displays
super+F8 | configure protonvpn
super+{F9,F10} | {mount,unmount} devices
XF86{LowerVolume,RaiseVoleume} | volume {down,up}
XF86AudioMute | mute audio
XF86Audio{Prev,Next} | {previous,next} music track
XF86AudioPlay | toggle (play/pause) music
XF86MonBrightness{Down,Up} | {lower,raise} display backlight
super+c | display clipboard contents
super+shift+e | select and edit config files

### window management
keybinding | description
---------- | -----------
super+q | close program
super+shift+q | kill program
super+f | toggle fullscreen
super+shift+f | toggle monocle layout
super+b | hide/show polybar
super+{[,]} | focus desktop {left,right}
super+{1-9} | focus desktop {1-9}
super+shift{1-9} | send program to desktop {1-9}
super+{h,j,k,l} | focus program {left,down,up,right}
super+shift{h,j,k,l} | swap program placement {left,down,up,right}
super+g | swap the current program with the largest one
super+alt+{h,j,k,l} | preselect direction to spawn program
super+alt+space | cancel preselection
super+shift+space | cycle window state (pseudo_tiled,tiled,floating)
super+{y,u,i,o} | expand a window {left,down,up,right}
super+shift+{y,u,i,o} | contract a window {left,down,up,right}
super+shift+{left,down,up,right} | move a floating window {left,down,up,right}
super+left click | move a floating window
super+right click | resize a floating window




