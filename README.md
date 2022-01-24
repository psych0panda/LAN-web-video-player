# LAN-web-video-player（局域网视频网站部署方案）  

[Install python3](https://realpython.com/installing-python/) and flask module if not done already.
> Alternative I recommend to use pip, and add future requirements later on to the list

```
pip3 install requirements.txt
```

Flask as the server, run the .py file and then you can watch the video online inside you LAN.  
change directory to current directory and run the following command on one of your LAN computer:  
python server.py  
and then put your video in directory /static/videos   
finish this, enjoy your LAN cinema.  
if your port 8888 is busy, change it in the last row of the server.py  

在局域网中的一台主机上运行 python server.py (需要将目录切换到文件路径)  
将视频文件放到/static/videos 目录下，然后在浏览器打开IP：8888即可  
如果端口占用，在server.py 文件中最后一行修改port= 你空闲的端口  

本项目使用了开源的播放器Dplayer， 在此对Dplayer的开发人员表示感谢 

![image](https://github.com/Areslight/LAN-web-video-player/blob/master/images/20190615143815.jpg)  


![image](https://github.com/Areslight/LAN-web-video-player/blob/master/images/20190615143805.png)
