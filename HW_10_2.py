# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()  # Предмети, які призначені викладачу


def create_schedule(subjects, teachers):
    """
    Жадібний алгоритм для створення розкладу занять.
    Вибирає викладача, який може покрити найбільше непокритих предметів.
    При однаковій кількості предметів обирає наймолодшого.
    """
    # Копії для роботи алгоритму
    uncovered_subjects = subjects.copy()
    available_teachers = teachers.copy()
    selected_teachers = []

    while uncovered_subjects and available_teachers:
        best_teacher = None
        max_coverage = 0

        # Пошук найкращого викладача на поточному етапі
        for teacher in available_teachers:
            # Кількість предметів, які викладач може покрити з непокритих
            coverage = len(teacher.can_teach_subjects & uncovered_subjects)

            # Якщо цей викладач може покрити більше предметів
            if coverage > max_coverage:
                best_teacher = teacher
                max_coverage = coverage
            # Якщо кількість предметів однакова, обираємо наймолодшого
            elif coverage == max_coverage and coverage > 0:
                if teacher.age < best_teacher.age:
                    best_teacher = teacher

        # Якщо знайдено викладача, який може щось викладати
        if best_teacher and max_coverage > 0:
            # Призначаємо предмети викладачу
            subjects_to_assign = best_teacher.can_teach_subjects & uncovered_subjects
            best_teacher.assigned_subjects = subjects_to_assign

            # Оновлюємо множину непокритих предметів
            uncovered_subjects -= subjects_to_assign

            # Додаємо викладача до розкладу
            selected_teachers.append(best_teacher)

            # Видаляємо викладача зі списку доступних
            available_teachers.remove(best_teacher)
        else:
            # Немає викладачів, які можуть покрити залишкові предмети
            break

    # Повертаємо розклад тільки якщо всі предмети покриті
    if not uncovered_subjects:
        return selected_teachers
    else:
        return None


if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    # Створення списку викладачів
    teachers = [
        Teacher('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com',
                {'Математика', 'Фізика'}),
        Teacher('Марія', 'Петренко', 38, 'm.petrenko@example.com',
                {'Хімія'}),
        Teacher('Сергій', 'Коваленко', 50, 's.kovalenko@example.com',
                {'Інформатика', 'Математика'}),
        Teacher('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com',
                {'Біологія', 'Хімія'}),
        Teacher('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com',
                {'Фізика', 'Інформатика'}),
        Teacher('Олена', 'Гриценко', 42, 'o.grytsenko@example.com',
                {'Біологія'})
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        print("=" * 50)
        for i, teacher in enumerate(schedule, 1):
            print(f"{i}. {teacher.first_name} {teacher.last_name}, {teacher.age} років")
            print(f"   Email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(sorted(teacher.assigned_subjects))}\n")

        # Додаткова інформація
        total_subjects_covered = set()
        for teacher in schedule:
            total_subjects_covered.update(teacher.assigned_subjects)

        print("=" * 50)
        print(f"Загальна кількість викладачів у розкладі: {len(schedule)}")
        print(f"Покриті предмети: {', '.join(sorted(total_subjects_covered))}")
        print(f"Кількість покритих предметів: {len(total_subjects_covered)} з {len(subjects)}")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")

        # Розклад занять:
        # ==================================================
        # 1. Наталія Шевченко, 29 років
        #    Email: n.shevchenko@example.com
        #    Викладає предмети: Біологія, Хімія
        #
        # 2. Дмитро Бондаренко, 35 років
        #    Email: d.bondarenko@example.com
        #    Викладає предмети: Інформатика, Фізика
        #
        # 3. Олександр Іваненко, 45 років
        #    Email: o.ivanenko@example.com
        #    Викладає предмети: Математика
        #
        # ==================================================
        # Загальна кількість викладачів у розкладі: 3
        # Покриті предмети: Інформатика, Біологія, Математика, Фізика, Хімія
        # Кількість покритих предметів: 5 з 5
