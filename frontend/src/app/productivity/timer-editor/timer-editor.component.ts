/**
 * The Timer Editor component allows pomodoro timers to be both
 * created and edited.
 *
 * @author Ajay Gandecha
 * @copyright 2024
 * @license MIT
 */

import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ProductivityService } from '../productivity.service';
import { FormBuilder, FormControl, Validators } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { isAuthenticated } from 'src/app/gate/gate.guard';

@Component({
  selector: 'app-timer-editor',
  templateUrl: './timer-editor.component.html',
  styleUrls: ['./timer-editor.component.css']
})
export class TimerEditorComponent {
  public static Route = {
    path: 'productivity/edit/:pomo_id',
    title: 'Timer Editor',
    component: TimerEditorComponent,
    canActivate: [isAuthenticated]
  };

  /** Form controls (individual form items) */
  name = new FormControl('', [Validators.required]);
  description = new FormControl('', [Validators.required]);
  timerLength = new FormControl(0, [Validators.required]);
  breakLength = new FormControl(0, [Validators.required]);

  /** Form group (stores all form controls) */
  public timerForm = this.formBuilder.group({
    name: this.name,
    description: this.description,
    timerLength: this.timerLength,
    breakLength: this.breakLength
  });

  /** Stores the ID of the timer currently being edited. */
  id: number = -1;

  /** Stores whether or not the timer is new. */
  isNew: boolean = false;

  constructor(
    private productivityService: ProductivityService,
    private route: ActivatedRoute,
    protected formBuilder: FormBuilder,
    private router: Router,
    protected snackBar: MatSnackBar
  ) {
    // Determine if the timer is new.
    this.isNew = route.snapshot.params['pomo_id'] == 'new';

    // If the timer is not new, set existing timer data and update the forms.
    if (!this.isNew) {
      this.id = route.snapshot.params['pomo_id'];
      productivityService.getTimer(this.id).subscribe((timerData) => {
        this.timerForm.setValue({
          name: timerData.name,
          description: timerData.description,
          timerLength: timerData.timer.timerLength,
          breakLength: timerData.timer.breakLength
        });
      });
    }
  }

  /** Function that runs when the form is submitted. */
  public onSubmitForm() {
    // First, ensure that the form is valid (all validators pass). Otherwise, display a snackbar error.
    if (this.timerForm.valid) {
      // If the timer is new, create it.
      if (this.isNew) {
        // TODO: Create a timer.
        this.productivityService
          .createTimer({
            id: null,
            name: this.name.value ?? '',
            description: this.description.value ?? '',
            timer_length: this.timerLength.value ?? 0,
            break_length: this.breakLength.value ?? 0
          })
          .subscribe((_) => {
            // Navigate back to the productivity page once the operation is complete.
            this.router.navigate(['/productivity/']);
          });
      } else {
        // TODO: Edit the existing timer.
        this.productivityService
          .editTimer({
            id: this.id,
            name: this.name.value ?? '',
            description: this.description.value ?? '',
            timer_length: this.timerLength.value ?? 0,
            break_length: this.breakLength.value ?? 0
          })
          .subscribe((_) => {
            // Navigate back to the productivity page once the operation is complete.
            this.router.navigate(['/productivity/']);
          });
      }
    } else {
      this.snackBar.open('Please enter values in the form correctly.', '', {
        duration: 2000
      });
    }
  }
}
