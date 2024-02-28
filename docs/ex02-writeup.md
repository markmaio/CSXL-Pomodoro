# EX02: FastAPI

# Introduction

In this exercise, you will begin to build out the backend that powers the Pomodoro Timer feature you all worked on in EX01. Specifically, you will build out the REST APIs for fetching, creating, updating, and deleting Pomodoro timer data. Then, you will connect your new APIs to an Angular frontend. This exercise will allow you to become more comfortable working with APIs and understand how the backend for the UNC CS Experience Lab site is set up.

Be sure to scan the **_entire_** full write up (especially the technical requirements) before you begin writing code to ensure that you adhere to all of the outlined specifications.

# Setup

Clone the repo.

# Navigating the Backend

## The File Structure

In EX01, you familiarized yourself with the `/frontend` directory. The `/frontend` directory stores your frontend Angular web application.

As you would expect, the `/backend` directory holds all of the code powering the backend of the CSXL site. There are a lot of files and subdirectories here! Below is a short summary for you to orient yourself with the `/backend` folder structure:

- **`main.py`**: This is the entry-point of the backend application and stores the FastAPI application (called `app` in the file). When we run the `honcho start` command in terminal, it kicks off many processes, including `uvicorn --port=1561 --reload backend.main:app`. This command effectively boots up our FastAPI application, allowing us to access and use the APIs we create.

- **`/api`**: This folder contains all of our FastAPI API functions and therefore all our API functionality. You will notice that `main.py` _imports_ all of these API files and stores them in a list called `feature_apis` (lines 64:82). When you want to create new APIs, you will need to import your new file into `main.py` and add it to this `feature_apis` list so that your API will route properly.

- **`/models`**: This folder contains all of your Pydantic Model classes. Remember that we use Pydantic models to represent the shape of data your APIs expect to work with.

- **`/services`**: This folder contains all of your backend service classes. Backend services are to FastAPI as frontend services are to components - they help to abstract functionality to include business logic. Backend services are neatly bundled, which makes it super convenient to test.

- **`/test`**: Speaking of testing, this folder contains Pytest unit tests that allow us to ensure our code is working as expected.

- _`/entities`, `/migrations`, and `/script`_: These folders are very important, but we will not be using them until the next exercise!

## The `PomodoroTimer` Pydantic Model

Recall that Pydantic Models are responsible for specifying the data your APIs expect to work with. For this project, we will be working with data for Pomodoro timers. So, our model needs to store the same data we were working with in EX01, including an ID, the timer's name and description, and the length of the timer's working and break times.

For simplicity, this model has been defined for you in `/backend/models/pomodorotimer.py`. The code for this model has been shown below:

```py
class PomodoroTimer(BaseModel):
    id: int | None
    name: str
    description: str
    timer_length: int
    break_length: int
```

Do note that in the future, when you are working on your own projects, you will need to construct your own Pydantic Models for the data you are trying to work with! Next, let's take a look at how we are storing this pomodoro timer data.

## The `ProductivityService`

Before you get started with the exercise, it is important that you have a good understanding on how the backend `ProductivityService` works. This class is located in `/backend/services/productivity.py`.

This file exposes a global `_timers` dictionary which serves as the backend timer storage for this exercise. This dictionary stores timer data such that the *key*s of the dictionary are Timer IDs, and the values are objects of type `PomodoroTimer` - the Pydantic Model we defined earlier. So, here is an example of the data that `_timers` might store:

```py
{
    1: PomodoroTimer(id: 1, name: "Hello", description: "World", timer_length: 10, break_length: 5),
    2: PomodoroTimer(id: 2, name: "Another", description: "One", timer_length: 20, break_length: 4)
}
```

With data stored this way, we can access any timer by its ID by calling `_timers[id]`. We also have an internal `_timer_id` variable, which incremenets each time a new timer is created, so that each timer has its own unique ID.

Now, **_thoroughly_ read through** the code provided and try to understand how it works. The functions in the backend `ProductivityService` just perform read, create, edit, and deleting operations. You will need to implement the _editing_ functionality of the service in this exercise, then use all of the service functions to create your own APIs.

# Technical Requirements

For this exercise, there are a series of tasks you will need to complete _in order_. Make sure to read the instructions carefully.

## Task 1: Complete the Backend `ProductivityService`.

The backend `ProductivityService` has almost been completed for you, but you must implement the `update_timer()` method. Complete all of the `TODO` items listed in the comment in the `update_timer()` method.

**Requirements:**

1. The method must update the correct timer in the backend. The number of elements in `_timers` before and after this operation should remain the same.
2. Throw the correct HTTP exception if the user tries to edit a timer that does not exist.
3. The method should return the model for the updated timer.

## Task 2: Write Unit Tests for `ProductivityService.update_timer()`.

Tests already exist for all of the other method of `ProductivityService`. These tests can be found in the `/backend/test/services/productivity_test.py` file.

Now, it is your turn to write PyTests for your new `.update_timer()` method! Carefully read through the tests for fetching, adding, and deleting timers. Note that all of the test functions inject a `ProductivityService`. Using what you see in the other provided tests, write at least two test functions that test your function in a variety of scenarios. If you are unfamiliar with PyTest, feel free to check out the [Official PyTest Docs](https://docs.pytest.org/en/7.1.x/contents.html).

_Hint: Look at the "Requirements" section of Task 1! Ideally, your tests should ensure that all of these requirements are met._

**Requirements:**

1. Write at least two test methods that ensure all requirements of Task 1 are met.
2. All of your tests should pass.

## Task 3: Write the Productivity Feature's APIs

Your next task is to implement all of the Productivity Feature's APIs! You will implement your FastAPI API functions in the `/backend/api/productivity.py` file.

In this file, you will notice 5 `# TODO` comments specifying the API you need to create. Beneath each comment, implement these APIs. Make use of the service functions you were just working on!

Note that when you run `honcho start`, you can navigate to `localhost:1560/docs` in your browser, which shows a nice page that shows all of the FastAPI APIs implemented for your site! You should be utilizing this page to view and test out the APIs you create.

**Requirements:**

1. Implement the following API: GET /api/productivity
2. Implement the following API: GET /api/productivity/{id}
3. Implement the following API: POST /api/productivity/
4. Implement the following API: PUT /api/productivity
5. Implement the following API: DELETE /api/productivity/{id}
6. All my new APIs should be accessible at `localhost:1560/docs`.
7. All my APIs work as expected when tested at `localhost:1560/docs`.

# Task 4: Connect the Angular Service to the New APIs

Now comes the fun part - tying everying together! Now that you have created your APIs, you will want to connect this to the frontend of your site.

Recall that in EX01, your frontend service was responsible for storing and managing your data. Now, your services will serve their necessary, true role - calling APIs to access data!

First though, it is important to familiarize yourself with the frontend Data Models for this project. Navigate to these models at `/frontend/src/app/productivity/timerdata.ts`.

You will notice two different models - `TimerResponse` and `TimerData`.

```ts
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
```

This is peculiar, because in EX01, you likely only had one model that looked like `TimerData`. However, there is a problem. Remember that APIs just send data in JSON format. Our backend has _no idea_ about the functionality of the `PomodoroTimer` class in our frontend! It just sends over the `timer_length` and `break_length` data - that is it! So, when we retrieve data from our APIs, we will be working with `TimerReponse` objects instead. Ultimately though, our frontend works with `TimerData` objects. So, we need some way to convert from `TimerResponse` objects to `TimerData` objects.

The data flow will eventually look something like the following:

```
Backend: `PomodoroTimer` Pydantic model
  --- received from the API as --->
Frontend: `TimerResponse` model
  --- converted to --->
Frontend: `TimerData` model
```

Navigate to the frontend `ProductivityService` at `/frontend/src/app/productivity/productivity.service.ts`.

You want to utilize the `http` client to call APIs! This client is already injected into the `ProductivityService`.

Like before, There are many `// TODO` comments that specify which functions you need to implement functionality for!

Using a similar format to other services in the frontend application, use the `http` client to interact with the API endpoints you created on the backend.

Note: The HTTP client will return data in the `Observable<T>` format. Since you are working with `TimerResponse` data, you will want to ultimately convert this data from the `TimerResponse` type to the `TimerData` type.

_Hint: Explore the pre-made `private` functions defined at the bottom of the page._
_Hint 2: Explore the `.pipe()` operator [here](https://rxjs.dev/guide/operators)._

Finally, explore the documentation above the `timers` and `timers$` fields of the class! You will need to work with these fields to store the most up-to-date list of timer values from your backend.

**Technical Requirements:**

1. Implement all frontend service methods as specified in the comments. All should use `TimerResponse` data to interact from the API, but ultimately return data in the form of `Observable` objects of type `TimerData` (or `TimerData[]` where applicable).
2. The `.getTimers()` method should update the internal `.timers$` observable field with the latest data once it is retrieved. _(Hint: Use the `.subscribe()` method)_.

# Task 5: Connect the Angular Components to the Data

Congrats! You are almost done. The final step of this exercise is to hook up our new functionality to our components and widgets in the Angular frontend. There are a few `TODO:` comments in the TypeScript files for the `ProductivityComponent`, `TimerEditorComponent`, and the `TimerWidget`. Complete these tasks using the new service methods you created.

**Technical Requirements:**

1. When loading the `ProductivityComponent` on the frontend, the page is updated with the timer data from the backend.
2. Creating or editing a timer in the `TimerEditorComponent` will call the appropriate APIs from the backend.
3. Clicking the "Delete" timer button in the `TimerWidget` will call the correct API from the backend to delete the timer.
4. After deleting a timer, the data of the service is also refreshed.

# Workflow Expectations

Pair Program, ideally in person, on each of the stories. Do so in work-in-progress branches that get pushed to your team’s repository and merged back into the main branch. Each member of the pair should be the commit author for at least one of the subtasks (unless there is only 1 subtask!). You should create a branch per story and a commit per subtask completion. Once all subtasks are complete, merge the story’s commits back into stage.

Once finished with a story, the “driving” partner should create a pull request for the completion of the story, and the “navigating” partner should review it and merge it into main via GitHub’s interface. Each partner should create at least two pull requests, and each partner must merge two pull requests from the other partner. For reference on pull requests see Creating a pull request and merging a pull request.

# Getting Started

1. Find your Team Name and paired partner on the sheet linked to from the Canvas announcement.
   Lookup their contact information in the UNC Directory if you do not have it already.
2. E-mail them, if they have not e-mailed you already, and propose some of the next possible dates and times you can get together to pair program!
3. Once together, follow the setup instructions.
