"""
The Productivity Service allows the API to manipulate pomodoro timer data in the database.
"""

from fastapi import Depends
from pytest import Session
from backend.database import db_session
from backend.entities.pomodoro_entity import PomodoroTimerEntity

from backend.models.user import User
from backend.services.exceptions import (
    ResourceNotFoundException,
    UserPermissionException,
)
from ..models.pomodorotimer import PomodoroTimer

__authors__ = ["Ajay Gandecha", "Jade Keegan"]
__copyright__ = "Copyright 2024"
__license__ = "MIT"


class ProductivityService:
    """Backend service that enables direct modification of pomodoro timer data."""

    def __init__(
        self,
        session: Session = Depends(db_session),
    ):
        """Initializes the `ProductivityService` session"""
        self._session = session

    def get_timers(self) -> list[PomodoroTimer]:
        """
        Retrieves all pomodoro timers for the currently logged in user.

        Returns:
            list[PomodoroTimer]: All pomodoro timer data for the currently logged in user.
        """
        # TODO: Query the PomodoroTimer table to retrieve the entries associated with the current user.

        # TODO: Return all the PomodoroTimer entities for the user in the correct format.
        return ...

    def get_timer(self, timer_id: int) -> PomodoroTimer:
        """Gets one timer by an ID.

        Args:
            timer_id: Timer to retrieve.
        Returns:
            PomodoroTimer: Timer with the matching ID.
        Raises:
            UserPermissionException: user attempting to retrieve a timer that
                they did not create.
            ResourceNotFoundException: Timer does not exist.
        """
        # TODO: Query the PomodoroTimer table to retrieve the timer with the matching id

        # TODO: Add error handling if there is no timer associated with the given id.
        # Check if result is null and raise the custom ResourceNotFoundException

        # TODO: Ensure that the user attempting to retrieve the timer is the same as the user
        # who created the timer. Raise an exception otherwise.

        # TODO: Return the timer if it exists
        return ...

    def create_timer(self, timer: PomodoroTimer) -> PomodoroTimer:
        """Stores a timer in the database.

        Args:
            timer: Timer to store.
        Returns:
            PomodoroTimer: Created timer.
        """
        # Set timer id to none if an id was passed in
        if timer.id is not None:
            timer.id = None

        # TODO: Create a new timer entity for the table.

        # TODO: Return the new pomodoro timer object.
        return ...

    def update_timer(self, timer: PomodoroTimer) -> PomodoroTimer:
        """Modifies one timer in the database.

        Args:
            timer: Data for a timer with modified values.
        Returns:
            PomodoroTimer: Updated timer.
        Raises:
            UserPermissionException: user attempting to update a timer that
                they did not create.
            ResourceNotFoundException: Timer does not exist.
        """
        # TODO: Query the table for the pomodoro with the matching id

        # TODO: Throw the custom ResourceNotFoundException if the user tries to edit a timer
        # that does not exist.

        # TODO: Ensure that the user attempting to update the timer is the same as the user
        # who created the timer. Raise an exception otherwise.

        # TODO: Update each field of the pomodoro timer object to match the fields of the given timer.

        # TODO: Return the updated pomodoro timer object
        return ...

    def delete_timer(self, timer_id: int) -> None:
        """Deletes one timer from the database.

        Args:
            timer_id: ID of the timer to delete.
        Raises:
            UserPermissionException: user attempting to delete a timer that
                they did not create.
            ResourceNotFoundException: Timer does not exist.
        """
        # TODO: Query the table for the pomodoro with the matching id

        # TODO: Throw the custom ResourceNotFoundException if the user tries to delete a timer
        # that does not exist.

        # TODO: Ensure that the user attempting to delete the timer is the same as the user
        # who created the timer. Raise an exception otherwise.

        # TODO: Delete the pomodoro entity from the table/session.

        # TODO: Commit the changes to the table/session.