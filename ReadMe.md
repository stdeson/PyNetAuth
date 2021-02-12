
# 更新公告

1.4.9
- 优化 aes算法


1.4.8
- 优化 通过base85对json字串进行编码后收发


1.4.7
- 添加 自定义数据添加按钮点击事件


1.4.6
- 添加 客户处理接收初始消息, RSA解密覆盖原来的aes密钥


1.4.5
- 优化 客户端发送消息时des加密
- 优化 服务端接收消息时des解密


1.4.4
- 优化 服务端处理回复初始消息前des加密
- 优化 客户端接收消息时des解密
- 优化 服务端添加到日志时加上互斥锁


1.4.3
- 添加 服务端和客户端添加des密钥


1.4.2
- 添加 服务端处理初始消息


1.4.1
- 添加 客户端登录窗口初始化时发送初始类型消息给服务端


1.4.0
- 优化 由服务端发送唯一通信密钥给所有的客户端


1.3.9
- 优化 通信密钥发送前先通过RSA加密


1.3.8
- 优化 客户端导入加密模块时随机生成通信密钥, 发给服务端


1.3.7
- 添加 对称加密相关算法


1.3.6
- 优化 客户端用两个变量分别存放客户端的公钥和私钥, 再用一个变量存放服务端的公钥
- 优化 服务端用两个变量分别存放服务端的公钥和私钥, 再用一个变量存放客户端的公钥


1.3.5
- 优化 客户端和服务端拆分为两个文件夹
- 优化 服务端记录日志时添加事件类型


1.3.4
- 添加 my_crypto模块
- 添加 RSA相关算法


1.3.3
- 优化 服务端右键菜单, 选中用户添加备注


1.3.2
- 添加 客户端一个记录上次心跳时间的变量
- 优化 若上次心跳时间大于15分钟就退出


1.3.1
- 修复 客户端心跳5次就自己退出, 不管是否成功


1.3.0
- 优化 服务端处理客户端消息时, 若发现账号不存在之类的异常获取IP
- 优化 向客户端回复时把客户端的ip和端口记录到日志


1.2.9
- 优化 客户端若心跳未收到服务端响应, 则每隔10秒发一个, 连发5个无响应就退出


1.2.8
- 修复 选中一个时列表转元组会多一个逗号导致异常
- 优化 删除选中卡号代码
- 优化 导出选中代码


1.2.7
- 添加 右键菜单_设置用户状态: 在线, 离线, 冻结


1.2.6
- 优化 把销售时间改为导出时间


1.2.5
- 优化 点击项目表项显示右侧内容
- 优化 点击项目表右侧确定按钮修改表格内容


1.2.4
- 优化 服务端项目表添加表头


1.2.3
- 添加 服务端项目允许登录, 允许注册, 允许解绑


1.2.2
- 添加 每日流水页


1.2.1
- 优化 服务端处理登录即绑定


1.2.0
- 添加 服务端项目_每日免费解绑次数
- 添加 服务端项目_解绑扣除小时数
- 添加 最后修改时间


1.1.9
- 优化 sql_table_系列函数 统一返回整型
- 优化 sql_table_系列函数的结果不要记录到日志, 用print


1.1.8
- 优化 接受登录窗口通过发信号的方式完成
- 优化 3分钟未操作自动关闭登录界面


1.1.7
- 优化 获取外部IP两个途径同时获取


1.1.6
- 修复 客户端登录卡死
- 优化 客户端开一个线程来代替定时器


1.1.5
- 修复 今日登录次数不显示


1.1.4
- 修复 服务端处理登录异常


1.1.3
- 添加 服务端右键菜单用户_续费全部用户


1.1.2
- 添加 服务端右键菜单用户_续费选中用户


1.1.1
- 优化 处理充值时先查账号, 再查卡密


1.1.0
- 修复 充值时只是从到期时间加时间的bug
- 修复 充值时会把所有用户的账号一起充值的bug


1.0.9
- 修复 批量续费时不加已到期用户时间


1.0.8
- 添加 服务端右键菜单用户_解冻选中用户


1.0.7
- 添加 服务端右键菜单用户_冻结选中用户


1.0.6
- 优化 服务端窗口初始化时读取数据库内容到表格


1.0.5
- 添加 服务端右键菜单卡密_删除选中卡密


1.0.4
- 添加 服务端右键菜单卡密_批量导出销售


1.0.3
- 优化 服务端界面


1.0.2
- 完善 删除已使用卡密


1.0.1
- 修复 充值显示卡密已使用


1.0.0
- 添加 卡密管理右键菜单信号槽


0.9.9
- 添加 卡密管理右键菜单


0.9.8
- 添加 卡密管理表, 销售时间


0.9.7
- 优化 卡密管理时间格式换为datetime


0.9.6
- 修复 全部用户显示异常bug


0.9.5
- 删除 服务端 更新用户到期时间函数, 改为调用sql表更新函数


0.9.4
- 添加 批量续费按钮点击事件


0.9.3
- 完善 服务端按钮查询按钮点击事件
- 优化 用户表格列宽


0.9.2
- 优化 服务端控件改名


0.9.1
- 添加 服务端用户管理表添加右键菜单


0.9.0
- 添加 服务端按钮查询按钮点击事件


0.8.9
- 优化 服务端用户管理界面


0.8.8
- 添加 客户端接收改密处理结果


0.8.7
- 添加 服务端处理改密事件


0.8.6
- 添加 客户端改密按钮点击事件
- 添加 获取外网IP异常处理


0.8.5
- 添加 客户端登录界面公告页


0.8.4
- 优化 客户端登录界面5分钟后自动关闭


0.8.3
- 优化 服务端状态为在线不允许登录
- 优化 服务端处理 解绑时若用户状态是在线或冻结, 则不允许解绑


0.8.2
- 优化 项目管理表右键菜单添加刷新


0.8.1
- 添加 sql表删除函数


0.8.0
- 优化 每隔15分钟设置心跳时间间隔久的在线用户状态为离线 


0.7.9
- 添加 项目管理表右键菜单


0.7.8
- 优化 按钮点击消息提示


0.7.7
- 添加 项目管理表点击表项在右侧设置该行信息到编辑框


0.7.6
- 添加 刷新项目管理表按钮点击事件


0.7.5
- 添加 项目管理表点击按钮事件


0.7.4
- 优化 4个表结构新增ID作为主键
- 优化 调整表格列宽


0.7.3
- 优化 服务端新增一个15分钟的定时器


0.7.2
- 修复 客户端点击登录按钮时鼠标移动就会重绘导致无响应


0.7.1
- 优化 服务端接收到心跳包设置用户状态为在线


0.7.0
- 优化 客户端主窗口显示后再开启心跳线程
- 优化 登录时不再设置用户状态


0.6.9
- 优化 服务端处理解绑时更新今日解绑次数


0.6.8
- 添加 解绑按钮点击事件
- 添加 服务端处理解绑消息


0.6.7
- 优化 客户端获取全局变量


0.6.6
- 修复 服务端刷新卡密库不显示


0.6.5
- 修复 客户端登录按钮点击后卡死
- 优化 不再从客户端获取IP归属地, 而是由服务端获取


0.6.4
- 优化 处理客户端消息状态添加到日志


0.6.3
- 优化 客户端退出后向服务端发出下线消息
- 优化 服务端收到后更新用户状态为离线


0.6.2
- 优化 服务端同意客户端登录后更新用户状态


0.6.1
- 优化 服务端 初始化数据库 和 tcp连接


0.6.0
- 优化 每天0点数据库某些记录清为空字符串


0.5.9
- 修复 服务端点击日志不更新


0.5.8
- 优化 服务端显示信息时添加到日志文件中
- 实现 一天换一个日志文件


0.5.7
- 优化 服务器窗口程序集 不导入mf


0.5.6
- 修复 客户端主界面改为QMainWindow


0.5.5
- 优化 服务端项目管理界面


0.5.4
- 优化 服务端窗口设为不可调整大小


0.5.3
- 修复 发送数据给服务端 函数 放到实例方法中


0.5.2
- 优化 注册时更新到期时间
- 优化 客户端心跳recv设置一个超时时间


0.5.1
- 优化 登录判定流程


0.5.0
- 添加 服务端处理心跳消息
- 优化 客户端登录发送数据


0.4.9
- 添加 客户端主界面添加 心跳线程


0.4.8
- 修复 tbr改为prefered避免随内容改变界面宽度
- 修复 客户端接收服务端消息的线程启动应放到登录界面初始化中


0.4.7
- 优化 服务端收到登录消息后记录到服务器


0.4.6
- 优化 注册时不记录机器码
- 优化 客户端登录时发送机器码, 上次登录时间, 上次登录IP, 上次登录地, 备注


0.4.5
- 修复 卡密制卡时间不显示


0.4.4
- 优化 服务端界面


0.4.3
- 添加 线程_获取服务端自定义数据
- 优化 替换数据表名称


0.4.2
- 优化 注册时qq不要加密
- 添加 客户端处理充值返回消息


0.4.1
- 完善 服务端处理充值类型消息
- 优化 使用datetime来增加时间


0.4.0
- 添加 服务端处理充值类型消息
- 优化 表查询算法
- 添加 表更新算法


0.3.9
- 完善 充值按钮点击事件


0.3.8
- 添加 充值按钮点击事件
- 优化 为充值卡号标签添加超链接


0.3.7
- 修复 设置表格项文本不显示的问题
- 修复 再刷新卡密库时会追加显示


0.3.6
- 添加 按钮刷新卡密库点击事件
- 优化 表查询算法


0.3.5
- 添加 生成随机卡密函数
- 添加 按钮生成卡密点击事件


0.3.4
- 优化 客户端登录窗口圆角效果


0.3.3
- 新增 解绑按钮
- 修复 起始点应为QPoint类型
- 优化 界面


0.3.2
- 修复 登录成功不显示主界面


0.3.1
- 优化 获取外网IP方法
- 优化 新开一个线程去获取公网IP, 避免阻塞界面


0.3.0
- 修复 客户端登录窗口无法拖动
- 优化 使用添加窗口背景的第二种方法
- 优化 添加退出按钮
- 修复 退出按钮点击后由于接收线程还在运行导致无法退出


0.2.9
- 优化 添加窗口背景


0.2.8
- 修复 客户端窗口类改为QDialog


0.2.7
- 添加 客户端登录成功关闭登录窗口, 显示软件主界面
- 优化 窗口程序集统一移到项目根目录
- 修复 服务端向客户端发数据失败的问题


0.2.6
- 添加 服务端接收登录消息处理
- 添加 客户端接收登录响应处理


0.2.5
- 添加 客户端登录按钮点击事件编写


0.2.4
- 优化 对注册密码和qq进行非对称加密后再发送给服务器


0.2.3
- 添加 客户端对注册结果处理


0.2.2
- 添加 服务器返回注册结果给客户端


0.2.1
- 优化 机器码=主板序列号+硬盘序列号, 再把从12:移到前面, :12移到后面, 再倒序排列
- 修复 注册插入到数据库失败的bug


0.2.0
- 完善 服务器收到"注册"类型的消息时, 把注册信息插入到数据库
- 添加 表-插入函数


0.1.9
- 优化 机器码=主板序列号+硬盘序列号+bios序列号


0.1.8
- 优化 表查询时异常则回滚
- 完善 服务端接收数据
- 修复 客户端先转为字节型再发送数据


0.1.7
- 添加 客户端注册按钮点击事件


0.1.6
- 优化 客户端控件名
- 优化 客户端界面


0.1.5
- 测试 服务端 数据库查询 
- 添加 客户端 发送数据时异常处理
- 优化 两窗口设置不同初始位置


0.1.4
- 优化 服务端套接字, 游标, 连接对象改全局变量


0.1.3
- 优化 客户端端口号改全局变量


0.1.2
- 优化 服务端连接mysql添加异常处理
- 测试 服务端响应客户端
- 添加 客户端初始时时连接tcp, 并开启线程接收数据


0.1.1
- 添加 客户端点击登录按钮发送账号文本字节给服务端
- 优化 控件重命名


0.1.0
- 添加 客户端tcp初始化代码
- 添加 客户端初始化状态栏
- 修复 服务端, 客户端退出时异常


0.0.9
- 完善 服务端tcp初始化代码


0.0.8
- 优化 服务端记录到日志窗口前加上当前时间


0.0.7
- 添加 服务端tcp初始化代码
- 优化 把资源相关的放到res目录
- 添加 服务端-执行日志
- 添加 服务端-日志标签


0.0.6
- 添加 服务端mysql初始化代码


0.0.5
- 设置 客户端工具栏图标
- 优化 服务端工具栏图标


0.0.4
- 添加 客户端界面


0.0.3
- 添加 服务端界面-在线用户页
- 添加 服务端界面-卡密管理页


0.0.2
- 显示 服务端界面
- 添加 qrc资源文件
- 设置 服务端工具栏图标


0.0.1
- 添加 服务端界面全部用户页