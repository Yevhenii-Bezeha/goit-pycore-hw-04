def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats = []

            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cats.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
                except ValueError:
                    print(f"Помилка обробки рядка: {line.strip()} (пропущено)")

            return cats

    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return []


file_path = "./cats_file.txt"
cats_info = get_cats_info(file_path)
print(cats_info)
