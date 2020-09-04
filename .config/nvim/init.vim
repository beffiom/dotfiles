let mapleader =","

if empty(glob('~/.local/share/nvim/site/autoload/plug.vim'))
  silent !curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

call plug#begin('~/.config/nvim/plugged/')
Plug 'tpope/vim-surround'
Plug 'powerline/powerline'
Plug 'scrooloose/nerdtree'
Plug 'junegunn/goyo.vim'
Plug 'jreybert/vimagit'
Plug 'LukeSmithxyz/vimling'
Plug 'vimwiki/vimwiki'
Plug 'tpope/vim-commentary'
Plug 'kovetskiy/sxhkd-vim'
Plug 'plasticboy/vim-markdown'
Plug 'elzr/vim-json'
Plug 'othree/html5.vim'
Plug 'hail2u/vim-css3-syntax'
call plug#end()

colorscheme peachpuff
set tabstop=4 shiftwidth=4 expandtab
set bg=light
set go=a
set mouse=a
set nohlsearch
set clipboard+=unnamedplus

" select all
map <C-a> <esc>ggVG<CR>

" tab remappings
map J :tabn<Enter>
map K :tabp<Enter>

" autoupdate programs
    	autocmd BufWritePost config.h !doas make install
    	autocmd BufWritePost *.html !qutebrowser :reload
    	autocmd BufWritePost ~/.config/appearance/Xresources !xrdb %
    	autocmd BufWritePost bspwmrc !bspc wm -r
    	autocmd BufWritePost sxhkdrc !bspc wm -r
    	autocmd BufWritePost picom.conf !bspc wm -r
    	autocmd BufWritePost .bashrc,.bash_profile,.profile !source ~/.bash_profile
    	autocmd BufWritePost .Xresources !xrdb ~/.Xresources
    	autocmd BufWritePost *ncmpcpp/config,*ncmpcpp/bindings !killall ncmpcpp ; st -e ncmpcpp &
    	autocmd BufWritePost *polybar/config !bspc wm -r
    	autocmd BufWritePost config.py !qutebrowser :config-source
    	autocmd BufWritePost darkstar.css !qutebrowser :'set content.user_stylesheets themes/darkstar.css'
    	autocmd BufWritePost darkstar-alt.css !qutebrowser :'set content.user_stylesheets themes/darkstar-alt.css'
    	autocmd BufWritePost default.css !qutebrowser :'set content.user_stylesheets themes/default.css'
    	autocmd BufWritePost darculized.css !qutebrowser :'set content.user_stylesheets themes/darculized.css'
    	autocmd BufWritePost ~/.config/transmission-daemon/settings.json !killall -HUP transmission-da

" Some basics:
	nnoremap c "_c
	set nocompatible
	filetype plugin on
	syntax on
	set encoding=utf-8
	set number relativenumber
" Enable autocompletion:
	set wildmode=longest,list,full
" Disables automatic commenting on newline:
	autocmd FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o

" Goyo plugin makes text more readable when writing prose:
	map <leader>f :Goyo \| set bg=light \| set linebreak<CR>

" Spell-check set to <leader>o, 'o' for 'orthography':
	map <leader>o :setlocal spell! spelllang=en_us<CR>
" Splits open at the bottom and right, which is non-retarded, unlike vim defaults.  set splitbelow splitright
" Nerd tree
	map <leader>n :NERDTreeToggle<CR>
	autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" vimling:
	nm <leader>d :call ToggleDeadKeys()<CR>
	imap <leader>d <esc>:call ToggleDeadKeys()<CR>a
	nm <leader>i :call ToggleIPA()<CR>
	imap <leader>i <esc>:call ToggleIPA()<CR>a
	nm <leader>q :call ToggleProse()<CR>

" Shortcutting split navigation, saving a keypress:
	map <C-h> <C-w>h
	map <C-j> <C-w>j
	map <C-k> <C-w>k
	map <C-l> <C-w>l

" Check file in shellcheck:
	map <leader>s :!clear && shellcheck %<CR>

" Replace all is aliased to S.
	nnoremap S :%s//g<Left><Left>

" Compile document, be it groff/LaTeX/markdown/etc.
	map <leader>c :w! \| !compiler <c-r>%<CR>

" Open corresponding .pdf/.html or preview
	map <leader>p :!opout <c-r>%<CR><CR>

" Ensure files are read as what I want:
	let g:vimwiki_ext2syntax = {'.Rmd': 'markdown', '.rmd': 'markdown','.md': 'markdown', '.markdown': 'markdown', '.mdown': 'markdown'}
	let g:vimwiki_list = [{'path': '~/vimwiki', 'syntax': 'markdown', 'ext': '.md'}]

" Enable Goyo by default for mutt writting
	" Goyo's width will be the line limit in mutt.
	autocmd BufRead,BufNewFile /tmp/neomutt* let g:goyo_width=80
	autocmd BufRead,BufNewFile /tmp/neomutt* :Goyo \| set bg=light
    autocmd BufRead,BufNewFile Filetype markdown let g:goyo_width=80
	autocmd BufRead,BufNewFile Filetype markdown :Goyo \| set bg=light

" Automatically deletes all trailing whitespace on save.
	autocmd BufWritePre * %s/\s\+$//e

" Navigating with guides
	inoremap <leader><leader> <Esc>/<++><Enter>"_c4l
	vnoremap <leader><leader> <Esc>/<++><Enter>"_c4l
	map <leader><leader> <Esc>/<++><Enter>"_c4l

"""HTML
	autocmd FileType html inoremap ;b <b></b><Space><++><Esc>FbT>i
	autocmd FileType html inoremap ;it <em></em><Space><++><Esc>FeT>i
	autocmd FileType html inoremap ;1 <h1></h1><Enter><Enter><++><Esc>2kf<i
	autocmd FileType html inoremap ;2 <h2></h2><Enter><Enter><++><Esc>2kf<i
	autocmd FileType html inoremap ;3 <h3></h3><Enter><Enter><++><Esc>2kf<i
    autocmd FileType html inoremap ;4 <h4></h4><Enter><Enter><++><Esc>2kf<i
	autocmd FileType html inoremap ;5 <h5></h5><Enter><Enter><++><Esc>2kf<i
	autocmd FileType html inoremap ;6 <h6></h6><Enter><Enter><++><Esc>2kf<i
	autocmd FileType html inoremap ;p <p></p><Enter><Enter><++><Esc>02kf>a
	autocmd FileType html inoremap ;a <a<Space>href=""><++></a><Space><++><Esc>14hi
	autocmd FileType html inoremap ;e <a<Space>target="_blank"<Space>href=""><++></a><Space><++><Esc>14hi
	autocmd FileType html inoremap ;ul <ul><Enter><li></li><Enter></ul><Enter><Enter><++><Esc>03kf<i
	autocmd FileType html inoremap ;li <Esc>o<li></li><Esc>F>a
	autocmd FileType html inoremap ;ol <ol><Enter><li></li><Enter></ol><Enter><Enter><++><Esc>03kf<i
	autocmd FileType html inoremap ;im <img src="" alt="<++>"><++><esc>Fcf"a
	autocmd FileType html inoremap ;td <td></td><++><Esc>Fdcit
	autocmd FileType html inoremap ;tr <tr></tr><Enter><++><Esc>kf<i
	autocmd FileType html inoremap ;th <th></th><++><Esc>Fhcit
	autocmd FileType html inoremap ;tab <table><Enter></table><Esc>O
	autocmd FileType html inoremap ;dt <dt></dt><Enter><dd><++></dd><Enter><++><esc>2kcit
	autocmd FileType html inoremap ;dl <dl><Enter><Enter></dl><enter><enter><++><esc>3kcc
	autocmd FileType html inoremap &<space> &amp;<space>
	autocmd FileType html inoremap á &aacute;
	autocmd FileType html inoremap é &eacute;
	autocmd FileType html inoremap í &iacute;
	autocmd FileType html inoremap ó &oacute;
	autocmd FileType html inoremap ú &uacute;
	autocmd FileType html inoremap ä &auml;
	autocmd FileType html inoremap ë &euml;
	autocmd FileType html inoremap ï &iuml;
	autocmd FileType html inoremap ö &ouml;
	autocmd FileType html inoremap ü &uuml;
	autocmd FileType html inoremap ã &atilde;
	autocmd FileType html inoremap ẽ &etilde;
	autocmd FileType html inoremap ĩ &itilde;
	autocmd FileType html inoremap õ &otilde;
	autocmd FileType html inoremap ũ &utilde;
	autocmd FileType html inoremap ñ &ntilde;
	autocmd FileType html inoremap à &agrave;
	autocmd FileType html inoremap è &egrave;
	autocmd FileType html inoremap ì &igrave;
	autocmd FileType html inoremap ò &ograve;
	autocmd FileType html inoremap ù &ugrave;

"MARKDOWN
	autocmd Filetype markdown,rmd map <leader>w yiWi[<esc>Ea](<esc>pa)
	autocmd Filetype markdown,rmd inoremap ,n ---<Enter><Enter>
	autocmd Filetype markdown,rmd inoremap ,b ****<++><Esc>F*hi
	autocmd Filetype markdown,rmd inoremap ,s ~~~~<++><Esc>F~hi
	autocmd Filetype markdown,rmd inoremap ,e **<++><Esc>F*i
	autocmd Filetype markdown,rmd inoremap ,h ====<Space><++><Esc>F=hi
	autocmd Filetype markdown,rmd inoremap .i ![](<++>)<++><Esc>F[a
	autocmd Filetype markdown,rmd inoremap ,a [](<++>)<++><Esc>F[a
	autocmd Filetype markdown,rmd inoremap ,1 #<Space><Enter><++><Esc>kA
	autocmd Filetype markdown,rmd inoremap ,2 ##<Space><Enter><++><Esc>kA
	autocmd Filetype markdown,rmd inoremap ,3 ###<Space><Enter><++><Esc>kA
	autocmd Filetype markdown,rmd inoremap ,l --------<Enter>
	autocmd Filetype rmd inoremap ,r ```{r}<CR>```<CR><CR><esc>2kO
	autocmd Filetype rmd inoremap ,p ```{python}<CR>```<CR><CR><esc>2kO
	autocmd Filetype rmd inoremap ,c ```<cr>```<cr><cr><esc>2kO

""".xml
	autocmd FileType xml inoremap ,e <item><Enter><title><++></title><Enter><guid<space>isPermaLink="false"><++></guid><Enter><pubDate><Esc>:put<Space>=strftime('%a, %d %b %Y %H:%M:%S %z')<Enter>kJA</pubDate><Enter><link><++></link><Enter><description><![CDATA[<++>]]></description><Enter></item><Esc>?<title><enter>cit
	autocmd FileType xml inoremap ,a <a href="<++>"><++></a><++><Esc>F"ci"
