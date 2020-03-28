# Kektor3000 bot

<a href="https://github.com/AnyKeyShik/Kektor3000/blob/master/LICENSE">
<img src ="https://img.shields.io/github/license/AnyKeyShik/Kektor3000.svg"  alt="License"/>
</a>
<a href="https://github.com/AnyKeyShik/Kektor3000/stargazers">
<img src ="https://img.shields.io/github/stars/AnyKeyShik/Kektor3000.svg"  alt="Stars"/>
</a>
<a href="https://github.com/AnyKeyShik/Kektor3000/issues">
<img src ="https://img.shields.io/github/issues/AnyKeyShik/Kektor3000.svg"  alt="Issues"/>
</a>

Bot for KEKS

# Now:
* CAN KEK


# Getting started

#### Requirements

To compile and run this project, you will need:
* pytelegrambotapi
* PySocks (optional, for proxy if needed)
* Python3

#### Deploy

##### Without Docker
1. Fill constants for your bot
2. Install requirements
3. Run `run.py` 

##### With Docker
1. Fill constants for your bot
2. Build image (`docker build -t <image_name> .`)
3. Create folder for logs
4. Start container with your folder (`docker run --restart=always -d -v <your_folder>:/Kektor3000/logs -t <image_name>`)

# In future:
* Give random picture through random or fixed time intervals
* Advise anime with genre and rating what user gives 
