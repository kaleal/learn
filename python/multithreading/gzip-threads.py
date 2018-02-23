import gzip
import os
import threading
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

threads = []

for file in files_to_compress:
   t = threading.Thread(target=compress, args=(file,))
   threads.append(t)
   t.start()

for thread in threads:
   thread.join()

end_time = time.time()

print('Time spent to compress both files: {} s'.format(end_time - start_time))

