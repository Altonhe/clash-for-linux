import requests
import gzip
import shutil

def download_file(url):
    url = f'https://ghproxy.com/{url}'
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

open('./tagname.txt', 'w').write(resp.json()["tag_name"])

# startdir =r'./RProxy2' 
# file_news = startdir +'.zip' 
# z = zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED) 
# for dirpath, dirnames, filenames in os.walk(startdir):
#     fpath = dirpath.replace(startdir,'') 
#     fpath = fpath and fpath + os.sep or ''
#     for filename in filenames:
#         z.write(os.path.join(dirpath, filename),fpath+filename)
# z.close()
print ('build suceess')