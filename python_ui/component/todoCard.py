from nicegui import ui
from services.api import SendData


STATUS_KEY = "status_code"

INK = "#1B2430"        # near-black navy, primary text / display
PAPER = "#F7F4EC"      # warm paper background
RULE = "#DDD6C4"       # faint ruled-line color
BRASS = "#B8862E"      # accent: button / focus / signature checkmark
SAGE = "#5C7A6B"       # success
CLAY = "#B5544B"  

    
def todoCard():
    todo = {"text": ""}
 
    def send():
        text = todo["text"].strip()
        if not text:
            ui.notify("Write something before adding it", color=CLAY)
            return
 
        data = SendData(text)
        print("data:", data)
 
        if data.get(STATUS_KEY) == 200:
            ui.notify(data.get("message", "Added to the list"), color=SAGE)
            todo["text"] = ""
            text_input.set_value("")
            check_mark.classes(add="todo-pop", remove="todo-pop-reset")
            ui.timer(0.01, lambda: check_mark.classes(add="todo-pop-reset"), once=True)
        else:
            ui.notify(data.get("message", "Todo not sent!"), color=CLAY)
 
    with ui.column().classes("todo-index-card"):
        with ui.row().classes("items-center gap-3 w-full").style("justify-content: space-between;"):
            ui.label("Today's list").classes("todo-eyebrow")
            check_mark = ui.label("✓").classes("todo-check")
 
        ui.label("What needs doing?").classes("todo-title")
 
        text_input = ui.input(
            placeholder="Type a task, press enter",
            validation={"Keep it under 100 characters": lambda value: len(value) < 100},
        ).props("borderless").classes("todo-input")
        text_input.bind_value(todo, "text")
        text_input.on("keydown.enter", lambda: send())
 
        ui.button("Add to list", on_click=send).classes("todo-button").props("unelevated")
 
 
def inject_styles():
    ui.add_head_html(f"""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
    <style>
        body {{
            background: {PAPER};
            background-image:
                repeating-linear-gradient(
                    to bottom,
                    transparent 0,
                    transparent 39px,
                    {RULE} 39px,
                    {RULE} 40px
                );
            font-family: 'Inter', sans-serif;
        }}
 
        .todo-index-card {{
            background: {PAPER};
            border: 1px solid {INK}22;
            border-radius: 4px;
            box-shadow: 0 1px 0 {INK}11, 0 12px 30px -12px {INK}33;
            padding: 2.25rem 2rem 2rem 2rem;
            width: 100%;
            max-width: 30rem;
            position: relative;
        }}
 
        .todo-index-card::before {{
            content: "";
            position: absolute;
            left: 1.6rem;
            top: 0;
            bottom: 0;
            width: 1px;
            background: {CLAY}55;
        }}
 
        .todo-eyebrow {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.7rem;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: {INK}99;
        }}
 
        .todo-check {{
            font-family: 'JetBrains Mono', monospace;
            color: {SAGE};
            font-size: 1.1rem;
            opacity: 0.25;
            transition: none;
        }}
        .todo-check.todo-pop {{
            opacity: 1;
            transform: scale(1.4);
            transition: transform 0.25s ease, opacity 0.25s ease;
        }}
        .todo-check.todo-pop-reset {{
            transform: scale(1);
            opacity: 0.25;
            transition: transform 0.6s ease, opacity 0.6s ease;
        }}
 
        .todo-title {{
            font-family: 'Fraunces', serif;
            font-weight: 500;
            font-size: 1.9rem;
            color: {INK};
            margin: 0.9rem 0 1.4rem 0;
            padding-left: 0.6rem;
        }}
 
        .todo-input {{
            padding-left: 0.6rem;
            font-family: 'Inter', sans-serif;
            font-size: 1.05rem;
            color: {INK};
            border-bottom: 1px solid {RULE} !important;
        }}
        .todo-input .q-field__control {{
            border-bottom: none;
        }}
 
        .todo-button {{
            margin-top: 1.5rem;
            margin-left: 0.6rem;
            background: {BRASS} !important;
            color: {PAPER} !important;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.8rem;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            border-radius: 3px;
            padding: 0.55rem 1.1rem;
            align-self: flex-start;
        }}
        .todo-button:hover {{
            filter: brightness(1.08);
        }}
    </style>
    """)
 