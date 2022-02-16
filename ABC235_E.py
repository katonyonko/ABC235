from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="235"
#問題
problem="e"

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
  #Union Find
  class UnionFind():
    def __init__(self, n):
      self.n = n
      self.parents = [-1] * n
    def find(self, x):
      if self.parents[x] < 0:
        return x
      else:
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
      x = self.find(x)
      y = self.find(y)
      if x == y:
        return
      if self.parents[x] > self.parents[y]:
        x, y = y, x
      self.parents[x] += self.parents[y]
      self.parents[y] = x
    def size(self, x):
      return -self.parents[self.find(x)]
    def same(self, x, y):
      return self.find(x) == self.find(y)
    def members(self, x):
      root = self.find(x)
      return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
      return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
      return len(self.roots())
    def all_group_members(self):
      return {r: self.members(r) for r in self.roots()}
    def __str__(self):
      return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

  def Kruskal(G):
    edges=set()
    for i in range(len(G)):
      for j in range(len(G[i])):
        c,k,a,b=G[i][j]
        l,m=min(i,k),max(i,k)
        edges.add((c,l,m,a,b))
    edges=list(edges)
    edges.sort()
    uf = UnionFind(len(G))
    res=['No']*Q
    for edge in edges:
      if edge[3]==0:
        if not uf.same(edge[1], edge[2]):
          uf.union(edge[1], edge[2])
      else:
        if not uf.same(edge[1], edge[2]):
          res[edge[4]]='Yes'
    return res

  N,M,Q=map(int,input().split())
  G=[[] for _ in range(N)]
  for _ in range(M):
    a,b,c=map(int,input().split())
    a-=1; b-=1
    G[a].append((c,b,0,0))
    G[b].append((c,a,0,0))
  for i in range(Q):
    u,v,w=map(int,input().split())
    u-=1; v-=1
    G[u].append((w,v,1,i))
    G[v].append((w,u,1,i))
  ans=Kruskal(G)
  for i in range(Q):
    print(ans[i])
  """ここから上にコードを記述"""

  print(test_case[__+1])