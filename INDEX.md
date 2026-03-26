# 📚 台灣碳足跡排放係數 Skill 文檔索引

## 🎯 按用途選擇文檔

### 👤 我是新手用戶

**推薦閱讀順序：**

1. **[QUICK_START.md](QUICK_START.md)** ⚡ (5 分鐘)
   - 30 秒快速開始
   - 常用命令速查
   - 常見排放係數表

2. **[READER.md](READER.md)** 📖 (20 分鐘)
   - 完整使用指南
   - 常見使用場景
   - 故障排除

3. **[EXAMPLES.md](EXAMPLES.md)** 💡 (15 分鐘)
   - 實際使用案例
   - 代碼示例
   - 最佳實踐

### 👨‍💻 我是開發者

**推薦閱讀順序：**

1. **[API_GUIDE.md](API_GUIDE.md)** 📡 (30 分鐘)
   - API 端點詳細說明
   - 請求/回應格式
   - 錯誤處理

2. **[SKILL.md](SKILL.md)** 🤖 (20 分鐘)
   - Skill 架構說明
   - 工作流程
   - 資源位置

3. **[EXAMPLES.md](EXAMPLES.md)** 💡 (15 分鐘)
   - Python 代碼示例
   - 進階用法

### 🏢 我要做企業碳盤查

**推薦閱讀順序：**

1. **[QUICK_START.md](QUICK_START.md)** ⚡ (5 分鐘)
   - 快速上手

2. **[READER.md](READER.md)** 📖 (20 分鐘)
   - 查看「企業碳盤查」場景

3. **[EXAMPLES.md](EXAMPLES.md)** 💡 (15 分鐘)
   - 查看「企業碳盤查」示例

---

## 📄 文檔詳細說明

### 1. README.md
**用途**：Skill 概覽  
**內容**：
- 功能介紹
- 快速開始
- 支援的產品列表
- 目錄結構

**適合**：所有用戶（首先閱讀）

---

### 2. QUICK_START.md ⭐ 推薦新手首先閱讀
**用途**：快速參考卡  
**內容**：
- 30 秒快速開始
- 常用命令速查
- 常見排放係數表
- 快速計算示例
- 常見問題

**適合**：想快速上手的用戶

---

### 3. READER.md ⭐ 推薦新手完整閱讀
**用途**：完整使用指南  
**內容**：
- 第一步：設置 API 金鑰
- 第二步：驗證連接
- 第三步：開始查詢
- 常見使用場景（3 個）
- 數據說明
- 進階功能
- 配置說明
- 故障排除
- 相關資源

**適合**：新手用戶、想了解完整功能的用戶

---

### 4. SKILL.md
**用途**：Skill 功能說明  
**內容**：
- 功能列表
- 快速開始
- 工作流程（基本和進階）
- API 說明
- 使用示例
- 資源位置
- 常見問題

**適合**：AI Agent、想了解 Skill 架構的開發者

---

### 5. API_GUIDE.md
**用途**：API 詳細文檔  
**內容**：
- API 端點說明
- 獲取 API 金鑰步驟
- 查詢端點詳細說明
- 請求參數
- 回應格式
- Python 客戶端使用
- 常見排放係數表
- 錯誤處理
- 最佳實踐
- 安全建議

**適合**：開發者、想深入了解 API 的用戶

---

### 6. EXAMPLES.md
**用途**：實際使用案例  
**內容**：
- 基本查詢（3 個示例）
- 排放量計算（3 個示例）
- 企業碳盤查（2 個示例）
- 產品碳足跡（1 個示例）
- 數據分析（2 個示例）
- 最佳實踐

**適合**：所有用戶、想看實際代碼的用戶

---

## 🗂️ 配置文件說明

### config/api_config.json
**用途**：API 配置  
**內容**：
- API 金鑰
- API 端點
- 超時設置
- 重試次數
- 緩存設置

**編輯**：需要填入你的 API 金鑰

---

### config/categories.json
**用途**：產品類別映射  
**內容**：
- 能源類
- 水資源類
- 建材類
- 廢棄物類
- 運輸類
- 農業類

**編輯**：可根據需要添加新類別

---

### config/units.json
**用途**：單位轉換規則  
**內容**：
- 能源單位轉換
- 質量單位轉換
- 體積單位轉換
- 距離單位轉換

**編輯**：可根據需要添加新單位

---

## 🔧 腳本說明

### scripts/cfp_client.py
**用途**：Python 客戶端  
**功能**：
- 查詢排放係數
- 計算排放量
- 測試連接
- 清除緩存

**使用**：
```bash
python scripts/cfp_client.py query --product "電力"
python scripts/cfp_client.py calculate --product "電力" --amount 1000 --unit "kWh"
python scripts/cfp_client.py test
python scripts/cfp_client.py clear-cache
```

---

## 📊 快速查詢表

### 按功能查詢

| 功能 | 文檔 | 位置 |
|------|------|------|
| 快速開始 | QUICK_START.md | 頂部 |
| 完整指南 | READER.md | 第一步 |
| API 詳情 | API_GUIDE.md | 查詢端點 |
| 代碼示例 | EXAMPLES.md | 基本查詢 |
| 企業盤查 | READER.md / EXAMPLES.md | 場景 1 / 示例 1 |
| 故障排除 | READER.md | 故障排除 |
| 配置說明 | READER.md | 配置說明 |

### 按用戶類型查詢

| 用戶類型 | 推薦文檔 | 閱讀時間 |
|---------|---------|---------|
| 新手 | QUICK_START.md → READER.md | 25 分鐘 |
| 開發者 | API_GUIDE.md → EXAMPLES.md | 45 分鐘 |
| 企業用戶 | READER.md (場景 1) → EXAMPLES.md (示例 1) | 30 分鐘 |
| 進階用戶 | API_GUIDE.md → SKILL.md | 50 分鐘 |

---

## 🎓 學習路徑

### 路徑 1：快速上手（15 分鐘）
```
QUICK_START.md (5 min)
    ↓
試試第一個命令
    ↓
READER.md 快速開始部分 (10 min)
```

### 路徑 2：完整學習（1 小時）
```
README.md (5 min)
    ↓
QUICK_START.md (5 min)
    ↓
READER.md (20 min)
    ↓
EXAMPLES.md (20 min)
    ↓
試試實際案例
```

### 路徑 3：深度開發（2 小時）
```
README.md (5 min)
    ↓
API_GUIDE.md (30 min)
    ↓
SKILL.md (20 min)
    ↓
EXAMPLES.md (20 min)
    ↓
查看 cfp_client.py 源碼 (30 min)
    ↓
開發自己的應用
```

---

## 🔗 快速鏈接

### 官方資源
- [環保署開放資料平台](https://data.moenv.gov.tw/)
- [台灣碳足跡標籤](https://cfp.moenv.gov.tw/)
- [環保署官網](https://www.moenv.gov.tw/)

### 標準與規範
- [ISO 14067 碳足跡標準](https://www.iso.org/standard/71096.html)
- [GHG Protocol](https://ghgprotocol.org/)
- [PAS 2050](https://www.bsigroup.com/en-GB/standards/PAS-2050/)

### 工具與軟體
- [Quantis CFP Calculator](https://www.quantis-intl.com/)
- [Carbon Trust](https://www.carbontrust.com/)
- [EPA Calculator](https://www.epa.gov/carbon-footprint-calculator)

---

## 💬 需要幫助？

### 常見問題

**Q: 我應該先讀哪個文檔？**  
A: 如果你是新手，先讀 QUICK_START.md，然後 READER.md

**Q: 我想快速計算排放量**  
A: 查看 QUICK_START.md 的「快速計算」部分

**Q: 我想做企業碳盤查**  
A: 查看 READER.md 的「企業碳盤查」場景，然後 EXAMPLES.md 的「企業碳盤查」示例

**Q: 我想開發自己的應用**  
A: 先讀 API_GUIDE.md，然後查看 EXAMPLES.md 的 Python 代碼示例

**Q: 遇到問題怎麼辦？**  
A: 查看 READER.md 的「故障排除」部分

---

## 📝 版本信息

- **Skill 版本**：1.0
- **發布日期**：2024-03-26
- **最後更新**：2024-03-26
- **文檔版本**：1.0

---

**開始使用**：選擇上面適合你的文檔，開始閱讀吧！ 🚀
