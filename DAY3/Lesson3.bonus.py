total_seconds = int(input('Введите количество секунд: '))

hours = total_seconds // 3600
minutes = (total_seconds // 60) - (hours*60)
seconds = total_seconds % 60
print(f"{hours}:{minutes}:{seconds}")
