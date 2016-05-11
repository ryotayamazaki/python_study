#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#*****************************************************************************************
# ぐるなびWebサービスの応援口コミAPIを実行しハンバーグの口コミを取得しパースするプログラム
# 注意：アクセスキーはユーザ登録後に発行されるキーを指定してください。
#*****************************************************************************************
import sys
import urllib
import json
import cgi
import os
from stat import *

os.chmod('5_2.py',0755)

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
url = "http://api.gnavi.co.jp/PhotoSearchAPI/20150630/"
# メニュー
menu_name = ""
#文字コード
encoding = 'utf-8'

vote_date = ""

hit_per_page = "3"
shop_name = ""
area = ""
form = cgi.FieldStorage()
if form.has_key("shop_name"):
    shop_name = form["shop_name"].value

if form.has_key("area"):
    area = form["area"].value

if form.has_key("menu_name"):
    menu_name = form["menu_name"].value

if form.has_key("vote_date"):
    vote_date = form["vote_date"].value

####
# APIアクセス
####
# URLに続けて入れるパラメータを組立
query = [
    ( "format","json"),
    ( "keyid", keyid),
    ( "menu_name", menu_name.encode(encoding) ),
    ( "hit_per_page", hit_per_page)
    ( "shop_name" , shop_name)
    ( "area" , area)
    ( "vote_date" , vote_date)
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

#print data
#print data["gnavi"]["error"]["message"]
# エラーの場合
if "error" in data :
    if "message" in data :
        print u"{0}".format( data["message"] )
    else :
        print u"データ取得に失敗しました。"
    sys.exit()

# ヒット件数取得
total_hit_count = None
if "total_hit_count" in data["response"]:
    total_hit_count = data["response"]["total_hit_count"]

#ページごとの件数を取得
hit_per_page = None
if "hit_per_page" in data["response"] :
    hit_per_page = data["response"]["hit_per_page"]

# ヒット件数が0以下、または、ヒット件数がなかったら終了
if total_hit_count is None or total_hit_count <= 0 or hit_per_page is None or hit_per_page <= 0 :
    print u"指定した内容ではヒットしませんでした。"
    sys.exit()

# ヒット件数表示
print "{0}件ヒットしました。".format( total_hit_count )
print "----"

# 出力件数
disp_count = 0

#f = open("5.html","w")
print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"http://www.w3.org/TR/html4/loose.dtd\">"
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">"
print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">"
print "<meta http-equiv=\"Content-Style-Type\" content=\"text/css\">"
print "<html lang=\"ja\">"
print "<body>"

# 応援口コミデータ取得
for i in range( hit_per_page ) :
    photo = data["response"]["{0}".format(i)]["photo"]
    line = []
    id = ""
    name = ""
    mname = ""
    comment = ""
    shop_url = ""
    image_url = []
    
    # 店舗番号
    if "shop_id" in photo and is_str( photo["shop_id"] ) :
        id = photo["shop_id"]
    line.append( id )
    
    # 店舗名
    if "shop_name" in photo and is_str( photo["shop_name"] ) :
        name = photo["shop_name"].encode(encoding) 
#        print name
        print "<h1>",name,"</h1>"
    line.append( name )
    
    # メニュー名
    if "menu_name" in photo and is_str( photo["menu_name"] ) :
        mname = photo["menu_name"]
    line.append( mname )
    
    # コメント
    print "<p>"
    if "shop_url" in photo:
        shop_url = photo["shop_url"]
        print "<a href=\"",shop_url,"\">",shop_url,"<a><br>"

    if "image_url" in photo:
        image_url = photo["image_url"]
        if "url_1024" in image_url:
            print "<img src=\"",image_url["url_1024"],"\" alt=\"1024px画像\">"
        elif "url_320" in image_url:
            print "<img src=\"",image_url["url_320"],"\" alt=\"320px画像\">"
        elif "url_250" in image_url:
            print "<img src=\"",image_url["url_250"],"\" alt=\"250px画像\">"
        elif "url_200" in image_url:
            print "<img src=\"",image_url["url_200"],"\" alt=\"200px画像\">"
        print "<br>"


    if "comment" in photo and is_str( photo["comment"] ) :
        comment = photo["comment"]
        print comment.encode(encoding)
    line.append( comment )
    print "</p>"
    # タブ区切りで出力
#    print "\t".join( line )
    disp_count += 1
    
# 出力件数を表示して終了
#print "----"
#print u"{0}件出力しました。".format( disp_count )
print "</body>"
print "</html>"
sys.exit()

