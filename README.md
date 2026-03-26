# VKama

Минимальная **Python библиотека для работы с VK API**.

VKama — это лёгкий sync-клиент для основных методов VK API.  
Подходит для:

- ботов
- парсеров
- рассылок
- автоматизации

Работает через обычный **access token**.

---

# Установка

Скопируйте библиотеку в проект:

```
vkama/
 ├─ __init__.py
 └─ vkama.py
```

или импортируйте из репозитория.

---

# Быстрый старт

```python
from vkama import VK

TOKEN = "your_vk_token"

vk = VK(TOKEN)

user = vk.users_get(user_ids="1")

print(user)
```

---

# Получение токена

Откройте ссылку:

```
https://oauth.vk.com/authorize?client_id=6287487&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=messages,groups,offline&response_type=token&v=5.199
```

После авторизации в адресной строке появится:

```
access_token=XXXXXXXX
```

Используйте этот токен в библиотеке.

---

# Примеры

## Получить пользователя

```python
vk.users_get(user_ids="1")
```

## Получить друзей

```python
vk.friends_get(user_id=1)
```

## Получить группы

```python
vk.groups_get(user_id=1)
```

## Получить участников группы

```python
vk.groups_get_members("python")
```

## Отправить сообщение

```python
vk.messages_send(
    user_id=123456,
    message="Привет!"
)
```

## Получить историю сообщений

```python
vk.messages_get_history(user_id=123456)
```

## Опубликовать пост

```python
vk.wall_post(
    owner_id=1,
    message="Hello VK!"
)
```

---

# Основные методы

VKama реализует базовые методы VK API:

### Users

```
users.get
users.search
```

### Friends

```
friends.get
```

### Groups

```
groups.get
groups.getMembers
```

### Messages

```
messages.send
messages.getHistory
```

### Wall

```
wall.post
wall.get
```

---

# Пример скрипта

Получение участников группы и отправка сообщения:

```python
from vkama import VK

vk = VK("TOKEN")

members = vk.groups_get_members("python")

for user in members["items"]:
    vk.messages_send(
        user_id=user,
        message="Привет!"
    )
```

---

# Обработка ошибок

Если VK API возвращает ошибку, библиотека выбрасывает исключение:

```
VK API Error {code}: {message}
```

---

# Требования

Python 3.7+

Зависимости:

```
requests
```

---

# Автор
Sargis Kazaryan
