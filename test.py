import time


today = time.strftime("%I")

if today == 'Saturday':
    print('Party')
elif today == 'Sunday':
    print('Отдыхай')
else:
    print('Работай')

