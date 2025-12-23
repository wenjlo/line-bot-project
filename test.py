from linebot import LineBotApi, WebhookHandler
from linebot.models import FlexSendMessage
from linebot.v3.messaging import MessagingApi
# --- 設定區 ---
# 繼續使用你的 Token (強烈建議測試完後去後台 Reissue 更新)
line_bot_api = LineBotApi('lRaLaca0Up47LTrj1YhOyxYUJkOq7vWog/cyU1YzwYCHO0GPm+0l4o2n1LCS27ONhP9936FfJzBObGAMNg0iaGnuwuw7Sy9zBWRKuyk6C8Z034SjLXapu1rTA+liWU3yz/PoXYHIWkdPHo7zkVdN9AdB04t89/1O/w1cDnyilFU=/rNjh4icfZTagfWaqPOj6T9nMc5IFzCrmPspNNG/zr41rDVi/tY4UcOrNcDzIM9sptBHGLizgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ea8e335a823665cef46a89b503479214')
target_group_id = "C7e6f5170bf193e29c5fdf33554e9482a"
BASE_URL = "https://f32f3c8682c3.ngrok-free.app"

def create_video_link_bubble(title, video_url, preview_img_url, description, tags):
    """
    tags: 一個包含字串的列表，例如 ["#風景", "#旅行", "#4K"]
    """

    # 1. 動態產生 Hash Tag 的 JSON 結構
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
# --- 6 組影片資料 (保持不變) ---
video_data_list = [
    {
        "title": "🎬 影片 1/6：大自然",
        "video": f"https://akuma-trstin.mushroomtrack.com/hls/72jLckgEy_gB-prZMezHIg/1766318041/55000/55563/55563.m3u8",
        "preview":"https://ipornbase.xyz/sites/default/files/styles/ipth2/public/avposter/MSD-124.jpg.webp?itok=haLuBLhW",
        "desc": "欣賞壯觀的山脈與自然景色。",
        "tags":["#City", "#Night", "#Traffic", "#4K"]
    },
    {
        "title": "🎬 影片 2/6：城市縮時",
        "video": f"{BASE_URL}/2.mp4",
        "preview": "https://mixkit.imgix.net/videos/preview/mixkit-aerial-view-of-city-traffic-at-night-106-0.jpg",
        "desc": "繁忙的城市夜晚交通縮時攝影。",
        "tags":["#City", "#Night", "#Traffic", "#4K"]
    },
    {
        "title": "🎬 影片 3/6：經典範例",
        "video": f"{BASE_URL}/3.mp4",
        "preview": "https://www.w3schools.com/images/w3schools_green.jpg",
        "desc": "Big Buck Bunny 經典開源動畫片段。","tags":["#City", "#Night", "#Traffic", "#4K"]
    },
    {
        "title": "🎬 影片 4/6：海洋生物",
        "video": f"{BASE_URL}/4.mp4",
        "preview": "https://i.vimeocdn.com/video/773972868-f155771865687531393547726206860303924866028122757173302753770343-d_640x360.jpg",
        "desc": "深海中優游的水母群。","tags":["#City", "#Night", "#Traffic", "#4K"]
    },
     {
        "title": "🎬 影片 5/6：科技抽象",
        "video": f"{BASE_URL}/5.mp4",
        "preview": "https://images.pexels.com/videos/5839887/pexels-photo-5839887.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
        "desc": "抽象的數據流動視覺效果。","tags":["#City", "#Night", "#Traffic", "#4K"]
    },
    {
        "title": "🎬 影片 6/6：咖啡時光",
        "video": f"{BASE_URL}/6.mp4",
        "preview": "https://mixkit.imgix.net/videos/preview/mixkit-pouring-milk-into-coffee-slow-motion-1993-0.jpg",
        "desc": "慢動作倒入牛奶的咖啡製作過程。","tags":["#City", "#Night", "#Traffic", "#4K"]
    }
]

# --- 建立輪播 ---
bubble_contents = []
for data in video_data_list:
    bubble = create_video_link_bubble(data["title"], data["video"], data["preview"], data["desc"],data["tags"])
    bubble_contents.append(bubble)

carousel_flex_message = {
  "type": "carousel",
  "contents": bubble_contents
}

# --- 執行發送 ---
try:
    line_bot_api.push_message(
        target_group_id,
        FlexSendMessage(
            alt_text="[影音公告] 6 則影片通知，請左右滑動",
            contents=carousel_flex_message
        )
    )
    print("修正後的輪播訊息發送成功！")
except Exception as e:
    print(f"發送失敗: {e}")