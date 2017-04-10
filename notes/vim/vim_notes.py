http://vim.wikia.com/wiki/Remove_unwanted_spaces
http://www.thegeekstuff.com/2009/04/vi-vim-editor-search-and-replace-examples
set smartindent tabstop=4 shiftwidth=4 expandtab
nnoremap <C-n> :bnext<CR>

sudo apt install libxml2-utils
:map <F5> : silent %!xmllint --encode UTF-8 --format - :bnext<CR>
export VISUAL=vim
export EDITOR="$VISUAL"



Delete a line if doesn't have a word
:%g!/word/d


