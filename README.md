# 医疗数据提取系统

## 简介
医疗数据提取系统是一个用于自动化提取和处理临床数据的应用程序。该系统能够从各种医疗记录中提取关键信息，并将其组织成结构化数据格式，便于进一步分析和使用。

## 特点
- 自动化数据提取功能
- 支持多种医疗记录格式
- 结构化数据输出
- 用户友好的界面

## 技术栈
- Python 3.8+
- Flask 2.0+
- SQLAlchemy 1.4+
- Flask-Testing 1.0.0
- BeautifulSoup 4.9+
- pandas 1.3+

## 安装步骤
1. 克隆项目仓库：
    ```bash
    git clone https://github.com/HougeLangley/clinical-data-extraction.git
    cd clinical-data-extraction
    ```

2. 创建虚拟环境并激活：
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate     # Windows
    ```

3. 安装依赖包：
    ```bash
    pip install -r requirements.txt
    ```

### `requirements.txt` 内容

```plaintext
Flask==2.0.1
SQLAlchemy==1.4.39
Flask-Testing==1.0.0
BeautifulSoup4==4.10.0
pandas==1.3.5