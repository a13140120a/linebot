# linebot

linebot  (在cmd上執行的方法)
準備環境  
1.下載git: https://git-scm.com/  
2.下載ngrok  
3.Line Developes  
https://developers.line.biz/console/channel/1654940932/messaging-api  
建立好providers 參考:TOP/tutorial/eb103-test/Messaging API  
在messaging-api下/ 回應設定 /加入好友的歡迎訊息、自動回應訊息[停用]/Webhook[啟用]  


step1.要去download code:  
老師的github git clone https://github.com/BingHongLi/line_chat_bot_tutorial.git  


cmd(要在有ngrok.exe2的地方執行)  
ngrok http 5000 -region ap  

要複製加密網址(https)  
Forwarding : https://5c6210c60747.ap.ngrok.io   
貼到line developers上的message api 的webhook settings (然後打開use webhook)  


老師的github: line_chat_bot_tutorial/material/line_secret_key  
 ```js
{
  "channel_access_token": (在line developer massaging API下面)
  "secret_key": (在line developer  basic setting底下的channel scret)
  "self_user_id": (secret_key下面(basic setting))
  "rich_menu_id": (於step 1 中函數create_rich_menu生成並貼上)
  "server_url":  (ngrok的cmd，https斜線後面的東西，到.io為止)
}
```
#########每次關掉server_url都會改變##########################
