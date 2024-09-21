# Introduction
Welcome to the Police Station in Front of Kameari Park in Katsushika Ward! We are here to assist all citizens in need.
## Environment
- ubuntu 20.04
- python 3.8.10
## Usage Instructions
1. Install `pipenv`
```shell
pip3 install `pipenv`
```
2. Install the required packages
```shell
pipenv install --three
// If you encounter issues installing `pygraphviz`, try the following command:
sudo apt-get install graphviz graphviz-dev
```
3. Generate a `.env file` from `.env.sample` and fill in the following information:

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
## Features
- Basic functionalities:
- `Report an Incident`
- `Assist the Elderly`
- `Officer Information`
- `Report Lost Property`
- `Police Station Location`
- `Surveys`
- `Add Friend Message`
## Usage Demonstration

### Add Friend Message
![](https://img.onl/i9GbSN)

### Report an Incident
![](https://img.onl/w4ED3H)
 
### Assist the Elderly
![](https://img.onl/VzluYf)

### Officer Information
![](https://img.onl/2TLuzd)

### Report Lost Property
![](https://img.onl/oJovVB)

### Police Station Location
![](https://img.onl/Zs9qQ0)

### Surveys
![](https://img.onl/TBX4Hc)

## FSM
![](https://img.onl/1zBDsZ)

### State Descriptions
- user: Enter "report an incident" to access the menu
- choose: Select the desired service
- help_old_people: Assist the elderly
- location: View police station location
- lose_money_amount: Report lost amount
- lose_money_time: Report lost time
- lose_money_result: Result of lost amount
- information: Officer information

### bonus
- Deploy on heroku
![](https://img.onl/uycMH8)

- Line api

- Image

- Video


