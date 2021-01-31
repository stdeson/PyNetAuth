import sys
import time, datetime
import json

from PySide2.QtGui import QIcon, QCloseEvent
from PySide2.QtWidgets import QApplication, QStyleFactory, QMainWindow, \
    QLabel, QMessageBox, QAbstractItemView, QTableWidget, QTableWidgetItem
from PySide2.QtCore import Qt, QTimer
import pymysql
import socket
from threading import Thread

from ui.wnd_server import Ui_WndServer
from res import qres
import mf

class WndServer(QMainWindow, Ui_WndServer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_status_bar()
        self.init_timer()
        self.init_all_controls()
        self.init_all_sig_slot()
        self.move(0, 160)
        self.show_info("窗口初始化成功")

    def closeEvent(self, event: QCloseEvent):
        tcp_socket.close()
        cursor.close()
        db.close()

    def init_status_bar(self):
        self.lbe_info = QLabel()
        self.status_bar.addWidget(self.lbe_info)

    def init_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timer_timeout)
        self.timer.start(1000)

    def init_all_controls(self):
        # 显示第一页
        self.stack_widget.setCurrentIndex(0)
        # 工具栏设置图标
        self.tool_bar.addAction(QIcon(":/users.png"), "全部用户")
        self.tool_bar.addAction(QIcon(":/user.png"), "在线用户")
        self.tool_bar.addAction(QIcon(":/card.png"), "卡密管理")
        self.tool_bar.addAction(QIcon(":/log.png"), "执行日志")
        # 所有表头可视化
        self.tbe_all_user.horizontalHeader().setVisible(True)
        self.tbe_online_user.horizontalHeader().setVisible(True)
        self.tbe_card_manage.horizontalHeader().setVisible(True)
        # 所有表格设置不可编辑
        # self.tbe_all_user.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tbe_online_user.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tbe_card_manage.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 全部用户表
        account, pwd, email, machine_code, reg_ip, reg_time, due_time, is_forbid = [i for i in range(8)]
        self.tbe_all_user.setColumnWidth(account, 100)
        self.tbe_all_user.setColumnWidth(pwd, 100)
        self.tbe_all_user.setColumnWidth(email, 100)
        self.tbe_all_user.setColumnWidth(machine_code, 90)
        self.tbe_all_user.setColumnWidth(reg_ip, 100)
        self.tbe_all_user.setColumnWidth(reg_time, 120)
        self.tbe_all_user.setColumnWidth(due_time, 120)
        self.tbe_all_user.setColumnWidth(is_forbid, 70)
        # 卡密管理表
        card_key, state, type, gen_time, use_time = [i for i in range(5)]
        self.tbe_card_manage.setColumnWidth(card_key, 340)
        self.tbe_card_manage.setColumnWidth(state, 80)
        self.tbe_card_manage.setColumnWidth(type, 80)
        self.tbe_card_manage.setColumnWidth(gen_time, 150)
        self.tbe_card_manage.setColumnWidth(use_time, 150)

    def init_all_sig_slot(self):
        self.tool_bar.actionTriggered.connect(self.on_tool_bar_actionTriggered)
        self.btn_card_gen.clicked.connect(self.on_btn_card_gen_clicked)
        self.btn_card_refresh.clicked.connect(self.on_btn_card_refresh_clicked)

    def show_info(self, text):
        self.lbe_info.setText(f"<提示> : {text}")
        self.tbr_log.append(f"{mf.cur_time_format}  {text}")
        print(text)

    def on_tool_bar_actionTriggered(self, action):
        action_name = action.text()
        self.show_info(f"切换到 {action_name}")
        if action_name == "全部用户":
            self.stack_widget.setCurrentIndex(0)
        elif action_name == "在线用户":
            self.stack_widget.setCurrentIndex(1)
        elif action_name == "卡密管理":
            self.stack_widget.setCurrentIndex(2)
        elif action_name == "执行日志":
            self.stack_widget.setCurrentIndex(3)

    def on_btn_card_gen_clicked(self):
        gen_time = mf.cur_time_format
        card_type = self.cmb_card_type.currentText()
        card_num = int(self.edt_card_num.text())
        for i in range(card_num):
            card_key = mf.gen_rnd_card_key()
            val_dict = {
                "card_key": card_key,
                "card_type": card_type,
                "gen_time": gen_time
            }
            sql_table_insert("card_manage", val_dict)
        self.show_info(f"已生成{card_num}张{card_type}")

    def on_btn_card_refresh_clicked(self):
        tbe = self.tbe_card_manage
        dict_list = sql_table_query("card_manage")
        tbe.setRowCount(len(dict_list))
        for row, info_dict in enumerate(dict_list):
            card_key = QTableWidgetItem(info_dict["card_key"])
            card_type = QTableWidgetItem(info_dict["card_type"])
            card_state = QTableWidgetItem(info_dict["card_state"])
            gen_time = QTableWidgetItem(info_dict["gen_time"])
            use_time = QTableWidgetItem(info_dict["use_time"])
            self.tbe_card_manage.setItem(row, 0, card_key)
            self.tbe_card_manage.setItem(row, 1, card_type)
            self.tbe_card_manage.setItem(row, 2, card_state)
            self.tbe_card_manage.setItem(row, 3, gen_time)
            self.tbe_card_manage.setItem(row, 4, use_time)


    def on_timer_timeout(self):
        mf.cur_time_stamp += 1
        mf.cur_time_format = time.strftime("%Y-%m-%d %H:%M:%S")


def thd_accept_client():
    wnd_server.show_info("服务器已开启, 准备接受客户请求...")
    while True:
        wnd_server.show_info("正在等待客户端发出连接请求...")
        try:
            client_socket, client_addr = tcp_socket.accept()
        except:
            break
        wnd_server.show_info(f"客户端IP地址及端口: {client_addr}, 已分配客服套接字")
        Thread(target=thd_serve_client, args=(client_socket, client_addr), daemon=True).start()
    wnd_server.show_info("服务端已关闭, 停止接受客户端请求...")


def thd_serve_client(client_socket: socket.socket, client_addr: tuple):
    while True:
        wnd_server.show_info("等待客户端发出消息中...")
        try:  # 若任务消息都没收到, 客户端直接退出, 会抛出异常
            recv_bytes = client_socket.recv(1024)
        except:
            recv_bytes = ""
        if not recv_bytes:  # 若客户端退出,会收到一个空str
            break
        # json字符串 转 py字典
        json_str = recv_bytes.decode()
        client_info_dict = json.loads(json_str)
        wnd_server.show_info(f"收到客户端的消息: {client_info_dict}")
        # 服务端消息处理
        msg_type = client_info_dict["msg_type"]
        client_info_dict.pop("msg_type")
        msg_func_dict = {
            "reg": deal_reg,
            "login": deal_login,
            "pay": deal_pay,
        }
        func = msg_func_dict.get(msg_type)
        if func is None:
            wnd_server.show_info(f"消息类型不存在: {msg_type}")
        else:
            func(client_socket, client_info_dict)
    wnd_server.show_info(f"客户端{client_addr}已断开连接, 服务结束")
    client_socket.close()


# 处理-注册
def deal_reg(client_socket: socket.socket, client_info_dict: dict):
    account = client_info_dict["account"]
    # 查询账号是否存在, 不存在则插入记录
    if sql_table_query("all_user", {"account": account}):  # 若查到数据
        reg_ret = False
        detail = f"失败, 账号{account}已被注册!"
        wnd_server.show_info(detail)
    else:  # 表插入记录
        client_info_dict["reg_time"] = mf.cur_time_format
        reg_ret = sql_table_insert("all_user", client_info_dict)
        detail = f"账号{account}注册成功!" if reg_ret else f"账号{account}注册失败!"
        wnd_server.show_info(detail)
    # 把注册结果整理成py字典, 并发送给客户端
    server_info_dict = {"msg_type": "reg", "reg_ret": reg_ret, "detail": detail}
    send_to_client(client_socket, server_info_dict)

# 处理-登录
def deal_login(client_socket: socket.socket, client_info_dict: dict):
    account = client_info_dict["account"]
    pwd = client_info_dict["pwd"]
    # 查询账号记录
    dict_list = sql_table_query("all_user", {"account": account})
    if dict_list:  # 若查到数据
        query_pwd = dict_list[0].get("pwd")
        login_ret = True if pwd == query_pwd else False
        detail = f"账号{account}登录成功!" if login_ret else f"账号{account}登录失败!"
    else:  # 没查到数据
        login_ret = False
        detail = f"账号{account}登录失败!"
    # 把登录结果整理成py字典, 并发送给客户端
    server_info_dict = {"msg_type": "login", "login_ret": login_ret, "detail": detail}
    send_to_client(client_socket, server_info_dict)

# 处理-充值
def deal_pay(client_socket: socket.socket, client_info_dict: dict):
    account = client_info_dict["account"]
    card_key = client_info_dict["card_key"]
    # 查询数据库, 判断卡密是否存在
    dict_list = sql_table_query("card_manage", {"card_key": card_key})
    pay_ret = False
    if dict_list:
        card_info = dict_list[0]
        if card_info["use_time"] == "":  # 卡密未被使用
            user_info_list = sql_table_query("all_user", {"account": account})  # 查找账号是否存在
            if user_info_list:  # 账号存在
                user_info = user_info_list[0]
                # 更新卡密的使用时间
                sql_table_update("card_manage", {"use_time": mf.cur_time_format}, {"card_key": card_key})
                # 更新账号到期时间
                type_time_dict = {"天卡": 1, "周卡": 7, "月卡": 30, "季卡": 120, "年卡": 365, "永久卡": 3650}
                card_type = card_info["card_type"]
                delta_day = type_time_dict[card_type]
                pay_ret = update_user_due_time(user_info, delta_day)
                detail = "充值成功" if pay_ret else "充值失败"
            else:
                detail = "失败, 账号不存在"
        else:  # 卡密被使用
            detail = "失败, 此卡密已被使用"
    else:  # 没查到数据
        detail = "失败, 卡密不存在"
    # 把登录结果整理成py字典, 并发送给客户端
    server_info_dict = {"msg_type": "pay", "pay_ret": pay_ret, "detail": detail}
    send_to_client(client_socket, server_info_dict)

# 发送数据给客户端
def send_to_client(client_socket: socket.socket, server_info_dict: dict):
    # py字典 转 json字符串
    json_str = json.dumps(server_info_dict, ensure_ascii=False)
    # 向客户端回复注册结果
    try:
        client_socket.send(json_str.encode())
        wnd_server.show_info("向客户端回复成功")
    except Exception as e:
        wnd_server.show_info(f"向客户端回复失败: {e}")

# 更新用户到期时间
def update_user_due_time(user_info: dict, delta_day: int):
    if user_info["due_time"] == "" or user_info["due_time"] < mf.cur_time_format:
        # 若所有用户表中此项记录没有到期时间, 或到期时间在今天以前, 则从当前时间开始加
        ori_time = mf.cur_time_format
    else:  # 否则, 取记录上的到期时间
        ori_time = user_info["due_time"]
    now_date_time = datetime.datetime.strptime(ori_time, "%Y-%m-%d %H:%M:%S")
    offset_date_time = datetime.timedelta(days=delta_day)
    due_time = (now_date_time + offset_date_time).strftime("%Y-%m-%d %H:%M:%S")
    account = user_info["account"]
    ret = sql_table_update("all_user", {"due_time": due_time}, {"account": account})
    return ret

# 表-插入, 成功返回True, 否则返回False
def sql_table_insert(table_name: str, val_dict: dict):
    # keys = "account, pwd,qq, machine_code, reg_ip"
    keys = ", ".join(val_dict.keys())
    vals = tuple(val_dict.values())
    # occupys = "%s, %s, %s, %s, %s, %s"
    occupys = ", ".join(["%s"] * len(val_dict))
    # 准备SQL语句
    sql = f"insert {table_name}({keys}) values({occupys});"
    ret = False
    try:
        ret = cursor.execute(sql, vals)  # 执行SQL语句
        db.commit()  # 提交到数据库
    except Exception as e:
        print(f"表插入异常: {e}")
        db.rollback()  # 数据库回滚
    print(f"表插入结果: {ret}")
    return ret

# 表-查询, 成功返回字典列表, 否则返回空列表
def sql_table_query(table_name: str, condition_dict=dict()):
    fields = condition_dict.keys()
    vals = tuple(condition_dict.values())
    condition = [f"{field}=%s" for field in fields]
    condition = " and ".join(condition)
    # 准备SQL语句, %s是SQL语句的参数占位符, 防止注入
    if condition:
        sql = f"select * from {table_name} where {condition};"
    else:
        sql = f"select * from {table_name};"
    try:
        ret = cursor.execute(sql, vals)  # 执行SQL语句
        ret = cursor.fetchall()  # 获取查询结果, 没查到返回空列表
        db.commit()  # 提交到数据库
    except:
        db.rollback()  # 数据库回滚
        ret = []
    print(f"表查询结果: {ret}")
    return ret

# 表-更新, 成功返回True, 否则返回False
def sql_table_update(table_name: str, update_dict: dict, condition_dict=dict()):
    update_fields = update_dict.keys()
    update_vals = tuple(update_dict.values())
    update = [f"{field}=%s" for field in update_fields]
    update = ", ".join(update)

    condition_fields = condition_dict.keys()
    condition_vals = tuple(condition_dict.values())
    condition = [f"{field}=%s" for field in condition_fields]
    condition = " and ".join(condition)
    # 准备SQL语句, %s是SQL语句的参数占位符, 防止注入
    if condition:
        sql = f"update {table_name} set {update} where {condition};"
    else:
        sql = f"update {table_name} set {update};"
    ret = False
    try:
        ret = cursor.execute(sql, update_vals + condition_vals)  # 执行SQL语句
        db.commit()  # 提交到数据库
    except Exception as e:
        print(f"表更新异常: {e}")
        db.rollback()  # 数据库回滚
    print(f"表更新结果: {ret}")
    return ret


if __name__ == '__main__':
    # 界面随DPI自动缩放
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    # 应用程序
    app = QApplication()
    app.setStyle(QStyleFactory.create("fusion"))
    app.setStyleSheet(mf.qss_style)
    # 窗口
    wnd_server = WndServer()
    wnd_server.show()
    # 初始化mysql
    try:
        # 创建数据库对象
        db = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="mysql",
            database="network_auth"
        )
        # 创建游标对象, 指定返回一个字典列表, 获取的每条数据的类型为字典(默认是元组)
        cursor = db.cursor(pymysql.cursors.DictCursor)
        wnd_server.show_info("连接数据库成功")
    except Exception as e:
        QMessageBox.critical(wnd_server, "错误", f"mysql连接失败: {e}")
        sys.exit(-1)
    # 初始化tcp连接
    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.bind((mf.server_ip, mf.server_port))  # 主机号+端口号
        tcp_socket.listen(128)  # 允许同时有XX个客户端连接此服务器, 排队等待被服务
        Thread(target=thd_accept_client, daemon=True).start()
    except Exception as e:
        QMessageBox.critical(wnd_server, "错误", f"tcp连接失败: {e}")
        sys.exit(-1)
    # 消息循环
    sys.exit(app.exec_())
