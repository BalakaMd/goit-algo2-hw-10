# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = []


def create_schedule(subjects, teachers):
    uncovered = subjects.copy()
    schedule = []
    available_teachers = teachers.copy()

    while uncovered:
        best_teacher = None
        best_cover = set()

        # Шукаємо викладача, який покриває найбільшу кількість непокритих предметів
        for teacher in available_teachers:
            cover = teacher.can_teach_subjects & uncovered
            if len(cover) > len(best_cover):
                best_teacher = teacher
                best_cover = cover
            # У випадку рівної кількості предметів — вибираємо наймолодшого
            elif len(cover) == len(best_cover) and cover:
                if best_teacher is not None and teacher.age < best_teacher.age:
                    best_teacher = teacher
                    best_cover = cover

        # Якщо не знайдено викладача, який міг би покрити хоча б один непокритий предмет
        if best_teacher is None or len(best_cover) == 0:
            return None

            # Призначаємо викладачу ті предмети, які він може викладати із непокритих
        best_teacher.assigned_subjects = list(best_cover)
        schedule.append(best_teacher)
        # Видаляємо покриті предмети
        uncovered -= best_cover
        # Видаляємо викладача зі списку доступних, оскільки він вже використаний
        available_teachers.remove(best_teacher)

    return schedule


if __name__ == '__main__':
    # Множина предметів, які потрібно покрити
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    # Створення списку викладачів
    teachers = [
        Teacher('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com', {'Математика', 'Фізика'}),
        Teacher('Марія', 'Петренко', 38, 'm.petrenko@example.com', {'Хімія'}),
        Teacher('Сергій', 'Коваленко', 50, 's.kovalenko@example.com', {'Інформатика', 'Математика'}),
        Teacher('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com', {'Біологія', 'Хімія'}),
        Teacher('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com', {'Фізика', 'Інформатика'}),
        Teacher('Олена', 'Гриценко', 42, 'o.grytsenko@example.com', {'Біологія'})
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
