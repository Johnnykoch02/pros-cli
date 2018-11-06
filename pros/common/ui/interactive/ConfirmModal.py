from typing import *

from . import application, components


class ConfirmModal(application.Modal):
    """
    ConfirmModal is used by the ui.confirm() method.

    In --machine-output mode, this Modal is run instead of a textual confirmation request (e.g. click.confirm())
    """
    def __init__(self, text: str, abort: bool = False, title: AnyStr = 'Please confirm:', log: Optional[AnyStr] = None):
        super().__init__(title, will_abort=abort, confirm_button='Yes', cancel_button='No')
        self.text = text
        self.log = log

    def confirm(self):
        self.set_return(True)
        self.exit()

    def cancel(self):
        print('Cancelling')
        self.set_return(False)
        super(ConfirmModal, self).cancel()

    def build(self) -> Generator[components.Component, None, None]:
        yield components.Label(self.text)
        if self.log:
            yield components.Label(self.log)
