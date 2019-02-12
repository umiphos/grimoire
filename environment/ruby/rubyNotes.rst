Installing new gems
===================

While installing Jekyll I found ruby to be installed in order to test. So, I need to make a clean ruby installation and the first problem was
access rights from the gems. To avoid this issue and using sudo for everything in ubuntu, I found that we can install the gems anywhere.

Example

```
gem install package --install-dir $HOME/.gem
```

