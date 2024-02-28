"""Productivity API

Productivity routes are used to create, retrieve, and update Pomodoro timers."""

from fastapi import APIRouter, Depends

from backend.api.authentication import registered_user
from backend.models.user import User
from ..models.pomodorotimer import PomodoroTimer
from ..services.productivity import ProductivityService

__authors__ = ["Ajay Gandecha"]
__copyright__ = "Copyright 2024"
__license__ = "MIT"

api = APIRouter(prefix="/api/productivity")
openapi_tags = {
    "name": "Productivity",
    "description": "Create, update, delete, and retrieve Pomodoro timers.",
}


# GET /api/productivity
# Gets all pomodoro timers.
# Expected return type: list[PomodoroTimer]
@api.get("", response_model=list[PomodoroTimer], tags=["Productivity"])
def get_timers(
    subject: User = Depends(registered_user),
    productivity_service: ProductivityService = Depends(),
) -> list[PomodoroTimer]:
    """
    Get all pomodoro timers.

    Parameters:
        productivity_service: a valid ProductivityService

    Returns:
        list[PomodoroTimer]: All pomodoro timers
    """

    # Return all pomodoro timers
    return productivity_service.get_timers(subject)


# GET /api/productivity/{id}
# Get a pomodoro timer by its ID.
# Expected return type: PomodoroTimer
@api.get("/{id}", response_model=PomodoroTimer, tags=["Productivity"])
def get_timer(
    id: int,
    subject: User = Depends(registered_user),
    productivity_service: ProductivityService = Depends(),
) -> PomodoroTimer:
    """
    Get pomodoro timer.

    Parameters:
        id: ID of the timer to get
        productivity_service: a valid ProductivityService
    """

    return productivity_service.get_timer(subject, id)


# POST /api/productivity/
# Creates a new pomodoro timer.
# Note: This API will take in a request body. What type should this be?
# Expected return type: PomodoroTimer
@api.post("", response_model=PomodoroTimer, tags=["Productivity"])
def create_timer(
    timer: PomodoroTimer,
    subject: User = Depends(registered_user),
    productivity_service: ProductivityService = Depends(),
) -> PomodoroTimer:
    """
    Create pomodoro timer.

    Parameters:
        timer: a valid PomodoroTimer model
        productivity_service: a valid ProductivityService

    Returns:
        PomodoroTimer: Created pomodoro timer
    """

    return productivity_service.create_timer(subject, timer)


# PUT /api/productivity
# Updates a pomodoro timer.
# Note: This API will take in a request body. What type should this be?
# Expected return type: PomodoroTimer
@api.put("", response_model=PomodoroTimer, tags=["Productivity"])
def update_timer(
    timer: PomodoroTimer,
    subject: User = Depends(registered_user),
    productivity_service: ProductivityService = Depends(),
) -> PomodoroTimer:
    """
    Update pomodoro timer.

    Parameters:
        timer: a valid PomodoroTimer model
        productivity_service: a valid ProductivityService

    Returns:
        PomodoroTimer: Updated pomodoro timer
    """

    return productivity_service.update_timer(subject, timer)


# DELETE /api/productivity/{id}
# Deletes a pomodoro timer.
# Expected return type: PomodoroTimer
@api.delete("/{id}", response_model=None, tags=["Productivity"])
def delete_timer(
    id: int,
    subject: User = Depends(registered_user),
    productivity_service: ProductivityService = Depends(),
) -> PomodoroTimer:
    """
    Delete pomodoro timer.

    Parameters:
        id: ID of the timer to delete
        productivity_service: a valid ProductivityService
    """

    return productivity_service.delete_timer(subject, id)
