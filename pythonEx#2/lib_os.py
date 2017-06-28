# lib os
import os
os.mkdir('dir')
os.chdir('dir')
os.getcwd()
os.listdir('.')
os.remove('file1')
os.unlink('file2')
os.rmdir('dir')

import os.path
os.path.abspath('file.txt')
os.path.split(os.path.abspath('file.txt'))
os.path.join('/fome/z', 'file.txt') # glue depend on opSys
for root, dirs, files in os.walk('/usr/lib/gss'):
    print(root, dirs, files)

#lib shutil

#tempfile
import tempfile

f = tempfile.TemporaryFile()
f.close()
f = tempfile.NamedTemoraryFile()
f.name

import io
s = io.StringIO('Hello!')
dir(s)
s.seek(0)
s.read()

b = io.ButesIO()
b.write(b'Hello')
b.seek(0)
b.read()
