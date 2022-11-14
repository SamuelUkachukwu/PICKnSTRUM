The codes were tested by doing the following:
### Manual Testing:
1.	Entered invalid inputs and wrong inputs where inputs are requested with respect to integers and strings.
2.	Recruited help from friends to use app and offer feedback
3.  Lunching site on different devices and browsers to check for responsiveness and bugs.
    * google chrome
    * fire fox
    * microsoft edge
    * Operamini

* page links are not broken ``passed``
* forms gets validated and submited as should ``passed``
* images display is responsive ```passed```
* contact us form works. ```passed```
![contact us](readme_imgs/contact-us1.png)
* post and product data sumbit pages work ```passed```
![add product](readme_imgs/add-product.png)
![edit product](readme_imgs/edit-product.png)
![delete product](readme_imgs/delete-product.png)
* 404 error display when page not found error is encountered ```passed```

### User Story Test
As a user I can see all products so that I can select some to purchase.

* Test that "Shop Now" and "All Product" Link works and User is directed to all product pages ``passed``

As a user I can view individual products so that I can see the rating, details, specifications, price, quantity.

* Test that clicking the product image directs users to view detail page of individual product ``passed``

As a user I can easily identify deals and clearance so that I can benefit from the deals and promotions

* Test that the "Seasonal offer" link directs users to sorted list of products under the Clearance and Deals tag. ```passed```

As a user I can search for a product by name or category so that I can find a product easily and quickly

* Test the search box option in both mobile and main navigation with random keywords and null. null returns error notification found returns a list of products and not found returns empty. ```passed```

<details>
<summary>Search tests</summary>
<br>Null Search

![null search](readme_imgs/null_search.png)

<br>Keyword found

![Search found](readme_imgs/search_found.png)

<br>Search Not Found

![Search not found](readme_imgs/search_not_found.png)
</details>

As a user I can sort available products in order of prices or brand so that I can make informed decision and manage purchase and expense parameters.

* Test that products are sorted by options in the sort box ```passed```

* ![sort products by price High to low](readme_imgs/sort_products.png)

As a user I can add items I want into a bag so that I can easily add or remove items.

* Test that clicking the "ADD TO CART" button adds the selected product to Users cart and User is notified immidiately: ```passed```

* ![Add to cart](readme_imgs/Add-to-cart.png)

As a user I can view the total of my purchase so that I can make informed decision on how much I am spending.

* Test that user can see prices and total sum of shopping cart when added to cart or checking out ```passed```

* ![Grand Total](readme_imgs/grand-total.png)

As a user I can view list of posted blogs so that I can select and read any one I like

* Test that all links labeled "Blog" directs user to the blog home page ```passed```

As a user I can click on a post so that I can read the full post..

* Test that on click of each post card user is directed to detail page of post ```passed```

<details>
<summary>Blog Pages Tests</summary>

<br>

![blog link](readme_imgs/blog1.png)

![blog home](readme_imgs/blog2.png)

![blog detail page](readme_imgs/blog3.png)
</details>

As a user I can easily register an account so that I will be able to view my profile

* Test that Users can easily creat accounts log in and log out

<details>
<summary>User Account</summary>

<br>

![Account link](readme_imgs/user-not-logged-in.png)

![Register page](readme_imgs/account2.png)

![Account page](readme_imgs/profile-1.png)
</details>

As a user I can save purchase history to my profile so that I can review the items and plan feature purchases

* Test that user can see svaed purchase history ```passed```
* Purchase history are listed in the profile pages and each order number acts as link that directs Users to to individual order history.
<details>
<summary>Order History</summary>

![Account page](readme_imgs/profile-1.png)
![order history](readme_imgs/order_history.png)

</details>

As a Site Admin I can view a data entry form so that I can add, update and delete products and posts.
* Test that only site admin logged in can view the data entry page ```passed```
* None superuser are directed to login page if they attempt to access the url "https://picknstrum.herokuapp.com/management/"
![Management page](readme_imgs/management-1.png)
<br>
<br>






#### W3C HTML Validation: No Errors returned
No errors were returned when each html page was passed through the official W3C validator.


<details>
<summary>HTML Validation Schreenshots</summary>
<br>HTML Link Validation

![HTML validation](readme_imgs/html-url-validation.png)

<br>Home Page Validation

![Home Page Validation](readme_imgs/homepage-validtion.png)

<br>Product Page Validation

![Product Page Validation](readme_imgs/product-page-validation.png)

<br>Product Detail Page Validation

![Product Detail Page Validation](readme_imgs/product-detail-page-validation.png)

<br>Cart Page Validation

![Cart Page Validation ](readme_imgs/cart-page-validation.png)

<br>Profile Page Validation

![Profile Page Validation ](readme_imgs/profile-page-html-validation.png)
<br>
</details>
<br>


#### W3C CSS Validation: No Errors returned
![CSS validation](readme_imgs/css-validation.png)

#### Pep8 Validation: No errors returned
All python code validated from the console troubleshooting using:
```
python3 -m flake8
```
note: [http://pep8online.com/] is currently parked free

#### Accessibility:

Accessibility testing was conducted using light house devtools and it confirmed that the fonts and colors selected are easy to read and accecssible.
![lighthouse validation](readme_imgs/light-house.png)


Back to [home](README.md)