# huuid - human UUIDs
python3-library to convert uuids forth and back to a human-readable and pronounceable format

## What is `huuid`

`hhuid` does a bijective transformation from uuids to a format that can be read, pronounced and typed a lot better than the default formats.
No Information is lost in the mapping.

Here is an example-output of the `demo.py` in the `tests`-folder:

```
generated uuid:          f3ad6cef-2732-4b18-97dd-137a459eb656
human-readable:          tapratnaz-vorjonfif-Tezjozdin-sejgipneh
Afer back-translation:   f3ad6cef-2732-4b18-97dd-137a459eb656
--- other usecases: ---
first 32bit human-readable:  tapratnaz
generated 32bit-Password:    Sunmuhnud
generated 64bit-Password:    Vezvegdum-ladzibkal
```

## How to use `huuid`

install it, i.e. using pip:

`pip install huuid`

then in python import in your code with

`import huuid`

and convert any uuid-object to a huuid-string with

`huuid.uuid2human(myUuidObject)`

## Background

The hexadecimal representation of the UUID is translated to letters that have an unambiguous pronounciation. The 2nd, and then every third letter is a vowel, the other ones are consonants which makes up a well pronounced word that sounds like it is made up of syllables.

There are 5 vowels and 16 consonants (just unambiguous ones) being used, and (only) for the first letter capitals are allowed.
(And a capital-C additional to the 16 chosen unambiguous consonants to reach 32bit with 9 letters)

With this pattern there are a little more than 2^32 possibilities to generate a word with 9 letters.
4 "Words" hit the 128bit of UUIDs (>10^38).

## Dependencies

This only uses the python3-modules `uuid` and `math`.

## Credits

This is highly inspired by

https://arxiv.org/html/0901.4016

published by Daniel Shawcross Wilkerson
and its implementation:

https://github.com/dsw/proquint
