from .MS_Time_Measure_Node import MS_Time_Measure_Node
NODE_CLASS_MAPPINGS = {"MS Time Measure Node": MS_Time_Measure_Node}
__all__ = ["NODE_CLASS_MAPPINGS"]


# WEB_DIRECTORY = "./js"

# import os
# import importlib.util

# # Путь к директории 'nodes', где находятся модули нод
# nodes_dir = os.path.join(os.path.dirname(__file__), 'nodes')
# NODE_CLASS_MAPPINGS = {}
# NODE_DISPLAY_NAME_MAPPINGS = {}

# # Перебираем файлы в директории 'nodes'
# for filename in os.listdir(nodes_dir):
#     if filename.endswith('.py') and not filename.startswith('__'):
#         # Создаем полный путь к файлу
#         module_path = os.path.join(nodes_dir, filename)
        
#         # Загружаем модуль динамически
#         module_name = filename[:-3]  # Убираем .py
#         spec = importlib.util.spec_from_file_location(module_name, module_path)
#         module = importlib.util.module_from_spec(spec)
#         spec.loader.exec_module(module)
        
#         # Добавляем NODE_CLASS_MAPPINGS из каждого модуля в общий словарь
#         if hasattr(module, 'NODE_CLASS_MAPPINGS'):
#             NODE_CLASS_MAPPINGS.update(module.NODE_CLASS_MAPPINGS)

#         # Добавляем NODE_DISPLAY_NAME_MAPPINGS из каждого модуля в общий словарь, если они существуют
#         if hasattr(module, 'NODE_DISPLAY_NAME_MAPPINGS'):
#             NODE_DISPLAY_NAME_MAPPINGS.update(module.NODE_DISPLAY_NAME_MAPPINGS)

# # Экспортируем NODE_CLASS_MAPPINGS и NODE_DISPLAY_NAME_MAPPINGS
# __all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']