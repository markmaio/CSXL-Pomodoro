"""Definition of SQLAlchemy table-backed object mapping entity for Pomodoro Timers."""

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self

from backend.models.pomodorotimer import PomodoroTimer
from backend.models.user import User
from .entity_base import EntityBase

__authors__ = ["Jade Keegan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class PomodoroTimerEntity(EntityBase):
    """Serves as the database model schema defining the shape of the `PomodoroTimer` table"""

    # Name for the pomodoro timer table in the PostgreSQL database
    __tablename__ = "pomodoro"

    # TODO: Define the main fields of the Pomodoro Timer entity.

    # TODO: Define the foreign key to establish the one-to-many-relationship between the user and timer tables.
    # The user associated with the timer
    # NOTE: This field establishes a one-to-many relationship between the user and timer tables.

    @classmethod
    def from_model(cls, subject: User, model: PomodoroTimer) -> Self:
        """
        Create a PomodoroTimerEntity from a PomodoroTimer model.

        Args:
            model (PomodoroTimer): The model to create the entity from.

        Returns:
            Self: The entity (not yet persisted).
        """
        # TODO: Finish implementing this method based on the doc string above.
        return ...

    def to_model(self) -> PomodoroTimer:
        """
        Create a PomodoroTimer model from a PomodoroTimerEntity.

        Returns:
            PomodoroTimer: A PomodoroTimer model for API usage.
        """
        # TODO: Finish implementing this method based on the doc string above.
        return ...