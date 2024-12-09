def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0

            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Помилка обробки рядка: {line.strip()} (пропущено)")

            if count == 0:
                return 0, 0

            average = total / count
            return total, average

    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return 0, 0


file_path = "./salary_file.txt"
count_total, count_average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {count_total}, Середня заробітна плата: {count_average}")
