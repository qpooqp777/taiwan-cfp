# INSTALL.md - 安裝與配置指南

## 📋 前置要求

- Python 3.7+
- pip（Python 包管理器）
- 網路連接
- 台灣環保署 API 金鑰

## 🚀 安裝步驟

### 第 1 步：檢查 Python 版本

```bash
python3 --version
# 應該顯示 Python 3.7 或更高版本
```

### 第 2 步：安裝依賴

```bash
# 安裝 requests 庫
pip install requests

# 或使用 pip3
pip3 install requests
```

### 第 3 步：獲取 API 金鑰

1. 訪問 [環保署開放資料平台](https://data.moenv.gov.tw/)
2. 點擊「會員登入」
3. 如無帳號，點擊「註冊」建立新帳號
4. 登入後進入「我的應用」
5. 點擊「建立新應用」
6. 填寫應用名稱（如「碳足跡計算工具」）
7. 複製生成的 **API 金鑰**

### 第 4 步：配置 API 金鑰

編輯 `config/api_config.json`：

```bash
nano config/api_config.json
```

填入你的 API 金鑰：

```json
{
  "api_key": "your-api-key-here",
  "api_endpoint": "https://data.moenv.gov.tw/api/v2/CFP_P_02",
  "timeout": 30,
  "retry_count": 3,
  "cache_enabled": true,
  "cache_ttl": 86400,
  "cache_dir": "data/cache",
  "log_level": "INFO"
}
```

### 第 5 步：測試安裝

```bash
python scripts/cfp_client.py test
```

預期輸出：

```
✓ API 連接成功
✓ 已獲取 1000 筆排放係數記錄
✓ 緩存已初始化
```

---

## 🔧 配置選項

### api_config.json 詳細說明

| 選項 | 類型 | 預設值 | 說明 |
|------|------|--------|------|
| `api_key` | string | - | 環保署 API 金鑰（必需） |
| `api_endpoint` | string | https://data.moenv.gov.tw/api/v2/CFP_P_02 | API 端點 |
| `timeout` | integer | 30 | 請求超時時間（秒） |
| `retry_count` | integer | 3 | 失敗重試次數 |
| `cache_enabled` | boolean | true | 是否啟用緩存 |
| `cache_ttl` | integer | 86400 | 緩存有效期（秒） |
| `cache_dir` | string | data/cache | 緩存目錄 |
| `log_level` | string | INFO | 日誌級別 |

### 環境變數配置

也可以使用環境變數設置 API 金鑰：

```bash
# Linux/Mac
export CFP_API_KEY="your-api-key-here"

# Windows (PowerShell)
$env:CFP_API_KEY="your-api-key-here"

# Windows (CMD)
set CFP_API_KEY=your-api-key-here
```

---

## 📁 目錄結構

安裝後的目錄結構：

```
taiwan-cfp/
├── config/
│   ├── api_config.json          # ✏️ 需要編輯
│   ├── categories.json          # 產品類別
│   └── units.json               # 單位轉換
├── scripts/
│   └── cfp_client.py            # Python 客戶端
├── data/
│   └── cfp_cache.json           # 自動生成
├── logs/
│   └── cfp.log                  # 自動生成
└── [文檔文件]
```

---

## ✅ 驗證安裝

### 1. 檢查依賴

```bash
python -c "import requests; print('requests 已安裝')"
```

### 2. 測試 API 連接

```bash
python scripts/cfp_client.py test
```

### 3. 執行查詢

```bash
python scripts/cfp_client.py query --product "電力"
```

### 4. 執行計算

```bash
python scripts/cfp_client.py calculate --product "電力" --amount 1000 --unit "kWh"
```

---

## 🐛 常見安裝問題

### 問題 1：Python 版本過低

**症狀**：`SyntaxError: invalid syntax`

**解決方案**：
```bash
# 檢查版本
python3 --version

# 升級 Python（如果需要）
# macOS
brew install python3

# Ubuntu/Debian
sudo apt-get install python3

# Windows
# 訪問 https://www.python.org/downloads/
```

### 問題 2：requests 庫未安裝

**症狀**：`ModuleNotFoundError: No module named 'requests'`

**解決方案**：
```bash
pip install requests
# 或
pip3 install requests
```

### 問題 3：API 金鑰無效

**症狀**：`API 返回錯誤: Invalid API key`

**解決方案**：
1. 檢查 API 金鑰是否正確複製
2. 確認 API 金鑰未過期
3. 在環保署平台重新生成 API 金鑰

### 問題 4：網路連接失敗

**症狀**：`ConnectionError: Failed to connect to API`

**解決方案**：
1. 檢查網路連接
2. 檢查防火牆設置
3. 嘗試使用 VPN
4. 檢查 API 端點是否可訪問

### 問題 5：權限不足

**症狀**：`PermissionError: [Errno 13] Permission denied`

**解決方案**：
```bash
# 給腳本執行權限
chmod +x scripts/cfp_client.py

# 或使用 python 直接執行
python scripts/cfp_client.py query --product "電力"
```

---

## 🔐 安全建議

### 1. 保護 API 金鑰

❌ **不要做**：
```bash
# 不要在命令行中暴露 API 金鑰
python cfp_client.py --api-key "abc123def456"

# 不要在代碼中硬編碼 API 金鑰
api_key = "abc123def456"
```

✅ **應該做**：
```bash
# 使用配置文件
# 使用環境變數
export CFP_API_KEY="your-api-key"

# 使用 .env 文件（不要提交到版本控制）
```

### 2. 定期輪換 API 金鑰

- 每 3-6 個月輪換一次
- 在環保署平台重新生成
- 更新配置文件

### 3. 限制 API 金鑰權限

- 在環保署平台設置 IP 白名單
- 限制 API 調用頻率
- 監控異常使用

---

## 📦 依賴管理

### 安裝所有依賴

```bash
pip install -r requirements.txt
```

### 生成 requirements.txt

```bash
pip freeze > requirements.txt
```

### 最小依賴

```
requests>=2.25.0
```

---

## 🚀 快速驗證

運行以下命令驗證安裝成功：

```bash
# 1. 測試連接
python scripts/cfp_client.py test

# 2. 查詢排放係數
python scripts/cfp_client.py query --product "電力"

# 3. 計算排放量
python scripts/cfp_client.py calculate --product "電力" --amount 1000 --unit "kWh"
```

如果所有命令都成功執行，說明安裝完成！

---

## 📚 下一步

安裝完成後，建議：

1. 閱讀 [QUICK_START.md](QUICK_START.md)（5 分鐘）
2. 閱讀 [READER.md](READER.md)（20 分鐘）
3. 查看 [EXAMPLES.md](EXAMPLES.md)（15 分鐘）

---

## 💬 需要幫助？

### 檢查日誌

```bash
# 查看最近的日誌
tail -f logs/cfp.log

# 查看所有日誌
cat logs/cfp.log
```

### 查看文檔

- [READER.md](READER.md) - 完整使用指南
- [API_GUIDE.md](API_GUIDE.md) - API 詳細文檔
- [EXAMPLES.md](EXAMPLES.md) - 使用示例

---

**安裝完成？** 開始使用 [QUICK_START.md](QUICK_START.md) 吧！ 🚀

---

**最後更新**：2024-03-26
