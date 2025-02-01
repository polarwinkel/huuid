#!/usr/bin/python3
'''
This will convert a UUID to a human-readable and pronouncable format.

version 0.9.0dev

(c) 2025 by Dirk Winkel

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

huuid was highly inspired by
inspired by https://arxiv.org/html/0901.4016
    
'''

import uuid
import math

def __int32string(num):
    '''converts a 32bit-integer to a human-readable string'''
    letters = ['b','d','f','g','h','j','k','l','m','n','p','r','s','t','v','z','B','C','D','F','G','H','J','K','L','M','N','P','R','S','T','V','Z'] # 33 options to start with (C is necessary to achieve 32bit)
    vowels = ['a','e','i','o','u'] # 5 vowels
    consonants = ['b','d','f','g','h','j','k','l','m','n','p','r','s','t','v','z'] # 16 phonetic-qunique consonants
    string = ''
    for i in range(9):
        if i == 0:
            j = num % 33
            num = num // 33
            string = string+letters[j]
        elif i % 3 == 1:
            j = num % 5
            num = num // 5
            string = string+vowels[j]
        else:
            j = num % 16
            num = num // 16
            string = string+consonants[j]
    return string

def __str2int32(s):
    '''converts a huuid-(sub-)string to a 32bit-integer'''
    letters = ['b','d','f','g','h','j','k','l','m','n','p','r','s','t','v','z','B','C','D','F','G','H','J','K','L','M','N','P','R','S','T','V','Z'] # 33 options to start with (C is necessary to achieve 32bit)
    vowels = ['a','e','i','o','u'] # 5 vowels
    consonants = ['b','d','f','g','h','j','k','l','m','n','p','r','s','t','v','z'] # 16 phonetic-qunique consonants
    out = consonants.index(s[8])
    out = vowels.index(s[7])+out*5
    out = consonants.index(s[6])+out*16
    out = consonants.index(s[5])+out*16
    out = vowels.index(s[4])+out*5
    out = consonants.index(s[3])+out*16
    out = consonants.index(s[2])+out*16
    out = vowels.index(s[1])+out*5
    out = letters.index(s[0])+out*33
    return out

def uuid2human(uid, depth=128):
    '''convert a uuid-object to a human-readable phonetic string'''
    if type(uid)==str:
        uid = uuid.UUID(uid)
    if not isinstance(uid, uuid.UUID):
        raise TypeError('not an uuid-object')
    ustr = str(uid.hex)
    if depth == 32:
        return __int32string(int('0x'+ustr[0:8],16))
    elif depth == 64:
        return __int32string(int('0x'+ustr[0:8],16))+'-'+__int32string(int('0x'+ustr[8:16],16))
    elif depth == 96:
        return __int32string(int('0x'+ustr[0:8],16))+'-'+__int32string(int('0x'+ustr[8:16],16))+'-'+__int32string(int('0x'+ustr[16:24],16))
    else:
        return __int32string(int('0x'+ustr[0:8],16))+'-'+__int32string(int('0x'+ustr[8:16],16))+'-'+__int32string(int('0x'+ustr[16:24],16))+'-'+__int32string(int('0x'+ustr[24:32],16))

def human2uuid(s):
    '''convert a huuid-string back to a uuid-hex-string (short if <128bit)'''
    if not isinstance(s, str):
        raise TypeError('not a string')
    ss = s.split('-')
    out = ''
    for s in ss:
        if len(s) != 9:
            raise ValueError('not a huuid: all blocks must be composed of nine chars')
        int32 = __str2int32(s)
        out = out+f'0x{int32:08X}'[2:]
    if len(out) == 32:
        return uuid.UUID(out)
    return out

def new():
    '''generate a new huuid'''
    uid = uuid.uuid4()
    return uuid2human(uid)

def pwgen(entropy=32):
    '''generate a password with an entropy of 32, 64, 96 or 128bit'''
    return uuid2human(uuid.uuid4(), entropy)
