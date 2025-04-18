import requests
import json
import time
from urllib.parse import urlencode

# ====================== 配置参数 ======================
ITEM_ID = "757658547929"  # 华硕天选商品ID（需从商品URL中获取）
MAX_PAGE = 10  # 最大爬取页数（每页约20条评论，根据实际调整）
SLEEP_TIME = 5  # 每次请求间隔（秒），避免被反爬

# ====================== 请求头（需填入有效Cookie） ======================
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": f"https://detail.tmall.com/item.htm?id={ITEM_ID}",
    "Connection": "keep-alive",
    "Cookie": "enc=icmCcJRFhtsiPzeCW0tl1qzrMGS%2FbLvW%2F8ozdWIpth2lhe3XoaqZdH22FcMG1KhqGwCBg%2FdGrhX5t03Kv6nyDg%3D%3D; xlly_s=1; lid=tb22014977; _l_g_=Ug%3D%3D; lgc=tb22014977; cookie1=AVxBWocnDpbrvnTpdVrt%2F9sx%2B%2Fs3SII%2BEHVyOMNjH8Y%3D; login=true; cookie2=1ff0470e0e4ed92d4f37e2d102109bcf; cancelledSubSites=empty; sg=790; sn=; _tb_token_=7d156baa04343; wk_unb=UNk%2FTdmFn0HJMQ%3D%3D; dnk=tb22014977; uc1=cookie14=UoYaj4GL1qrm%2Fg%3D%3D&existShop=false&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&cookie15=URm48syIIVrSKA%3D%3D&pas=0&cookie21=WqG3DMC9FxUx; uc3=vt3=F8dD2EuKwbiIR1dWeys%3D&id2=UNk%2FTdmFn0HJMQ%3D%3D&lg2=UIHiLt3xD8xYTw%3D%3D&nk2=F5RHo3vN8chjXA%3D%3D; tracknick=tb22014977; havana_lgc_exp=1744976167824; uc4=nk4=0%40FY4MsTFUSAo891Hck3PylPqn%2F2La&id4=0%40Ug41TPXAgnk54oAkf%2FatOaGSzmYE; unb=3985244159; wk_cookie2=11abfce84e7ff84c2c7728babd879ac6; cookie17=UNk%2FTdmFn0HJMQ%3D%3D; _nk_=tb22014977; sgcookie=E100z1maGgcPJQbCdmrPcgnk6QORW0RhqeVc32ZZkz7LI9GW6dBRgVVIlctUh4gLEa2CLMWBm3P23OeDhvxTWVn%2BpOLmXlXVtNGlqBJr5mftrf4%3D; t=f54f1f99b7b930ba1636dd70cf282533; csg=63ee663f; isg=BBISyShCrqzHP9LQs0mWvfOVY9j0Ixa9xn7ou9xrPkWw77LpxLNmzRgMX0tTn45V; mtop_partitioned_detect=1; _m_h5_tk=cc35df66f7f743fff420177b571997a9_1744953759374; _m_h5_tk_enc=4030fdaca7fa347d6aeb4984a5be524b; cna=362IIMXiXGEBASQOBCjl+6/s; havana_sdkSilent=1745031521818; tfstk=g30ZLNt6qFLNrc2Tj2aV4mFdhCUTqrJW_qwbijc01R2MHCF0uAM3mZG6XIR4Lxe_fPm_iZkQdx_j1qodubhx5CUX6PhTkrvWFUgq6fUAgDt4DVzhKSc3sGVMAyYmGKXHFUTSshVTlXvSlHGJLJN0o5qcS6AUi5fgooVitBP0GOjcSxAeTSN0s520jW43w540nxqMTk2LgrVinrcyLoqP8SEMGW1MtIX5FkyosJ7cz_FgjQhCcabkw5ZTEkVdokgU_lyos47qOnFnR2r7As9Q-bnIIWzy7TFZxbzggqdl0-rqWyyEUUbY9cDZ-ouBMUlL7Sruok5coXzsxYugrUXU9DcsmVHNgZVt54Z4ekRckoanPumoQsd-tPVmHu3XeNeiib3-Vz8Ne5onaySy0tFHoa0xbtj4jWFUFBRE3C1sUS4WHksADl6LT8OMsiIYjWFUFBRFDiE62WyWsCf.."}


# ====================== 评论保存函数 ======================
def save_comment_to_txt(comments, page):
    with open("taobao_comments.txt", "a", encoding="utf-8") as f:
        f.write(f"==================== 第 {page + 1} 页评论 ====================\n")
        for comment in comments:
            content = comment["rateContent"].strip() if "rateContent" in comment else "无评论内容"  # 评论内容
            score = comment["rateLevel"]  # 评分（5=好评，3=中评，1=差评）
            time_str = comment["rateTime"]  # 评论时间
            user_level = comment.get("userLevelInfo", {}).get("userLevel", "未提及")  # 用户等级
            product_spec = comment.get("auctionSku", "未提及")  # 购买的配置规格（如内存/硬盘）

            f.write(f"【评分】{'★' * score if score != 0 else '未评分'}\n")
            f.write(f"【时间】{time_str}\n")
            f.write(f"【配置】{product_spec}\n")
            f.write(f"【用户等级】{user_level}\n")
            f.write(f"【内容】{content}\n")
            f.write("-" * 50 + "\n")
        print(f"第 {page + 1} 页评论保存成功")


# ====================== 主爬取逻辑 ======================
def crawl_taobao_comments():
    base_url = "https://rate.tmall.com/list_detail_rate.htm"
    for page in range(MAX_PAGE):
        # 构造请求参数（通过浏览器抓包获取最新参数）
        params = {
            "itemId": ITEM_ID,  # 商品ID
            "spuId": ITEM_ID,  # SPU ID（通常与itemId相同）
            "sellerId": "3421709570",  # 卖家ID（需从商品页获取，可能需要替换）
            "order": "3",  # 排序方式（3=按时间倒序，2=按评分排序）
            "currentPage": page + 1,  # 页码（从1开始）
            "append": "0",
            "content": "1",
            "tag": "0",
            "groupId": "0",
            "callback": "jsonp1",  # 回调函数名（可能随版本变化）
        }
        url = f"{base_url}?{urlencode(params)}"

        try:
            response = requests.get(url, headers=headers, timeout=15)
            if response.status_code == 200:
                # 处理JSONP响应（去除回调函数前缀）
                data = response.text[len("jsonp1("):-1]
                json_data = json.loads(data)
                comments = json_data.get("rateList", {}).get("rateDetail", [])

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
    print("开始爬取淘宝/天猫华硕天选笔记本评论...")
    print("注意：请先填入有效的Cookie（登录后获取），否则可能无法获取数据！")
    crawl_taobao_comments()
    print("所有评论已保存至 taobao_comments.txt")