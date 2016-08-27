# l2a
Language Learning Assist

# 基本仕様

## 翻訳

* Input
   * 単語もしくは文章
   * 翻訳エンジン
   * ユーザー
* Output
   * 翻訳した結果(日英/英日)
   * リクエストした単語の検索回数
* 処理
   * リクエストされた単語を翻訳APIに投げる
   * 投げる時と同時にその単語とリクエスト日付とユーザーをDBに格納する
   * 翻訳APIから返ってきた結果をレスポンスする

## 統計情報表示

* Input
   * 開始日付
   * 終了日付

* Output
   * 開始日付-終了日付範囲の単語と検索回数

# DB
MongoDB

# 言語
Python

# アプリケーションサーバー
AppServer: nginx+uWSGI+Python3 and jenkins
