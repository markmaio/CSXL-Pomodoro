/**
 * The Timer Widget shows the details for one pomodoro timer.
 *
 * @author Ajay Gandecha
 * @copyright 2024
 * @license MIT
 */

import { Component, Input } from '@angular/core';
import { ProductivityService } from '../productivity.service';
import { TimerData } from '../timerdata';
import { Router } from '@angular/router';
import { PomodoroTimerState } from 'src/app/pomodoro';

@Component({
  selector: 'timer-widget',
  templateUrl: './timer.widget.html',
  styleUrls: ['./timer.widget.css']
})
export class TimerWidget {
  /** Timer this widget is showing. */
  @Input() timerData!: TimerData;

  /** Local redeclaration of the `PomodoroTimerState` type so that we can access this in the HTML. */
  PomodoroTimerState = PomodoroTimerState;

  constructor(
    private productivityService: ProductivityService,
    private router: Router
  ) {}

  /** Runs when the edit button is pressed (navigate to the edit page) */
  editTimer() {
    this.router.navigate(['/productivity/edit', this.timerData.id]);
  }

  /** Deletes the current timer */
  deleteTimer() {
    // TODO:
    // - Delete the timer. Upon completion of the delete, re-retrieve all timers
    //   using the productivityService's `.getTimers()` method so that the list
    //   of timers is updated.
    this.productivityService.deleteTimer(this.timerData.id).subscribe((_) => {
      this.productivityService.getTimers();
    });
  }
}
