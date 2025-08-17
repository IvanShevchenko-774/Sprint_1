new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006'] 


completed_tasks.append(new_tasks.pop(-1)) # выполнение задачи task_005, перенос в список completed_tasks
new_tasks.remove('task_007') # удаление задачи из списка
new_tasks[0], new_tasks[-1] = new_tasks[-1], new_tasks[0] # изменение приоритета задачи, перемещение вначало списка

print (f'У задачи {new_tasks[0]} поднят приоритет, ее нужно взять следующей')
