from pages.base.page import BasePage
from pages.components.header.component import HeaderComponent
from pages.login.page import LoginPage
from pages.inventory.page import InventoryPage
from pages.cart.page import CartPage
from pages.checkout_step_one.page import CheckoutStepOnePage
from pages.checkout_step_two.page import CheckoutStepTwoPage
from pages.checkout_complete.page import CheckoutCompletePage
from pages.inventory_item.page import InventoryItemPage


class App:
    def __init__(self, page):
        self.base_page = BasePage(page)
        self.header_component = HeaderComponent(page)
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)
        self.cart_page = CartPage(page)
        self.checkout_step_one = CheckoutStepOnePage(page)
        self.checkout_step_two = CheckoutStepTwoPage(page)
        self.checkout_complete = CheckoutCompletePage(page)
        self.inventory_item_page = InventoryItemPage(page)