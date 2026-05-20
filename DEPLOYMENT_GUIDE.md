# Hi5 Electrical 网站部署指南

## 域名 + Cloudflare + GitHub 自动化部署

---

## 前提条件

- ✅ 已在 Cloudflare 购买域名
- ✅ 代码已上传到 GitHub 仓库
- ✅ 本地项目文件已调整好结构

---

## 当前项目结构

```
Electric Grid Web/
├── index.html          ← 网站首页（图片路径已修复为 images/)
├── images/             ← 网站图片（已复制到根目录）
├── app.py              ← Flask 后端（可选，如需动态功能）
├── requirements.txt
├── Procfile            ← Render 部署配置
├── render.yaml
└── README.md
```

---

## 方案一：Cloudflare Pages 部署（推荐）

### 优点
- 🚀 部署速度快（全球 CDN）
- 🔒 免费 HTTPS
- ⚡ 自动从 GitHub 同步更新
- 🌏 全球低延迟访问

### 部署步骤

#### 1. 登录 Cloudflare

访问 https://dash.cloudflare.com → 登录你的账号

#### 2. 创建 Pages 项目

1. 点击左侧菜单 **Workers & Pages**
2. 点击 **Create application**
3. 选择 **Pages** → **Connect to Git**

#### 3. 连接 GitHub

1. 点击 **Authorize GitHub**（首次需要授权）
2. 选择你的仓库（如 `your-username/electric-grid-web`）
3. 选择 **main** 分支

#### 4. 配置构建设置

因为这是纯静态网站，配置如下：

| 设置项 | 值 |
|--------|-----|
| **Project name** | `hi5electrical`（或你的域名） |
| **Production branch** | `main` |
| **Build command** | （留空） |
| **Build output directory** | `/` |
| **Environment variables** | （无需设置） |

#### 5. 保存并部署

点击 **Save and Deploy** → 等待几分钟

#### 6. 绑定自定义域名

1. 部署成功后，点击 **Custom domains**
2. 输入你的域名（如 `hi5electrical.co.nz`）
3. 点击 **Activate domain**
4. Cloudflare 会自动配置 SSL 证书

---

## 方案二：GitHub Pages + Cloudflare DNS

### 步骤

#### 1. 启用 GitHub Pages

1. 进入 GitHub 仓库 → **Settings** → **Pages**
2. **Source**: 选择 `Deploy from a branch`
3. **Branch**: 选择 `main`，目录选择 `/ (root)`
4. 点击 **Save**

#### 2. 获取 GitHub Pages URL

部署后会得到类似：`https://your-username.github.io/electric-grid-web/`

#### 3. 在 Cloudflare 配置 DNS

1. 登录 Cloudflare Dashboard
2. 选择你的域名 → **DNS** → **Records**
3. 添加记录：

| Type | Name | Content | Proxy status |
|------|------|---------|--------------|
| CNAME | www | `your-username.github.io` | DNS only (橙色云) |
| CNAME | @ | `your-username.github.io` | DNS only |

> ⚠️ 重要：GitHub Pages 需要验证域名，建议先用 DNS only 测试，验证完成后再开启代理。

#### 4. 域名验证（可选）

在 GitHub 仓库 Settings → Pages → Custom domain 输入你的域名，点击 **Configure** 进行验证。

---

## 域名 DNS 设置参考

如果你使用 `www` 子域名：

```
类型    名称    内容                        代理状态
-----------------------------------------------------------
CNAME   www     your-username.github.io    已代理 (橙色)
```

如果直接使用根域名 (@)：

```
类型    名称    内容                        代理状态
-----------------------------------------------------------
CNAME   @       your-username.github.io    仅 DNS
```

> 📝 注意：根域名 CNAME 需要使用 Cloudflare 的 **APEX 域名** 功能，或使用 **CNAME Flattening**。

---

## 自动部署验证

### 推送代码自动更新

使用 Cloudflare Pages 时，每次你 push 到 GitHub：

```bash
git add .
git commit -m "Update website content"
git push origin main
```

Cloudflare Pages 会自动：
1. 检测到代码变更
2. 拉取最新代码
3. 重新部署网站
4. 更新 HTTPS 证书

---

## 常见问题

### Q: 部署后图片不显示？

A: 检查图片路径。当前 `index.html` 使用相对路径 `images/logo.jpg`，确保 `images/` 文件夹在网站根目录。

### Q: HTTPS 证书问题？

A: Cloudflare Pages 会自动为自定义域名申请 Let's Encrypt 证书，通常需要 5-10 分钟生效。

### Q: 网站加载很慢？

A: Cloudflare Pages 默认使用全球 CDN，首次部署后全球节点需要几分钟同步。

---

## 快速检查清单

- [ ] 代码已 push 到 GitHub
- [ ] Cloudflare 账号已登录
- [ ] 域名已添加到 Cloudflare
- [ ] GitHub 已授权 Cloudflare Pages
- [ ] 首次部署成功
- [ ] 自定义域名已绑定
- [ ] HTTPS 证书已生效

---

## 技术支持

- Cloudflare Pages 文档: https://developers.cloudflare.com/pages/
- GitHub Pages 文档: https://docs.github.com/en/pages
