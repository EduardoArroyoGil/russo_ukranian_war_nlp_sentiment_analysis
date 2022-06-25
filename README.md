# Russo-Ukranian War Sentiment Analysis

Link al dashbaord [Dashboard](https://public.tableau.com/app/profile/eduardo.arroyo.gil/viz/russo-ukranianwar-politicalsentimentanalysis/Summary?publish=yes)



<div id="top"></div>
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
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/EduardoArroyoGil/russo_ukranian_war_nlp_sentiment_analysis">
    <img src="images/readme/politician-icon.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Russo-Ukrainian War Sentiment Analysis</h3>
</div>

[Presentation](https://docs.google.com/presentation/d/1fxxxqB1LBgWhg2PB84cYwxWtmVlDILNVrjqV_6a3i-Y/edit?usp=sharing)

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
    <li><a href="#getting-started">Objectives</a></li>
    <li><a href="#usage">Methodology</a></li>
    <li><a href="#roadmap">Repository Structure</a></li>
    <li><a href="#contributing">Conclusions</a></li>
    <li><a href="#contributing">Needed Libraries</a></li>
    <li><a href="#contributing">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<div align="center">
  <a href="https://public.tableau.com/app/profile/eduardo.arroyo.gil/viz/russo-ukranianwar-politicalsentimentanalysis/Summary?publish=yes">
    <img src="images/readme/screenshot_project.png" alt="screenshot_project" width="200">
  </a>
</div>

Este proyecto trata de analizar mediante una inteligencia artificial el sentimiento 
de los tweets emitidos sobre la guerra de ucrania. Principalmente el uso que han dado
los partidos politicos españoles a este tema para usarlo en su beneficio.

Asi como el impacto en la poblacion.

Para ello se han realizado busquedas en twitter bajo los conceptos:

*  Guerra de Ucrania
* Ukraine War
* Putin
* Ucrania
* Guerra Putin

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

las principales tecnollogias que se han utilizado para la realizacion de este proyecto son:

* Python
* Twitter
* OpenAI - GPT3
* Tableau
* MySQL
* Github

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Objectives -->
## Objectives

**Reason**: Interest on Politics and its relation with the psychology and the complexity of the Language and its connection with the reality.

**Objective**: Analyse the Russo-Ukrainian War usage on Twitter by the Politician & Political Parties and general public

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Methodology -->
## Methodology

The methodology to get the final solution is explained in the following image:

![](images/readme/Screenshot 2022-06-25 at 07.43.02.png)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Repository Structure -->
## Repository Structure

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Conclusions -->
## Conclusions

The two most active political parties on Twitter are PSOE and VOX:

PSOE may be for being in government, however VOX would not be explained by this.

The use that the PSOE makes of this topic is by making comments that convey emotions typically classified as positive or order-oriented and VOX negative or disorder-oriented. This can be explained because VOX does not govern and the PSOE does and the intentions of each one of them are the opposite.

We see that there is a clear tendency towards two sentiments in a generic way, Anger and Pride, from the part of the general public. This may be explained by the polarization also observed in political parties. However, we cannot guarantee that:
* Political tweets influence general opinion
* General public tweets influence political tweets
* Both at the same time


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Needed Libraries -->
## Needed Libraries

Main libraries to develop this project in python are:
* **pandas**: to manage dataframes
* **openai**: to connect to OpenAI GPT3 API
* **request**: to connect to APIs
* **tweepy**: to connect to Twitter API
* **tqdm**: to understand how much time code will take in each launch
* **time**: for time calculus
* **dotenv**: to manage .env files
* **SQLAlchemy**: to connect to data base

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Eduardo Arroyo Gil - [LinkedIn](https://www.linkedin.com/in/eduardo-arroyo/) - eduardoarroyogil@gmail.com

Project Link: [https://github.com/EduardoArroyoGil/russo_ukranian_war_nlp_sentiment_analysis](https://github.com/EduardoArroyoGil/russo_ukranian_war_nlp_sentiment_analysis)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/EduardoArroyoGil/russo_ukranian_war_nlp_sentiment_analysis.svg?style=for-the-badge
[contributors-url]: https://github.com/EduardoArroyoGil/russo_ukranian_war_nlp_sentiment_analysis/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/EduardoArroyoGil/russo_ukranian_war_nlp_sentiment_analysis.svg?style=for-the-badge
[forks-url]: https://github.com/EduardoArroyoGil/russo_ukranian_war_nlp_sentiment_analysis/network/members
[stars-shield]: https://img.shields.io/github/stars/EduardoArroyoGil/russo_ukranian_war_nlp_sentiment_analysis.svg?style=for-the-badge
[stars-url]: https://github.com/EduardoArroyoGil/russo_ukranian_war_nlp_sentiment_analysis/stargazers
[issues-shield]: https://img.shields.io/github/issues/EduardoArroyoGil/russo_ukranian_war_nlp_sentiment_analysis.svg?style=for-the-badge
[issues-url]: https://github.com/EduardoArroyoGil/russo_ukranian_war_nlp_sentiment_analysis/issues
[license-shield]: https://img.shields.io/github/license/EduardoArroyoGil/russo_ukranian_war_nlp_sentiment_analysis.svg?style=for-the-badge
[license-url]: https://github.com/EduardoArroyoGil/russo_ukranian_war_nlp_sentiment_analysis/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/eduardo-arroyo/
[product-screenshot]: images/readme/screenshot_project.png
