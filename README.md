# rename_user_dirs

Переименовывает или создает (если нету) пользовательские папки и изменяет файлы `'.config/user-dirs.dirs'` и `'.config/user-dirs.locale'` на соответствующий язык.

На данный момент поддерживается всего 2 языка: `ru_RU` и `en_US`

## использование

```
rename_user_dirs lang_code_now lang_code_renaming
```

- **lang_code_now** - текущий код языка папок (можно посмотреть в `'.config/user-dirs.locale'`)
- **lang_code_renaming** - код языка на который хотите переименовать папки

Пример:

```
rename_user_dirs ru_RU en_US
```

Ищет папки из словаря ru_RU и переименовывает в en_US. Если не находить папку, создает его.
