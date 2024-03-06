"""Definition of SQLAlchemy table-backed object mapping entity for Pomodoro Timers."""

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self

from backend.models.pomodoro_timer import PomodoroTimer
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
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, default="")
    description: Mapped[str] = mapped_column(String)
    timer_length: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    break_length: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    # TODO: Define the foreign key to establish the one-to-many-relationship between the user and timer tables.
    # The user associated with the timer
    # NOTE: This field establishes a one-to-many relationship between the user and timer tables.
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["UserEntity"] = relationship(back_populates="president_for")

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
        return cls(
            id=model.id,
            name=model.name,
            description=model.description,
            timer_length=model.timer_length,
            break_length=model.break_length,
        )

    def to_model(self) -> PomodoroTimer:
        """
        Create a PomodoroTimer model from a PomodoroTimerEntity.

        Returns:
            PomodoroTimer: A PomodoroTimer model for API usage.
        """
        # TODO: Finish implementing this method based on the doc string above.
        return PomodoroTimer(
            id=self.id,
            name=self.name,
            description=self.description,
            timer_length=self.timer_length,
            break_length=self.break_length,
        )
