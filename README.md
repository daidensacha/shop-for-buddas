
![](/documentation/images/shopforbuddhas-home.jpg)

# Welcome

## Code Institute: Milestone Project 4

### Project Name - Daiden Sacha - Full Stack Web Developer

View the [Project_name](project-URL) on Heroku.

[TESTING/](/documentation/testing.md) outlines my testing strategy, development, deployment and post-deployment.

## UX DESIGN

### 1. Strategy

#### User Stories:

[TESTING/User Stories Review](/documentation/testing.md/#user-stories-review-development-deployment)

### User Stories

1.  **As an vendor:**

- I want to be able to register to sell my work.
- I want to create a profile.
- I want to be able to upload my products to be sold in the shop.
- I want to be able to edit, update or delete my listed products.
- I want to be able to see a current list of my items listed for sale.
- I want to be able to see a current list of my sold items
- I would like to be informed when something sells.
- I want customers to be able to commission particular works with specific preferences. 

2.  **As a customer:**

- I want to buy quality statues.
- I want to be able to contact the seller if I have questions about the product.
- I want to be able to commission work for items I cannot find in the shop.
- I'm interested in knowing about the statue making process and the artisans that make the statues.

	***Browsing Products***

	- I want to be able to view items by category.
	- I want to be able to sort the items by ascending, descending order.
	- I want to be able to search statues by name.

	***Accounts & Registration***

	- I want a seamless registration process.
	- I want to be able to log in with an email and password, or with my social network account.
	- I want to be able to have a profile to save time for future purchases.
	- I want an option to be able to close my account.

	***Orders & Checkout***

	- It's important that I can easily and intuitively navigate the site.
	- I want to easily select and pay for items.
	- I want to receive confirmation of purchase.
	- I want a record of my orders attached to my account profile.

3.  **As the site owner:**

- I want to support grass root artists to continue their work.
- I want to provide a website where grass root artists can sell their work.
- I want to educate about the complexity of producing quality statues.
- I want to help to preserve the rich tradition of statue making.
- I want to provide quality hand made Buddhist dharma products to Buddhist practitioners.
- I want to make a nominal commission to pay for the maintenance of the site.

  
  

### 2. Scope

#### Required Features

##### ALL USERS:

-  **Navbar:** A simple navbar with the site logo, links to landing page sectons the shop, and the contact form. A search bar, and the shopping cart.
-  **Landing Page Banner:** I full screen banner with a link to the shop, simple callout message to engage the visitors attention.
-  **Contact Form:** A simple contact form for users to be able to contact the site administrator.
-  **Testimonial Carousel:** A Testimonial carousel displaying customer feedback.
-  **Blog:** A blog displaying providing information about the site, products, vendors, and other inforamtion to inform customers about the site and its activities.
-  **Shop:** An e-commerce shop to display the products produced and uploaded by teh vendors.
-  **Shopping Cart:** A shopping cart to display items selected by customers to purchase.

##### REGISTERED VENDOR USERS:

-  **Profile:** A user profile displaying the vendors registration information.
-  **Profile Management** A profile management section where the user can update information.
-  **Order History** Show a a list of the users order history.
-  **Sales History** Show a a list of the vendors sales history.
-  **Product List** Show a a list of the vendors products.
-  **Favorites List** Show a a list of the users favorites.
-  **Product Management** The vendor should be able to create and upload, edit, and or delete products.

##### REGISTERED CUSTOMER USERS:

-  **Profile:** A user profile displaying the customers registration information.
-  **Profile Management** A profile management section where the user can update information.
-  **Order History** Show a a list of the users order history.
-  **Favorites List** Show a a list of the users favorites.
-  **Checkout:** The user should be able to select and purchase items.

#### Functional Requirements
-  **Navbar:** Links to landing page sections, and to the shop.
-  **Search bar:** The user can search for shop items by name or category.
-  **Register Form:** New users can register an account.
-  **Login Form:** Users can login to their profile.
-  **Login Form:** Users can update their password.
-  **Profile management:** Users can update their profile details.
-  **Blog posts** Blog posts will be displayed in a list view.
-  **Blog Featured Post** Superusr can select posts to be displayed as featured posts.
-  **Blog pagination** Pagination will enable blog posts to be displayed on multiple pages.
-  **Blog tags and categories** Post tags and categories will allow for easy filtering of posts.
-  **Blog archive** A blog archive will display posts by year and month.
-  **Blog comments** A comment form will follow all blog posts so users can comment on the posts.
-  **Testinmnial Carousel** A carousel will display user testimonials that are publoished once approved by the superuser.
-  **Testinmnial Form** Logged in users will have access to a link on the testimonial carousel that will take them to a form to leave a testimonial.
-  **Contact Form:** Users can send a message easily using the simple form at the bottom of the landing page.
-  **Product Page:** The website shop will display products in a responsive grid. Users can select a product to view more detail and to purchase.
-  **Product Favorites:** An icon will allow users to select item to be added to a favorites list. The same button will also allow the user to remove the items from the favorite list. The status of the product will be evident by the color of the icon which will be a red heart when favorited, and an outlined heart when not favorited.
-  **Quick view/add:** Icons enable the user to easily add or view the products in the list view.
-  **Simple navigation:** Links and buttons provide easy and clear navigation options for the user to have a seamless experience navigating the site.
-  **Search Filters:** Users can select products by category and sub category. Links from the main navbar. Users will further be able to filter by ascending and descending order.
-  **Product Display:** Each product will display images, along with details of the product, and a add to cart button.
-  **Messages:** User actions will prompt messages that will be displayed in a drop down message div, that the user can then close.
-  **Shopping Cart:** When the user adds items to the cart, it will be displayed along with a link to the secure checkout. The cart will be easily accessible in a side modal, and enable the user to easily delete items from the cart without leaving the products page.
-  **Secure Checkout:** Transactions will be processed using Stripe, and will save the oder to the user profile when the transaction is processed.
-  **Image lightbox:** Images will be easily viewable in an image lightbox by clicking a quickview icon in the product list view.
-  **Admin Management** The site owner will be able to log in the the admin panel to view and manage products and users.
-  **Products Management:** In the admin panel, the admin user can add, update and delete products.
-  **User Management:** In the admin panel, the admin user can add, update and delete users.

#### Content Requirements

1.  **Inform and Educate:**

	- The main focus of the landing page will be to engage the site visitor, to inform and to educate them about Buddhist statues, the complexities time-consuming processes involved in making them. I want users to understand the history of the art, and how it is becoming lost. It is important to understand that quality comes at a price.

	- The motivation for the site is a not for profit site providing suppor to grass root artists making Traditional Tibetan Buddhist Statues. This is a theme that is imortant to convey.

2.  **Display and Sell:**

	- The site will provide a shop displaying the artists works for sale. Each product will show images, along with information about the items.

	- The site will focus on selling qualtiy hand made Buddhist Dharma items to support practicing Buddhists.

	- The items will also be available for novice practitioners or those appreciative of the art.

### 3. Structure

#### Interaction Design

Visitors to the site will be greeted by a full screen dark banner, with with callout text gteeting them, and a link to the shop.

The landing page will display cascading sections, each flowing into the next in a logical order.

Navbar | Jumbotron | Services | Features | Testimonials | Contact

The home page goal is to engage the user, though the contrast in color, and interesting content. It is meant to be an out of the box clean and crisp design. Interest engaged, the user is then led to visit the shop out of curiosity to view the works on offer.

The flow of informatin and the structure is meant to be easy and intuitive to navigate. An adventrure to discover and enjoy.

#### Information Architecture

***Navigation***

- Fixed minimal navbar at the top of the page.

- Navbar: Logo links to the homepage. Links to Shop, Services, Statue Making, Artisans, Contact. Search bar for searching products. My account link. Shopping cart to show added products and link to the secure checkout.

***Services Section***

- Outlines the sites services.

***Features***

- A section displaying the main products of the site. Hand crafted Buddha statues, and meditation malas.

***Testimonial Section***

- A carousel displaying user testimonials. A link for logged in users will guide them to the form to leave the testimonial.

***Contact Form***

- Simple form with name, email, subject and message for users to be able to easily contact the site adminsistrator.

***Footer***

- Contains social icons linking to Facebook, Github and Linkedin.
- Contains 2021 copyright and website name.

***Shop***

- Products laid out in grid format, displaying the product image that users can select to view more info. Clicking on the link will open the product display page, showing all images for the product, along with the product infomation, rating, price and add to cart button.

***Shopping Cart***

- Clicking on the add to cart button adds the product to the shopping cart. A success message appears informing the user the item was added to the cart, along with the total. The cart information and a link to the secure checkout also appears.

***Secure Checkout***

- The user can edit the cart contents, and click the link to the secure checkout, or click the link to continue shopping. At the secure checkout, the user is required to fill out the form with their details, to complete the transaction. They can also create an account or login to save the order information to their account. The carts contents with the order total is also displayed.

***My Account***

- The user can login to view, and or update their account profile. All orders are displayed on this page, with a link to view the order information. The admin user can also add, update or delete product information on from the user profile. A section in the profile will also display the list of users selected favorites.

### Database Schema

#### Shop for Buddhas Database Schema

![](/documentation/images/sfb-db-schema.jpg)

Being new to Django, planning the database schema was a big challenge. The schema I started with gave me a roadmap to create what I needed. The reality on the way was that at times I needed to change, or add, or adapt certain aspects to encorporate, or fully achive what my goal was.

**Django Models**

1.  **Accounts Model**

I needed to create a custom user registration to allow users to select their type of account, a customer, or a vendor. This presented several problems.
- The Allauth registration form template does not include the fields for first and last names. I fixed this after creatign the user profile, when I realised that it should have been included in the initial registration

- Adding select for the ```user_type``` required including the additional fields in the form, and ensuring that the information was saved to the database.  

To do this I extended the ```AbstractUser``` model, adding a select field to the allauth user registration form with the option for users to select the type of account.

```python
# models.py

user_type = (
('is_admin', "Admin"),
('is_customer', "Customer"),
('is_vendor', "Vendor")
)

"""Add user_type field to user profile model"""
user_type = models.CharField(max_length=25, choices=user_type, blank=True)
```

```python
# forms.py
"""
Note the is_admin option is excluded here intenionally as I did not want
this choice available to users in the registraion process. This option was
included purely for use in the administraion panel.
"""
user_type = (
('is_customer', "Customer"),
('is_vendor', "Vendor")
)

"""Add user_type field to user profile model"""
user_type = forms.ChoiceField(
choices=user_type,
label='Register as a customer or vendor?',
required=True)
```

This allowed users to register either as a customer, or as a vendor.
  

2.  **Products Model**

- My products model is an extended version of the same model used in the Boutique Ado project. I needed to add additional fields to

allocate ownership of the product to a vendor, or admin. For this I added the ```created_by``` field which references the ```user_id```.

- Adding the functionality for users to add products to a favorite list was initially problematic. I initially tried creating a separate table for the favorites. That table container references to the primary key of the user and of the product. I encountered issues displaying the items as I wanted, so I changed to a simpler method.
I added a favorites ManyToManyField to the product model that references the user primary key. The favorites column then contains a list of users who added it to their favorites. This allowed me to filter each product for the authenticated user to return the list of their favorites, and display the result on the products page, and in the users profile.

**Favorites: Product List Page**
![](/documentation/images/favorites-products.jpg)

**Favorites: User Profile Page**
![](/documentation/images/favorites-profile.jpg)

3.  **Testimonial Model**
The testimonial model was fairly straight formard. I allows authenticated users to create a testimonial, which once approved, is then displayed in the home page testimonial carousel.
 
 Here I wanted the users rating to be refelcted in the HTML by displaying visually the rating of the user. For this I added the select options to the user form.
In the Django model.
```python
rating = (('1', '1/5 stars'),
		  ('2', '2/5 stars'),
		  ('3', '3/5 stars'),
		  ('4', '4/5 stars'),
		  ('5', '5/5 stars')
	)
```
In the HTML I then looped the rating adding one full star for each loop.
```python html
{% for star in stars %}
	{% if star < testimonial.user_rating|add:"1" %}
		<span  class="text-warning"><i  class="fas fa-star"></i></span>
	{% endif %}
	{% if star > testimonial.user_rating|add:"0"%}
		<span  class="text-warning"><i  class="far fa-star"></i></span>
	{% endif %}
{% endfor %}
```

**User Rating**
![](/documentation/images/user-rating.jpg)

I incorporated this into the product model as well for the product rating.

4.  **Blog Model**
The blog was initially meant to be simple, as I wasn't sure how complex it can be, and with limitations on time I wanted to limit the scope to ensure it didn't blow out. 
I created a ```Post``` model, a ```Category``` model, and a ```Comment``` model. In addition to this, I added ```django-taggit==2.0.0``` to add tags to the posts. 
Displaying the posts was a relatively straight forward. I had many issues with returning and displaying correct results for the category and search query. The root of the issue always seemed to come back to the featured article. It was not being included in the filter, or when it was it was being displayed as the featured article. 
It now displays correctly, and the tag, category, and blog search queries all work as I expect. 

5.  **Checkout Model**
The checkout model is based on the Boutique Ado model, with some minor changes as my handling os the size for my products is different, using a charfield. 
  
6.  **UserProfile Model**
The UserProfile model is also based on the Boutique Ado project. By including the user type field in the user registration, I was able to use the same profile model to display the same profile information for both customers and vendors. 
In the HTML, i have included additional tabs in the vendor profile, one for vendor sales, and one for vendor products. 
I was able to do this by filtering the order line items and product models to list the vendors sold products, and listed products. 
The vendors can upload their products by completing a form linked from their profile menu, or the vendors products list in their profile. 
  
### 4. Skeleton

#### Wireframing:
I created the wireframes for the project in Adobe XD. Wireframes are basic and only a guide.

I made one change to the theme very early in the project. I changed from the dark navbar to a light one as it was much cleaner and a better fit for the style.

[View the wireframes/](/documentation/wireframes.md)

### 5. Surface

**Visual Design:**

The selection of colors for the site displays stark contrast between dark and light, giving a clean and crisp feel. the choice of purple and green gives a fresh and uplifting feeling and highlights UI points to be focussed on. 

The navigation is minimal, offering a home, shop, blog and contact links. A megamenu drops down to display all the shop categories. I used a side modal for the shopping cart, easily accessiible at all times and on all pages. 

A contact form is at the bottom of the home page, and the link in the menu scrolls the page to the form. As the user navigates the site, I have placed links and buttons anticipating the users desire to move to other parts of the site or shopping process. 

Toast messages inform the user of the success of their interactions. The toast messages slide in, then slide off screen automatically. 

The design intention is for the experience of visiting the site to be seemless and enjoyable.

## TECHNOLOGIES USED

**Languages Used**

1. HTML
2. CSS3
3. SCSS
4. JavaScript
5. jQuery
6. Python
7. Jinja
8. Markdown

 
**Frameworks, Libraries, Programs used**

1.  [Django 3.2](https://www.djangoproject.com/)
"The web framework for perfectionists with deadlines".
2.  [Bootstrap 5](https://getbootstrap.com/)
The responsive framework of choice for this project.
3.  [Heroku](https://www.heroku.com/home)
Hosting the project.
7.  [Font Awesome](https://fontawesome.com/)
Icons used in the website.
8.  [GitHub](https://github.com/)
Used to host project repository and to deploy the project live via GitHub Pages
9.  [Git Version Control](https://git-scm.com/)
I used it to commit blocks of work to the GitHub repository and create branches to work on specific changes or testing.
10.  [Gitpod](https://gitpod.io/workspaces)
The editor used to work on the project.
11.  [Adobe XD](https://www.adobe.com/products/xd.html)
Used to create wireframes
12.  [Adobe Photoshop](https://www.adobe.com/products/photoshop.html)
I used the software to work on the project images.
13.  [Adobe Illustrator](https://www.adobe.com/de/products/illustrator.html)
Used to create my 404, 405, and 500 error images to display if users encountered missing or broken page links.
14.  [Squoosh](https://squoosh.app/)
I used it to compress images to optimize load performance.
15.  [Quire](https://quire.io/)
Free project and task planning application used for adding and planning tasks for the project.
16.  [Depositphotos](https://depositphotos.com/?gclsrc=aw.ds&&utm_source=google&utm_medium=cpc&utm_campaign=DP_EU_EN_Brand_Search&utm_term=depositphotos&gclid=CjwKCAjwuvmHBhAxEiwAWAYj-EVeHDBPdjs594mAT_HDLeFGM_g2IVcGn78NSArH7vXIYqfoO1BuhBoCv_kQAvD_BwE)
My source of choice for stock images.
17.  [StackEdit](https://stackedit.io/)
It's a free, online note-taking and markdown application. I used it to create the README file for GitHub.
18.  [Webmaker App](https://webmaker.app/app/) It is a free application similar to codepen, used to create and save the work locally. I use it to implement and experiment with using components of different frameworks that I am using, so I am familiar with how to use them when I come to implementing them in my work.

  

## TESTING

[TESTING/Testing Checklist](/documentation/testing.md#testing-checklist-development-deployment)

### Research

#### Boostrap 5 Theme Templates
  I researched bootstrap 5 themes to look for inspiration and style ideas that would fit with the motication for building this site. I foudn two thems that I liked, niether in its entirety, but as they were relatively inexpensive, I bought them both and used part of them in the site to build the pages. 
  
**Theme 1.** [Shopapp](http://pxdraft.com/wrap/shopapp/home/index.html#).
This is the main theme that I used, namely for the navbar, modal cart, homepeage serach modal, and shop product detail page. 

**Theme 2.** [Amino Bootstrap 5 Theme](https://template.hasthemes.com/amino/amino/blog-list-right-sidebar.html) Offered a freshness that I liked for the blog. The greens, complimented the purples of the Shopapp theme perfectly. 

The Shoppapp theme is a fully customised Bootstrap theme that fit perfectly with what I wanted to achieve. I integrated that theme, adding parts of the css for the sections of the blog I used from the Amino theme. 

#### Images
All products in the site were photographed by me, and photoshopped to clean up the backgrounds, and add subtle drop shadows. I created json files for the products, and product categories so I could easily add the products to the shop. 

[TESTING/Research](/documentation/testing.md/#research)

### Development

[TESTING/Development](/documentation/testing.md/#development)

  
  

[notes about creating the project]

  

#### Create Project

  

-  **Create Project Repository** I used the Code Institute [gitpod-full-template](https://github.com/Code-Institute-Org/gitpod-full-template). I clicked on "Use this template" and created my project repository name "mp3-garden-journal". I then opened this in GitPod to start the project.

  

-  **Initialise Git** To begin my project, I started with `git init` to initialize git within the project.

-  **Git Ignore** I created a **.gitignore** file to add files and directories I didn't want to upload to GitHub.

`git echo "file_name" >> .gitignore` is the terminal command I used to add files and directories to **.gitignore**.


-  **Create Application File Structure**

- Once I had the project in GitPod, I created the initial file structure needed to get started.

***Create folders***

```bash

mkdir templates static static/css static/js static/images

mkdir documentation documentation/images documentation/images/wireframes

```

***Create files*** [update file structure]

```bash

touch app.py env.py Procfile README.md css/style.css js/main.js

touch templates/base.html templates/home.html

```


-  **Implement Django** [notes about implementation of Django]

-  **Implement Templates** [notes about the template implementation]

-  **Create login and register page and function** [user profile notes?]

  

[crud notes if any?]

  

-  **Add Create Functionality**

-  **Add Update Functionality**

-  **Add Delete Functionality**


#### TESTING DEVICES INFORMATION (update operating systems)

[TESTING/Testing Devices](/documentation/testing.md/#testing-devices)

**Personal Testing Devices/ Software/ Browsers**

- Macbook Pro (15-inch)
- macOS Monterey 12.1
- Safari Version  15.2 (17612.3.6.1.6)
- Chrome Version 96.0.4664.110 (Official Build) (x86_64)
- Firefox 95.0.2 (64-bit)
- Windows 10 (bootcamp)
- Microsoft Edge
- Chrome
- Firefox
- Dell 2419 Monitor
- iPad Air
- iPhone 13 Pro

**Secondary Testing Device/ Sofware/ Browser**

- HP ProDesk 600 Desktop PC
- Windows 10 Pro
- Microsoft Edge Version 90.0.818.42 (Official Build) (64-Bit)
- Firefox 78.10.0esr (64-Bit)
- Chrome Version 90.0.4430.85 (Official Build) (64-Bit)
- AOC 22E15 21.5-inch Full HD 1920x1080 at 75 Hz

#### Git Version Control

[notes about use of git version control]

  

**ERROR Pages**

[404, 405, 500 error pages]

  

### Deployment

[TESTING/Deployment](/documentation/testing.md/#deployment)

[Deployment notes]

  

[TESTING/Testing Checklist](/documentation/testing.md#testing-checklist-development-deployment)

  

#### Forking or Cloning [project]

[instructions on how to fork or clone the project]

  

### Feedback

[add feedback about the site/ project]

  

### Credits

[add credits for any code used from other parties]

  

## NOTES

[additional notes about the project, if any]

  

## IMPROVEMENTS/ FUTURE FEATURES

  

## BUGS and ISSUES

See also [TESTING/Issues and Fixes](/documentation/testing.md/#issues-and-fixes)

See also [README/Database Issues and Notes](/README.md/#database-issues-and-notes)

  

##### ISSUE: [NUMBER]

**ISSUE_NAME**

**Issue**

**Description**

**Troubleshooting**