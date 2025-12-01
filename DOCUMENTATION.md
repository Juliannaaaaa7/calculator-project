# Документація проекту

## Модуль greetings

### Функція greet_user(name)
```python
def greet_user(name):
    """Виводить персоналізоване привітання для користувача."""
    from datetime import datetime
    time = datetime.now().strftime("%H:%M:%S")
    print(f"Hello, {name}! Current time: {time}")
Приклад:
greet_user("Anna")
# Виведе: Hello, Anna! Current time: 10:22:37
Функція greet_from_file(filename)
def greet_from_file(filename):
    """Зчитує імена з файлу та вітає кожного користувача."""
    from datetime import datetime
    with open(filename, "r", encoding="utf-8") as f:
        names = [line.strip() for line in f if line.strip()]
    time = datetime.now().strftime("%H:%M:%S")
    for name in names:
        print(f"Hello, {name}! Current time: {time}")
Приклад:

greet_from_file("data/names.txt")
# Виведе:
# Hello, Anna! Current time: 10:22:37
# Hello, Petro! Current time: 10:22:37
# Hello, Maria! Current time: 10:22:37

---

Щоб додати посилання на `DOCUMENTATION.md` у `README.md`, у відповідному місці напиши:

```markdown
## Документація
Докладний опис функцій доступний у [DOCUMENTATION.md](DOCUMENTATION.md)
