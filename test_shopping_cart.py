from shopping_cart import ShoppingCart
import pytest
from item_database import ItemDatabase
from unittest.mock import Mock


@pytest.fixture
def cart():
    return ShoppingCart(5)


# all pytest functions must contain test_
# in their name (best to have it at the start)
def test_can_add_item_to_cart(cart):
    cart.add("apple")

    # use assertions to test different conditions
    assert cart.size() == 1


def test_when_item_added_cart_has_item(cart):
    cart.add("apple")
    assert "apple" in cart.get_items()


def test_when_add_more_than_max_items_should_fail(cart):
    # if we want a function to raise an exception under certain conditions,
    # use pytest.raises()
    for i in range(5):
        cart.add("apple")

    with pytest.raises(OverflowError):
        cart.add("apple")

    pass


def test_can_get_total_price(cart):
    cart.add("apple")
    cart.add("orange")
    cart.add("apple")
    cart.add("banana")

    price_map = {"apple": 1.0, "orange": 2.0, "banana": 1.5}

    # mocks are used for altering/simplifying
    # the behavior of functions that may not be
    # implemented yet.
    def mock_get_item(item):
        return price_map[item]

    # in this example, ItemDatabase() may be very complex
    # and fetch info from a server, but we don't
    # have to wait for it to be completely implemented.
    item_database = ItemDatabase()
    item_database.get = Mock(side_effect=mock_get_item)

    assert cart.get_total_price(item_database) == 5.5
