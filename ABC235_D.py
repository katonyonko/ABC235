from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="235"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''

additional_case = [x,y]
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  from collections import deque
  def bfs(G,s):
    inf=10**30
    D=[inf]*len(G)
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
    return D
  a,N=map(int,input().split())
  G=[[] for _ in range(10**6)]
  for i in range(10**6):
    if a*i<10**6:
      G[i].append(a*i)
    if i%10!=0:
      k=max([j for j in range(6) if i//(10**j)>0])
      G[i].append(i%10*(10**k)+i//10)
  ans=bfs(G,1)[N]
  if ans<10**30:
    print(ans)
  else:
    print(-1)
  """ここから上にコードを記述"""

  print(test_case[__+1])