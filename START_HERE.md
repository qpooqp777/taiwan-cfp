# 🚀 START_HERE.md - 從這裡開始

歡迎使用 **台灣碳足跡排放係數 Skill 包**！

這是一個完整的碳足跡查詢與分析工具。無論你是新手還是開發者，都能在這裡找到你需要的。

---

## ⚡ 30 秒快速開始

### 1️⃣ 設置 API 金鑰（2 分鐘）

```bash
# 編輯配置文件
nano config/api_config.json

# 填入你的 API 金鑰
{
  "api_key": "your-api-key-here"
}
```

**如何獲取 API 金鑰？** 訪問 [環保署開放資料平台](https://data.moenv.gov.tw/) 申請

### 2️⃣ 測試連接（1 分鐘）

```bash
python scripts/cfp_client.py test
```

### 3️⃣ 開始使用（1 分鐘）

```bash
# 查詢排放係數
python scripts/cfp_client.py query --product "電力"

# 計算排放量
python scripts/cfp_client.py calculate --product "電力" --amount 1000 --unit "kWh"
```

---

## 📖 選擇你的路徑

### 👤 我是新手用戶

**推薦時間**：30 分鐘

1. 閱讀 **[QUICK_START.md](QUICK_START.md)** (5 min)
   - 快速參考卡
   - 常用命令
   - 常見排放係數

2. 閱讀 **[READER.md](READER.md)** (20 min)
   - 完整使用指南
   - 常見場景
   - 故障排除

3. 查看 **[EXAMPLES.md](EXAMPLES.md)** (5 min)
   - 實際案例

👉 **立即開始**：[QUICK_START.md](QUICK_START.md)

---

### 👨‍💻 我是開發者

**推薦時間**：1 小時

1. 閱讀 **[INSTALL.md](INSTALL.md)** (5 min)
   - 安裝配置

2. 閱讀 **[API_GUIDE.md](API_GUIDE.md)** (30 min)
   - API 詳細文檔
   - 請求/回應格式
   - 錯誤處理

3. 查看 **[EXAMPLES.md](EXAMPLES.md)** (20 min)
   - Python 代碼示例
   - 進階用法

4. 查看 **[SKILL.md](SKILL.md)** (5 min)
   - Skill 架構

👉 **立即開始**：[INSTALL.md](INSTALL.md)

---

### 🏢 我要做企業碳盤查

**推薦時間**：45 分鐘

1. 閱讀 **[INSTALL.md](INSTALL.md)** (5 min)
   - 安裝配置

2. 閱讀 **[READER.md](READER.md)** (20 min)
   - 查看「企業碳盤查」場景

3. 查看 **[EXAMPLES.md](EXAMPLES.md)** (20 min)
   - 查看「企業碳盤查」示例

👉 **立即開始**：[INSTALL.md](INSTALL.md)

---

## 📚 完整文檔導航

### 快速參考

| 文檔 | 用途 | 時間 |
|------|------|------|
| **[QUICK_START.md](QUICK_START.md)** | 快速參考卡 | 5 min |
| **[README.md](README.md)** | Skill 概覽 | 5 min |
| **[INSTALL.md](INSTALL.md)** | 安裝配置 | 5 min |

### 完整指南

| 文檔 | 用途 | 時間 |
|------|------|------|
| **[READER.md](READER.md)** | 完整使用指南 | 20 min |
| **[API_GUIDE.md](API_GUIDE.md)** | API 詳細文檔 | 30 min |
| **[EXAMPLES.md](EXAMPLES.md)** | 實際使用案例 | 15 min |

### 參考資料

| 文檔 | 用途 |
|------|------|
| **[SKILL.md](SKILL.md)** | Skill 功能說明 |
| **[INDEX.md](INDEX.md)** | 文檔索引 |
| **[SUMMARY.md](SUMMARY.md)** | 完成總結 |

---

## 💡 常見任務

### 查詢排放係數

```bash
python scripts/cfp_client.py query --product "電力"
```

📖 詳見：[QUICK_START.md](QUICK_START.md) 或 [EXAMPLES.md](EXAMPLES.md)

### 計算排放量

```bash
python scripts/cfp_client.py calculate --product "電力" --amount 1000 --unit "kWh"
```

📖 詳見：[QUICK_START.md](QUICK_START.md) 或 [EXAMPLES.md](EXAMPLES.md)

### 企業碳盤查

查看 [READER.md](READER.md) 的「企業碳盤查」場景

📖 詳見：[EXAMPLES.md](EXAMPLES.md) 的「企業碳盤查」示例

### 遇到問題

查看 [READER.md](READER.md) 的「故障排除」部分

📖 詳見：[READER.md](READER.md)

---

## 🔢 常見排放係數（2024）

| 產品 | 排放係數 | 單位 |
|------|---------|------|
| 電力 | 0.509 | kg CO2e/kWh |
| 天然氣 | 2.04 | kg CO2e/m³ |
| 汽油 | 2.31 | kg CO2e/L |
| 柴油 | 2.68 | kg CO2e/L |
| 自來水 | 0.27 | kg CO2e/m³ |
| 水泥 | 0.92 | kg CO2e/kg |
| 鋼鐵 | 2.1 | kg CO2e/kg |

📖 詳見：[QUICK_START.md](QUICK_START.md)

---

## ❓ 常見問題

### Q: 如何獲取 API 金鑰？

A: 訪問 [環保署開放資料平台](https://data.moenv.gov.tw/)，註冊帳號後申請

📖 詳見：[INSTALL.md](INSTALL.md)

### Q: 排放係數多久更新？

A: 每年更新一次（通常 1 月）

📖 詳見：[READER.md](READER.md)

### Q: 支援哪些產品？

A: 支援電力、天然氣、汽油、柴油、水、水泥、鋼鐵等主要產業

📖 詳見：[READER.md](READER.md)

### Q: 可以離線使用嗎？

A: 可以。首次查詢後會緩存數據，後續可離線查詢

📖 詳見：[READER.md](READER.md)

### Q: 遇到問題怎麼辦？

A: 查看 [READER.md](READER.md) 的「故障排除」部分

📖 詳見：[READER.md](READER.md)

---

## 🎯 下一步

### 立即開始（5 分鐘）

1. 閱讀 [QUICK_START.md](QUICK_START.md)
2. 設置 API 金鑰
3. 運行第一個命令

### 深入學習（30 分鐘）

1. 閱讀 [READER.md](READER.md)
2. 查看 [EXAMPLES.md](EXAMPLES.md)
3. 嘗試實際案例

### 開發應用（1+ 小時）

1. 閱讀 [API_GUIDE.md](API_GUIDE.md)
2. 查看 Python 示例
3. 開發自己的應用

---

## 📞 需要幫助？

### 快速查詢

- **快速開始**：[QUICK_START.md](QUICK_START.md)
- **完整指南**：[READER.md](READER.md)
- **API 文檔**：[API_GUIDE.md](API_GUIDE.md)
- **使用示例**：[EXAMPLES.md](EXAMPLES.md)
- **文檔索引**：[INDEX.md](INDEX.md)

### 常見問題

- **安裝問題**：[INSTALL.md](INSTALL.md)
- **使用問題**：[READER.md](READER.md)
- **技術問題**：[API_GUIDE.md](API_GUIDE.md)

---

## 🎁 Skill 包內容

### 📚 10 份詳細文檔

- README.md - Skill 概覽
- QUICK_START.md - 快速參考卡
- READER.md - 完整使用指南
- INSTALL.md - 安裝配置指南
- SKILL.md - Skill 功能說明
- API_GUIDE.md - API 詳細文檔
- EXAMPLES.md - 實際使用案例
- INDEX.md - 文檔索引
- SUMMARY.md - 完成總結
- START_HERE.md - 本文檔

### 🔧 3 個配置文件

- config/api_config.json - API 配置
- config/categories.json - 產品類別
- config/units.json - 單位轉換

### 🐍 1 個 Python 客戶端

- scripts/cfp_client.py - 完整的 Python 客戶端

---

## 🚀 準備好了嗎？

選擇你的路徑，開始使用吧！

- 👤 **新手用戶**：[QUICK_START.md](QUICK_START.md)
- 👨‍💻 **開發者**：[INSTALL.md](INSTALL.md)
- 🏢 **企業用戶**：[READER.md](READER.md)

---

**祝你使用愉快！** 🎉

---

**最後更新**：2024-03-26  
**版本**：1.0  
**授權**：MIT License
