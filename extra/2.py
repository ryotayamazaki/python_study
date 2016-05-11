#!/usr/bin/env python
# -*- coding: utf-8 -*-
#*****************************************************************************************
# ぐるなびWebサービスのレストラン検索APIで緯度経度検索を実行しパースするプログラム
# 注意：ここでは緯度と経度の値は固定でいれています。
# 　　　APIアクセスキーの値にはユーザ登録で取得したものを入れてください。
#*****************************************************************************************
import sys
import urllib
import json
import unicodedata
import re

####
# 変数の型が文字列かどうかチェック
####
def is_str( data = None ):
    if isinstance( data, str ) or isinstance(data, unicode):
        return True
    else:
        return False

def is_japanese(string):
    result = re.search('[ぁ-んァ-ヴ一-龥]', string)
#    print result
    return result

def check_jpn( deta = None ):
#    print type(deta)
    if is_japanese(deta):
        return 'jpn'
    else:
        return 'notjpn'

sarch_word = sys.argv[1]
mode = check_jpn(sarch_word)

keyid = "566dadc5af736b7ec641331380682728"
if mode == 'jpn':
    url = "http://api.gnavi.co.jp/RestSearchAPI/20150630/"
    print u"日本語モード"
elif mode == 'notjpn':
    url = "http://api.gnavi.co.jp/ForeignRestSearchAPI/20150630/"
    print u"他言語モード"
query = [
    ("format","json"),
    ("keyid",keyid),
    ("freeword",sarch_word),
#  ( "latitude",  latitude  ),
#  ( "longitude", longitude ),
#  ( "range",     range     )
]
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
    if mode == 'jpn':
#    print rest["name"][u'name']
        if "name" in rest and is_str( rest["name"] ) :
            name = u"{0}".format( rest["name"] )
        line.append( name )
        print "\t".join( line )
        disp_count += 1
    elif mode == 'notjpn':
        print rest["name"][u"name"]
        disp_count += 1

# 出力件数を表示して終了
print "----"
print u"{0}件出力しました。".format( disp_count )
sys.exit()

