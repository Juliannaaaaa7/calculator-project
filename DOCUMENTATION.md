\# Документація API

\## Модуль Calculator

\### Функція add()

``````python

def add(a, b):

&nbsp;"""Додавання двох чисел"""

&nbsp;return a + b

``````

\*\*Параметри:\*\*

\- `a` (float): Перше число

\- `b` (float): Друге число

\*\*Повертає:\*\*

\- `float`: Сума двох чисел

\*\*Приклад:\*\*

``````python

result = add(5, 3)

print(result) # Виведе: 8

``````

\### Функція divide()

``````python

def divide(a, b):

&nbsp;"""Ділення двох чисел"""

&nbsp;if b != 0:

&nbsp;return a / b

&nbsp;else:

&nbsp;return "Помилка: ділення на нуль!"

``````

\*\*Параметри:\*\*

\- `a` (float): Ділене

\- `b` (float): Дільник

\*\*Повертає:\*\*

\- `float`: Результат ділення, або помилка якщо b = 0

\*\*Приклад:\*\*

``````python

result = divide(10, 2)

print(result) # Виведе: 5.0

