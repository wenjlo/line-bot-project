from linebot import LineBotApi, WebhookHandler
from linebot.models import FlexSendMessage
import pandas as pd

class LineBot:
    def __init__(self,token,channel_secret):
        self.line_bot_api = LineBotApi(token)
        self.channel_secret = channel_secret

    @staticmethod
    def create_video_link_bubble(title, video_url, preview_img_url, description="", tags=None):
        """
        tags: 一個包含字串的列表，例如 ["#風景", "#旅行", "#4K"]
        """

        # 1. 動態產生 Hash Tag 的 JSON 結構
        if tags is None:
            tags = []
        tag_contents = []
        for tag in tags:
            tag_contents.append({
                "type": "text",
                "text": tag,
                "size": "xs",
                "color": "#1E90FF",  # 使用像連結一樣的藍色
                "decoration": "none",
                "margin": "md",  # 標籤之間的間距
                "action": {
                    "type": "message",
                    # 點擊標籤後，使用者會發送這段文字
                    "text": f"搜尋標籤：{tag}"
                }
            })

        # 2. 回傳完整的 Bubble 結構
        return {
            "type": "bubble",
            "size": "mega",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {"type": "text", "text": title, "weight": "bold", "color": "#FFFFFF", "size": "md"}
                ],
                "backgroundColor": "#00B900", "paddingAll": "10px"
            },
            "hero": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image", "url": preview_img_url, "size": "full",
                        "aspectRatio": "16:9", "aspectMode": "cover"
                    },
                    {
                        "type": "box", "layout": "vertical",
                        "contents": [
                            {"type": "text", "text": "▶", "size": "xl", "color": "#ffffff"}
                        ],
                        "position": "absolute", "backgroundColor": "#00000099",
                        "cornerRadius": "100px", "width": "40px", "height": "40px",
                        "justifyContent": "center", "alignItems": "center",
                        "offsetStart": "45%", "offsetTop": "40%"
                    }
                ],
                "action": {"type": "uri", "label": "Play Video", "uri": video_url},
                "width": "100%", "height": "200px"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    # 內文說明
                    {"type": "text", "text": description, "wrap": True, "color": "#555555", "size": "sm"},

                    # --- Hash Tags 區塊 ---
                    {
                        "type": "box",
                        "layout": "baseline",  # 使用 baseline 讓標籤橫向排列且自動換行(如果空間夠)
                        "margin": "md",
                        "spacing": "sm",  # 每個元件之間的間隔
                        "contents": tag_contents
                    }
                ]
            }
        }

    @staticmethod
    def bubble_data(title,video_url,preview_img_url,description=""):
        return {
            "title": title,
            "video": video_url,
            "preview": preview_img_url,
            "desc": description,
            "tags": []
        }

    def send_bubble_message(self,video_df,target_group_id):
        video_data_list = []
        for index, row in video_df.iterrows():
            video_data_list.append(self.bubble_data(title=row['標題'],video_url=row['影片'],
                                                    preview_img_url=row['圖片'],description=row['標題']))

        bubble_contents = []
        for data in video_data_list:
            bubble = self.create_video_link_bubble(data["title"], data["video"], data["preview"], data["desc"], data["tags"])
            bubble_contents.append(bubble)

        carousel_flex_message = {
            "type": "carousel",
            "contents": bubble_contents
        }

        try:
            self.line_bot_api.push_message(
                target_group_id,
                FlexSendMessage(
                    alt_text=f"[影音公告] {len(bubble_contents)} 則影片通知，請左右滑動",
                    contents=carousel_flex_message
                )
            )
            print("修正後的輪播訊息發送成功！")
        except Exception as e:
            print(f"發送失敗: {e}")