
# untuk deklarasi python
import re

# membuka filebahan.txt
fileopen = open('filebahan.txt', 'rb')
data_string = fileopen.read()
# menampilkan data string
print data_string

# melakukan pencarian charakter dengan regex
total = re.findall(r'Total : [^\d]+(\d+,\d+)', data_string)
# menampilan regex
print "halo "
print total[0]
