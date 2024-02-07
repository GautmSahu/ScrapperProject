from celery import shared_task
from .models import ProxyModel
import requests

@shared_task
def scrap_and_save_data():
    try:
        response = requests.get("https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc")
        response_json = response.json()
        bulk_data = []
        if 'data' in response_json and len(response_json['data']) > 0:
            for proxy_data in response_json['data']:
                bulk_data.append(
                    ProxyModel(
                    ip=proxy_data.get('ip'),
                    port=proxy_data.get('port'),
                    protocol=proxy_data.get('protocols')[0] if proxy_data.get('protocols') else '',
                    country=proxy_data.get('country'),
                    uptime=round(proxy_data.get('uptime',0), 2)
                    ))
            ProxyModel.objects.bulk_create(bulk_data)
    except Exception as e:
        print(e)