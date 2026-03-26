# 台灣碳足跡排放係數 Skill

🌍 **台灣環保署碳足跡排放係數查詢與分析工具**

快速查詢產品碳足跡排放係數、計算排放量、生成碳盤查報告。

## ✨ 功能

- 🔍 **查詢排放係數** - 按產品類別、行業、物質名稱搜尋
- 📊 **計算排放量** - 基於排放係數計算碳足跡
- 📈 **數據分析** - 統計、比較、趨勢分析
- 📄 **報告生成** - 自動生成碳盤查報告（Excel、PDF）
- 💾 **數據緩存** - 本地緩存減少 API 調用

## 🚀 快速開始

### 1. 設置 API 金鑰

訪問 [環保署開放資料平台](https://data.moenv.gov.tw/)，申請 API 金鑰，然後編輯 `config/api_config.json`：

```json
{
  "api_key": "your-api-key-here",
  "api_endpoint": "https://data.moenv.gov.tw/api/v2/CFP_P_02",
  "cache_enabled": true,
  "cache_ttl": 86400
}
```

### 2. 查詢排放係數

```bash
python scripts/cfp_client.py query --product "電力"
```

### 3. 計算排放量

```bash
python scripts/cfp_client.py calculate --product "電力" --amount 1000 --unit "kWh"
```

## 📚 文檔

| 文檔 | 說明 |
|------|------|
| **READER.md** | 📖 使用指南（推薦新手閱讀） |
| **SKILL.md** | 🤖 Skill 功能說明 |
| **API_GUIDE.md** | 📡 API 詳細文檔 |
| **EXAMPLES.md** | 💡 實際使用案例 |

## 📋 支援的產品

### 能源
- 電力
- 天然氣
- 汽油
- 柴油
- 燃料油

### 水資源
- 自來水
- 污水處理

### 建材
- 水泥
- 鋼鐵
- 玻璃

### 廢棄物
- 一般廢棄物
- 有害廢棄物

## 💻 使用示例

### 查詢電力排放係數

```bash
$ python scripts/cfp_client.py query --product "電力"

查詢結果: 電力

  產品名稱: 電力
  排放係數: 0.509 kg CO2e/kWh
  數據年份: 2024
  資料來源: 台灣電力公司
  更新日期: 2024-01-15
```

### 計算家庭用電排放量

```bash
$ python scripts/cfp_client.py calculate --product "電力" --amount 300 --unit "kWh"

排放量計算結果

  產品: 電力
  使用量: 300 kWh
  排放係數: kg CO2e/kWh
  總排放量: 0.15 公噸 CO2e
```

### Python 代碼示例

```python
from cfp_client import CFPClient

client = CFPClient()

# 查詢排放係數
results = client.query('電力')
print(f"電力排放係數: {results[0]['EmissionFactor']} {results[0]['Unit']}")

# 計算排放量
emission, _ = client.calculate('電力', 1000, 'kWh')
print(f"1000 kWh 的排放量: {emission:.2f} 公噸 CO2e")
```

## 🔧 配置

### `config/api_config.json`

```json
{
  "api_key": "your-api-key",
  "api_endpoint": "https://data.moenv.gov.tw/api/v2/CFP_P_02",
  "timeout": 30,
  "retry_count": 3,
  "cache_enabled": true,
  "cache_ttl": 86400
}
```

### `config/categories.json`

定義產品類別映射。

### `config/units.json`

定義單位轉換規則。

## 📁 目錄結構

```
taiwan-cfp/
├── SKILL.md              # Skill 功能說明
├── READER.md             # 使用指南
├── API_GUIDE.md          # API 詳細文檔
├── EXAMPLES.md           # 使用示例
├── README.md             # 本文檔
├── scripts/
│   ├── cfp_client.py     # Python 客戶端
│   ├── cfp_batch.py      # 批量查詢工具
│   └── cfp_report.py     # 報告生成工具
├── config/
│   ├── api_config.json   # API 配置
│   ├── categories.json   # 產品類別
│   └── units.json        # 單位轉換
└── data/
    ├── cfp_cache.json    # 排放係數緩存
    └── emission_factors.csv  # 參考表
```

## 🐛 故障排除

### API 連接失敗

```bash
# 測試連接
python scripts/cfp_client.py test

# 檢查 API 金鑰
cat config/api_config.json
```

### 查詢結果為空

```bash
# 清除緩存重試
python scripts/cfp_client.py clear-cache

# 使用模糊搜尋
python scripts/cfp_client.py query --product "電" --fuzzy
```

## 📞 支援

- 📖 [環保署開放資料平台](https://data.moenv.gov.tw/)
- 🌐 [台灣碳足跡標籤](https://cfp.moenv.gov.tw/)
- 📚 [ISO 14067 標準](https://www.iso.org/standard/71096.html)

## 📝 版本

- **版本**：1.0
- **發布日期**：2024-03-26
- **授權**：MIT License

## 🙏 致謝

感謝台灣環保署提供開放資料集。

---

**開始使用**：閱讀 [READER.md](READER.md) 了解詳細使用方法。
