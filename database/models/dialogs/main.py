from database.models.dialogs.config import DialogBranchConfig, DialogConfig

class Dialog:
    def __init__(self, config: DialogConfig) -> None:
        self.name = config.name
        self.message = config.message
        self.answers = config.answers

    @property
    def is_end(self):
        if len(self.answers) == 0:
            return True
        return False

    def answer_index(self, answer_user: str) -> int:
        if answer_user in self.answers.keys():
            return self.answers[answer_user]
        return -1

class DialogBranch:

    def __init__(self, config: DialogBranchConfig) -> None:
        self.name = config.name
        self.answers = dict[str, Dialog]()
        for config_dialog in config.dialogs:
            self.answers[config_dialog.name] = Dialog(config_dialog)

    def get_dialog(self, index: int) -> Dialog | None:
        dialog = self.dialogs.get(index)
        if dialog is None:
            return None
        return dialog