import requests
import json
import time
from urllib.parse import urlencode

# ====================== 配置参数 ======================
GOODS_ID = "524789429236"  # 拼多多商品ID（需从商品链接中获取）
MAX_PAGE = 10  # 最大爬取页数（每页约10条评论，根据实际调整）
SLEEP_TIME = 3  # 每次请求间隔（秒），避免被反爬

# ====================== 请求头（模拟手机端） ======================
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": f"https://mobile.yangkeduo.com/goods.html?goods_id={GOODS_ID}",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
}


# ====================== 评论保存函数 ======================
def save_comment_to_txt(comments, page):
    with open("pdd_comments.txt", "a", encoding="utf-8") as f:
        f.write(f"==================== 第 {page + 1} 页评论 ====================\n")
        for comment in comments:
            content = comment.get("goods_eval", "无评论内容").strip()  # 评论内容
            score = comment.get("star", 0)  # 评分（1-5星，0=未评分）
            time_str = comment.get("eval_time", "未提及")  # 评论时间
            user_level = comment.get("user_info", {}).get("user_level", "普通用户")  # 用户等级
            spec = comment.get("sku_name", "未提及")  # 购买的配置规格（如内存/硬盘）

            f.write(f"【评分】{'★' * score if score != 0 else '未评分'}\n")
            f.write(f"【时间】{time_str}\n")
            f.write(f"【配置】{spec}\n")
            f.write(f"【用户等级】{user_level}\n")
            f.write(f"【内容】{content}\n")
            f.write("-" * 50 + "\n")
        print(f"第 {page + 1} 页评论保存成功")


# ====================== 主爬取逻辑 ======================
def crawl_pdd_comments():
    base_url = "https://mobile.yangkeduo.com/goods_comments.html"
    for page in range(MAX_PAGE):
        # 构造请求参数（通过浏览器抓包获取最新参数）
        params = {
            "goods_id": GOODS_ID,
            "page": page,
            "size": 10,  # 每页评论数（最大10）
            "type": 3,  # 评论类型（3=全部评论，1=好评，2=中评，3=差评）
            "sort": 1,  # 排序方式（1=按时间倒序，2=按时间正序）
        }
        url = f"{base_url}?{urlencode(params)}"

        try:
            response = requests.get(url, headers=headers, timeout=15)
            if response.status_code == 200:
                json_data = response.json()
                comments = json_data.get("data", {}).get("comments", [])

                if not comments:
                    print(f"第 {page + 1} 页无评论，可能已爬完所有数据")
                    break

                save_comment_to_txt(comments, page)
                time.sleep(SLEEP_TIME)  # 控制请求频率
            else:
                print(f"请求失败，状态码：{response.status_code}")
        except Exception as e:
            print(f"爬取第 {page + 1} 页时出错：{str(e)}")


if __name__ == "__main__":
    print("开始爬取拼多多华硕天选笔记本评论...")
    crawl_pdd_comments()
    print("所有评论已保存至 pdd_comments.txt")