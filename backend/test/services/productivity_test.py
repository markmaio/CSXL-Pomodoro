"""
Tests for the ProductivityService class.

These tests now reference data added to a test session that is set up in the 
productivity_data.py file! Note that each tests has it's own "session", so
changes made to the session in one test will NOT impact another test.

Another important change is that tests that previously created timers with the
create method before testing other methods (or just didn't have any timers to begin with) 
are now able to directly test the method individually since we have three timers 
pre-loaded into the session!
"""

from backend.services.exceptions import (
    ResourceNotFoundException,
    UserPermissionException,
)

# PyTest
import pytest

# Tested Dependencies
from ...models.pomodoro_timer import PomodoroTimer
from ...services import ProductivityService

# Injected Service Fixtures
from .fixtures import productivity_svc_integration

# Explicitly import Data Fixture to load entities in database
from .core_data import setup_insert_data_fixture

# Data Models for Fake Data Inserted in Setup
from .productivity_data import new_timer, updated_timer1, timers
from .user_data import user, root

__authors__ = ["Jade Keegan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


def test_get_timers(productivity_svc_integration: ProductivityService):
    """Test that retrieving timers retrieves all timers."""
    result = productivity_svc_integration.get_timers(user)
    assert len(result) == len(timers)
    assert timers[0] in result
    assert timers[1] in result
    assert timers[2] in result


def test_add_timer(productivity_svc_integration: ProductivityService):
    """Test that adding a timer creates and returns the correct timer"""
    result = productivity_svc_integration.create_timer(user, new_timer)
    assert result is not None
    assert new_timer.name == result.name
    assert new_timer.description == result.description
    assert new_timer.timer_length == result.timer_length
    assert new_timer.break_length == result.break_length
    assert len(productivity_svc_integration.get_timers(user)) == 4


def test_add_timer_already_exists(productivity_svc_integration: ProductivityService):
    """Test that attempting to create two timers with the same ID allows the create but increments the ID"""
    productivity_svc_integration.create_timer(user, new_timer)
    result = productivity_svc_integration.create_timer(user, new_timer)
    assert len(productivity_svc_integration.get_timers(user)) == 5
    assert result.id == 5


def test_get_timer(productivity_svc_integration: ProductivityService):
    """Test that get timer by id returns the correct timer"""
    result = productivity_svc_integration.get_timer(user, 1)
    assert result is not None

    assert result.id == 1
    assert result.name == timers[0].name
    assert result.description == timers[0].description
    assert result.timer_length == timers[0].timer_length
    assert result.break_length == timers[0].break_length


def test_get_timer_not_user(productivity_svc_integration: ProductivityService):
    """Test that a user cannot get a timer that another user created"""
    with pytest.raises(UserPermissionException):
        productivity_svc_integration.get_timer(root, 1)


# TODO: Update the tests for updating timers to reference the Pomodoro Timer table
# NOTE:
# - Be sure to use the updated_timer1 model from the productivity_data.py file.
# - Pay careful attention to the new parameters required for update_timer.
def test_update_timer(productivity_svc_integration: ProductivityService):
    """Test that updating a timer properly edits the timer's fields"""


def test_update_timer_none_exists(productivity_svc_integration: ProductivityService):
    """Test that attempting to update a timer that does not exist raises a ResourceNotFoundException"""


def test_update_timer_not_user(productivity_svc_integration: ProductivityService):
    """Test that another user cannot update a timer that another user created"""
    with pytest.raises(UserPermissionException):
        productivity_svc_integration.update_timer(root, updated_timer1)


def test_delete_timer(productivity_svc_integration: ProductivityService):
    """Test that deleting a timer appropriately removes the timer"""
    productivity_svc_integration.delete_timer(user, 1)

    result = productivity_svc_integration.get_timers(user)
    assert len(timers) - 1 == len(result)
    assert timers[0] not in result


def test_delete_timer_none_exists(productivity_svc_integration: ProductivityService):
    """Test that attempting to delete a timer that does not exist throws a ResourceNotFoundException"""
    with pytest.raises(ResourceNotFoundException):
        productivity_svc_integration.delete_timer(user, 6)


def test_delete_timer_not_user(productivity_svc_integration: ProductivityService):
    """Test that a user cannot delete a timer another user created"""
    with pytest.raises(UserPermissionException):
        productivity_svc_integration.delete_timer(root, 1)
