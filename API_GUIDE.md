# API_GUIDE.md - 台灣碳足跡排放係數 API 詳細文檔

## 📡 API 端點

### 基本信息

- **服務提供者**：台灣環保署
- **平台**：開放資料平台
- **API 版本**：v2
- **基礎 URL**：`https://data.moenv.gov.tw/api/v2/CFP_P_02`
- **認證方式**：API Key（查詢參數）
- **回應格式**：JSON

### 獲取 API 金鑰

1. 訪問 [環保署開放資料平台](https://data.moenv.gov.tw/)
2. 點擊「會員登入」
3. 如無帳號，點擊「註冊」建立新帳號
4. 登入後進入「我的應用」
5. 點擊「建立新應用」
6. 填寫應用名稱和描述
7. 複製生成的 **API 金鑰**
8. 將金鑰保存到 `config/api_config.json`

---

## 🔍 查詢端點

### GET /api/v2/CFP_P_02

查詢台灣碳足跡排放係數資料集。

#### 請求參數

| 參數 | 類型 | 必需 | 說明 | 示例 |
|------|------|------|------|------|
| `api_key` | string | ✓ | API 金鑰 | `abc123def456` |
| `limit` | integer | ✗ | 返回筆數（最大 1000） | `1000` |
| `offset` | integer | ✗ | 分頁偏移 | `0` |
| `sort` | string | ✗ | 排序方式 | `ImportDate desc` |
| `format` | string | ✗ | 回應格式（json/xml） | `json` |
| `filter` | string | ✗ | 篩選條件 | `ProductName:電力` |

#### 請求示例

```bash
# 基本查詢
curl "https://data.moenv.gov.tw/api/v2/CFP_P_02?api_key=YOUR_API_KEY&limit=100&format=json"

# 帶排序
curl "https://data.moenv.gov.tw/api/v2/CFP_P_02?api_key=YOUR_API_KEY&limit=1000&sort=ImportDate%20desc&format=json"

# 帶篩選
curl "https://data.moenv.gov.tw/api/v2/CFP_P_02?api_key=YOUR_API_KEY&filter=ProductName:電力&format=json"
```

#### 回應格式

```json
{
  "success": true,
  "info": {
    "count": 1000,
    "limit": 1000,
    "offset": 0,
    "resourceId": "CFP_P_02"
  },
  "result": [
    {
      "id": "CFP_001",
      "ProductName": "電力",
      "EmissionFactor": 0.509,
      "Unit": "kg CO2e/kWh",
      "DataYear": 2024,
      "Source": "台灣電力公司",
      "Category": "能源",
      "Description": "台灣電力排放係數",
      "ImportDate": "2024-01-15",
      "UpdateDate": "2024-01-15"
    },
    {
      "id": "CFP_002",
      "ProductName": "天然氣",
      "EmissionFactor": 2.04,
      "Unit": "kg CO2e/m³",
      "DataYear": 2024,
      "Source": "中油",
      "Category": "能源",
      "Description": "天然氣燃燒排放係數",
      "ImportDate": "2024-01-15",
      "UpdateDate": "2024-01-15"
    }
  ]
}
```

#### 回應欄位說明

| 欄位 | 類型 | 說明 |
|------|------|------|
| `success` | boolean | 請求是否成功 |
| `info` | object | 分頁信息 |
| `info.count` | integer | 返回記錄數 |
| `info.limit` | integer | 限制筆數 |
| `info.offset` | integer | 偏移位置 |
| `result` | array | 排放係數記錄陣列 |
| `result[].id` | string | 記錄 ID |
| `result[].ProductName` | string | 產品名稱 |
| `result[].EmissionFactor` | number | 排放係數值 |
| `result[].Unit` | string | 排放係數單位 |
| `result[].DataYear` | integer | 數據年份 |
| `result[].Source` | string | 數據來源 |
| `result[].Category` | string | 產品類別 |
| `result[].Description` | string | 描述 |
| `result[].ImportDate` | string | 導入日期（YYYY-MM-DD） |
| `result[].UpdateDate` | string | 更新日期（YYYY-MM-DD） |

---

## 🔗 Python 客戶端使用

### 安裝依賴

```bash
pip install requests
```

### 基本使用

```python
from cfp_client import CFPClient

# 初始化客戶端
client = CFPClient('config/api_config.json')

# 查詢排放係數
results = client.query('電力')
for item in results:
    print(f"{item['ProductName']}: {item['EmissionFactor']} {item['Unit']}")

# 計算排放量
total_emission, unit = client.calculate('電力', 1000, 'kWh')
print(f"排放量: {total_emission:.2f} 公噸 CO2e")

# 測試連接
client.test_connection()

# 清除緩存
client.clear_cache()
```

### 進階使用

```python
# 模糊搜尋
results = client.query('電', fuzzy=True)

# 按年份篩選
results = client.query('電力', year=2024)

# 獲取所有數據
data = client.fetch_data(limit=1000, offset=0)
```

---

## 📊 常見排放係數

### 能源

| 產品 | 排放係數 | 單位 | 備註 |
|------|---------|------|------|
| 電力 | 0.509 | kg CO2e/kWh | 2024 年台灣電力 |
| 天然氣 | 2.04 | kg CO2e/m³ | 燃燒排放 |
| 汽油 | 2.31 | kg CO2e/L | 含上游排放 |
| 柴油 | 2.68 | kg CO2e/L | 含上游排放 |
| 燃料油 | 3.15 | kg CO2e/L | 重油 |

### 水資源

| 產品 | 排放係數 | 單位 | 備註 |
|------|---------|------|------|
| 自來水 | 0.27 | kg CO2e/m³ | 供應與處理 |
| 污水處理 | 0.48 | kg CO2e/m³ | 污水處理 |

### 建材

| 產品 | 排放係數 | 單位 | 備註 |
|------|---------|------|------|
| 水泥 | 0.92 | kg CO2e/kg | 水泥製造 |
| 鋼鐵 | 2.1 | kg CO2e/kg | 粗鋼生產 |
| 玻璃 | 0.85 | kg CO2e/kg | 玻璃製造 |

---

## ⚠️ 錯誤處理

### 常見錯誤碼

| 狀態碼 | 說明 | 解決方案 |
|--------|------|---------|
| 200 | 成功 | 正常處理 |
| 400 | 請求參數錯誤 | 檢查參數格式 |
| 401 | 認證失敗 | 檢查 API 金鑰 |
| 403 | 禁止訪問 | 檢查 API 金鑰權限 |
| 404 | 資源不存在 | 檢查端點 URL |
| 429 | 請求過於頻繁 | 降低請求頻率 |
| 500 | 服務器錯誤 | 稍後重試 |

### 錯誤回應示例

```json
{
  "success": false,
  "message": "Invalid API key",
  "code": "AUTH_ERROR"
}
```

---

## 🚀 最佳實踐

### 1. 使用緩存

```python
# 啟用緩存以減少 API 調用
client = CFPClient('config/api_config.json')
# 首次調用會從 API 獲取，後續調用使用緩存
results = client.query('電力')
```

### 2. 錯誤處理

```python
try:
    results = client.query('電力')
    if not results:
        print("未找到排放係數")
except Exception as e:
    print(f"查詢失敗: {e}")
```

### 3. 批量查詢

```python
# 批量查詢多個產品
products = ['電力', '天然氣', '汽油']
for product in products:
    results = client.query(product)
    # 處理結果
```

### 4. 速率限制

```python
import time

# 避免過於頻繁的請求
for product in products:
    results = client.query(product)
    time.sleep(1)  # 等待 1 秒
```

---

## 📈 數據更新頻率

- **排放係數**：每年更新一次（通常 1 月）
- **API 緩存**：24 小時（可配置）
- **數據版本**：按年份區分

---

## 🔐 安全建議

1. **不要在代碼中硬編碼 API 金鑰**
   ```python
   # ❌ 不要這樣做
   api_key = "abc123def456"
   
   # ✅ 應該這樣做
   api_key = os.getenv('CFP_API_KEY')
   ```

2. **使用環境變數**
   ```bash
   export CFP_API_KEY="your-api-key"
   ```

3. **限制 API 金鑰權限**
   - 在環保署平台設置 IP 白名單
   - 定期輪換 API 金鑰

4. **監控 API 使用**
   - 記錄所有 API 調用
   - 監控異常流量

---

## 📞 支援

- **官方文檔**：https://data.moenv.gov.tw/
- **API 文檔**：https://data.moenv.gov.tw/api/
- **問題報告**：通過環保署平台提交

---

**最後更新**：2024-03-26
