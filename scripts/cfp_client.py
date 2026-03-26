#!/usr/bin/env python3
"""
台灣碳足跡排放係數 API 客戶端
Taiwan CFP (Carbon Footprint) API Client

功能：
- 查詢排放係數
- 計算排放量
- 生成報告
- 數據緩存
"""

import json
import os
import sys
import argparse
import requests
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import logging

# 配置日誌
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/cfp.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# 創建必要的目錄
Path('logs').mkdir(exist_ok=True)
Path('data').mkdir(exist_ok=True)
Path('config').mkdir(exist_ok=True)


class CFPClient:
    """台灣碳足跡排放係數客戶端"""
    
    def __init__(self, config_path: str = 'config/api_config.json'):
        """初始化客戶端"""
        self.config = self._load_config(config_path)
        self.cache_file = 'data/cfp_cache.json'
        self.cache = self._load_cache()
        
    def _load_config(self, config_path: str) -> Dict:
        """載入配置文件"""
        if not os.path.exists(config_path):
            logger.warning(f"配置文件不存在: {config_path}，使用默認配置")
            return {
                'api_key': os.getenv('CFP_API_KEY', ''),
                'api_endpoint': 'https://data.moenv.gov.tw/api/v2/CFP_P_02',
                'timeout': 30,
                'retry_count': 3,
                'cache_enabled': True,
                'cache_ttl': 86400
            }
        
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _load_cache(self) -> Dict:
        """載入緩存數據"""
        if not os.path.exists(self.cache_file):
            return {'data': [], 'timestamp': None}
        
        try:
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                cache = json.load(f)
            
            # 檢查緩存是否過期
            if cache.get('timestamp'):
                cache_time = datetime.fromisoformat(cache['timestamp'])
                if datetime.now() - cache_time > timedelta(seconds=self.config['cache_ttl']):
                    logger.info("緩存已過期，將重新獲取數據")
                    return {'data': [], 'timestamp': None}
            
            return cache
        except Exception as e:
            logger.error(f"載入緩存失敗: {e}")
            return {'data': [], 'timestamp': None}
    
    def _save_cache(self, data: List[Dict]):
        """保存緩存數據"""
        cache = {
            'data': data,
            'timestamp': datetime.now().isoformat()
        }
        
        try:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(cache, f, ensure_ascii=False, indent=2)
            logger.info(f"緩存已保存: {len(data)} 筆記錄")
        except Exception as e:
            logger.error(f"保存緩存失敗: {e}")
    
    def fetch_data(self, limit: int = 1000, offset: int = 0) -> List[Dict]:
        """從 API 獲取排放係數數據"""
        if self.config['cache_enabled'] and self.cache['data']:
            logger.info(f"使用緩存數據: {len(self.cache['data'])} 筆記錄")
            return self.cache['data']
        
        if not self.config['api_key']:
            logger.error("API 金鑰未設置")
            return []
        
        url = self.config['api_endpoint']
        params = {
            'api_key': self.config['api_key'],
            'limit': limit,
            'offset': offset,
            'sort': 'ImportDate desc',
            'format': 'json'
        }
        
        try:
            logger.info(f"正在從 API 獲取數據...")
            response = requests.get(url, params=params, timeout=self.config['timeout'])
            response.raise_for_status()
            
            result = response.json()
            if result.get('success'):
                data = result.get('result', [])
                logger.info(f"成功獲取 {len(data)} 筆記錄")
                
                # 保存到緩存
                if self.config['cache_enabled']:
                    self._save_cache(data)
                
                return data
            else:
                logger.error(f"API 返回錯誤: {result.get('message', '未知錯誤')}")
                return []
        
        except requests.exceptions.RequestException as e:
            logger.error(f"API 請求失敗: {e}")
            return []
    
    def query(self, product: str, year: Optional[int] = None, fuzzy: bool = False) -> List[Dict]:
        """查詢排放係數"""
        data = self.fetch_data()
        
        if not data:
            logger.warning("沒有可用的數據")
            return []
        
        results = []
        product_lower = product.lower()
        
        for item in data:
            product_name = item.get('ProductName', '').lower()
            
            # 精確匹配或模糊匹配
            if fuzzy:
                match = product_lower in product_name or product_name in product_lower
            else:
                match = product_lower == product_name
            
            # 年份篩選
            if year and item.get('DataYear') != year:
                continue
            
            if match:
                results.append(item)
        
        return results
    
    def calculate(self, product: str, amount: float, unit: str = 'kWh') -> Tuple[float, str]:
        """計算排放量"""
        results = self.query(product)
        
        if not results:
            logger.error(f"找不到產品: {product}")
            return 0, "未找到排放係數"
        
        item = results[0]  # 使用第一個結果
        emission_factor = float(item.get('EmissionFactor', 0))
        factor_unit = item.get('Unit', '')
        
        # 計算排放量
        total_emission = amount * emission_factor
        
        # 轉換為公噸 CO2e
        if 'kg' in factor_unit:
            total_emission_ton = total_emission / 1000
        else:
            total_emission_ton = total_emission
        
        return total_emission_ton, factor_unit
    
    def test_connection(self) -> bool:
        """測試 API 連接"""
        logger.info("正在測試 API 連接...")
        
        data = self.fetch_data(limit=10)
        
        if data:
            logger.info("✓ API 連接成功")
            logger.info(f"✓ 已獲取 {len(data)} 筆排放係數記錄")
            logger.info("✓ 緩存已初始化")
            return True
        else:
            logger.error("✗ API 連接失敗")
            return False
    
    def clear_cache(self):
        """清除緩存"""
        try:
            if os.path.exists(self.cache_file):
                os.remove(self.cache_file)
                self.cache = {'data': [], 'timestamp': None}
                logger.info("✓ 緩存已清除")
            else:
                logger.info("緩存文件不存在")
        except Exception as e:
            logger.error(f"清除緩存失敗: {e}")


def main():
    """主函數"""
    parser = argparse.ArgumentParser(
        description='台灣碳足跡排放係數查詢工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例：
  # 查詢電力排放係數
  python cfp_client.py query --product "電力"
  
  # 計算排放量
  python cfp_client.py calculate --product "電力" --amount 1000 --unit "kWh"
  
  # 測試連接
  python cfp_client.py test
  
  # 清除緩存
  python cfp_client.py clear-cache
        '''
    )
    
    subparsers = parser.add_subparsers(dest='command', help='命令')
    
    # query 命令
    query_parser = subparsers.add_parser('query', help='查詢排放係數')
    query_parser.add_argument('--product', required=True, help='產品名稱')
    query_parser.add_argument('--year', type=int, help='數據年份')
    query_parser.add_argument('--fuzzy', action='store_true', help='模糊搜尋')
    
    # calculate 命令
    calc_parser = subparsers.add_parser('calculate', help='計算排放量')
    calc_parser.add_argument('--product', required=True, help='產品名稱')
    calc_parser.add_argument('--amount', type=float, required=True, help='數量')
    calc_parser.add_argument('--unit', default='kWh', help='單位')
    
    # test 命令
    subparsers.add_parser('test', help='測試 API 連接')
    
    # clear-cache 命令
    subparsers.add_parser('clear-cache', help='清除緩存')
    
    args = parser.parse_args()
    
    client = CFPClient()
    
    if args.command == 'query':
        results = client.query(args.product, args.year, args.fuzzy)
        
        if results:
            print(f"\n查詢結果: {args.product}\n")
            for item in results:
                print(f"  產品名稱: {item.get('ProductName')}")
                print(f"  排放係數: {item.get('EmissionFactor')} {item.get('Unit')}")
                print(f"  數據年份: {item.get('DataYear')}")
                print(f"  資料來源: {item.get('Source')}")
                print(f"  更新日期: {item.get('ImportDate')}")
                print()
        else:
            print(f"找不到產品: {args.product}")
    
    elif args.command == 'calculate':
        total_emission, unit = client.calculate(args.product, args.amount, args.unit)
        
        print(f"\n排放量計算結果\n")
        print(f"  產品: {args.product}")
        print(f"  使用量: {args.amount} {args.unit}")
        print(f"  排放係數: {unit}")
        print(f"  總排放量: {total_emission:.2f} 公噸 CO2e")
        print()
    
    elif args.command == 'test':
        client.test_connection()
    
    elif args.command == 'clear-cache':
        client.clear_cache()
    
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
