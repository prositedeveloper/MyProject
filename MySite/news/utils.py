from datetime import datetime

class ContextMixin:
    """Миксин с дополнительными данными для контекста"""
    
    # Можно переопределить в дочернем классе
    extra_context = {}
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Добавляем текущий год
        context['current_year'] = datetime.now().year
        
        # Добавляем текущее время
        context['current_time'] = datetime.now().strftime('%H:%M:%S')
        
        # Добавляем дополнительные данные из атрибута
        if hasattr(self, 'extra_context'):
            context.update(self.extra_context)
        
        return context