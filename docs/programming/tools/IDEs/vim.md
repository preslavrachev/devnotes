# VIM as an IDE

Despite being lightweight enough to fit in everywhere, vim offers advanced capabilities that go well beyond simple editing. With the right customisations, one can turn vim from an advanced text editor, into a full-blown IDE, while keeping its minimalist nature.[^vim_ide]

## Plugin Managers
The secret in turning vim into a full-blown IDE lies in its extension capabilities. Up until version 8[^native_packager], vim did not have a native option to install plugins. Initially, this led the community to come up tools that could help make this a breeze. The simplest and perhaps, most well-known community package manager is called [pathogen](https://github.com/tpope/vim-pathogen)[^pathogen], and is widely used even nowadays. In fact, vim's native package manager has been inspired by and follows the structure laid out by pathogen, so regardless of whether you use pathogen or not, you'd certainly come across it many times.

[^native_packager]: [Vim: So long Pathogen, hello native package loading | George Ornbo](https://shapeshed.com/vim-packages/)

[^pathogen]: [Pathogen | Github](https://github.com/tpope/vim-pathogen)

[^vim_ide]: [Boost your VIM | Preslav Mihaylov](https://pmihaylov.com/category/boost-your-vim/)
