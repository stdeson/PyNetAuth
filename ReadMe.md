
# 更新公告

3.0.0
- 优化 用线程池代替多线程


2.9.9
- 修复 更新自定义数据翻页异常


2.9.8
- 优化 json添加缩进
- 优化 表格行数


2.9.7
- 修复 添加版本异常


2.9.6
- 优化 处理登录时把到期时间发回去
- 优化 客户端登录成功设置标题


2.9.5
- 优化 客户端公告改为纯文本
- 优化 使用封装后的json相关函数


2.9.4
- 优化 界面
- 添加 读取配置按钮


2.9.3
- 优化 处理充值显示返回新的到期时间给用户
- 修复 季卡天数为90天


2.9.2
- 添加 充值赠送天数 (月卡以上才送)代码
- 删除 设置公告相关菜单项


2.9.1
- 修复 公告移到项目中 代码


2.9.0
- 优化 界面和配置读写


2.8.9
- 添加 充值赠送天数 (月卡以上才送)
- 优化 公告移到项目中


2.8.8
- 添加 用户表按ID排序
- 修复 表格排序后改变内容刷新显示异常


2.8.7
- 添加 部分表格允许排序


2.8.6
- 优化 细节


2.8.5
- 添加 项目表右键菜单_选中版本设置公告


2.8.4
- 优化 客户端日志输出的细节


2.8.3
- 优化 客户端和服务端日志


2.8.2
- 优化 登录界面背景图


2.8.1
- 修复 点击表项异常
- 优化 spec文件


2.8.0
- 优化 登录界面随机背景


2.7.9
- 修复 全部换为*args, 不传元组


2.7.8
- 优化 查询语句效率, 封装一个函数专门判断指定表是否有某记录
- 修复 项目表按钮点击事件更新的内容过多


2.7.7
- 修复 处理自定义数据异常


2.7.6
- 添加 处理充值, 按充值天数 整除 30来加充值月数


2.7.5
- 添加 用户管理表字段-充值月数


2.7.4
- 添加 用户管理表右键菜单刷新IP归属地


2.7.3
- 添加 设置IP归属地 函数


2.7.2
- 添加 删除选中流水信息 函数


2.7.1
- 添加 页码框验证器


2.7.0
- 添加 用户管理表排序相关控件


2.6.9
- 优化 为其它表格添加翻页相关控件点击事件


2.6.8
- 优化 为其它表格添加翻页相关控件


2.6.7
- 添加 按钮GO事件


2.6.6
- 完善 用户管理表分页显示2
- 添加 按钮上一页,下一页事件


2.6.5
- 修复 刷新显示时应先清空该表格中的内容


2.6.4
- 完善 用户管理表分页显示1


2.6.3
- 添加 用户管理表分页显示


2.6.2
- 优化 登录窗口发送与接收登录消息前, 检测调试器
- 优化 主窗口发送与接收心跳消息前, 检测调试器
- 优化 主窗口发送与接收离线消息前, 检测调试器


2.6.1
- 优化 处理心跳备注用户
- 优化 处理离线时备注用户


2.6.0
- 优化 服务器响应超时显示在状态栏


2.5.9
- 优化 服务端收到离线消息后还要回复客户端, 客户端收到后才关闭套接字
- 修复 服务客户端线程要循环
- 优化 服务端接收消息设为非阻塞, 只等2秒


2.5.8
- 优化 服务客户端线程不要循环


2.5.7
- 优化 处理登录时备注用户


2.5.6
- 优化 每日流水表查询时按日期降序
- 优化 项目表查询时按版本降序


2.5.5
- 优化 最新客户端版本不查表, 通过右键菜单设置


2.5.4
- 优化 时钟改为1分钟


2.5.3
- 优化 添加spec文件


2.3.6
- 优化 客户端添加 C++dll
- 优化 客户端连接服务器前先检测是否在虚拟机运行
- 优化 服务端和客户端拆分为两个独立项目


2.3.5
- 优化 客户端close通过发信号
- 优化 客户端通讯失败后就直接关闭


2.3.4
- 优化 服务端设置标题: 服务端IP+端口+版本
- 优化 服务端设置图标


2.3.2
- 优化 连接服务器mysql数据库


2.3.1
- 修复 客户端版本过低时不弹出更新网址


2.3.0
- 优化 服务端每连接一个用户, IP表今日连接数指定ip连接数+1
- 修复 处理项目异常


2.2.9
- 修复 打开日志会卡界面, 在线程里运行cmd


2.2.8
- 优化 时钟检测到过了一天则清零IP表的今日连接时间和今日连接次数


2.2.7
- 添加 显示与刷新IP管理表 函数


2.2.6
- 添加 IP管理表菜单


2.2.5
- 添加 服务端界面_IP管理表


2.2.4
- 优化 用户危险操作记录警告日志


2.2.3
- 优化 日志不要显示控件中, 而是打开notepad显示


2.2.2
- 优化 改用logging模块添加日志


2.2.1
- 优化 服务端配置保存与读取


2.2.0
- 优化 客户端登录配置保存与读取


2.1.9
- 移动 服务端库文件到窗口程序集
- 修复 登录界面的一些bug


2.1.8
- 优化 资源文件命名


2.1.7
- 优化 服务端初始化代码


2.1.6
- 修复 服务端用户按钮查询


2.1.5
- 添加 冻结IP下的所有账号


2.1.4
- 添加 公告标签设置超链接到更新地址


2.1.3
- 优化 封装读取json文件返回字典的函数


2.1.2
- 优化 mf模块改名
- 优化 加密模块改名


2.1.1
- 优化 活跃用户数算法, 计算心跳时间是今天的


2.1.0
- 优化 把到期时间放到心跳时间前


2.0.9
- 优化 客户端添加新版本更新提示复选框


2.0.8
- 优化 服务端窗口程序集放到服务端文件夹根目录
- 优化 登录窗口退出时不要自动保存设置


2.0.7
- 完善 验证码窗口


2.0.6
- 优化 登录界面配置用json


2.0.5
- 优化 登录界面自动生成一个验证码, 正确才发送给服务器


2.0.4
- 优化 服务端处理心跳时检测机器码


2.0.3
- 优化 把cfg放到成员属性


2.0.2
- 优化 客户端登录界面初始化时检查全局变量是否被修改, 防爆破
- 优化 客户端发送初始消息时发送备注和机器码
- 优化 服务端接收初始消息备注, 发送一个假的通信密钥回去


2.0.1
- 添加 解绑后加次数代码


2.0.0
- 优化 客户端主界面状态栏设置文本通过信号槽


1.9.9
- 优化 客户端连接tcp套接字函数放到mf
- 修复 客户端登录界面tab顺序


1.9.8
- 优化 把登录界面程序集的部分解密流程代码放到mf, 避免反编绎


1.9.7
- 优化 注册时发送机器码
- 优化 处理注册时检测机器码, 避免用户一台机器注册多个账号


1.9.6
- 添加 充值赠送天数代码


1.9.5
- 添加 服务端项目表右键菜单_选中版本全部允许, 选中版本全部禁止


1.9.4
- 优化 服务端项目信息时发送字典中的值


1.9.3
- 添加 服务端界面保存与读取配置


1.9.2
- 重构 项目管理表, 界面


1.9.1
- 优化 用户账号第一次登录重新计算到期时间


1.9.0
- 优化 客户端登录界面设置各页的tooltip


1.8.9
- 优化 服务端添加一个pedit存放导出卡号
- 优化 只导出未使用的选中卡号


1.8.8
- 优化 客户端连接失败不要弹消息框
- 优化 服务端所有表格设置间隔色


1.8.7
- 优化 服务端用户表显示最后更新时间


1.8.6
- 添加 每日流水表显示天卡充值数, 周卡充值数, 月卡充值数, 季卡充值数


1.8.5
- 完善 显示当前在线用户数
- 优化 把执行日志页放到最后


1.8.4
- 完善 查询用户最后更新时间是今天的用户数, 即为今日活跃用户数, 显示全部时更新
- 添加 分时钟事件刷新全部表


1.8.3
- 完善 充值成功充值用户数+1


1.8.2
- 优化 用户管理表增加 最后更新时间字段
- 优化 更新今日次数前判断最后更新时间是否是今天


1.8.1
- 优化 服务端窗口初始化mysql时更新和插入今日记录


1.8.0
- 优化 时钟插入每日流水记录
- 优化 时钟刷新用户状态sql语句


1.7.9
- 添加 每日流水刷新右键菜单_显示全部流水信息


1.7.8
- 优化 登录界面的tab顺序


1.7.7
- 优化 初始消息 和 项目消息在同一个tcp连接发送和接收
- 优化 两个自定义消息在同一个tcp连接发送和接收


1.7.6
- 优化 客户端show_info通过发信号来设置文本, 避免被逆向跟踪


1.7.5
- 完善 客户端记住账号密码


1.7.4
- 优化 重命名客户端窗口类
- 优化 重命名qt资源文件


1.7.3
- 添加 客户端记住账号密码


1.7.2
- 优化 客户端心跳时发送自身机器码, 若跟数据库的机器码比对, 若不符, 则令其下线


1.7.1
- 添加 用户表查询到期时间 < now()的用户


1.7.0
- 优化 若用户已到期, 从now()开始加, 否则从到期时间开始加


1.6.9
- 优化 用户管理显示全部时, 筛选出未查过归属地的ip
- 优化 获取这些ip的归属地, 添加到ip归属地表中
- 优化 更新用户表的ip归属地


1.6.8
- 优化 分两次获取自定义数据


1.6.7
- 添加 用户管理 右键菜单_删除选中用户


1.6.6
- 优化 客户端不用获取外网IP, 而是服务端通过套接字来获取


1.6.5
- 优化 服务端响应项目消息时把最新版本也发给客户端
- 添加 客户端更新网址, 发卡网址
- 添加 客户端允许登录, 允许注册, 允许解绑


1.6.4
- 添加 服务端窗口初始化时获取最新客户端版本, 放到一个变量里
- 优化 每次显示全部时刷新最新客户端版本


1.6.3
- 添加 客户端发送接收自定义和项目消息
- 优化 服务端发送自定义数据的结构


1.6.2
- 优化 客户端登录窗口接收消息改为短连接
- 优化 客户端登录窗口取消使用互斥体


1.6.1
- 优化 登录界面
- 优化 显示公告内容


1.6.0
- 添加 客户端发送项目数据消息
- 添加 服务端响应项目数据消息
- 添加 客户端处理项目数据消息


1.5.9
- 添加 客户端发送自定义数据消息
- 添加 服务端响应自定义数据消息
- 添加 客户端处理自定义数据消息


1.5.8
- 添加 自定义数据表右键菜单


1.5.7
- 优化 点击自定义数据表项设置文本到右侧编辑框


1.5.6
- 修复 服务端添加自定义数据


1.5.5
- 优化 把表格选中项用集合来接收


1.5.4
- 优化 服务端项目右键菜单删除选中版本


1.5.3
- 优化 客户端发送时对内容加密, 服务端接收时对内容解密


1.5.2
- 优化 服务端发送时对内容加密, 客户端接收时对内容解密
- 优化 AES算法加密后要转为字符串


1.5.1
- 优化 客户端发送和服务端接收字典结构


1.5.0
- 优化 服务端发送和客户端接收字典结构


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