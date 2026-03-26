# READER.md - 台灣碳足跡排放係數 Skill 使用指南

## 📖 文檔導航

本 Skill 包含以下核心文檔：

| 文檔 | 用途 | 適合對象 |
|------|------|---------|
| **SKILL.md** | Skill 功能說明與工作流程 | AI Agent、開發者 |
| **READER.md** | 本文檔，使用指南 | 終端用戶、新手 |
| **API_GUIDE.md** | API 詳細文檔 | 開發者、進階用戶 |
| **EXAMPLES.md** | 實際使用案例 | 所有用戶 |

---

## 🎯 快速開始

### 第一步：設置 API 金鑰

1. 訪問 [環保署開放資料平台](https://data.moenv.gov.tw/)
2. 點擊「會員登入」→ 註冊新帳號
3. 登入後進入「我的應用」→ 「建立新應用」
4. 填寫應用名稱（如「碳足跡計算工具」）
5. 複製生成的 **API 金鑰**
6. 將金鑰保存到 `config/api_config.json`：

```json
{
  "api_key": "your-api-key-here",
  "api_endpoint": "https://data.moenv.gov.tw/api/v2/CFP_P_02",
  "cache_enabled": true,
  "cache_ttl": 86400
}
```

### 第二步：驗證連接

運行測試腳本：

```bash
python scripts/cfp_client.py test
```

預期輸出：
```
✓ API 連接成功
✓ 已獲取 1000 筆排放係數記錄
✓ 緩存已初始化
```

### 第三步：開始查詢

```bash
# 查詢電力排放係數
python scripts/cfp_client.py query --product "電力"

# 計算排放量
python scripts/cfp_client.py calculate --product "電力" --amount 1000 --unit "kWh"

# 生成報告
python scripts/cfp_client.py report --output "report.xlsx"
```

---

## 💡 常見使用場景

### 場景 1：企業碳盤查

**目標**：計算公司 2024 年的總碳排放量

**步驟**：
1. 收集排放數據（電力、天然氣、水、廢棄物等）
2. 使用 Skill 查詢各項排放係數
3. 逐項計算排放量
4. 生成碳盤查報告

**命令**：
```bash
python scripts/cfp_batch.py --input "company_data.csv" --output "carbon_report.xlsx"
```

### 場景 2：產品碳足跡標籤

**目標**：為產品計算碳足跡，申請環保署標籤

**步驟**：
1. 分解產品生命週期（原料、製造、運輸、使用、廢棄）
2. 查詢各階段排放係數
3. 計算總碳足跡
4. 生成標籤申請文檔

**命令**：
```bash
python scripts/cfp_client.py calculate \
  --product "水泥" \
  --amount 1000 \
  --unit "kg" \
  --lifecycle "cradle-to-gate"
```

### 場景 3：碳中和目標規劃

**目標**：規劃達成碳中和的路徑

**步驟**：
1. 計算當前排放量
2. 設定減排目標
3. 識別高排放環節
4. 提出改善建議

**命令**：
```bash
python scripts/cfp_report.py \
  --baseline "2024" \
  --target "2030" \
  --reduction_rate 0.5 \
  --format "html"
```

---

## 📊 數據說明

### 排放係數單位

| 產品/活動 | 排放係數 | 單位 | 備註 |
|----------|---------|------|------|
| 電力 | 0.509 | kg CO2e/kWh | 2024 年台灣電力 |
| 天然氣 | 2.04 | kg CO2e/m³ | 燃燒排放 |
| 汽油 | 2.31 | kg CO2e/L | 含上游排放 |
| 柴油 | 2.68 | kg CO2e/L | 含上游排放 |
| 水 | 0.27 | kg CO2e/m³ | 自來水供應 |
| 水泥 | 0.92 | kg CO2e/kg | 水泥製造 |
| 鋼鐵 | 2.1 | kg CO2e/kg | 粗鋼生產 |

### 數據來源

- **台灣電力公司**：電力排放係數
- **中油**：油品排放係數
- **台灣自來水公司**：水排放係數
- **水泥業**：水泥排放係數
- **鋼鐵業**：鋼鐵排放係數

### 更新頻率

- 排放係數：**每年更新**（通常 1 月）
- 緩存數據：**每 24 小時刷新**（可配置）

---

## 🔧 進階功能

### 1. 批量計算

處理多個排放源的批量計算：

```bash
python scripts/cfp_batch.py \
  --input "emissions.csv" \
  --output "results.xlsx" \
  --format "detailed"
```

**輸入格式** (`emissions.csv`)：
```csv
產品,數量,單位,備註
電力,5000,kWh,辦公室用電
天然氣,1000,m³,供暖
汽油,500,L,公務車
```

### 2. 趨勢分析

對比不同時期的排放變化：

```bash
python scripts/cfp_client.py trend \
  --product "電力" \
  --start_year 2020 \
  --end_year 2024 \
  --chart "line"
```

### 3. 對標分析

與行業平均水平對比：

```bash
python scripts/cfp_client.py benchmark \
  --industry "製造業" \
  --company_emissions 1000 \
  --unit "ton CO2e"
```

### 4. 減排建議

基於數據提出改善方案：

```bash
python scripts/cfp_client.py recommendations \
  --current_emissions "company_data.csv" \
  --target_reduction 0.3 \
  --output "recommendations.md"
```

---

## ⚙️ 配置說明

### `config/api_config.json`

```json
{
  "api_key": "your-api-key",
  "api_endpoint": "https://data.moenv.gov.tw/api/v2/CFP_P_02",
  "timeout": 30,
  "retry_count": 3,
  "cache_enabled": true,
  "cache_ttl": 86400,
  "cache_dir": "data/cache",
  "log_level": "INFO"
}
```

### `config/categories.json`

定義產品類別映射：

```json
{
  "能源": ["電力", "天然氣", "汽油", "柴油"],
  "水資源": ["自來水", "污水處理"],
  "建材": ["水泥", "鋼鐵", "玻璃"],
  "廢棄物": ["一般廢棄物", "有害廢棄物"]
}
```

### `config/units.json`

定義單位轉換：

```json
{
  "能源": {
    "kWh": 1,
    "MWh": 1000,
    "GJ": 277.78
  },
  "質量": {
    "kg": 1,
    "ton": 1000,
    "g": 0.001
  }
}
```

---

## 🐛 故障排除

### 問題 1：API 連接失敗

**症狀**：`ConnectionError: Failed to connect to API`

**解決方案**：
1. 檢查 API 金鑰是否正確
2. 檢查網路連接
3. 確認 API 端點是否可訪問
4. 查看 `logs/cfp.log` 獲取詳細錯誤信息

### 問題 2：查詢結果為空

**症狀**：`No results found for query`

**解決方案**：
1. 檢查產品名稱拼寫
2. 嘗試使用模糊搜尋：`--fuzzy`
3. 查看 `config/categories.json` 中的有效產品列表
4. 清除緩存重試：`python scripts/cfp_client.py clear-cache`

### 問題 3：計算結果不準確

**症狀**：計算結果與預期不符

**解決方案**：
1. 確認使用的排放係數版本（年份）
2. 檢查單位轉換是否正確
3. 驗證輸入數據格式
4. 查看計算日誌：`python scripts/cfp_client.py calculate --debug`

---

## 📚 相關資源

### 官方文檔

- [環保署開放資料平台](https://data.moenv.gov.tw/)
- [台灣碳足跡標籤](https://cfp.moenv.gov.tw/)
- [環保署碳盤查指南](https://www.moenv.gov.tw/)

### 標準與規範

- [ISO 14067 - 碳足跡標準](https://www.iso.org/standard/71096.html)
- [PAS 2050 - 商品與服務生命週期碳足跡評估](https://www.bsigroup.com/en-GB/standards/PAS-2050/)
- [GHG Protocol - 溫室氣體盤查議定書](https://ghgprotocol.org/)

### 工具與軟體

- [Quantis CFP Calculator](https://www.quantis-intl.com/)
- [Carbon Trust 碳足跡計算器](https://www.carbontrust.com/)
- [EPA 碳足跡計算器](https://www.epa.gov/carbon-footprint-calculator)

---

## 📞 支援與反饋

### 報告問題

如遇到問題，請提供：
1. 錯誤信息與日誌（`logs/cfp.log`）
2. 使用的命令與參數
3. 輸入數據樣本
4. 系統環境信息（OS、Python 版本等）

### 功能建議

歡迎提出改進建議，如：
- 新增產品類別
- 支援新的排放係數來源
- 改進計算算法
- 增強報告功能

---

## 📝 版本歷史

| 版本 | 日期 | 更新內容 |
|------|------|---------|
| 1.0 | 2024-01-15 | 初始版本，支援基本查詢與計算 |
| 1.1 | 2024-02-01 | 新增批量計算、趨勢分析 |
| 1.2 | 2024-03-01 | 新增對標分析、減排建議 |

---

**最後更新**：2024-03-26  
**維護者**：OpenClaw Taiwan CFP Team  
**授權**：MIT License
