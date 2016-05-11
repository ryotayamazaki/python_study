#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import urllib
import json

####
# 変数の型が文字列かどうかチェック
####
def is_str( data = None ):
    if isinstance( data, str ) or isinstance( data, unicode ):
        return True
    else:
        return False


sarch_word = sys.argv[1]

keyid = "566dadc5af736b7ec641331380682728"
url = "http://api.gnavi.co.jp/RestSearchAPI/20150630/"
query = [
    ("format","json"),
    ("keyid",keyid),
    ("freeword",sarch_word),
#    ("pref",pref)
]

if len(sys.argv) == 3:
#    print len(sys.argv[2])
    pref = "PREF"
    if len(sys.argv[2])==1:
        pref += "0"
    pref += sys.argv[2]
    query.append(("pref",pref))

# URL生成
url += "?{0}".format( urllib.urlencode( query ) )
# API実行
try :
    result = urllib.urlopen( url ).read()
except ValueError :
    print u"APIアクセスに失敗しました。"
    sys.exit()

####
# 取得した結果を解析
####
data = json.loads( result )

# エラーの場合
if "error" in data :
    if "message" in data :
        print u"{0}".format( data["message"] )
    else :
        print u"データ取得に失敗しました。"
    sys.exit()

# ヒット件数取得
total_hit_count = None
if "total_hit_count" in data :
    total_hit_count = data["total_hit_count"]

# ヒット件数が0以下、または、ヒット件数がなかったら終了
if total_hit_count is None or total_hit_count <= 0 :
    print u"指定した内容ではヒットしませんでした。"
    sys.exit()

# レストランデータがなかったら終了
if not "rest" in data :
    print u"レストランデータが見つからなかったため終了します。"
    sys.exit()

# ヒット件数表示
print "{0}件ヒットしました。".format( total_hit_count )
print "----"

# 出力件数
disp_count = 0

# レストランデータ取得
for rest in data["rest"] :
    line = []
#  id                   = ""
    name = ""
    if "name" in rest and is_str( rest["name"] ) :
        name = u"{0}".format( rest["name"] )
    line.append( name )
    print "\t".join( line )
    disp_count += 1

# 出力件数を表示して終了
print "----"
print u"{0}件出力しました。".format( disp_count )
sys.exit()
