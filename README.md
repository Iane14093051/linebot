# 前言
歡迎各位來到葛氏署的龜有公園前派出所，只要有困難，我們都可以盡力為各位市民服務!
## 環境
- ubuntu 20.04
- python 3.8.10
## 使用教學
1. install `pipenv`
```shell
pip3 install pipenv
```
2. install 所需套件
```shell
pipenv install --three
// 若遇到pygraphviz安裝失敗，則嘗試下面這行
sudo apt-get install graphviz graphviz-dev
```
3. 從`.env.sample`產生出一個`.env`，並填入以下個資訊

- Line
    - LINE_CHANNEL_SECRET
    - LINE_CHANNEL_ACCESS_TOKEN
4. install `ngrok`

```shell
sudo snap install ngrok
```
5. run `ngrok` to deploy Line Chat Bot locally
```shell
ngrok http 8000
```
6. execute app.py
```shell
python3 app.py
```
## 使用說明
- 基本功能
- `報案`
- `幫助老人家`
- `警員資訊`
- `遺失錢財`
- `派出所位置`    
## 使用示範
### 幫助老人家

### 警員資訊

### 遺失錢財

### 派出所位置

## FSM
![](https://img.onl/1zBDsZ)

### state說明
- user: 輸入報案以進入選單
- choose: 選擇需要的服務
- help_old_people: 幫助老人家
- location: 查看派出所位置
- lose_money_money: 遺失金額
- lose_money_time: 遺失時間
- lose_money_result: 遺失金額結果
- information: 警員資訊

### bonus
- Deploy on heroku
![](https://img.onl/uycMH8)


