import json
import os
import datetime

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            notes = json.load(file)
        return notes
    else:
        return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note(title, message):
    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": message,
        "timestamp": str(datetime.datetime.now())
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена\n")

def list_notes(date_filter=None):
    notes = load_notes()
    if date_filter:
        filtered_notes = [note for note in notes if date_filter in note['timestamp']]
        if not filtered_notes:
            print("Заметок с указанной датой не найдено.\n")
            return
        notes = filtered_notes
    
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Дата/время: {note['timestamp']}")
        print(f"Содержание: {note['message']}\n")

def edit_note(note_id, new_title, new_message):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = new_title
            note["message"] = new_message
            note["timestamp"] = str(datetime.datetime.now())
            save_notes(notes)
            print("Заметка успешно отредактирована\n")
            return
    print("Заметка с указанным ID не найдена\n")

def delete_note(note_id):
    notes = load_notes()
    updated_notes = [note for note in notes if note["id"] != note_id]
    if len(updated_notes) < len(notes):
        save_notes(updated_notes)
        print("Заметка успешно удалена\n")
    else:
        print("Заметка с указанным ID не найдена\n")

def main():
    while True:
        print("1. Добавить заметку")
        print("2. Просмотреть список заметок")
        print("3. Просмотреть список заметок по дате")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Выйти")

        choice = input("Введите номер команды: \n")

        if choice == "1":
            title = input("Введите заголовок заметки: \n")
            message = input("Введите тело заметки: \n")
            add_note(title, message)
        elif choice == "2":
            list_notes()
        elif choice == "3":
            date_filter = input("Введите дату (гггг-мм-дд) для фильтрации заметок: \n")
            list_notes(date_filter)
        elif choice == "4":
            note_id = int(input("Введите ID заметки для редактирования: \n"))
            new_title = input("Введите новый заголовок заметки: \n")
            new_message = input("Введите новое тело заметки: \n")
            edit_note(note_id, new_title, new_message)
        elif choice == "5":
            note_id = int(input("Введите ID заметки для удаления: \n"))
            delete_note(note_id)
        elif choice == "6":
            break
        else:
            print("Неверный выбор, попробуйте ещё раз.")
            print("-" * 60)

if __name__ == "__main__":
    main()
