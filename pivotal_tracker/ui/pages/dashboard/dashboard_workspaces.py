from core.ui.pages.action_page import ActionPage
from pivotal_tracker.ui.pages.tabs.user_main_tabs import UserMainTabs

create_workspace_button = '#create-workspace-button'


class DashboardWorkspaces(ActionPage):
    def __init__(self, driver):
        super().__init__(driver)
        actions = {
            "Create workspace": lambda: self.open_create_workspace_form()
        }
        self.update_actions(**actions)

    def open_create_workspace_form(self):
        self.click(create_workspace_button)
        return UserMainTabs.WORKSPACE_CREATION
