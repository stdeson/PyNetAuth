import time
import urllib.request
import wmi
import platform
import hmac
import json
import random
import ssl

qss_style = """
    * {
        font-size: 12px;
        font-family: "Microsoft YaHei";
    }
    QTableView {
        selection-color: #000000;
	    selection-background-color: #c4e1d2; 
    }
    QTableView::item:hover	{	
	    background-color: #a1b1c9;		
    }
"""

cur_time_stamp = time.time()
cur_time_format = time.strftime("%Y-%m-%d %H:%M:%S")

server_ip = "127.0.0.1"
server_port = 47123

card_key_lenth = 30

# 随机数
def rnd(min: int, max: int):
    return random.randint(min, max)

# 获取外网IP
def get_outer_ip() -> str:
    # ip = urllib.request.urlopen("http://ip.42.pl/raw").read().decode()  # 法一
    req = urllib.request.urlopen("http://httpbin.org/ip")
    ip = json.load(req)["origin"]  # 法二
    print("ip:", ip)
    return ip

# 获取IP归属地
def get_ip_location(ip: str) -> str:
    appcode = "3799d32779864269b80bd92e70619498"
    url = f"https://hcapi20.market.alicloudapi.com/ip?ip={ip}"
    request = urllib.request.Request(url)
    request.add_header("Authorization", "APPCODE " + appcode)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    response = urllib.request.urlopen(request, context=ctx)
    content = response.read().decode()  # 返回json字符串
    if not content:
        return ""
    ret_dict = json.loads(content)  # json字符串 转 py字典
    if ret_dict["msg"] != "success":
        return ""
    data = ret_dict["data"]
    country, region, city, isp = data["country"], data["region"], data["city"], data["isp"]
    location = f"{country}-{region}-{city}-{isp}"
    print("location:", location)
    return location

# 获取机器码(主板序列号+硬盘序列号)
def get_machine_code():
    c = wmi.WMI()
    try:
        board_serial = c.Win32_BaseBoard()[0].SerialNumber
        disk_serial = c.Win32_DiskDrive()[0].SerialNumber
        disk_serial = disk_serial.strip(".").replace("_", "")
        machine_code = board_serial + disk_serial
        machine_code = machine_code[12:]+machine_code[:12]
        machine_code = machine_code[::-1]
    except:
        machine_code = ""
    print("机器码:", machine_code)
    return machine_code

# 获取操作系统
def get_operation_system():
    return platform.platform()

# 获取加密后字符
def get_encrypted_str(ori_bytes: bytes):
    encrypted = hmac.new(b"dkstFeb.1st", ori_bytes, "sha1")
    return encrypted.hexdigest()

# 生成随机卡密
def gen_rnd_card_key(lenth=card_key_lenth):
    char_list = "0123456789qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP"
    max_idx = len(char_list) - 1
    card_key = ""
    for _ in range(lenth):
        idx = rnd(0, max_idx)
        char = char_list[idx]
        card_key += char
    return card_key

if __name__ == '__main__':
    ip = get_outer_ip()
    get_ip_location(ip)