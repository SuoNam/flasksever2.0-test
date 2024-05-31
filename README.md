# 2024/4/18
__项目规划__
* 被试登录实现(用户等级为Subject)
* 被试的参与记录与主试的发布记录(只可读不可写)(id user subject experiment [topic] content startDate  endDate material subjects_number fee location)
* 实验招募平台内招募
  * (对每个实验建个experiment_subject表)(experiment subject subject_id subject_phone ...)
  * (在实验招募界面前加个按钮 点击后将被试信息与实验信息发给服务器 利用其中有效信息添加到experiment_subject表)
  * (同时将信息提交给被试的 实验状态表(id experiment startDate endDate status)(默认审核中)中)
  * (在主试个人界面添加 正在进行的实验按钮: (日期:实验名)按钮:1.实验信息(experiment表) 2.实验招募人员(获取experiment_subject表信息) (带有不通过按钮(将该id改为不通过)和通过按钮(将该id改为通过)))
  * (设置事件 实验到截止时间 所有id 审核中 改为 通过)
  * (签到事项 更新experiment_subject表 )....
  * (主试 在正在进行的实验按钮 下的(日期:实验名)按钮 右侧添加停止实验按钮  点击 个人实验状态表中相关信息删除 提交给个人历史记录表中)
* 
