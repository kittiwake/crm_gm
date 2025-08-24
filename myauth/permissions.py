# myauth/permissions.py

class Permissions:
    """Класс со всеми разрешениями системы"""
    # Графики
    VIEW_TIMETABLE = 'view_timetable'

    # Заказы
    VIEW_ORDER = 'view_order'
    CREATE_ORDER = 'create_order'
    EDIT_ORDER = 'edit_order'
    DELETE_ORDER = 'delete_order'
    SET_PLAN_DATE = 'set_plan_date'
    
    # Лиды
    VIEW_LEAD = 'view_lead'
    CREATE_LEAD = 'create_lead'
    EDIT_LEAD = 'edit_lead'
    DELETE_LEAD = 'delete_lead'
    
    # Сотрудники
    VIEW_EMPLOYEE = 'view_employee'
    EDIT_EMPLOYEE = 'edit_employee'
    MANAGE_EMPLOYEES = 'manage_employees'
    
    # Аналитика
    VIEW_ANALYTICS = 'view_analytics'
    EXPORT_DATA = 'export_data'
    
    # Системные
    ADMIN_ACCESS = 'admin_access'
    
    # Choices для админки/форм
    CHOICES = [
        (VIEW_TIMETABLE, 'Просмотр графика вывоза'),

        (VIEW_ORDER, 'Просмотр заказов'),
        (CREATE_ORDER, 'Создание заказов'),
        (EDIT_ORDER, 'Редактирование заказов'),
        (DELETE_ORDER, 'Удаление заказов'),
        (SET_PLAN_DATE, 'Установка плановой даты'),
        
        (VIEW_LEAD, 'Просмотр лидов'),
        (CREATE_LEAD, 'Создание лидов'),
        (EDIT_LEAD, 'Редактирование лидов'),
        (DELETE_LEAD, 'Удаление лидов'),
        
        (VIEW_EMPLOYEE, 'Просмотр сотрудников'),
        (EDIT_EMPLOYEE, 'Редактирование сотрудников'),
        (MANAGE_EMPLOYEES, 'Управление сотрудниками'),
        
        (VIEW_ANALYTICS, 'Просмотр аналитики'),
        (EXPORT_DATA, 'Экспорт данных'),
        
        (ADMIN_ACCESS, 'Административный доступ'),
    ]
    
    # Словарь для удобного доступа
    DICT = {code: name for code, name in CHOICES}
    
    # Группы разрешений (опционально)
    GROUPS = {
        'ORDERS': [VIEW_ORDER, CREATE_ORDER, EDIT_ORDER, DELETE_ORDER, SET_PLAN_DATE],
        'LEADS': [VIEW_LEAD, CREATE_LEAD, EDIT_LEAD, DELETE_LEAD],
        'EMPLOYEES': [VIEW_EMPLOYEE, EDIT_EMPLOYEE, MANAGE_EMPLOYEES],
        'ANALYTICS': [VIEW_ANALYTICS, EXPORT_DATA],
        'ADMIN': [ADMIN_ACCESS]
    }

# Короткие алиасы для удобства
PERMISSIONS = Permissions()