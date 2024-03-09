"""
The Productivity Service allows the API to manipulate pomodoro timer data in the database.
"""

from fastapi import Depends
from pytest import Session
from backend.database import db_session
from backend.entities.pomodoro_timer_entity import PomodoroTimerEntity

from backend.models.user import User
from backend.services.exceptions import (
    ResourceNotFoundException,
    UserPermissionException,
)
from ..models.pomodoro_timer import PomodoroTimer

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

    def get_timers(self, subject: User) -> list[PomodoroTimer]:
        """
        Retrieves all pomodoro timers for the currently logged in user.

        Args:
            subject: a valid User model representing the currently logged in User
        Returns:
            list[PomodoroTimer]: All pomodoro timer data for the currently logged in user.
        """

        # TODO: Query the PomodoroTimer table to retrieve the entries associated with the current user.
        entities = (
            self._session.query(PomodoroTimerEntity)
            .where(PomodoroTimerEntity.user_id == subject.id)
            .all()
        )
        
        # TODO: Return all the PomodoroTimer entities for the user in the correct format.
        return [entity.to_model() for entity in entities]

    def get_timer(self, subject: User, timer_id: int) -> PomodoroTimer:
        """Gets one timer by an ID.

        Args:
            subject: a valid User model representing the currently logged in User
            timer_id: Timer to retrieve.
        Returns:
            PomodoroTimer: Timer with the matching ID.
        Raises:
            UserPermissionException: user attempting to retrieve a timer that
                they did not create.
            ResourceNotFoundException: Timer does not exist.
        """
        # TODO: Query the PomodoroTimer table to retrieve the timer with the matching id
        entity = self._session.get(PomodoroTimerEntity, timer_id)

        # TODO: Add error handling if there is no timer associated with the given id.
        # Check if result is null and raise the custom ResourceNotFoundException
        if entity is None:
            raise ResourceNotFoundException("Timer does not exist.")

        # TODO: Ensure that the user attempting to retrieve the timer is the same as the user
        # who created the timer. Raise an exception otherwise.
        if entity.user_id != subject.id:
            raise UserPermissionException(
                "productivity.view", f"productivity/{timer_id}"
            )

        # TODO: Return the timer if it exists
        return entity.to_model()

    def create_timer(self, subject: User, timer: PomodoroTimer) -> PomodoroTimer:
        """Stores a timer in the database.

        Args:
            subject: a valid User model representing the currently logged in User
            timer: Timer to store.

        Returns:
            PomodoroTimer: Created timer.
        """
        # Set timer id to none if an id was passed in
        if timer.id is not None:
            timer.id = None

        # TODO: Create a new timer entity for the table.
        entity = PomodoroTimerEntity.from_model(subject, timer)
        self._session.add(entity)
        self._session.commit()

        # TODO: Return the new pomodoro timer object.
        return entity.to_model()

    def update_timer(self, subject: User, timer: PomodoroTimer) -> PomodoroTimer:
        """Modifies one timer in the database.

        Args:
            subject: a valid User model representing the currently logged in User
            timer: Data for a timer with modified values.
        Returns:
            PomodoroTimer: Updated timer.
        Raises:
            UserPermissionException: user attempting to update a timer that
                they did not create.
            ResourceNotFoundException: Timer does not exist.
        """
        # TODO: Query the table for the pomodoro with the matching id
        entity = self._session.get(PomodoroTimerEntity, timer.id)

        # TODO: Throw the custom ResourceNotFoundException if the user tries to edit a timer
        # that does not exist.
        if entity is None:
            raise ResourceNotFoundException("Timer does not exist.")

        # TODO: Ensure that the user attempting to update the timer is the same as the user
        # who created the timer. Raise an exception otherwise.
        if entity.user_id != subject.id:
            raise UserPermissionException(
                "productivity.view", f"productivity/{timer.id}"
            )
        # TODO: Update each field of the pomodoro timer object to match the fields of the given timer.
        print("timer id" + str(timer.id))
        print("entity id" + str(entity.id))
        entity.name = timer.name
        entity.description = timer.description
        entity.timer_length = timer.timer_length
        entity.break_length = timer.break_length
        self._session.commit()
        print("updated entity id" + str(entity.id))
        # TODO: Return the updated pomodoro timer object
        return entity.to_model()

    def delete_timer(self, subject: User, timer_id: int) -> None:
        """Deletes one timer from the database.

        Args:
            timer_id: ID of the timer to delete.
        Raises:
            UserPermissionException: user attempting to delete a timer that
                they did not create.
            ResourceNotFoundException: Timer does not exist.
        """
        # TODO: Query the table for the pomodoro with the matching id
        entity = self._session.get(PomodoroTimerEntity, timer_id)
        # TODO: Throw the custom ResourceNotFoundException if the user tries to delete a timer
        # that does not exist.
        if entity is None:
            raise ResourceNotFoundException("Timer does not exist.")
        # TODO: Ensure that the user attempting to delete the timer is the same as the user
        # who created the timer. Raise an exception otherwise.
        if entity.user_id != subject.id:
            raise UserPermissionException(
                "productivity.view", f"productivity/{timer_id}"
            )
        # TODO: Delete the pomodoro entity from the table/session.
        self._session.delete(entity)
        # TODO: Commit the changes to the table/session.
        self._session.commit()
