from datetime import datetime, timedelta
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from .models import OrderEtapModel, EtapModel, CehModel

class PlanCeh(ListView):
    model = OrderEtapModel
    template_name = 'planCeh.html'
    
    def get_queryset(self):
        # Получаем код цеха из URL
        ceh_code = self.kwargs.get('ceh_code')
        
        # Находим цех или возвращаем 404
        self.ceh = get_object_or_404(CehModel, code=ceh_code)
        
        # Определяем диапазон дат
        yesterday = datetime.now().date() - timedelta(days=1)
        end_date = yesterday + timedelta(days=7)
        
        # Фильтруем записи по цеху и диапазону дат
        queryset = super().get_queryset().filter(
            etap__ceh=self.ceh,  # Фильтр по цеху через этап
            date__gte=yesterday,
            date__lt=end_date
        ).select_related('order', 'etap', 'responsible', 'etap__ceh')
        print(queryset)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Вчерашняя дата
        yesterday = datetime.now().date() - timedelta(days=1)
        
        # Генерируем 7 дат начиная со вчера
        dates = []
        for i in range(7):
            current_date = yesterday + timedelta(days=i)
            dates.append({
                'full': current_date,
                'day_month': current_date.strftime('%d.%m'),
                'day': current_date.day,
                'month': current_date.month
            })
        
        # Получаем этапы только для этого цеха
        etap_list = EtapModel.objects.filter(ceh=self.ceh).order_by('subsequence')
        
        # Группируем OrderEtapModel по этапам и датам
        etap_orders = {}
        for order_etap in context['object_list']:
            key = (order_etap.etap.id, order_etap.date)
            if key not in etap_orders:
                etap_orders[key] = []
            etap_orders[key].append(order_etap)
        
        print(etap_orders)
        context['dates'] = dates
        context['etap_list'] = etap_list
        context['etap_orders'] = etap_orders
        context['current_ceh'] = self.ceh
        
        return context