# Zadanie 1 – Usuwanie zadań (Raw SQL)
# Dodaj do aplikacji app_raw_sql.py opcję menu "Usuń zadanie". Zaimplementuj funkcję
# usun_zadanie(id_zadania) w database_raw.py, która użyje zapytania DELETE FROM
# zadania WHERE id = ?.

<!-- # CO ZROBIŁAM:
# 1. W database_raw.py dodałam funkcję usun_zadanie(id_zadania).
# 2. Funkcja używa DELETE FROM zadania WHERE id = ?, aby usunąć zadanie
#    o konkretnym ID.
# 3. (id_zadania,) przekazuje wartość do placeholdera ? w zapytaniu SQL.
# 4. conn.commit() zapisuje usunięcie zadania w bazie.
#
# 5. W app_raw_sql.py dodałam nową opcję w menu: "Usuń zadanie".
# 6. Użytkownik podaje ID zadania, które jest zamieniane na int.
# 7. Następnie wywołuję db.usun_zadanie(id_zadania), czyli funkcję
#    znajdującą się w database_raw.py.
# 8. Dodałam ValueError na wypadek wpisania czegoś innego niż liczba.
 -->

