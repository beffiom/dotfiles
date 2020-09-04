#!/bin/bash
stty -ixon # Disable ctrl-s and ctrl-q.
shopt -s autocd #Allows you to cd into directory merely by typing the directory name.
HISTSIZE= HISTFILESIZE= # Infinite history.

powerline-daemon -q
POWERLINE_BASH_CONTINUATION=1
POWERLINE_BASH_SELECT=1
. /usr/share/powerline/bindings/bash/powerline.sh

#aliases
alias logout='prompt "Logout?" "kill -9 -1"'
alias mpv="mpv --input-ipc-server=/tmp/mpvsoc$(date +%s)"
alias g="git"
alias x="sxiv -ft *"
alias v="nvim"
alias e="nvim"
alias c="castero"
alias n="newsboat"
alias m="show_art & ncmpcpp -c ~/.config/ncmpcpp/config-art"
alias f="bash ~/.config/vifm/scripts/vifmrun"
alias vifm="bash ~/.config/vifm/scripts/vifmrun"
alias newsboat="newsboat -c ~/.config/newsboat/cache.db -C ~/.config/newsboat/config -u ~/.config/newsboat/url"
alias sdn="shutdown -h now"
alias ls="ls -hN --color=auto --group-directories-first"
alias la="ls -A"
alias grep="grep --color=auto"
alias diff="diff --color=auto"
alias kiwix-start="kiwix-serve --port=8000 ~/Devices/A\:A_Drive/Multimedia/Books/Wikipedia/*.zim"
alias dv="youtube-dl --add-metadata --embed-subs -i -o '[%(uploader)s] %(title)s.%(ext)s'"
alias da="youtube-dl --add-metadata -i -o '%(title)s.%(ext)s' -x -f bestaudio/best"
alias dl="wget --backups"
alias apu='doas pacman -Sy'
alias api='doas pacman -Syu'
alias apr='doas pacman -Rcns'
alias apq='doas pacman -Ss'
alias apc='doas pacman -Sc'
alias bt-start='pactl load-module module-bluetooth-discover; pactl load-module module-bluetooth-policy; doas sv restart bluetoothd'
alias ffmpeg="ffmpeg -hide_banner"
alias file-metadata="for file in *; do mkvpropedit "$file" -s title=$filename; done"
alias cbz="for i in *.zip; do mv "$i" "${i/.zip/.cbz}"; done"

#vi mode
set -o vi

# bind ctrl-l to clear
bind -x '"\C-l":clear'
