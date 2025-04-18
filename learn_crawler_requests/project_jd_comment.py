import requests
import json
import time
from urllib.parse import urlencode

# ====================== 配置参数 ======================
PRODUCT_ID = "100063434183"  # 华硕天选5 2024款商品ID（需替换为目标商品ID）
MAX_PAGE = 100  # 最大爬取页数（每页约10条评论，根据实际需求调整）
SLEEP_TIME = 3  # 每次请求间隔（秒），避免被反爬

# ====================== 请求头（模拟浏览器） ======================
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": f"https://item.jd.com/{PRODUCT_ID}.html",
    "Connection": "keep-alive",
    "Cookie": "your_cookie_here",  # 可选：如需登录状态可填入Cookie
}


# ====================== 评论保存函数 ======================
def save_comment_to_txt(comments, page):
    with open("jd_comments.txt", "a", encoding="utf-8") as f:
        f.write(f"==================== 第 {page + 1} 页评论 ====================\n")
        for comment in comments:
            # 提取关键信息
            content = comment["content"].strip()  # 评论内容
            score = comment["score"]  # 评分（1-5分，0表示未评分）
            creation_time = comment["creationTime"]  # 评论时间
            product_color = comment.get("productColor", "未提及")  # 购买颜色
            product_size = comment.get("productSize", "未提及")  # 配置规格（如内存/硬盘）

            f.write(f"【评分】{'★' * score if score != 0 else '未评分'}\n")
            f.write(f"【时间】{creation_time}\n")
            f.write(f"【配置】{product_size}\n")
            f.write(f"【颜色】{product_color}\n")
            f.write(f"【内容】{content}\n")
            f.write("-" * 50 + "\n")
        print(f"第 {page + 1} 页评论保存成功")


# ====================== 主爬取逻辑 ======================
def crawl_jd_comments():
    base_url = "https://club.jd.com/comment/productPageComments.action"
    for page in range(MAX_PAGE):
        # 构造请求参数
        params = {
            "sku": PRODUCT_ID,
            "page": page,
            "pageSize": 10,
            "sortType": 5,  # 排序方式（5=按时间倒序）
            "score": 0,  # 0=全部评分，1=好评，2=中评，3=差评
            "callback": "fetchJSON_comment98"  # 可选：京东接口的回调函数名
        }
        url = f"{base_url}?{urlencode(params)}"

        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                # 处理京东的JSONP响应（去除回调函数前缀）
                data = response.text[len("fetchJSON_comment98("):-2]
                json_data = json.loads(data)
                comments = json_data.get("comments", [])

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
    print("开始爬取京东华硕天选笔记本评论...")
    crawl_jd_comments()
    print("所有评论已保存至 jd_comments.txt")