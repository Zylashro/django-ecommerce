![HTML Validator](#)

[Live Site](https://ms4-django-ecommerce.herokuapp.com/)

# Medb

This project is designed to be a simple e-commerce site selling software. The project serves to demonstrate my ability and understanding of Django.


## Table of Contents:
1. [**Project Overview**](#project-overview)
2. [**UX**](#UX)
    - [**User Stories**](#user-stories)
	- [**Mockup**](#mockup)
3. [**Features**](#features)
    - [**Header**](#header)
    - [**Home Page**](#home-page)
    - [**Store**](#store)
    - [**Product Detail Page**](#product-detail-page)
    - [**Login / Register Page**](#login-/-register-page)
    - [**Profile**](#profile)
    - [**Footer**](#footer)
4. [**Technologies**](#technologies)
    - [**Pips**](#pips)
5. [**Testing**](#testing)
    - [**HTML Validator**](#html-validator)
    - [**CSS Validator**](#css-validator)
    - [**JavaScript Validator**](#javascript-validator)
    - [**Browsers**](#browsers)
    - [**Manual Testing**](#manual-testing)
6. [**Deployment**](#deployment)
7. [**Self-Reflection**](#self-reflection)
8. [**Credits**](#credits)
    - [**Icons**](#icons)


## Project Overview

The goal of this site is to sell all kind of software to users. With the users being able to add each individual item into their cart, and remove them, before checking out their purchase. 


## UX

- As an user, I want to be able to browse through the sites collection of items.
- As an user, I want to be able to view the details of each individual item.
- As an user, I want to be able to add items into a cart so I can purchase in bulk.
- As an user, I want to be able to view all the items in my cart.
- As an user, I want to be able to remove an item from the cart.
- As an user, I want to be able to navigate to to each item from the cart.
- As an user, I want to be able to see both the total cost of all items in my cart and each individual item.
- As an user, I want to be able to purchase my items through a secure method.
- As an user, I want to be able to view the history of my purchases.
- As an user, I want to be able to view each individual license for the software I purchases.

### Mockup

A link that takes you to the mockup I made for this project. **Note, that the links take you to a PDF file and do not display an image!**

- ![Mockup Desktop](#)
- ![Mockup Mobile](#)

## Features

### Header:

The header contains the logo to the site which when clicked will take the user to the home page. Along side that there are four additional icons.

A search icon which when clicked will open up the search bar for the store.

An user icon which will take the user to the login/register page or their profile depending if they are currently logged in.

A cart icon which will display all the users items if they have any in the cart.

And a burger icon which when clicked will open a dropdown with links to other pages of the site.

### Home Page: 

A simple page with a carousel showing either three products that are currently on sale, or showing three random products. The carousel slides can be scrolled through using either the arrows or highlighters below.

### Store Page:

The page will display all the products that the user can purchase in neat little cards.

If a product/s is currently on sale it will display at the top of the store with a title indicating that the product is on a sale. If no product is on sale than no on sale title will be present.

The user will be able to sort the order of the products with the select menu near the title of the products list.

Each product card contains an image, the products name, description, rating, price, and an option to add the product to their cart. Clicking on either the image or title will take the user to that products detail page.

The user won't be able to add a product to their cart unless they are signed in.

### Product Detail Page:

This page will reiterate all the information about the product just like the products card on the store page albeit in a nicer, easier to read format.

If the product is currently on sale, their will be an indicator on the page notifying the user of this detail.

The user will be able to add the product to their cart if they are signed in.

### Login / Register Page:

A brief page containing both a login and register form.

The user will also be able to click a link to change their password if they forgot it.

Along side the two forms the user will have an option to create an account through their Google, Facebook, or Twitter account if they prefer.

### Profile:

On the users profile the user will be able to see their username and email, their order history, and all the software licenses that they have bought in the store.

The user will also be able to change their password here through a change password form.

### Footer:

The footer contains some information about the store and contains the links to all manners of legal pages.


## Technologies

The list of technologies and third-party packages used in the making of this project:

- **HTML5:** HTML5: Modern HTML to form the structure of the site.
- **CSS3:** Used to style the site along with Flexbox and Grid.
- **JS:** Used for the logic between HTML elements and interaction between the user and the site.
- **Python3:** Used to create the backend and data-manipulation portion of the project.
- **Django:** A Python based web-framework used to create the templates and function views for the project.
- **Git:** Used for version control from the very beginning of the project.
- **Github:** A remote repository used to store the source code for the project.
- **Heroku:** A third-party hosting service used to deploy the live project.
- **VsCode:** Source code editor used to write, edit, test, and debug the source code.

### Pips

Along with the technologies listed above, I've also used the following pips while making this project:

- **[Flask](https://flask.palletsprojects.com/en/1.1.x/):** A micro web framework written in Python used to loop over the database, create the HTML templates, and append the results from the backend code to the frontend.

For any additional pips please refer to the requirements.txt file.

## Testing

### HTML Validator

The result of the HTML Validator can be seen in the image below:

![HTML Validator](#)

### CSS Validator

The result of the CSS Validator can be seen in the image below:

![CSS Validator](#)

### JavaScript Validator

The JS used in this project was tested with **[JSHint](https://jshint.com/)** to ensure bug free and correct code.

Due to the fact that the JS for this project is split between five different files, I have opted to combine the results of each tested file into a single result for easier analytical purposes.

Each file has been separately tested to ensure lack of conflict between files.

- Metrics:
    - There are 19 functions in this project.
    - Function with the largest signature take 1 arguments, while the median is 1.
    - Largest function has 6 statements in it, while the median is 2.
    - The most complex function has a cyclomatic complexity value of 3 while the median is 1.

### Browsers

The site has been tested on the following browsers:

- Chrome
- IE
- Edge

Chrome and Edge work as intended without issue.

IE is broken with the table on both the indexes being out of line. The icon on the home page being displaced. And the charts not displaying at all.

### Manual Testing




## Deployment

The process it took to deploy this project goes as follows:

1. Download and install **[Python](https://www.python.org/)** and **[Node.js](https://nodejs.org/en/)**.
2. Clone the repository
```
git clone https://github.com/Zylashro/data-index-project.git
```
3. Move into the folder
```
cd data-index-project
```
4. After you've done that, make sure Node is installed and run the following to get all the JS dependencies
```
npm install
```
5. Install requirements with pip
```
pip install requirements.txt
```
6. Create and activate your virtual environment
```
python venv env
```
7. Either create a seperate .py file, or in the app.py file add the following code
```python
app.config["MONGO_DBNAME"] = 'ENTER_DBNAME'
app.config["MONGO_URI"] = 'CONNECT_TO_YOUR_DB'
app.secret_key = 'ENTER_SECRET_KEY'
```
8. Start the app
```
python app.py
```

## Self-Reflection




## Credits

The project would not be possible without the following:

### Icons

The icons pulled for this project come from [Font Awesome](https://fontawesome.com/).
