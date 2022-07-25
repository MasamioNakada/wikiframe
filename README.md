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

[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://cdn.discordapp.com/attachments/826683941053399091/928700680661782628/unknown.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Wiki-Tools</h3>

  <p align="center">
    Convert all csv files in a folder to a diccionary of dataframe and more!.
    <br />
    <a href="https://github.com/MasamioNakada/wiki-tool"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#installation">Installation</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This package scan all the .csv files in a folder a convert into a dataframe, It is accept different csv delimiter and encodings. Also if you want to add transform functions, you can add it.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Installation

1. Install from [PyPI](https://example.com)
    ```sh
   git clone https://github.com/MasamioNakada/wiki-tools.git
   ```


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

### Extractor:  
This function will extract all the csv files in the folder and convert them to a dictionary of dataframe.

        Parameters:
        -----------
        func : A list of functions that will be applied to the dataframe. (e.g. [func1, func2, func3])
        verbose : If True, will print the name of the dataframe that is transformed. (default False)

        Returns:
        --------
        data_dict : A dictionary of dataframe.

        Notes:
        ------
        The order of the dataframe in the dictionary is the same as the order of the csv files in the folder.
        func could be a list of functions or a single function.

Example:

```python
from wiki_tools import Extractor # Import the Extractor function

extractor = Extractor(path='path/to/folder') # path to folder with csv files

data_dictonary = extractor.extract_from_csv() # extract all csv files on a folder and convert into a dictionary of dataframe
```

### Say:
A cow helper function to say something
    Parameters:
    -----------
    something:  A string to say in console

Example:

```python

    from wiki_tools import Say # Import the Say function    
    say = Say('Hello World') # Say something
    say.cow_says_good() # Say something in cow speak
    say.cow_says_error() # Say something in cow speak
 ```

Output:
    
```
< Hello World >
 -------------
        \   ^__^
         \  (oo)\_______
            (__)\ good🙈 )\/\
                ||----w |
                ||     ||
 _____________
< Hello World >
 -------------
        \   ^__^
         \  (oo)\_______
            (__)\ good🙈 )\/\
                ||----w |
                ||     ||

```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/MasamioNakada/wiki-tool.svg?style=for-the-badge
[contributors-url]: https://github.com/MasamioNakada/wiki-tools/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/MasamioNakada/wiki-tools.svg?style=for-the-badge
[forks-url]: https://github.com/MasamioNakada/wiki-tools/network/members
[stars-shield]: https://img.shields.io/github/stars/MasamioNakada/wiki-tools.svg?style=for-the-badge
[stars-url]: https://github.com/MasamioNakada/wiki-tools/stargazers
[issues-shield]: https://img.shields.io/github/issues/MasamioNakada/wiki-tool.svg?style=for-the-badge
[issues-url]: https://github.com/MasamioNakada/wiki-tools/issues
[license-shield]: https://img.shields.io/github/license/MasamioNakada/wiki-tool.svg?style=for-the-badge
[license-url]: https://github.com/MasamioNakada/wiki-tools/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/MasamioNakada
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
