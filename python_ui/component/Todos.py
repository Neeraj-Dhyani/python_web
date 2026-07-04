from nicegui import ui
from services.api import all_Todo, delete_todo ,edit_todo, complete_todo

STATUS_KEY = "status_code"
 
 
def _ok(res):
    return res.get(STATUS_KEY) == 200

@ui.refreshable
def all_Todos():
    todos = all_Todo()  
 
    def delete_this(id):
        res = delete_todo(id)
        if _ok(res):
            ui.notify(res.get("data", "Deleted"))
            all_Todos.refresh()
        else:
            ui.notify(res.get("message", "Error deleting todo"), color="negative")
 
    def complete_this(id):
        res = complete_todo(id)
        if _ok(res):
            ui.notify(res.get("data", "Updated"))
        else:
            ui.notify(res.get("message", "Error updating todo"), color="negative")
        all_Todos.refresh()
 
    if not todos or not todos.get("data"):
        ui.label("No todos yet — add one above!").classes("text-gray-500 italic")
        return
 
    for todo in todos["data"]:
        state = {"text": todo["title"]}
 
        with ui.card().classes("w-full p-4 gap-2 relative"):
            ui.badge(
                "Complete" if todo["complete"] else "Incomplete",
                color="green" if todo["complete"] else "red",
            ).classes("absolute top-2 left-2")
 
            label = ui.label(state["text"]).classes("mt-4")
            input_field = ui.input(value=state["text"]).bind_value(state, "text")
            input_field.set_visibility(False)
 
            def save(todo=todo, input_field=input_field, label=label, state=state):
                res = edit_todo(todo["id"], state["text"])
                if _ok(res):
                    ui.notify(res.get("message", "Saved"))
                    label.set_text(state["text"])
                    input_field.set_visibility(False)
                    label.set_visibility(True)
                    save_btn.set_visibility(False)
                    edit_btn.set_visibility(True)
                else:
                    ui.notify(res.get("message", "Error saving"), color="negative")
 
            def start_edit(label=label, input_field=input_field):
                label.set_visibility(False)
                input_field.set_visibility(True)
                save_btn.set_visibility(True)
                edit_btn.set_visibility(False)
 
            with ui.row().classes("gap-2 mt-2"):
                edit_btn = ui.button("Edit", on_click=start_edit).props("flat")
                save_btn = ui.button("Save", on_click=save).props("flat color=primary")
                save_btn.set_visibility(False)
                ui.button(
                    "Complete", on_click=lambda e, id=todo["id"]: complete_this(id)
                ).props("flat color=green")
                ui.button(
                    "Delete", on_click=lambda e, id=todo["id"]: delete_this(id)
                ).props("flat color=red")