import os
import django
import csv

# Настройка Django (важно сделать это до импорта моделей!)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from office.models.lead_model import LeadModel
from office.models.order_model import OrderModel

def import_leads():
    with open('for_import/leads.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
                LeadModel.objects.update_or_create(
                    contract=row['contract'],
                    defaults={
                        'contact_date': row['contact_date'],
                        'name': row['name'],
                        'product': row['product'],
                        'adress': row['adress'],
                        'phone': row['phone'],
                        'email': row['email']
                    }
                )
    print("Leads imported!")

def import_orders():
    with open('for_import/orders.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            lead = LeadModel.objects.get(id=int(row['lead']))

            OrderModel.objects.update_or_create(
                lead=lead,
                contract_date=row['contract_date'],
                defaults={
                    'company': row['company'],
                    'product': row['product'],
                    'phone': row['phone'],
                    'email': row['email'] if row['email'] != 'null' else None,
                    'personal_agree': row['personal_agree'],
                    'add_date': row['add_date'],
                    'term': row['term'],
                    'sum': float(row['sum']),
                    'prepayment': float(row['prepayment']),
                    'rassr': row['rassr'].lower() == 'true',
                    'beznal': row['beznal'].lower() == 'true',
                    'note': row['note'] if row['note'] else None,
                    'sumdeliv': float(row['sumdeliv']),
                    'sumcollect': float(row['sumcollect'])
                }
            )    
            print("Orders imported!")

if __name__ == '__main__':
    # import_leads()
    import_orders()