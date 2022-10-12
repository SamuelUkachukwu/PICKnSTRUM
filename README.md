# Pick & Strum
Pick&Strum is a specially designed website application for a business that sells stringed instruments, including anything from guitars to violins, and related accessories. It is intended to provide users with a secure and simple experience. This project was created utilizing the Django framework and supporting languages in Python, HTML, CSS, JavaScript, as well as other libraries like Crispy, Summernote Allauth and Stripe.

## Table of Content

- [Responsiveness](#responsiveness)

- [Site Scope](#site-scope)
    * [user stories](#user-stories)

- [Features](#features)
    * [Navigation](#navigation)
    * [Features left to implement](#features-left-to-implement)

- [Database Model](#database-model)

- [Wire Frame](#wire-frame)

- [Language, Framework, Library and Tools](#language-framework-library-and-tools)

- [Testing](#testing)

- [Bugs](#bugs)

- [Deployment](#deployment)

- [Credits](#credits)

- [Acknowledgment](#acknowledgment)

- [Disclaimer](#disclaimer)

<details>
<summary>Dropdown Heading</summary>
<br>
Choice 1
<br> Choice 2
<br> Choice 2
<br>
</details>

## Responsiveness:
The site is responsive and can be easily accessed with full functionality in full screen, tablet and mobile screen
![responsive design of the website from ami.responsive.com]()

## Site Scope
* Responsive Design: Pick&Strum website should be fully responsive in all devices from screen size 280 upwards
* No loss to functionality between mobile devices and tablets or desktops
* Site user can view products and blog post.
* Site users can make purchase without need to create an account.
* Site users can view blog post and intaract by liking or disliking post.
* Site users can create a personal account and save and view thier order history
* Site Users can update thier data and review product they have purchased.
* Restrictions to key site features unless site user is registered and logged in
* Logged in users’ ability to perform full CRUD functionality to their profile and reviews posted on the site
* Logged in users ability to interact with posts in the blog section

### User stories
| As a...                | I can...                                                 | So I can...                                                                 |
| :------------          |   :------------------------                              |        :--------------------------                                          |
|As a user               | I can see all products           |  so that I can select some to purchase.                                          |
|As a user               | I can view individual products                          |so that I can see the rating, details, specifications, price, quantity
|As a user                |I can easily identify deals and clearance               |so that I can benefit from the deals and promotions
|As a user               |I can search for a product by name or category           |so that I can find a product easily and quickly
|As a user               |I can sort available products in order of prices or brand |so that I can make informed decision and manage purchase and expense parameters
|As a user               |I can add items I want into a bag                        |so that I can easily add or remove items
|As a user                |I can view the total of my purchase                       |so that I can make informed decision on how much I am spending
|As a user                  |I can view list of posted blogs                        |so that I can select and read any one I like
|As a user                  | I can click on a post                                  |  so that I can read the full post.
|As a user             |I can easily register an account                       |so that I will be able to view my profile
|As a user             |I can Easily Login and Logout                          |so that I can access my personal information
|As a user             |I can easily recover my password                       |so that I can log back into my profile
|As a user             |I can have a personalized user profile                 |so that I can view my order history update my user profile and save my payment confirmation
|As a user             |I can Subscribe to sites newsletter                    |so that I can receive informative newsletters and benefit from any deals available
|As a user               |I can save purchase history to my profile              |so that I can review the items and plan feature purchases
|As a user               |I can pay for products in my shopping bag securely     |so that I can feel safe and confident using my card on the site
|As a Site Admin        |I can view a data entry form                           |so that I can add, update and delete products and posts


[back to content](#table-of-content)

## Features
### Navigation:
Navigation bar is fully responsive and show different layout yet equal functionality in mobile and desktop site.
the company name also servers as a home button for users to get to the home page on a click.
a search bar is convinently placed in the middle for ease of use and in mobile it drops down below the navbar at a convinent line of sight .
on the right is the user account and store cart link, both icons are degined to show informations easily recognized by the user.
* The account icon hides a dropdown indicated by the down chevron arrow.
* If user is not logged in the options to register or login is shown.
* if logged in the opitins to manage store (if superuser) profile and logout is shown.

<details>
<summary>Navigation ScreenShots</summary>
<br>Site Navigation

![navigation user logged in](readme_imgs/user-logged-in.png)

<br>Navigation user not logged in

![navigation user not logged in](readme_imgs/user-not-logged-in.png)

<br>Navigation mobile view

![navigation mobile view](readme_imgs/mobile-dropdown.png)

<br>Navigation mobile view search dropdown

![navigation mobile view search dropdown](readme_imgs/mobile-search-position.png)
<br>
</details>


### Home Page:
The site Home page features a bold statement in line with what the site offers. A call out to music lovers and an offer to assist in making that dream come through.
the home page is built around a Carousel that imtermitently changes both eye catching and informative presenting clients to the options of: shop Now, shop deals or blog post.
<details>
<summary>Home Page</summary>
<br> Home Page 1

![home page](readme_imgs/home-page1.png)
<br> Home Page 2

![home page](readme_imgs/Home-page-2.png)
</details>



![category list page](static/img/category_page.png)
site users need to be logged in to view the category page.

Each post can be viewed in detail by clicking the Title of the post this takes the site user to a detail view page were logged in users can interact with the post by liking or disliking the post or leaving a public comment.
site users not logged in are requested to do so to be able to interact with the post they are viewing.
![request to login before interaction](static/img/sign_in_required.png)

In addition to being able to interact with posts, registered users can also add, edit and delete own posts in a custom user page.
![private profile page](static/img/user_profile_page.png)

When each post is viewed, site users can also view a public profile of the author with a list of all the authors published post sorted in order of new to old.
![public profile page](static/img/public_profile.png)

### Features left to implement:
* Follow Author functionality


 [back to content](#table-of-content)
## Database Model

Relational Database Model was used in this project
![Data Model](static/img/relational%20database%20model.png)

[back to content](#table-of-content)
## Wire Frame
Mock up site was created using figma wireframing. individual frames can be seen [here](wireframe.md)

[back to content](#table-of-content)
## Language, Framework, Library and Tools
* HTML5 [More on HTML5 ](https://en.wikipedia.org/wiki/HTML5)
* CSS3 [More on CSS](https://en.wikipedia.org/wiki/CSS)
* JavaScript [More on JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* Python [Python](https://www.python.org/) [Read More on Python](https://en.wikipedia.org/wiki/Python_(programming_language))

* Bootstarp 5 [Bootstrap](https://getbootstrap.com/)
* Django [Django](https://www.djangoproject.com/)

* Django-allauth [django-allauth read the doc](https://django-allauth.readthedocs.io/en/latest/)
* Cloudinary [Image hosting](https://cloudinary.com/)
* Crispy-form [django-crispy-form read the doc](https://django-crispy-forms.readthedocs.io/en/latest/install.html)
* Summernote [Summernote Docs](https://summernote.org/)

* Figma [more on Figma](https://www.figma.com/)
* Heroku [more on Heroku](https://devcenter.heroku.com/)

[back to content](#table-of-content)

## Testing
The codes were tested by doing the following:
### Manual Testing:
1.	Entered invalid inputs and wrong inputs where inputs are requested with respect to integers and strings.
2.	Recruited help from friends to use app and offer feedback
3.  Lunching site on different devices and browsers to check for responsiveness and bugs.
    * google chrom
    * fire fox
    * microsoft edge
    * Operamini

#### W3C CSS Validation: No Errors returned
![CSS validation](static/img/css_validation.png)

#### Pep8 Validation: No errors returned
![pep8 validation](static/img/pep8_check.png)

#### Accessibility:

Accessibility testing was conducted using light house devtools and it confirmed that the fonts and colors selected are easy to read and accecssible.
![lighthouse validation](static/img/lighthousetest.png)

#### Unittest:
Unit test was created to test the form.py, views.py and models.py

[back to content](#table-of-content)

## Bugs
* none found

[back to content](#table-of-content)

## Deployment
The project was deployed to Heroku with the following steps:
1. create a Heroku account
1.  in the settings section reveal the config var and enter the key and value pair from the settings.py file
DJANGO_URL, SECRET_KEY, PORT and CLOUDINARY_URL
1.	on the Resources tab select Heroku Postgres as the database
1. on the treminal type:
 ```
 python3 manage.py makemigrations
 ```
 and
 ```
 python3 manage.py migrate
 ```
 to migrate your database.
1.	on the CLI create a requirements.txt file using the command:
 ```
 pip3 freeze -–local > requirements.txt
 ```
1.	Add a Procfile with the required codes in it: ```web: gunicorn .wasgi```
1.	Change Debug to False and commit repository to Github.
1. In the deploy section select github and search for the repository name. link up the Heroku app to the github repository code.
1. Scroll down and setup automatic deploy to allow Heroku to update app from gitpod push and click on the manual deploy option.
1. click view to view the app.
* The Deployed App can be viewed here [](https://story-base.herokuapp.com/)

[back to content](#table-of-content)

## Credits
* Code Institute [Code Institute](https://codeinstitute.net/ie/)
* Django Doc [read the doc](https://docs.djangoproject.com/en/4.0/)
* Pixabay for the images used on the site [Pixabay](https://pixabay.com/)
* Ukachukwu Sherifat [@Nurse_Ukachukwu](https://twitter.com/nurse_ukachukwu) for external user testing.

[back to content](#table-of-content)

## Acknowledgment
* Code Institute Tutor Assistance
* Caleb Mbakwe Mentor
* Sherifat and Olivia for all the love and support

[back to content](#table-of-content)

## Disclaimer
This site was developed for educational purposes only. _Samuel Ukachukwu 22/06/2022_
