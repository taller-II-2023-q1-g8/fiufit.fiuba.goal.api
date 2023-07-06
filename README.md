<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![codecov](https://codecov.io/gh/taller-II-2023-q1-g8/fiufit.fiuba.user.api/branch/master/graph/badge.svg?token=CM3FJKHBQ0)](https://codecov.io/gh/taller-II-2023-q1-g8/fiufit.fiuba.user.api)



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/taller-II-2023-q1-g8/fiufit.fiuba.app.mobile">
    <img src="https://firebasestorage.googleapis.com/v0/b/fiufit-73a11.appspot.com/o/app.png?alt=media&token=77feb7b5-9fcc-4cd0-aa4a-54236b810170" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Goals and Metrics Microservice</h3>

  <p align="center">
    DDD Oriented REST API
    <br />
    <a href="https://fiufit-goals-and-metrics.onrender.com/docs">View Docs</a>
    .
    <a href="https://github.com/github_username/repo_name">View Demo</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
The APP has Goals which represent an Objective which should be fulfilled before a certain deadline. The progress towards the completion is based on metrics. These metrics represent an event such as a user walking a certain distance in a given time, or him/her completing an exercise set, including the weight lifted and repetitions performed. When goals are loaded from a repository, metrics are fetched automatically and the goal state is calculated based on them.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
* [![FastAPI][FastAPI]][FastAPI.com]
* [![MongoDB][MongoDB]][MongoDB.com]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* Docker-Compose

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/taller-II-2023-q1-g8/fiufit.fiuba.goal.api.git
   ```
2. Run App and Database with Docker-Compose
   ```sh
   docker-compose up --build
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This is a basic example of the main workflow:
- Create a goal: POST \<app-url>/goals/
- Create a metric to feed the goal: POST \<app-url>/metrics/
- Check the progress of the goal: GET \<app-url>/goals/\<goal-id>

_For more examples, please refer to the [Documentation](https://fiufit-goals-and-metrics.onrender.com/docs)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Define the Domain: Goals and Metrics
- [x] Define the project Structure
- [x] Impl. Goals & Metrics 
  - [x] Goal: MaxWeightLiftedInExerciseTraining
  - [x] Goal: TrainingPlanCompletion
  - [x] Metric: ExerciseSetCompleted
  - [x] Metric: TrainingPlanCompleted
  - [x] Goal: TotalStepsTaken
  - [x] Goal: TotalDistanceTravelled
  - [x] Metric: StepsTaken
  - [x] Metric: DistanceTravelled

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Franco Papa - fpapa@fi.uba.ar

Project Link: [https://github.com/taller-II-2023-q1-g8/fiufit.fiuba.user.api](https://github.com/taller-II-2023-q1-g8/fiufit.fiuba.user.api)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/https://github.com/github_username/repo_name
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[FastAPI]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[FastAPI.com]: https://fastapi.tiangolo.com/
[JQuery-url]: https://jquery.com 
[MongoDB]: https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white
[MongoDB.com]: https://www.mongodb.com/