# QUICK_START.md - 快速參考卡

## 🎯 30 秒快速開始

### 第一步：設置 API 金鑰

```bash
# 編輯配置文件
nano config/api_config.json

# 填入你的 API 金鑰
{
  "api_key": "your-api-key-here"
}
```

### 第二步：測試連接

```bash
python scripts/cfp_client.py test
```

### 第三步：開始查詢

```bash
# 查詢排放係數
python scripts/cfp_client.py query --product "電力"

# 計算排放量
python scripts/cfp_client.py calculate --product "電力" --amount 1000 --unit "kWh"
```

---

## 📋 常用命令

### 查詢

```bash
# 查詢單個產品
python scripts/cfp_client.py query --product "電力"

# 按年份查詢
python scripts/cfp_client.py query --product "電力" --year 2024

# 模糊搜尋
python scripts/cfp_client.py query --product "氣" --fuzzy
```

### 計算

```bash
# 計算排放量
python scripts/cfp_client.py calculate --product "電力" --amount 1000 --unit "kWh"

# 計算天然氣排放
python scripts/cfp_client.py calculate --product "天然氣" --amount 100 --unit "m³"

# 計算汽油排放
python scripts/cfp_client.py calculate --product "汽油" --amount 50 --unit "L"
```

### 維護

```bash
# 測試連接
python scripts/cfp_client.py test

# 清除緩存
python scripts/cfp_client.py clear-cache
```

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

---

## 💡 快速計算

### 家庭月均用電 300 度

```bash
python scripts/cfp_client.py calculate --product "電力" --amount 300 --unit "kWh"
# 結果：0.15 公噸 CO2e
```

### 月均加油 50 公升

```bash
python scripts/cfp_client.py calculate --product "汽油" --amount 50 --unit "L"
# 結果：0.12 公噸 CO2e
```

### 冬季月均用氣 100 立方米

```bash
python scripts/cfp_client.py calculate --product "天然氣" --amount 100 --unit "m³"
# 結果：0.20 公噸 CO2e
```

---

## 🐍 Python 快速示例

```python
from cfp_client import CFPClient

client = CFPClient()

# 查詢
results = client.query('電力')
print(results[0]['EmissionFactor'])

# 計算
emission, _ = client.calculate('電力', 1000, 'kWh')
print(f"{emission:.2f} 公噸 CO2e")
```

---

## ❓ 常見問題

**Q: 如何獲取 API 金鑰？**  
A: 訪問 https://data.moenv.gov.tw/ 註冊並申請

**Q: 排放係數多久更新？**  
A: 每年更新一次（通常 1 月）

**Q: 支援離線使用嗎？**  
A: 可以，首次查詢後會緩存數據

**Q: 如何批量計算？**  
A: 使用 `scripts/cfp_batch.py` 或 Python 循環

---

## 📚 更多資源

- 📖 [READER.md](READER.md) - 完整使用指南
- 📡 [API_GUIDE.md](API_GUIDE.md) - API 詳細文檔
- 💡 [EXAMPLES.md](EXAMPLES.md) - 實際使用案例

---

**需要幫助？** 查看 [READER.md](READER.md) 的故障排除部分。
