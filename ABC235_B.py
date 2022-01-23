from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="235"
#問題
problem="b"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''5
1 5 10 4 2
'''
y = '''10'''

additional_case = [x,y]
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  N=int(input())
  H=list(map(int,input().split()))
  i=0
  while i<N-1 and H[i]<H[i+1]:
    i+=1
  print(H[i])
  """ここから上にコードを記述"""

  print(test_case[__+1])