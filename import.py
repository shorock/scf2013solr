import csv, json
from SolrClient import SolrClient

headers = list(csv.reader(open('2013map.txt', 'r'), delimiter='\t'))

solr = SolrClient('http://localhost:32333/solr')

bigfile = open('scf2013.ascii', 'r')

linenum=1

for line in bigfile:
    grid = {}
    grid['id']=linenum
    linenum = linenum+1
    for header in headers:
        length = int(header[2])
        tail = int(header[3])
        offset = tail-length
        titles = header[0].split()
        title = titles[0]
        svalue = line[offset:tail]
        try:
            grid[title + '_f']=float(svalue)
        except:
            pass
    arry = []
    arry.append(grid)
    solr.index_json('scf', json.dumps(arry))
    print(linenum)
pass
