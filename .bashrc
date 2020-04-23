#!/bin/bash
stty -ixon # Disable ctrl-s and ctrl-q.
shopt -s autocd #Allows you to cd into directory merely by typing the directory name.
HISTSIZE= HISTFILESIZE= # Infinite history.

export PS1="$ "

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
alias kiwix-start="kiwix-serve --port=8080 ~/Devices/A\:A_Drive/Multimedia/Books/Wikipedia/*.zim"
alias dv="youtube-dl --add-metadata --all-subs -i -o '[%(uploader)s] %(title)s.%(ext)s'"
alias da="youtube-dl --add-metadata -i -o '%(title)s.%(ext)s' -x -f bestaudio/best"
alias dl="wget --backups"
alias vpu='doas xbps-install -Su'
alias vpi='doas xbps-install -S'
alias vpr='doas xbps-remove -R'
alias vpq='xbps-query -Rs'
alias vpc='doas xbps-remove -Oo'
alias ffmpeg="ffmpeg -hide_banner"
alias file-metadata="for file in *; do mkvpropedit "$file" -s title=$filename; done"
alias acestream="acestreamengine --client-console"
alias cbz="for i in *.zip; do mv "$i" "${i/.zip/.cbz}"; done"

#vi mode
set -o vi

# bind ctrl-l to clear
bind -x '"\C-l":clear'
