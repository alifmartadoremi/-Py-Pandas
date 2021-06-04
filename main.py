import pandas as pd
import os

def readLink(self):

        path = r'[path]'

        try:
            os.mkdir(path)

        except OSError:
            print('Folder sudah ada')
        else:
            print('Folder berhasil dibuat')

        os.chdir(path)
        print(os.getcwd())

        with open('[nama file].csv', 'w') as f:
            w = csv.writer(f)
            for purinzu in range(len(a)):
                LinkenSphere = QueryForElastic.getHash(a[purinzu])
                repeater = []
                linkContainer = []
                for offset in LinkenSphere['hits']['hits']:
                    repeater.append(offset['_source'])
                    linkContainer.append(repeater[0]['_id'])
                    print("ID Hash :"+a[purinzu]+" -> "+repeater[0]['_id'])
                    w.writerow([a[purinzu], linkContainer])
            print("Pertukaran Selesai | KVDA 2020")