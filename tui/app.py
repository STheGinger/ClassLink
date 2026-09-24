from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

class TUI(App):
    TITLE = "ClassLink"
    ENABLE_COMMAND_PALETTE = False

    def compose(self) -> ComposeResult:
        yield Header(id="header", show_clock=True, time_format="%H:%M")
        #Note to self: Use `textual.containers` for grid-layout.
        #Note to self: Use `Grid()` and `container()` is my first idea.
        yield Footer(id="footer")

    def on_mount(self) -> None:
        self.theme = "flexoki"