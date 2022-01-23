from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="235"
#問題
problem="c"

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
  from collections import defaultdict
  N,Q=map(int,input().split())
  A=list(map(int,input().split())) 
  D=defaultdict(list)
  for i in range(N):
    D[A[i]].append(i)
  for i in range(Q):
    x,k=map(int,input().split())
    if len(D[x])<k:
      print(-1)
    else:
      print(D[x][k-1]+1)
  """ここから上にコードを記述"""

  print(test_case[__+1])