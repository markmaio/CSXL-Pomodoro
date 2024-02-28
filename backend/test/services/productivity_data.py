"""
Mock data for pomodoros in the system.

This file creates some Pomodoro Timer models to be added as test data for the
Productivity Service.
"""

import pytest
from sqlalchemy.orm import Session

from ...entities.pomodoro_entity import PomodoroTimerEntity

from ...models.pomodorotimer import PomodoroTimer

from .reset_table_id_seq import reset_table_id_seq

from .user_data import user

__authors__ = ["Jade Keegan"]
__copyright__ = "Copyright 2024"
__license__ = "MIT"

timer1 = PomodoroTimer(
    id=1, name="Sample 1", description="Description 1", timer_length=10, break_length=5
)
timer2 = PomodoroTimer(
    id=2, name="Sample 2", description="Description 2", timer_length=10, break_length=5
)
timer3 = PomodoroTimer(
    id=3, name="Sample 3", description="Description 3", timer_length=10, break_length=5
)
new_timer = PomodoroTimer(
    id=None,
    name="My New Timer",
    description="My Timer Description",
    timer_length=25,
    break_length=5,
)
updated_timer1 = PomodoroTimer(
    id=1,
    name="Sample 1",
    description="Description 1",
    timer_length=30,
    break_length=5,
)
timers = [timer1, timer2, timer3]


def insert_fake_data(session: Session):
    """Inserts fake pomodoro timer data into the test session."""

    global timers

    # Create entities for test organization data
    entities = []
    for timer in timers:
        # Timers created will be associated with Sally Student
        timer_entity = PomodoroTimerEntity.from_model(user, timer)
        session.add(timer_entity)
        entities.append(timer_entity)

    # Reset table IDs to prevent ID conflicts
    reset_table_id_seq(
        session, PomodoroTimerEntity, PomodoroTimerEntity.id, len(timers) + 1
    )

    # Commit all changes
    session.commit()


@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    """Insert fake data the session automatically when a test is run.
    Note:
        This function runs automatically for each test due to the fixture property `autouse=True`.
    """
    insert_fake_data(session)
    session.commit()
    yield
