#! /home/anirudha/Desktop/lectures/soft_comp/soft_boi/bin/python
import hashlib

hashobject = hashlib.md5(b'hello')
print(hashobject.hexdigest())