#!/usr/bin/env python
# -*- coding: utf-8 -*-
#*****************************************************************************************
# ぐるなびWebサービスの都道府県マスタ取得APIを実行しパースするプログラム
# 注意：APIアクセスキーの値にはユーザ登録で取得したものを入れてください。
#*****************************************************************************************
import sys
import urllib
import json

####
# 変数の型が文字列かどうかチェック
####
def is_str( data = None ) :
    if isinstance( data, str ) or isinstance( data, unicode ) :
        return True
    else :
        return False

####
# 初期値設定
####
# APIアクセスキー
keyid = "566dadc5af736b7ec641331380682728"
# エンドポイントURL
url = "http://api.gnavi.co.jp/master/PrefSearchAPI/20150630/"

####
# APIアクセス
####
# URLに続けて入れるパラメータを組立
query = [
    ( "format", "json"),
    ( "keyid", keyid)
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

# データがなかったら終了
if not "pref" in data :
    print u"エリアデータがなかったため終了します。"
    sys.exit()

# 出力件数
disp_count = 0

# レストランデータ取得
for pref in data["pref"] :
    line = []
    pref_code = ""
    pref_name = ""
    area_code = ""

    #エリアコード
    if "area_code" in pref and is_str( pref["area_code"] ) :
        area_code = u"{0}".format( pref["area_code"] )
    line.append( area_code )
    # 都道府県コード
    if "pref_code" in pref and is_str( pref["pref_code"] ) :
        pref_code = pref["pref_code"]
    line.append( pref_code )
    # 都道府県名
    if "pref_name" in pref and is_str( pref["pref_name"] ) :
        pref_name = u"{0}".format( pref["pref_name"] )
    line.append( pref_name )
    # タブ区切りで出力
    print "\t".join( line )
    disp_count += 1

# 出力件数を表示して終了
print "----"
print u"{0}件出力しました。".format( disp_count )
sys.exit()
