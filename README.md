yayson
======

Yay, beautiful JSON on the command line!

`yayson` will take input on `stdin` and print pretty JSON with color in your terminal. It will come out something like this:

![Example Yayson output](http://sebdah.github.com/yayson/img/screenshot.png)

Example usage
-------------

    cat my.json | yayson

or

    curl -s http://www.example.com/my.json | yayson

`--help` output
---------------

    usage: yayson [-h] [-i INDENT] [-c] [-s] [--version]

    Yayson produces beautiful JSON

    optional arguments:
      -h, --help            show this help message and exit
      -i INDENT, --indent INDENT
                            Number of spaces to indent with (default: 2)
      -c, --compact         Print JSON in compact mode, i.e. without spaces
                            between keys and values
      -s, --sort            Turn on key sorting
      --version             Print version information

Release information
-------------------

**0.2.0 (2013-04-08)**

- [Set default indenting to 2 spaces (#2)](https://github.com/sebdah/yayson/issues/2)
- [Add compact mode (#1)](https://github.com/sebdah/yayson/issues/1)

**0.1.0 (2013-04-07)**

- Initial release

Releasing to PyPI
-----------------

    make release

Author
------

This project is maintained by [Sebastian Dahlgren](http://www.sebastiandahlgren.se) ([GitHub](https://github.com/sebdah) | [Twitter](https://twitter.com/sebdah) | [LinkedIn](www.linkedin.com/in/sebastiandahlgren))
