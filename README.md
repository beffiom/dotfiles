# dotfiles

## screenshots

chromium
![chromium](https://raw.github.com/beffiom/linux-dotfiles/master/Pictures/Screenshots/chromium.png)
**source**: [beffiom.tech](https://beffiom.tech)

mpv
![mpv](https://raw.github.com/beffiom/linux-dotfiles/master/Pictures/Screenshots/mpv.png)
mpris script to display media content from chromium/mpv/freetube in polybar

ncmpcpp
![ncmpcpp](https://raw.github.com/beffiom/linux-dotfiles/master/Pictures/Screenshots/ncmpcpp.png)

vifm
![vifm](https://raw.github.com/beffiom/linux-dotfiles/master/Pictures/Screenshots/vifm.png)
**[wallpaper](https://raw.githubusercontent.com/beffiom/dotfiles/master/.config/appearance/wallpapers/%23city/purple_clouds.jpg)**
## system information

* **distribution:** arch linux
* **window manager:** bspwm
* **panel:** polybar
* **keybinding daemon:** sxhkd
* **notification daemon:** dunst
* **program launcher:** dmenu
* **screenlocker:** slock

## universal keybindings
### programs

keybinding | function | description
---------- | -------- | -----------
super+enter | st | terminal emulator
super+shift+enter | vifm | file browser
super+w | ungoogled-chromium | web browser
super+d | dmenu (key programs) | program launcher
super+shift+d | dmenu (all programs) | program launcher
super+m | ncmpcpp | music client
super+t | rtorrent | torrent client
super+s | htop | system processes
super+a | pulsemixer | audio mixer

### system processes
keybinding | description
---------- | -----------
super+shift+r | reloads bspwm
super+shift+x | menu prompt to lockscreen, logout, reboot, or shutdown
super+shift+w | wifi menu
super+shift+b | bluetooth menu
super+shift+m | start/kill mpd
super+F6 | keepmenu
super+F7 | configure multi-monitor displays
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

## FAQ
### How do I set up my music?
1. Add your music to ~/Music and playlists to ~/Music/.playlists
2. Run `mpd` in terminal
3. Launch ncmpcpp by:
   * super+n
   * running `ncmpcpp` in terminal
   * super+d and selecting ncmpcpp

ncmpcpp keybindings | function
------------------- | --------
? | show help/full keybind list
h,j,k,l | left,down,up,right
enter | choose selection/play song
p | pause
< or > | previous or next track
, or . | seek backward or forward
space | add to main playlist
c | clear main playlist
z | randomize playlist
r | repeat playlist
x | set crossfade
1 | view main playlist
2 | view file browser
3 | view search engine
4 | view music library
5 | view playlist editor
6 | view tag editor
7 | visualizer

### How do I create new playlists in ncmpcpp?
1. press `c` to clear main playlist
2. press `2` or `4` to browse for the songs you want to add
3. press `space` to add a song to the main playlist
4. once all songs have been added, press `1` to return to main playlist
5. press `S` to name the new playlist
