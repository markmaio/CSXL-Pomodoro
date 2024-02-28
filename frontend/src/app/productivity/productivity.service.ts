/**
 * The Productivity Service enables the retrieval, creation, modification, and deletion
 * of pomodoro timers from the Productivity API endpoint.
 *
 * @author Ajay Gandecha
 * @copyright 2024
 * @license MIT
 */

import { Injectable } from '@angular/core';
import { TimerData, TimerResponse } from './timerdata';
import { PomodoroTimer } from '../pomodoro';
import { Observable, OperatorFunction, ReplaySubject, map } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProductivityService {
  /** Internal construction to create an observable `timers$` that stores the last retreived
   *  list of timers from the backend. Every time we call `getTimers()`, we push the resulting
   *  timer list from the .get() API call to the `timers` ReplaySubject. The ReplaySubject stores
   * the last retreived list of timers, and `timers$` exposes this list as an observable.
   *
   * This construction is very useful because it allows us to have an observable we can update that
   * always stores the most up-to-date timer list. So, if we were to delete a timer on the productivity page,
   * for example, we can call getTimers() to update this internal list, refreshing the data on the
   * productivity page automatically without a page refresh.
   *
   * This construction is abstracted out in the CSXL Codebase as `RxObject<T>`, an abstract class located
   * in `src/app/rx-object.ts`.
   */
  private timers: ReplaySubject<TimerData[]> = new ReplaySubject(1);
  timers$: Observable<TimerData[]> = this.timers.asObservable();

  constructor(protected http: HttpClient) {
    // Sets the initial value of the timers replay subject to an empty list of timers.
    // This way, we can always guarantee that the next value from `timers$` will never be null.
    this.timers.next([]);
  }

  /** Refreshes the internal `timer$` observable with the latest timer data from the API. */
  getTimers() {
    // TODO:
    // - Get all TimerResponse objects by calling the GET /api/productivity API
    // - Then, convert the data from TimerResponse objects to TimerData objects. using RxJS operators,
    //    pass the resulting list through the `mapTimerResponseListToDataList` function.
    // - Finally, update the internal timers$ observable by calling `this.timers.next(...)`.
    // - Return the result.

    this.http
      .get<TimerResponse[]>('/api/productivity')
      .pipe(this.mapTimerResponseListToDataList)
      .subscribe((timers) => this.timers.next(timers));
  }

  /** Returns a single timer from the API as an observable.  */
  getTimer(id: number): Observable<TimerData> {
    // TODO:
    // - Get one TimerResponse object by calling the GET /api/productivity/{id} API
    // - Then, convert the data from TimerResponse object to a TimerData object. using RxJS operators,
    //    pass the resulting list through the `mapTimerResponseToData` function.
    // - Return the result.

    return this.http
      .get<TimerResponse>('/api/productivity/' + id)
      .pipe(this.mapTimerResponseToData);
  }

  /** Creates a new timer and returns the created timer from the API as an observable. */
  createTimer(request: TimerResponse): Observable<TimerData> {
    // TODO:
    // - Create one TimerResponse object by calling the POST /api/productivity/ API
    // - Then, convert the data from TimerResponse object to a TimerData object. using RxJS operators,
    //    pass the resulting list through the `mapTimerResponseToData` function.
    // - Return the result.

    return this.http
      .post<TimerResponse>('/api/productivity', request)
      .pipe(this.mapTimerResponseToData);
  }

  /** Edits a timer and returns the edited timer from the API as an observable. */
  editTimer(request: TimerResponse): Observable<TimerData> {
    // TODO:
    // - Create one TimerResponse object by calling the PUT /api/productivity/ API
    // - Then, convert the data from TimerResponse object to a TimerData object. using RxJS operators,
    //    pass the resulting list through the `mapTimerResponseToData` function.
    // - Return the result.

    // Delete the line below once you complete your solution -
    // This is a placeholder to prevent Angular from failing to build.

    return this.http
      .put<TimerResponse>('/api/productivity', request)
      .pipe(this.mapTimerResponseToData);
  }

  /** Deletes a timer and returns the delete action as an observable. */
  deleteTimer(id: number) {
    // TODO:
    // - Delete one TimerResponse object by calling the DELETE /api/productivity/ API
    // - Return the result.

    return this.http.delete('/api/productivity/' + id);
  }

  /********* PROVIDED FUNCTIONS: Do not modify. *********/

  /**
   * Operator function that converts a list of timer responses into a list
   * of timer data objects.
   */
  private mapTimerResponseListToDataList: OperatorFunction<
    TimerResponse[],
    TimerData[]
  > = map((responses) =>
    responses.map((response) => this.timerResponseToData(response))
  );

  /**
   * Operator function that converts a timer response object into
   * a timer data object.
   */
  private mapTimerResponseToData: OperatorFunction<TimerResponse, TimerData> =
    map(this.timerResponseToData);

  /**
   * Converts a `TimerResponse` object to a `TimerData` object.
   * @param response `TimerResponse` to convert
   * @returns Resulting `TimerData` object
   */
  timerResponseToData(response: TimerResponse): TimerData {
    // Creates and resets a timer for the TimerData object
    let newTimer = new PomodoroTimer(
      response.timer_length,
      response.break_length
    );
    newTimer.reset();

    return {
      id: response.id!,
      name: response.name,
      description: response.description,
      timer: newTimer
    };
  }
}
