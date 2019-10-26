#!/bin/bash
stty -ixon # Disable ctrl-s and ctrl-q.
shopt -s autocd #Allows you to cd into directory merely by typing the directory name.
HISTSIZE= HISTFILESIZE= # Infinite history.
export PS1="\[$(tput bold)\]\[$(tput setaf 1)\][\[$(tput setaf 3)\]\u\[$(tput setaf 2)\]@\[$(tput setaf 4)\]\h \[$(tput setaf 5)\]\W\[$(tput setaf 1)\]]\[$(tput setaf 7)\]\\$ \[$(tput sgr0)\]"

#aliases
alias logout='prompt "Logout?" "kill -9 -1"'
alias mpv="mpv --input-ipc-server=/tmp/mpvsoc$(date +%s)"
alias g="git"
alias x="sxiv -ft *"
alias v="nvim"
alias e="nvim"
alias music="show_art & ncmpcpp -c ~/.config/ncmpcpp/config-art"
alias f="bash ~/.config/vifm/scripts/vifmrun"
alias vifm="bash ~/.config/vifm/scripts/vifmrun"
alias sdn="shutdown -h now"
alias ls="ls -hN --color=auto --group-directories-first"
alias grep="grep --color=auto"
alias diff="diff --color=auto"
alias dv="youtube-dl --add-metadata -i -o '[%(uploader)s] %(title)s.%(ext)s'"
alias da="youtube-dl --add-metadata -i -o '%(title)s.%(ext)s' -x -f bestaudio/best"
alias dl="wget --backups"
alias pi="sudo pacman -S"
alias pr="sudo pacman -Rcs"
alias ps="sudo pacman -Ss"
alias pu="sudo pacman -Syu"
alias ffmpeg="ffmpeg -hide_banner"
alias file-metadata="for file in *; do mkvpropedit "$file" -s title=$filename; done"
alias acestream="acestreamengine --client-console"

#vi mode
set -o vi
