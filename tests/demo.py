#!/usr/bin/python3
#coding: utf-8
'''
test and demo for huuid
'''

import uuid
import huuid

# generate a new uuid:
uid = uuid.uuid4()
print('generated uuid:          '+str(uid))

# convert to human-readable:
huid = huuid.uuid2human(uid)
print('human-readable:          '+huid)

# convert back to uuid:
back = huuid.human2uuid(huid)
print('Afer back-translation:   '+str(back))

print('--- other usecases: ---')

# get only the first 32bit of the uuid human-readable:
huid = huuid.uuid2human(uid, 32)
print('first 32bit human-readable:  '+huid)

# generate a 32- and a 64bit-password with huuid:
pw = huuid.pwgen()
print('generated 32bit-Password:    '+pw)
pw = huuid.pwgen(64)
print('generated 64bit-Password:    '+pw)
