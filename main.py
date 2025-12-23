from src.lib.line_bot import LineBot
import pandas as pd

group_id = "C7e6f5170bf193e29c5fdf33554e9482a"
bot_df = pd.read_csv('data/群組機器人.csv')
video_df = pd.read_csv('data/影片.csv')
line_bot = LineBot(token=bot_df['token'].values[0],channel_secret=bot_df['secret'].values[0])
line_bot.send_bubble_message(video_df,group_id)