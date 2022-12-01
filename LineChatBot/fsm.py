

from transitions.extensions import GraphMachine
from utils import send_text_message, send_carousel_message, send_button_message, send_image_message
from bs4 import BeautifulSoup
import requests
from linebot.models import (ImageCarouselColumn, URITemplateAction, MessageTemplateAction,MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,LocationSendMessage)
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
import pandas as pd
import random


import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv




channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

# global variable
hour = 0
minute = 0
part = ''
people = 0
line_bot_api = LineBotApi(channel_access_token)

class TocMachine(GraphMachine):

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    # user start
         
    def is_going_to_choose(self, event):
        text = event.message.text
        if text == '報案':
            return True
        return False
    
    def on_enter_choose(self, event):
        title = '這裡是龜有公園前派出所'
        text = '請問需要甚麼服務? 遺失錢財/查看派出所位置/警員資訊/幫助老人家'
        btn = [
            MessageTemplateAction(
		 label = '遺失錢財',
                text ='遺失錢財'
            ),
            MessageTemplateAction(
                label = '幫助老人家',
                text = '幫助老人家'
            ),
            
             MessageTemplateAction(
                label = '查看派出所位置',
                text = '查看派出所位置'
            ),
             MessageTemplateAction(
                label = '警員資訊',
                text = '警員資訊'
            ),
        ]
        url = 'https://img.onl/Vxtl8n'
        send_button_message(event.reply_token, title, text, btn, url)
        
          
        
    def is_going_to_help_old_people(self, event):
        text = event.message.text
        if text == '幫助老人家':
            return True
        return False

   
    def on_enter_help_old_people(self, event):
        message = [ 
            ImageSendMessage(  
            original_content_url='https://img.onl/jyUUuW',
            preview_image_url='https://img.onl/jyUUuW'
            
            ),
		TextSendMessage(  
    		text = '輸入任意值以返回'
		),
            ]
        line_bot_api.reply_message(event.reply_token,message)   

       
        
    def is_going_to_location(self, event):
        text = event.message.text
        if text == '查看派出所位置':
            return True
        return False

    def on_enter_location(self, event):
        
        message= [
        LocationSendMessage(
        title='my location',
        address='龜有公園前派出所',
        latitude=35.76804770161627,
        longitude=139.84845189774526),
        TextSendMessage(  
    		text = '輸入任意值以返回'
		),
        ]
        line_bot_api.reply_message(event.reply_token,message)
       

        
       
      
      
    def is_going_to_lose_money_money(self, event):
        text = event.message.text
        if text == '遺失錢財':
            return True
        return False        
      
    def on_enter_lose_money_money(self, event):
        send_text_message(event.reply_token, '請輸入金額')

    def is_going_to_lose_money_time(self, event):
        global people
        text = event.message.text
        if text.lower().isnumeric():
            people = int(text)
            return True
        return False
        
    def on_enter_lose_money_time(self, event):
        send_text_message(event.reply_token, '請輸入時間(格式xx:xx)')
        
    def is_going_to_lose_money_result(self, event):
        global hour
        global minute
        text = event.message.text
        time = text.split(':')
        if time[0].lower().isnumeric():
            hour = int(time[0])
        else:
            return False
        if time[1].lower().isnumeric():
            minute = int(time[1])
        else:
            return False   
            
        if hour>=0 and hour <24 and  minute>=0 and minute <60:
            return True
        return False
        

    def on_enter_lose_money_result(self, event):
        global x
        x=random.randint(0,1)

        if x == 0:
            message = [ 
            ImageSendMessage(  
            original_content_url='https://img.onl/XEPDRf',
            preview_image_url='https://img.onl/XEPDRf'
		),
		TextSendMessage(  
    		text = '輸入任意值以返回'
		),
            ]
        else:
            message = [ 
            ImageSendMessage(  
            original_content_url='https://img.onl/eSqTVZ',
            preview_image_url='https://img.onl/eSqTVZ'
            
            ),
		TextSendMessage(  
    		text = '輸入任意值以返回'
		),
            ]
        line_bot_api.reply_message(event.reply_token,message)   

        
        
        
    def is_going_to_information(self, event):
        text = event.message.text
        if text == '警員資訊':
            return True
        return False
   
    def on_enter_information(self, event):
        send_text_message(event.reply_token, '輸入任意值以返回')    
        
     
    def go_back(self, event):
        return True
