# Funny JSON Explorer
Funny JSON Explorer（**FJE**），是一个JSON文件可视化的命令行界面小工具.

1. FJE可以快速切换**风格**（style），包括：树形（tree）、矩形（rectangle）；

2. 也可以指定**图标族**（icon family），为中间节点或叶节点指定一套icon

3. 通过配置文件(icon_config.json)，可添加新的图标族

运行指令：
```bash
# icon_A可换为icon_config.json中设置的图标名字
fje -f example.json -s tree -i icon_A
fje -f example.json -s tree -i icon_B

fje -f example.json -s rectangle -i icon_A
fje -f example.json -s rectangle -i icon_B
```