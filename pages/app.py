from pages.base.page import BasePage
from pages.login.page import LoginPage
from pages.inventory.page import InventoryPage
from pages.cart.page import CartPage
from pages.checkout_step_one.page import CheckoutStepOnePage
from pages.components.header.component import HeaderComponent

class App:
    def __init__(self, page):
        self.base_page = BasePage(page)
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)
        self.cart_page = CartPage(page)
        self.checkout_step_one = CheckoutStepOnePage(page)
        self.header_component = HeaderComponent(page)
