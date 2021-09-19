<h1 align="center">
  <a href="https://gitee.com/louisyoung1/projects">
    <img src="https://portrait.gitee.com/uploads/avatars/user/2529/7589523_louisyoung1_1597595544.png"/>
  </a>
</h1>

<p align="center">
  <sub>v1.0</sub><br/>
  <small>一个简单 & 轻量的 web 仪表盘 for linux 系统</small>
</p>

<p align="center">
  <small>
    <a href="#">Demo</a> &nbsp;|&nbsp;
    <a href="https://gitee.com/louisyoung1/linux-sys-dashboard/blob/master/README.md">
      文档
    </a> &nbsp;|&nbsp;
    <a href="https://gitee.com/louisyoung1/linux-sys-dashboard/blob/master/README.en.md">
      English
    </a>
  </small>
</p>



<br/>

## Features
* **轻量** ------ 占用在400KB以下
* **美观** ------ 极简主义，漂亮的仪表盘
* **简单** ------ 上手简洁
* **多样** ------ 选择使用 Python, Docker的版本

## 安装

### Step 1
```sh
## 1. clone the repo
git clone https://gitee.com/louisyoung1/linux-sys-dashboard.git

## 2. go to the cloned directory
cd linux-sys-dashboard

```
或者，如果你喜欢手动下载:

```sh
## 1. Download the .zip
curl -LOk https://gitee.com/louisyoung1/linux-sys-dashboard/repository/archive/master.zip && unzip master.zip

## 2. navigate to downloaded & unzipped dir
cd linux-sys-dashboard
chmod 777 linux_json_api.sh

```

### Step 2

详见 linux-dash server 支持的版本 :

* [Python](#使用-Python)
* [Docker](#使用-Docker)

#### 使用 Python
```sh
# Start the server (on port 80 by default; may require sudo).
python index.py
```

#### 使用 Docker

确保你已经启用了Docker，你可以用一行命令安装Docker

```sh
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
```

## 技术支持

有技术难题，在 [Louis-House](https://www.louisyoung.work/Contact)有我的联系方式

## 安全

**强烈建议 **在安全的环境下安装**[Linux-sys Dashboard](https://gitee.com/louisyoung1/linux-sys-dashboard)**

**[Linux-sys Dashboard](https://gitee.com/louisyoung1/linux-sys-dashboard)** 不提供任何安全性或身份验证特性。

## 许可

The MIT License (**[MIT](https://gitee.com/louisyoung1/linux-sys-dashboard/blob/master/LICENSE)**)