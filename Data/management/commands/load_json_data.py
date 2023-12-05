import json
from Data.models import JsonToSQLModel
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Load JSON data into the JSONModel"
    
    def handle(self, *args, **kwargs):
        json_file_path = 'stock_market_data.json'
        
        with open(json_file_path, 'r') as json_file:
            json_data = json.load(json_file)
            
            for item in json_data:
                JsonToSQLModel.objects.create(
                    date = item['date'],
                    trade_code = item['trade_code'],
                    high = item['high'].replace(',', ''),
                    low = item['low'].replace(',', ''),
                    open = item['open'].replace(',', ''),
                    close = item['close'].replace(',', ''),
                    volume = item['volume'].replace(',', '')
                )
    
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))