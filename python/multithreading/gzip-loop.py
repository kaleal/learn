import gzip
import os
import time

start_time = time.time()

files_to_compress = ['bigfile1.img','bigfile2.img','bigfile3.img','bigfile4.img','bigfile5.img','bigfile6.img','bigfile7.img','bigfile8.img']

def compress(file):
   in_file = file
   in_data = open(in_file, "rb").read()
   out_gz = file+'.gz'
   gzf = gzip.open(out_gz, "wb")
   gzf.write(in_data)
   gzf.close()

for file in files_to_compress:
   compress(file)

end_time = time.time()

print('{} files compressed in {} seconds.'.format(len(files_to_compress), end_time - start_time))
