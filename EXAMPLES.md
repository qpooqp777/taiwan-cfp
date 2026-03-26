# EXAMPLES.md - 台灣碳足跡排放係數使用示例

## 📋 目錄

1. [基本查詢](#基本查詢)
2. [排放量計算](#排放量計算)
3. [企業碳盤查](#企業碳盤查)
4. [產品碳足跡](#產品碳足跡)
5. [數據分析](#數據分析)

---

## 基本查詢

### 示例 1：查詢單個產品排放係數

**需求**：查詢 2024 年電力的碳足跡排放係數

**命令**：
```bash
python scripts/cfp_client.py query --product "電力" --year 2024
```

**輸出**：
```
查詢結果: 電力

  產品名稱: 電力
  排放係數: 0.509 kg CO2e/kWh
  數據年份: 2024
  資料來源: 台灣電力公司
  更新日期: 2024-01-15
```

### 示例 2：模糊搜尋

**需求**：搜尋所有包含「氣」的產品

**命令**：
```bash
python scripts/cfp_client.py query --product "氣" --fuzzy
```

**輸出**：
```
查詢結果: 氣

  產品名稱: 天然氣
  排放係數: 2.04 kg CO2e/m³
  數據年份: 2024
  資料來源: 中油
  更新日期: 2024-01-15

  產品名稱: 液化石油氣
  排放係數: 3.02 kg CO2e/kg
  數據年份: 2024
  資料來源: 中油
  更新日期: 2024-01-15
```

### 示例 3：查詢多個產品

**需求**：查詢主要能源產品的排放係數

**Python 代碼**：
```python
from cfp_client import CFPClient

client = CFPClient()

products = ['電力', '天然氣', '汽油', '柴油']

for product in products:
    results = client.query(product)
    if results:
        item = results[0]
        print(f"{item['ProductName']}: {item['EmissionFactor']} {item['Unit']}")
```

**輸出**：
```
電力: 0.509 kg CO2e/kWh
天然氣: 2.04 kg CO2e/m³
汽油: 2.31 kg CO2e/L
柴油: 2.68 kg CO2e/L
```

---

## 排放量計算

### 示例 1：計算家庭用電排放量

**需求**：計算家庭月均用電 300 度的碳足跡

**命令**：
```bash
python scripts/cfp_client.py calculate --product "電力" --amount 300 --unit "kWh"
```

**輸出**：
```
排放量計算結果

  產品: 電力
  使用量: 300 kWh
  排放係數: kg CO2e/kWh
  總排放量: 0.15 公噸 CO2e
```

**解釋**：
- 300 kWh × 0.509 kg CO2e/kWh = 152.7 kg CO2e = 0.153 公噸 CO2e
- 相當於種植 7-8 棵樹一年的吸收量

### 示例 2：計算汽車燃油排放量

**需求**：計算月均加油 50 公升汽油的碳足跡

**命令**：
```bash
python scripts/cfp_client.py calculate --product "汽油" --amount 50 --unit "L"
```

**輸出**：
```
排放量計算結果

  產品: 汽油
  使用量: 50 L
  排放係數: kg CO2e/L
  總排放量: 0.12 公噸 CO2e
```

**解釋**：
- 50 L × 2.31 kg CO2e/L = 115.5 kg CO2e = 0.116 公噸 CO2e

### 示例 3：計算天然氣供暖排放量

**需求**：計算冬季月均用氣 100 立方米的碳足跡

**命令**：
```bash
python scripts/cfp_client.py calculate --product "天然氣" --amount 100 --unit "m³"
```

**輸出**：
```
排放量計算結果

  產品: 天然氣
  使用量: 100 m³
  排放係數: kg CO2e/m³
  總排放量: 0.20 公噸 CO2e
```

---

## 企業碳盤查

### 示例 1：小型辦公室年度碳盤查

**需求**：計算 20 人辦公室的年度碳排放

**數據**：
```csv
項目,數量,單位
辦公室用電,50000,kWh
供暖用氣,5000,m³
員工通勤用油,2000,L
廢棄物處理,10,ton
```

**Python 代碼**：
```python
from cfp_client import CFPClient

client = CFPClient()

# 定義排放源
emissions = [
    ('電力', 50000, 'kWh'),
    ('天然氣', 5000, 'm³'),
    ('汽油', 2000, 'L'),
]

total_emission = 0

print("辦公室碳盤查報告\n")
print("排放源 | 數量 | 單位 | 排放係數 | 排放量(ton CO2e)")
print("-" * 60)

for product, amount, unit in emissions:
    emission_ton, factor_unit = client.calculate(product, amount, unit)
    total_emission += emission_ton
    print(f"{product:6} | {amount:6} | {unit:4} | {factor_unit:12} | {emission_ton:6.2f}")

print("-" * 60)
print(f"總排放量: {total_emission:.2f} 公噸 CO2e")
print(f"人均排放: {total_emission/20:.2f} 公噸 CO2e/人")
```

**輸出**：
```
辦公室碳盤查報告

排放源 | 數量 | 單位 | 排放係數 | 排放量(ton CO2e)
------------------------------------------------------------
電力   |  50000 | kWh  | kg CO2e/kWh | 25.45
天然氣 |   5000 | m³   | kg CO2e/m³  | 10.20
汽油   |   2000 | L    | kg CO2e/L   |  4.62
------------------------------------------------------------
總排放量: 40.27 公噸 CO2e
人均排放: 2.01 公噸 CO2e/人
```

### 示例 2：製造企業碳盤查

**需求**：計算水泥製造企業的年度碳排放

**數據**：
```
生產水泥: 10,000 ton
電力消耗: 100,000 kWh
天然氣消耗: 50,000 m³
```

**Python 代碼**：
```python
from cfp_client import CFPClient

client = CFPClient()

# 製造企業排放源
emissions = [
    ('水泥', 10000, 'kg'),      # 生產排放
    ('電力', 100000, 'kWh'),    # 能源排放
    ('天然氣', 50000, 'm³'),    # 燃料排放
]

total_emission = 0

print("水泥製造企業碳盤查報告\n")

for product, amount, unit in emissions:
    emission_ton, _ = client.calculate(product, amount, unit)
    total_emission += emission_ton
    print(f"{product}: {amount} {unit} → {emission_ton:.2f} 公噸 CO2e")

print(f"\n總排放量: {total_emission:.2f} 公噸 CO2e")
print(f"單位產品排放: {total_emission/10000:.2f} 公噸 CO2e/ton 水泥")
```

**輸出**：
```
水泥製造企業碳盤查報告

水泥: 10000 kg → 9.20 公噸 CO2e
電力: 100000 kWh → 50.90 公噸 CO2e
天然氣: 50000 m³ → 102.00 公噸 CO2e

總排放量: 162.10 公噸 CO2e
單位產品排放: 0.0162 公噸 CO2e/ton 水泥
```

---

## 產品碳足跡

### 示例 1：計算產品生命週期碳足跡

**需求**：計算 1 公斤水泥的完整碳足跡

**生命週期階段**：
1. 原料開採：0.1 kg CO2e
2. 製造：0.92 kg CO2e（排放係數）
3. 運輸：0.05 kg CO2e
4. 使用：0 kg CO2e
5. 廢棄：0.02 kg CO2e

**Python 代碼**：
```python
from cfp_client import CFPClient

client = CFPClient()

# 計算製造階段排放
manufacturing_emission, _ = client.calculate('水泥', 1, 'kg')

# 其他階段排放
other_stages = {
    '原料開採': 0.1,
    '運輸': 0.05,
    '廢棄': 0.02
}

total_emission = manufacturing_emission

print("水泥產品生命週期碳足跡\n")
print(f"製造: {manufacturing_emission:.2f} kg CO2e")

for stage, emission in other_stages.items():
    total_emission += emission
    print(f"{stage}: {emission:.2f} kg CO2e")

print(f"\n總碳足跡: {total_emission:.2f} kg CO2e/kg 水泥")
```

**輸出**：
```
水泥產品生命週期碳足跡

製造: 0.92 kg CO2e
原料開採: 0.10 kg CO2e
運輸: 0.05 kg CO2e
廢棄: 0.02 kg CO2e

總碳足跡: 1.09 kg CO2e/kg 水泥
```

---

## 數據分析

### 示例 1：能源排放對比

**需求**：比較不同能源的排放強度

**Python 代碼**：
```python
from cfp_client import CFPClient

client = CFPClient()

# 查詢主要能源排放係數
energy_sources = ['電力', '天然氣', '汽油', '柴油']

print("能源排放係數對比\n")
print("能源 | 排放係數 | 單位")
print("-" * 40)

for source in energy_sources:
    results = client.query(source)
    if results:
        item = results[0]
        print(f"{item['ProductName']:6} | {item['EmissionFactor']:8.2f} | {item['Unit']}")
```

**輸出**：
```
能源排放係數對比

能源 | 排放係數 | 單位
----------------------------------------
電力   |     0.51 | kg CO2e/kWh
天然氣 |     2.04 | kg CO2e/m³
汽油   |     2.31 | kg CO2e/L
柴油   |     2.68 | kg CO2e/L
```

### 示例 2：年度排放趨勢

**需求**：分析過去 5 年的電力排放係數變化

**Python 代碼**：
```python
from cfp_client import CFPClient

client = CFPClient()

print("電力排放係數年度變化\n")
print("年份 | 排放係數 | 變化")
print("-" * 30)

previous_factor = None

for year in range(2020, 2025):
    results = client.query('電力', year=year)
    if results:
        factor = results[0]['EmissionFactor']
        change = ""
        if previous_factor:
            change = f"{(factor - previous_factor)/previous_factor*100:+.1f}%"
        print(f"{year} | {factor:8.3f} | {change}")
        previous_factor = factor
```

**輸出**：
```
電力排放係數年度變化

年份 | 排放係數 | 變化
------------------------------
2020 | 0.533 |
2021 | 0.528 | -0.9%
2022 | 0.520 | -1.5%
2023 | 0.515 | -1.0%
2024 | 0.509 | -1.2%
```

---

## 🎯 最佳實踐

### 1. 數據驗證

```python
# 驗證查詢結果
results = client.query('電力')
if not results:
    print("警告：未找到排放係數")
elif len(results) > 1:
    print(f"警告：找到 {len(results)} 個結果，使用第一個")
```

### 2. 單位轉換

```python
# 確保單位一致
# 1 MWh = 1000 kWh
# 1 ton = 1000 kg
# 1 m³ = 1000 L

amount_kwh = 1000  # kWh
amount_mwh = amount_kwh / 1000  # MWh
```

### 3. 精度控制

```python
# 保留適當的小數位
emission = 152.7 kg CO2e
print(f"排放量: {emission:.2f} kg CO2e")  # 0.15 ton CO2e
```

---

**最後更新**：2024-03-26
