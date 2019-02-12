Installing new gems
===================

While installing Jekyll I found ruby to be installed in order to test. So, I need to make a clean ruby installation and the first problem was
access rights from the gems. To avoid this issue and using sudo for everything in ubuntu, I found that we can install the gems anywhere.

Example

```
gem install package --install-dir $HOME/.gem
```

Problems with PATH
==================

First, you need to understand that if you mess this variable you will end up without any software file usefull in the terminal, so, be careful.
Changing the Path is one way to ensure linux to recognise the gems while calling them

We just set the path like this:

```
export PATH=$PATH:path_to_gems
```

Installing ruby and gem in ubuntu
=================================


**Source:**
https://onextrapixel.com/start-jekyll-blog-github-pages-free/

