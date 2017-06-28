import urllib.request
import multiprocessing

# Pool starts needed q-tity of processes
way = 'https://git-scm.com'

def f(url):
    r = urllib.request.urlopen(url)
    print(len(r.read()))

p = multiprocessing.Pool(5)

p.map(f, [way] * 20)
