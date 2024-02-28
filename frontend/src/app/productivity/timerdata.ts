import { PomodoroTimer } from '../pomodoro';

export interface TimerResponse {
  id: number | null;
  name: string;
  description: string;
  timer_length: number;
  break_length: number;
}

export interface TimerData {
  id: number;
  name: string;
  description: string;
  timer: PomodoroTimer;
}
