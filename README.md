### 0 简介

果酱助手是某学校国奖填表助手，后端django，前端css js scss，数据库sqlite，核心是把网页版xml文件转成word文件，起到辅助填表的作用。

### 1 进入服务器

别去找上一届的技术人员要账号。后台要绑定自己的微信账号，所以去和管理员要个新账号。

学校用堡垒机管理服务器，使用者需要拿到管理员新创建的初始账户。一开始给你一个账号，附带两个密码。第一次登陆需要去微信搜索小程序LogBaseMFA，用其中的一个密码，绑定自己的微信账号，然后选择OTP登陆，用另一个密码加上小程序实时生成的密码才能登陆进去。

堡垒机后台的网址是这个，很难想象当时老师居然没给我网址，我还是去跟上届学长要的。

[Logbase运维安全管理系统 (sdu.edu.cn)](https://safety.wh.sdu.edu.cn/bhost/)

进入后台，你会在学生工作部底下看到一个主机名为“国奖申报小助手”的东西，可以选择SFTP和SSH连接两种方式。

在连接之前，你需要去“访问工具-相关下载”里下载其中的BHostClient这个软件，再在“访问工具-全局设定“里配置好自己在本地连接所用的软件，SFTP我推荐用WinSCP，SSH推荐XShell，那个密钥查看器我下载后似乎不能用，所以大概没有用wsl自己ssh的可能。

上一步是我摸索出来的，相关人员啥说明都没给。

### 2 项目运行

今年我用的60000端口，不知道他们收回服务器的时候会不会把端口也闭了。

今年我一开始run是没问题，但在网页上访问不到，焦头烂额搞了一两天，发现是外网防火墙没开，得联系管理员让他开个端口，搞半天原来不是我的问题。然后内部的防火墙也得用命令打开，具体是啥我忘了。

拿到这服务器，一开始连yum都没法用，防火墙也是坏的，自己修了挺久才正常了一点，本来是跟负责人说需要重装系统，后来自己修好了能勉强跑起来了也就没有不折腾了，其实我很想跟他说重装是为了造福下一届，唉。

### 3 代码工作

进入服务器你会看到多届学长留下来的代码。我在2022年搞了V5.0~5.3版本，也就是说这个代码已经用了五年了。

为什么每年都要改，因为每年的要求都不一样。表格的各种细节格式、专业列表和奖项列表几乎每年都要改，要做好非常小的小细节都要修改的准备，很难想象那些搞学生工作的人每天的精神状态。

项目目录结构如下，除了django自己的配置文件，我由上到下大致介绍一下。

![image-20221021170623447.png](http://www.lter.space/usr/uploads/2022/10/1274662559.png)

生成的所有文件都放在students文件夹下，到时候会让你导出。

data2doc里的代码用来把填写的xml转化成doc文件，内有模板填写的格式，如果想在表格内添加新项可以在这里的模板处添加。同时解决奖项名称专业名称太长放在两行而不美观的问题，比如颁奖单位是“中国国际“互联网+”大学生创新创业大赛组织委员会”，这种长达23个字的颁奖单位就要用代码自动缩小字号。

JamList放的是奖项，用户在网页前端下拉列表里选择奖项之后代码需要到这里边查找奖项的具体信息，然后把找到的具体信息如奖项名称日期和颁奖单位都填到表格里。

studentjson放用户提交到服务器的json文件。

template.xml文件是重点，选择用word打开，按照学校要求在里边调整表格的格式，~~我今年可能改了有五十次~~。

![image-20221021171924495.png](http://www.lter.space/usr/uploads/2022/10/2779010852.png)

views放http请求之后的操作，明年加上2023的奖项之后也得改这玩意，具体看看代码就知道。

JamAssistantWeb里边的东西不用管，基本不用改。

templates文件夹里的JamAssistantIndex文件是重点，~~我今年也得改了三十次，~~它控制网页表单的内容，好消息是，我在极度懒得人工搞的情况下写了仨小东西，放在了tool文件夹里，

csv2list把学校给的奖项列表生成为JamList里的内容，

list2code把学校给的奖项列表生成网页表单需要的代码，

maj2code把学校给的专业列表生成网页表单需要的代码，

具体咋使用看看代码就知道

![image-20221021173928153.png](http://www.lter.space/usr/uploads/2022/10/1559162009.png)

### 4 其它问题

如果生成表之后，打开时word提示 “一个xml位于无效位置，因此无法打开文件”，说明在申请理由或者推荐理由那里填写的文字中有html标签之类的奇怪的符号，重新填一遍就行。

如果负责人多次对生成的表单格式不满意，你可以告诉他你不精通于word，可以把template.xml模板发给他让他自己改。

比如我确实不会调整表格最底部的线有多高，就是让负责人改了再传给我的。

对了，

前年薪资1500，两个人一块干

去年1000，两个人一块干，

今年定的是400，我一个人干，听负责人说今年事儿相比起来还特多，现在还没发，希望能给我加班费。

如果遇到很麻烦的操作，记得要加班费。