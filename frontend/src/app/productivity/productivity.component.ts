/**
 * The Productivity Component shows active pomodoro timers and allows
 * users to use, create, modify, and delete current timers.
 *
 * @author Ajay Gandecha
 * @copyright 2024
 * @license MIT
 */

import { Component } from '@angular/core';
import { ProductivityService } from './productivity.service';
import { Router } from '@angular/router';
import { isAuthenticated } from '../gate/gate.guard';

@Component({
  selector: 'app-productivity',
  templateUrl: './productivity.component.html',
  styleUrls: ['./productivity.component.css']
})
export class ProductivityComponent {
  public static Route = {
    path: 'productivity',
    title: 'My Pomodoro Timers',
    component: ProductivityComponent,
    canActivate: [isAuthenticated]
  };

  constructor(
    public productivityService: ProductivityService,
    public router: Router
  ) {
    // TODO: Retrieve all timers (which updates the service's `timers$` observable)
    this.productivityService.getTimers();
  }
}
