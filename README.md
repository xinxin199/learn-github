# learn-github

学习目标：通过一个小改动，理解 Git diff、commit、分支和 GitHub Pull Request（PR）。

`cart.py` 是供你修改的原始代码，无需安装第三方库。运行：

```powershell
python cart.py
```

初始合计应为 `33.00 元`。

## 1. 保存原始版本

在终端进入本目录后执行（每条命令单独执行）：

```powershell
git init -b main
git add README.md cart.py
git commit -m "Add initial shopping cart example"
```

如果 Git 提示缺少身份，按照提示设置你自己的用户名和邮箱，然后重新提交。

## 2. 创建分支并修改代码

```powershell
git switch -c feature/receipt-details
```

练习：修改 `print_receipt`，让每件商品同时显示单价和小计。例如：

```text
笔记本 x 2，单价：12.00 元，小计：24.00 元
签字笔 x 3，单价：3.00 元，小计：9.00 元
```

保持合计仍为 `33.00 元`。先自己修改，再运行程序验证。

## 3. 阅读 diff

```powershell
git diff
```

- `---` 和 `+++`：修改前后的文件。
- `@@`：变化所在的行号范围。
- 行首 `-`：删除的旧代码。
- 行首 `+`：新增的代码。
- 行首空格：没有变化的上下文。

修改一行通常会显示为一行删除加一行新增。

```powershell
git add cart.py
git diff --staged
git commit -m "Show unit prices and subtotals on receipt"
git diff main...feature/receipt-details
```

`git diff` 查看尚未暂存的改动；`git diff --staged` 查看准备提交的改动；最后一条命令查看该分支相对 main 分叉点的变化。提交后，前两条命令通常没有输出，分支比较仍能看到改动。

## 4. 在 GitHub 上创建 PR

在 GitHub 创建一个空仓库，不要预先添加 README。将下面的地址换成自己的仓库地址：

```powershell
git remote add origin https://github.com/YOUR_NAME/learn-github.git
git push -u origin main
git push -u origin feature/receipt-details
```

在 GitHub 仓库页面创建 Pull Request，选择 base 为 `main`，compare 为 `feature/receipt-details`。

标题可写：`在购物清单中显示单价和小计`。

描述可写：

> 每件商品增加单价和小计，方便核对金额。运行 python cart.py，确认小计为 24.00 和 9.00，合计仍为 33.00。

diff 是代码变化的对比；PR 是围绕分支改动发起的审查和合并请求。在 PR 的 Files changed 中阅读 diff，确认只修改了预期内容，然后合并。

合并后，本地同步：

```powershell
git switch main
git pull origin main
```

本目录只提供初始代码和练习说明，尚未初始化 Git、提交代码或创建远程仓库与 PR。
