import requests
from dotenv import load_dotenv
import os


load_dotenv()
PAYSTACK_SECRET_KEY = os.getenv('PAYSTACK_SECRET_KEY')

PAYSTACK_API_URL = 'https://api.paystack.co/'


def get_products():
    try:
        response = requests.get(f"{PAYSTACK_API_URL}product",
                                headers={
            'Authorization': f'Bearer {PAYSTACK_SECRET_KEY}'
        })
    except Exception as e:
        response={}
    return response.json()['data']


def get_product(_id):
    response = requests.get(f"{PAYSTACK_API_URL}product/{_id}",
                            headers={
        'Authorization': f'Bearer {PAYSTACK_SECRET_KEY}'
    })
    return response.json()


if __name__ == "__main__":
    for product in get_products():
        if product['files']:
            dic = product['files'][0]['path']
            #print(dic)
            pass

    dictkeys = (['digital_assets',
                'integration',
                'name', 'description',
                'product_code',
                'price', 'currency',
                'quantity','quantity_sold',
                'type', 'files',
                'file_path',
                'is_shippable',
                'shipping_fields', 'unlimited',
                'domain', 'active', 'features',

                'in_stock', 'metadata', 'slug', 'success_message', 'redirect_url', 'split_code', 'notification_emails',
                'minimum_orderable', 'maximum_orderable', 
                'low_stock_alert', 'stock_threshold', 
                'expires_in', 'id', 'createdAt', 'updatedAt'])
    p = ['id',
        'name',
        'description',
        'product_code',
        'slug',
        'currency',
        'price',
        'quantity',
        'quantity_sold',
        'active',
        'domain',
        'type',
        'in_stock',
        'unlimited',
        'metadata',
        'files',
        'success_message',
        'redirect_url',
        'split_code',
        'notification_emails',
        'minimum_orderable',
        'maximum_orderable',
        'createdAt',
        'updatedAt',
        'digital_assets',
        'variant_options',
        'is_shippable',
        'shipping_fields',
        'integration',
        'low_stock_alert']
