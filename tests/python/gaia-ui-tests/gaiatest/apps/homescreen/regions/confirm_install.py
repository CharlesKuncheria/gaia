from marionette.by import By
from gaiatest.apps.base import Base


class ConfirmInstall(Base):

        _confirm_install_button_locator = (By.ID, 'app-install-install-button')

        def tap_confirm(self):
            self.wait_for_element_displayed(*self._confirm_install_button_locator)
            self.marionette.find_element(*self._confirm_install_button_locator).tap()
