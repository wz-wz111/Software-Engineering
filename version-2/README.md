# Funny JSON Explorer
对已有FJE实现进行设计重构
改用**迭代器+访问者**模式

运行指令：
```bash
# icon_A可换为icon_config.json中设置的图标名字
fje -f example.json -s tree -i icon_A
fje -f example.json -s tree -i icon_B

fje -f example.json -s rectangle -i icon_A
fje -f example.json -s rectangle -i icon_B

# 可以运行FJE.py文件
```