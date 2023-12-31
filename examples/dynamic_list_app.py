import random
from fwif import BaseApp, Component, Color


class App(BaseApp):
    def __init__(self):
        super().__init__()
        self.selected_index = -1

    def setup_keybindings(self):
        super().setup_keybindings()
        self.keybindings.add('a', self.add_item)
        self.keybindings.add('d', self.delete_item)
        self.keybindings.add('D', self.delete_all)
        # FIXME: keybinding sequences not working, only the first key is
        # self.keybindings.add('dG', self.delete_from_selection_to_last)
        # self.keybindings.add('dgg', self.delete_from_selection_to_first)
        self.keybindings.add('g', self.select_first)
        self.keybindings.add('G', self.select_last)
        self.keybindings.add('k', self.move_selection_up)
        self.keybindings.add('j', self.move_selection_down)
        self.keybindings.add('K', self.move_item_up)
        self.keybindings.add('J', self.move_item_down)
        self.keybindings.add('c', self.change_color)

    def change_color(self):
        if self.selected_index >= 0 and len(self.components) > 0:
            component = self.components[self.selected_index]
            component.background = self.random_color()
            self.update_items()

    def delete_from_selection_to_first(self):
        if self.selected_index >= 0 and len(self.components) > 0:
            for _ in range(self.selected_index + 1):
                self.components.pop(0)
            self.selected_index = 0
            self.update_items()

    def delete_from_selection_to_last(self):
        if self.selected_index >= 0 and len(self.components) > 0:
            for _ in range(self.selected_index, len(self.components)):
                self.components.pop()
            self.selected_index = min(
                self.selected_index, len(self.components) - 1)
            self.update_items()

    def select_first(self):
        if len(self.components) > 0:
            self.selected_index = 0
            self.update_items()

    def select_last(self):
        if len(self.components) > 0:
            self.selected_index = len(self.components) - 1
            self.update_items()

    def add_item(self):
        item = Component(
            x=10,
            y=30 * (len(self.components) + 1),
            width=150,
            height=50,
            background=self.random_color(),
            foreground=Color(0, 0, 0),
            border_color=Color(0, 0, 0),
            border_width=1,
            text="",
            font_size=20,
        )
        self.components.append(item)
        self.selected_index = len(self.components) - 1
        self.update_items()

    def delete_all(self):
        self.components = []
        self.selected_index = -1
        self.update_items()

    def delete_item(self):
        if self.selected_index >= 0 and len(self.components) > 0:
            self.components.pop(self.selected_index)
            self.selected_index = min(
                self.selected_index, len(self.components) - 1)
            self.update_items()

    def move_selection_down(self):
        if self.selected_index < len(self.components) - 1:
            self.selected_index += 1
            self.update_items()

    def move_selection_up(self):
        if self.selected_index > 0:
            self.selected_index -= 1
            self.update_items()

    def move_item_down(self):
        if self.selected_index < len(self.components) - 1:
            self.components[
                self.selected_index
            ], self.components[
                self.selected_index + 1
            ] = self.components[
                self.selected_index + 1
            ], self.components[
                self.selected_index
            ]

            self.selected_index += 1
            self.update_items()

    def move_item_up(self):
        if self.selected_index > 0:
            self.components[
                self.selected_index
            ], self.components[
                self.selected_index - 1
            ] = self.components[
                self.selected_index - 1
            ], self.components[
                self.selected_index
            ]

            self.selected_index -= 1
            self.update_items()

    def update_items(self):
        for i, component in enumerate(self.components):
            component: Component
            component.x = 10
            component.y = 30 * (i + 1)
            if i == self.selected_index:
                component.border_width = 3
            else:
                component.border_width = 0

    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        return Color(r, g, b)

    def view(self):
        view = super().view()
        view["components"].insert(0, {
            "x": 190,
            "y": 10,
            "width": 200,
            "height": 200,
            "background_color": {
                "r": 255,
                "g": 255,
                "b": 255
            },
            "foreground_color": {
                "r": 0,
                "g": 0,
                "b": 0
            },
            "border_color": {
                "r": 0,
                "g": 0,
                "b": 0
            },
            "border_width": 0,
            "text": "Press 'a' to add an item,\n"
            "'d' to delete an item,\n"
            "'D' to delete all items,\n"
            "'k' to move selection up,\n"
            "'j' to move selection down,\n"
            "'g' to select first,\n"
            "'G' to select last,\n"
            "'K' to move item up,\n"
            "'J' to move item down,\n"
            "'c' to change color,\n"
            "'q' to quit.",
            "font_size": 50,
        })
        print(view)
        return view


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()
