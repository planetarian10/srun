# Srun
 Log in to the Srun Campus Network with Python  
 使用这个Python脚本以登录使用深澜提供校园网服务的认证系统  

## Description
 若使用模拟登录(加密)，使用encryption文件夹内脚本  
 若使用模拟登录(点击)，使用click文件夹内脚本  
 北航校园网用户请使用buaa文件夹内的专用稳定版本  
 加密方式从加密原理出发，直接认证，消耗资源较小  
 点击方式则模拟浏览器点击，理论上就算加密方式改变也能成功认证，但消耗资源高  

## Cautions
 Python3以上版本必须，否则无法import子文件夹的库  
 若认证失败，考虑将ac_id更改为'1'或'2'中的另一个  
 运行前检查设备日期时间是否正确，否则会因证无法验证证书而失败  
 确保内存充足，否则脚本可能无法运行  
 OpenWrt系统请关闭重绑定保护，否则会过滤掉所有内网解析导致认证失败  
 若不能认证，可尝试DHCP或断电后几十分钟后再尝试  
 ac_id错误将导致认证失败  
 请将IP修改为各自的认证网址  
 header与jQuery按需修改  
 修改各自的用户名和密码，用户名后应@运营商缩写（如中国电信：CTCC）  
 若将此脚本放在路由器上运行，需注意闪存大小，过小可能无法运行该Python脚本的相关依赖库(尤其是click方法)  

## Contributors
 CSDN @huxiaofan1223  
 neko.ooo @Hanabi  
 github @planetarian  
