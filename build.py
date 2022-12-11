import requests
import gzip
import shutil

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

filename = ''
resp = requests.get('https://api.github.com/repos/MetaCubeX/Clash.Meta/releases/latest')
assets = resp.json()["assets"]
for i in assets:
    if 'Clash.Meta-linux-amd64-compatible' in i["name"]:
        filename = download_file(i["browser_download_url"])


print(filename)
with gzip.open(filename, 'rb') as f_in:
    with open('./bin/clash-linux-amd64', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

open('./tagname', 'w').write(resp.json()["tag_name"])
print ('build suceess')