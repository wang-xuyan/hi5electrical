# Faraday Sigma Electrical 网站

基于Flask框架搭建的企业展示网站，参考Faraday Sigma Electrical官网的布局结构，实现响应式设计，整体风格简洁专业。

## 项目结构

```
Electric Grid Web/
├── main.py                # Flask应用入口文件
├── requirements.txt       # 项目依赖
├── README.md              # 项目说明
├── static/                # 静态资源
│   └── images/            # 图片文件
└── templates/             # HTML模板
    ├── index.html         # 主页
```

## 安装与运行

1. 安装依赖

```bash
pip install -r requirements.txt
```

2. 运行应用

```bash
python main.py
```

3. 访问网站

在浏览器中访问 http://localhost:5000

## 功能模块

1. 导航栏设计
   - Logo区域：点击返回主页
   - 导航菜单：About Us、Services、Projects、Contact Us

2. 页面结构
   - 主页：顶部横幅图片、主标题文案、简短描述文案、CTA按钮
   - About Us：团队照片、公司介绍文案、价值观/使命宣言文案
   - Services：服务图标/图片、服务名称、服务描述文案（6项）
   - Projects：项目展示网格布局、项目封面图、项目名称、项目简述（6个）
   - Contact Us：联系信息、联系表单

## 注意事项

- 请在static/images目录中放置相应的图片文件
- 网站使用Bootstrap 5进行响应式设计
- 开发模式下运行，生产环境需要调整配置
