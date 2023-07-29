# Dandy Flaneur – Portfolio Project 5

![A screenshot of the application in action]()

## [Link to live web application](#)

---

## Project Documentation
### Welcome to [Dandy Flaneur](#)

---

## Table of Contents

-   [User Experience (UX)](#user-experience-ux)
    -   [Target Audiance](#target-audiance)
    -   [User Stories](#user-stories)
    -   [Typography](#typography)
    -   [Colour Palette](#colour-palette)
    -   [Wireframes](#wireframes)

-   [Agile Development](#agile-development)
    -   [MoSCow](#moscow-prioritization-system)

- [Technical Design](#technical-design)
    -   [Flowchart](#flowchart)
    -   [Data Model](#data-model)

-   [Website Features](#website-features)
    -   [Application Elements](#application-elements)

-   [Future Features](#future-features) 

-   [Testing](#testing)
    -   [Manual Testing](#manual-testing)
        -   [User Stories Testing](#user-stories-testing)
    -   [Automated Testing](#automated-tests)
        -   [Unit Tests](#unit-tests)
    -   [Performance](#performance)

-   [Validation](#validation)
    -   [HTML](#html)
    -   [CSS](#css)
    -   [JavaScript](#javascript)
    -   [Python](#python)

-   [Bug Fixes](#bug-fixes)

-   [Deployment](#deployment)
    -   [Local Deployment](#local-deployment)
    -   [Heroku Deployment](#heroku-deployment)

-   [Technologies Used](#technologies-used)
    -   [Hardware](#hardware)
    -   [Software](#software)
    -   [Platforms](#platforms)
    -   [Libraries](#libraries)
        -   [Local Libraries](#local-libraries)
        -   [Third Party Libraries](#third-party-libraries)

-   [Credits and References](#credits-and-references)
    -   [Repositories](#repositories)
    -   [Code Troubleshooting](#code-troubleshooting)
    -   [Documentation](#documentation)
    -   [Library Information](#library-information)
    -   [Theory](#theory)

-   [Acknowledgements](#acknowledgements)

-   [Closing Remarks](#closing-remarks)

---

## User Experience (UX)

### Target Audiance

This project primarily focuses on art enthusiasts that are looking to purchase a painting and related products online.


### User Stories

#### EPIC #1 - User Registration and Accounts

`(MUST HAVE)`

- As a user I can login and logout so that I can access a personal account on the site for rapid access to relevant shop features.
- As a user I can create and view a profile page so that I input and save relevant personal information for faster checkouts.
- As a user I can register an account on the site so that I have a personal account with a unique profile.
- As a user I can reset my password so that I can set a new password for my account whenever I need to do so.
- As a user I can be sent a confirmation email from the site once I create an account so that I am notified that my account registration was successful.

#### EPIC #2 - Site Viewing and Navigation

`(MUST HAVE)`

- As a shopper, I can navigate across the site so that I can access all relevant elements of the site.
- As a shopper I can use header and footer to access navigation, menus and Social Media links.
- As a shopper I can receive a dedicated notification in response to my actions so that I get real-time feedback about the status of my actions.
- As a shopper I can access a list of products available so that I can choose an item to buy.
- As a shopper I can view a welcome page so that I am introduced to the business and its products.
- As a shopper I can access details for a specific product so that I can better inform myself about the item to help with making a purchase decision.
- As a shopper I can view a readout of my login status that is visible at all times so that I can confirm my authentication whenever I want.
- As a shopper I can add new items to my basket so that I list the items that I want to buy.
- As a shopper I can view available booking times for workshops so that I can decide if they fit my schedule.
- As a shopper I can view a list of workshop classes so that I can easily inform myself of the experiences available on offer.
- As a shopper I can make changes in my basket so that I can make the exact purchase that I want.
- As a shopper I can remove items so that I don't accidentally purchase items that I don't want.
- As a shopper I can submit my email with a message attached so that I can establish a personal correspondence with the company about a specific topic.

`(SHOULD HAVE)`

- As a shopper I can view a page with all the relevant details of a workshop so that I can decide if it fits my interests.
- As an admin I can post, edit and remove blog content so that users can read about various topics relevant to the context of the site.
- As a user I can view well-formated layouts so that I can have a coherent visual experience while using the website.

`(COULD HAVE)`

- As a user I can leave comments on blog articles so that I can share my views and opinions about the matters discussed in the blog posts.
- As a viewer I can leave likes so that I can express my fondness for a blog post anonymously.

#### EPIC #3 - Content Sorting and Searching

`(MUST HAVE)`

- As a shopper I can put in keywords into a search bar so that I receive a page with all relevant products to my interests.

`(SHOULD HAVE)`

- As a shopper I can search for a specific item by entering its name or description so that I can precisely find the product that I am looking for.
- As a shopper I can sort products on the basis of their assigned categories so that I can focus on items that fit into categories that I am interested in.
- As a shopper I can sort products by price so that I can easily view products that are appropriate to my financial capabilities.

#### EPIC #4 - Stripe Payments and Checkout

`(MUST HAVE)`

- As a shopper I can easily access my shopping bag so that I can check the items that I will be purchasing whenever I need to.
- As a shopper I can receive a notification about the status of my order confirmation so that I am sure my payment went through and my order was placed successfully.
- As a shopper I can use my card to pay for my order so that I don't have to worry about alternative payment methods.
- As a shopper I can select the specific size and quantity preferences on the product page so that I can put exactly what I want in my shopping basket.

`(SHOULD HAVE)`

- As a shopper I can increase or decrease the quantities of items in my basket so that I can buy more or less of the product I want.

`(COULD HAVE)`

- As a shopper I can receive an email confirming my order with relevant details so that I can be sure that my order was processed successfully.

#### EPIC #5 - Administrator Features and Store Management

`(MUST HAVE)`

- As an admin I can add a new product so that I can update items available in the shop. 
- As an admin I can remove a product item from the store so that users don't have access to inactive products.
- As an admin I can change product details so that the relevant item has the most accurate and up-to-date information associated with it on the website.

`(COULD HAVE)`

- As an admin I can add a workshop so that users can view new experiences.
- As an admin I can change the details of a workshop as needed so that they represent the most accurate and relevant information to the users.
- As an admin I can remove a redundant workshop from the website so that users are not misled into inactive workshops.
- As an admin I can add more time slots to workshops so that users can benefit from added time availability.
- As an admin I can change booking time slot information so that users have the most accurate information.
- As an admin I can remove time slots as needed so that workshop details represent the most accurate availability information.

#### EPIC #6 - Web Marketing and Search Engine Optimization

`(MUST HAVE)`

- As a shopper I can find the correct site by searching it online so that I don't have to worry about opening an unrelated website.
- As a shopper I can submit my email so that I can receive information about deals and product insights from the company.


### Typography

- [Bodoni Moda](https://fonts.google.com/specimen/Bodoni+Moda?query=Bodoni+Moda) is the primary font that is present across all textual elements present in the project.
    - ![screenshot](docs/text-preview.png)

- [EB Garamond](https://fonts.google.com/knowledge/glossary/sans_serif) is the fallback font set in case the primary font fails.
    - ![screenshot](docs/text-preview2.png)

### Colour Palette

[Coolors](https://coolors.co/) was a highly beneficial resource that provided significant help in identifying matching colours that also have appropriate contrast.

More importantly, this colour combination consists of items designed to motivate excitement and aesthetic pleasure from users through the use of minimalist design elements coupled with a clean page formating.

![Colour Palette](docs/color-palette.png)

---

### Wireframes

<details>

<summary>Home Page</summary>

#### Mobile
![screenshot](docs/wireframes/ios-home.png)

#### Tablet
![screenshot](docs/wireframes/ipad-home.png)

#### Desktop
![screenshot](docs/wireframes/desktop-home.png)

</details>

<details>

<summary>Blog Page</summary>

#### Mobile
![screenshot](docs/wireframes/ios-blog.png)

#### Tablet
![screenshot](docs/wireframes/ipad-blog.png)

#### Desktop
![screenshot](docs/wireframes/desktop-blog.png)

</details>

<details>

<summary>Blog Detail Page</summary>

#### Mobile
![screenshot](docs/wireframes/ios-blog-detail.png)

#### Tablet
![screenshot](docs/wireframes/ipad-blog-detail.png)

#### Desktop
![screenshot](docs/wireframes/desktop-blog-detail.png)

</details>

<details>

<summary>Store Page</summary>

#### Mobile
![screenshot](docs/wireframes/ios-store.png)

#### Tablet
![screenshot](docs/wireframes/ipad-store.png)

#### Desktop
![screenshot](docs/wireframes/desktop-store.png)

</details>

<details>

<summary>Store Detail Page</summary>

#### Mobile
![screenshot](docs/wireframes/ios-store-detail.png)

#### Tablet
![screenshot](docs/wireframes/ipad-store-detail.png)

#### Desktop
![screenshot](docs/wireframes/desktop-store-detail.png)

</details>

<details>

<summary>Contact Us Page</summary>

#### Mobile
![screenshot](docs/wireframes/ios-contact.png)

#### Tablet
![screenshot](docs/wireframes/ipad-contact.png)

#### Desktop
![screenshot](docs/wireframes/desktop-contact.png)

</details>

<details>

<summary>Basket Page</summary>

#### Mobile
![screenshot](docs/wireframes/ios-basket.png)

#### Tablet
![screenshot](docs/wireframes/ipad-basket.png)

#### Desktop
![screenshot](docs/wireframes/desktop-basket.png)

</details>

<details>

<summary>Checkout Page</summary>

#### Mobile
![screenshot](docs/wireframes/ios-checkout.png)

#### Tablet
![screenshot](docs/wireframes/ipad-checkout.png)

#### Desktop
![screenshot](docs/wireframes/desktop-checkout.png)

</details>

<details>

<summary>Checkout Success Page</summary>

#### Mobile
![screenshot](docs/wireframes/ios-checkoutsuccess.png)

#### Tablet
![screenshot](docs/wireframes/ipad-checkoutsuccess.png)

#### Desktop
![screenshot](docs/wireframes/desktop-checkoutsuccess.png)

</details>

<details>

<summary>Forms Page</summary>

- These wireframes illustrate the fundamental layout used in forms with one or more of editing, adding, and deletion functionalities.

#### Mobile
![screenshot](docs/wireframes/ios-addeditforms.png)

#### Tablet
![screenshot](docs/wireframes/ipad-addeditforms.png)

#### Desktop
![screenshot](docs/wireframes/desktop-addeditforms.png)

</details>

<details>

<summary>Authentication Page</summary>

- These wireframes represent the base design of all authentication pages that feature login, logout, and signup functionalities.

#### Mobile
![screenshot](docs/wireframes/ios-auth.png)

#### Tablet
![screenshot](docs/wireframes/ipad-auth.png)

#### Desktop
![screenshot](docs/wireframes/desktop-auth.png)

</details>

<details>

<summary>Profile Page</summary>

#### Mobile
![screenshot](docs/wireframes/ios-profile.png)

#### Tablet
![screenshot](docs/wireframes/ipad-profile.png)

#### Desktop
![screenshot](docs/wireframes/desktop-profile.png)

</details>

---

## Agile Development

### MoSCoW Prioritization System

This project relies on agile methodology for its task management. This allows for more accurate estimation of time needed for successful task completion. You can access the kanban board used for this project [here](https://github.com/users/beratzorlu/projects/4/views/1)

Below are the labels used on GitHub to illustrate the various importance levels.

- Must Have: MVP feature (60% of user stories)
- Should Have: secondary importance (20% of user stories)
- Could Have: Tertiary importance (20% of stories)
- Won't Have: No longer in consideration

---

## Technical Design

### Data Model - Entity Relationship Diagram

[Draw.io](https://www.drawio.com/) was a highly beneficial resource that provided significant help in building a ERP to illustrate the various table relationships of data models present in the project.

![Data Relationship Diagram](docs/entity-relationship-diagram.png)

---

## Website Features

The design considerations that impacted the envisioned features were mainly structured around user interaction and content sharing. While there were more features planned in the initial stages of the project, some were not entertained to the benefit of serving the needs referenced in the [User Stories](#user-stories) section. Thus, it was important to focus on a minimum viable project rather than prioritizing the implementation of further features for the sake of it. This would only bloat the application without adding much real value to the user experience overall. There are [records available](#future-features) as a part of this documentation that demonstrate the change in scope that took place moving further into development.

### Application Elements

The below elements are available to be experienced by the user across the application as a whole.

| Feature | Screenshot |
| --- | --- |
| Site Logo | ![screenshot](docs/features/site-logo.png) |
| Favicon | ![screenshot](docs/features/custom-favicon.png) |
| Default Post Banner | ![screenshot](docs/features/default-post-banner.png) |
| Custom Login Banner | ![screenshot](docs/features/login-banner-custom.png) |
| Navigation (Logged in) | ![screenshot](docs/features/sitenav-1.png) |
| Navigation (Logged Out) | ![screenshot](docs/features/sitenav-2.png) |
| Sign Up | ![screenshot](docs/features/signup.png) |
| Messages | ![screenshot](docs/features/messages.png) |
| Logout | ![screenshot](docs/features/logout.png) |
| Login | ![screenshot](docs/features/login.png) |
| Footer | ![screenshot](docs/features/footer.png) |
| Featured Blogs | ![screenshot](docs/features/featured-blogs.png) |
| Comment Content Editing | ![screenshot](docs/features/edit-comment.png) |
| Blog Content Editing | ![screenshot](docs/features/edit-blog.png) |
| Application Content Editing | ![screenshot](docs/features/edit-apply.png) |
| Post Deletion | ![screenshot](docs/features/delete-post.png) |
| Comment Deletion | ![screenshot](docs/features/delete-comment.png) |
| Application Deletion | ![screenshot](docs/features/delete-apply.png) |
| Comment Form | ![screenshot](docs/features/comment-form.png) |
| No Comments Placeholder | ![screenshot](docs/features/comment-0.png) |
| Home Page Carousel | ![screenshot](docs/features/carousel.png) |
| Blog Sidebar | ![screenshot](docs/features/add-post.png) |
| Blog Sidebar | ![screenshot](docs/features/blog-sidebar.png) |
| Blog Posts | ![screenshot](docs/features/blog-posts.png) |
| Blog Content | ![screenshot](docs/features/blog-content.png) |
| Blog Buttons | ![screenshot](docs/features/blog-buttons.png) |
| Blog Banner Image | ![screenshot](docs/features/blog-banner.png) |
| Application Summary | ![screenshot](docs/features/apply-summary.png) |
| Application Guide | ![screenshot](docs/features/apply-info.png) |
| Application Page (Logged In) | ![screenshot](docs/features/apply-1.png) |
| Add Application **(DISCLAIMER: The phone field will not accept any random combination of numbers that match the selected area number format. It needs to be a real number because of the security features that come with PhoneNumberField library.)** | ![screenshot](docs/features/add-apply.png) |
| Custom 500.html Page | ![screenshot](docs/features/custom-500.png) |
| Custom 404.html Page | ![screenshot](docs/features/custom-404.png) |
| Custom 403.html Page | ![screenshot](docs/features/custom-403.png) |
| Custom 400.html Page | ![screenshot](docs/features/custom-400.png) |
| Paginate Forward | ![screenshot](docs/features/paginate-1.png) |
| Paginate Backward | ![screenshot](docs/features/paginate-2.png) |

---

## Future Features

This section documents the features that were taken out of consideration for the benefit of the completion of the minimum viable project. The central observation in this area is that the level of ambition that the project initially set out with does not match with the intellectual labour required to complete a significant sum of the features first assigned. Below, are user stories that were deemed no longer necessary. You can view the full kanbar board used for project planning [here](https://github.com/users/beratzorlu/projects/4/views/1).

That being said, these features remain relevant to the overall scope of the project and it would see them expand its functional capacity in the future if the situation allowed it.

| Label | Feature |
| --- | --- |
| Won't Have | Direct Messaging |
| Won't Have | Unfollow Users |
| Won't Have | Admin/Inappropriate Blog Posts#52 |
| Won't Have | Car Finance Calculator#41 |
| Won't Have | Car Profile#40 |
| Won't Have | Comments/Post Card Comment Count#51 |
| Won't Have | Contact Us/Google Maps and Marker Clusterer#33 |
| Won't Have | Background Refresh For Post Likes#32 |
| Won't Have | Authentication/SSO#30 |
| Won't Have |  Profiles/Private Profiles#28 |
| Won't Have | Admin/Suspend Users#27 |
| Won't Have | Direct Messaging/Notifications#26 |
| Won't Have | Admin/View Reported Posts#24 |
| Won't Have | Post Report#23 |
| Won't Have | Follow Users#6 |
| Won't Have | Notifications/New Follower#22 |
| Won't Have | Notifications/Post Engagement#21 |
| Won't Have | Search Users & Posts#20 |
| Won't Have | Password Reset#9 |
| Won't Have | Profiles/Create Profile#13 |
| Won't Have | Profiles/Edit Profile#7 |

---

## Testing

### Automated Testing

#### Unit Tests

| Scope | Screenshot | Result |
| --- | --- | --- |
| Global | ![screenshot](docs/validation/python/unittest.png) | Pass |

### Manual Testing

#### User Stories Testing

| **Feature**   |  **Screenshot**          | **Result** |
| ------------- | ------------------------ | ----------------- |
| As an admin I can provide a disclaimer at the bottom of the page so that I can specify that all outsourced content (texts, images etc.) is used for purposes of education as a part of this academic project and is in no circumstance to be used for commercial motivations. | ![screenshot](docs/features/footer.png) | Pass |
|  As a user I can browse a website that incorporates overall cohesion among its various elements so that I have an aesthetically pleasing user experience. | ![screenshot](docs/features/carousel.png) | Pass |
| As a user I can be directed to an error page so that I know something went wrong with the website. | ![screenshot](docs/features/custom-404.png) | Pass (This is valid for all custom error pages.) | 
| As a user I can view all the newest posts on the website so that I can directly access the most up-to-date content available on the website. | ![screenshot](docs/features/blog-posts.png) | Pass |
| As a user I can view the consultation page so that I can learn about the various consultation service that the site offers. | ![screenshot](docs/features/apply-1.png) | Pass |
| As a registered I can remove comments that I posted so that they are no longer visible on the site. | ![screenshot](docs/features/delete-comment.png) | Pass |
| As a registered user I can edit the comments I posted so that I can change the content I originally posted in my comment. | ![screenshot](docs/features/edit-comment.png) | Pass |
| As a registered user I can create new posts so that I can share my thoughts and opinions on the platform. | ![screenshot](docs/features/add-post.png) | Pass |
| As a registered user I can use a dedicated form to edit my blog so that I can make changes to my content when I feel there is a need to do so. | ![screenshot](docs/features/edit-blog.png) | Pass |
| As a registered user I can delete my posts so that my published content is removed. | ![screenshot](docs/features/delete-post.png) | Pass |
| As a user I can view the number of comments on any post so that I see if the post is popular or not and decide if it's worth checking out based on this information. | ![screenshot](docs/features/blog-banner.png) | Pass |
| As a registered user I can view posts from other users so that I can access and read content posted by others. | ![screenshot](docs/features/blog-list-1.png) | Pass |
| As a registered user I can like other people's posts so that I inform them that I had a positive experience with their posts. | ![screenshot](docs/features/blog-banner.png) | Pass |
| As a user I can see special styling for particular usernames in comments so that I can identify which users are admins. | ![screenshot](docs/features/admin-crown.png) | Pass |
| As a registered user I can clearly see date/time information on a post so that I learn how old or new the post is to determine its relevance. | ![screenshot](docs/features/blog-banner.png) | Pass |
| As an unregistered I can sign up to create an account so that I can fully access the features available on the website. | ![screenshot](docs/features/signup.png) | Pass |
| As a registered I can leave comments on other users' blog posts so that I share my thoughts on the content they have posted. | ![screenshot](docs/features/comment-form.png) | Pass |
| As a registered user I can log out of my account so that I can securely quit the current session active on my device. | ![screenshot](docs/features/logout.png) | Pass |
| As a registered user I can log in to my account so that I access the full functionality of the website. | ![screenshot](docs/features/login.png) | Pass |
| As an unregistered user I can use a password and username I choose so that I can securely access the user-exclusive features of the website. | ![screenshot](docs/features/signup.png) | Pass |
| As a user I can click on a clearly labelled button on a blog card so that I am easily directed to the details of the relevant full blog post. | ![screenshot](docs/features/featured-blogs.png) | Pass |
| As a registered user I can navigate the site so that I can interact with the available features. | ![screenshot](docs/features/sitenav-1.png) | Pass |
| As an admin I can approve or reject comments left by registered users so that I can ensure that the content available on the site follows the community guidelines. | ![screenshot](docs/features/comments-approve.png) | Pass |
| As an admin I can create draft posts so that I can come back to them when I want to. | ![screenshot](docs/features/post-draft.png) | Pass |
| As an admin I can create, read, update and delete content so that I can manage my blog content. | ![screenshot](docs/features/admin-content-manage.png) | Pass |

### Performance

The Lighthouse tests returned an overall acceptable result considering the scope and purpose of the project. Most notably, the performance value appears to be the more lacking area compared to the rest of the parameters available on Lighthouse. Information gathered from the testing process indicates that these scores are a result of Cloudinary slowing down the loading times of the images. In future projects, more effective cloud solutions such AWS will help prevent the recurrance of similar results.

| **Page** | **Screenshot** |
| -------- | ------ |
| Home | ![screenshot](docs/features/lighthouse-home.png) |
| Blog | ![screenshot](docs/features/lighthouse-home.png) |
| Consultation | ![screenshot](docs/features/lighthouse-consultation.png) |

---

## Validation

### HTML

| Page | Screenshot | Result |
| --- | --- | --- |
| Home | ![screenshot](docs/validation/html/w3c-index.png) | Pass |
| Blog | ![screenshot](docs/validation/html/w3c-blog.png) | Pass |
| Consultation | ![screenshot](docs/validation/html/w3c-apply.png) | Pass |
| Login | ![screenshot](docs/validation/html/w3c-login.png) | Pass |
| Logout | ![screenshot](docs/validation/html/w3c-logout.png) | Pass |
| Signup | ![screenshot](docs/validation/html/w3c-signup.png) | Pass |
| Add Post | ![screenshot](docs/validation/html/w3c-add-post.png) | Pass |
| Edit Post | ![screenshot](docs/validation/html/w3c-edit-post.png) | Pass |
| Add Consultation | ![screenshot](docs/validation/html/w3c-add-app.png) | 1 Error: Caused by widget properties set for the DateTimeField. This input field needs a placeholder, thus the error is allowed to remain. |
| Edit Consultation | ![screenshot](docs/validation/html/w3c-edit-app.png) | Pass |

### CSS

| File | Screenshot | Result |
| --- | --- | --- |
| style.css | ![screenshot](docs/validation/css/jigsaw-css.png) | Pass |

### JavaScript

| File | Screenshot | Result |
| --- | --- | --- |
| fade.js | ![screenshot](docs/validation/js/jshint.png) | Pass (It is not possible to install Bootstrap in jshint, thus the warning is allowed to remain.) |

### PYTHON

| File | Screenshot | Result |
| --- | --- | --- |
| urls.py (main) | ![screenshot](docs/validation/python/linter-urls-main.png) | Pass |
| settings.py (main) | ![screenshot](docs/validation/python/linter-settings.png) | Pass |
| admin.py (blog) | ![screenshot](docs/validation/python/linter-admin-blog.png) | Pass |
| forms.py (blog) | ![screenshot](docs/validation/python/linter-forms-blog.png) | Pass |
| tests.py (blog) | ![screenshot](docs/validation/python/linter-tests-blog.png) | Pass |
| urls.py (blog) | ![screenshot](docs/validation/python/linter-urls-blog.png) | Pass |
| views.py (blog) | ![screenshot](docs/validation/python/linter-views-blog.png) | Pass |
| admin.py (consultation) | ![screenshot](docs/validation/python/linter-admin-consultation.png) | Pass |
| cars.py (consultation) | ![screenshot](docs/validation/python/linter-cars-consultation.png) | Pass |
| forms.py (consultation) | ![screenshot](docs/validation/python/linter-forms-consultation.png) | Pass |
| models.py (consultation) | ![screenshot](docs/validation/python/linter-models-consultation.png) | Pass |
| tests.py (consultation) | ![screenshot](docs/validation/python/linter-tests-consultation.png) | Pass |
| urls.py (consultation) | ![screenshot](docs/validation/python/linter-urls-consultation.png) | Pass |
| views.py (consultation) | ![screenshot](docs/validation/python/linter-views-consultation.png) | Pass |

---

## Bug Fixes

In this section, all bugs that cased errors that prevented the successful execution of the application and their relevant fixes are provided.

| **Bug** | **Fix** |
| ------- | ------- |
| SyntaxError on STATIC_ROOT variable. | [here](https://github.com/beratzorlu/AutoMate/commit/70e0273a16c29968d5ed463f5bb69cf63e9aba7e). |
| Alignment issue for like and comment icons. | [here](https://github.com/beratzorlu/python-quiz/commit/d3fc300dc47d88aecd65f99b7ab7cbb6ca6f13b7). |
| Comment textfield issue.  | [here](https://github.com/beratzorlu/AutoMate/commit/11c99d53f14d9b4e536b8c5522019e194061ab74) |
| Delete blog button positioning issue.  | [here](https://github.com/beratzorlu/AutoMate/commit/306849d24d314e52ec4e2bd863d3d56942024e76) |
| Post detail render issue when logged in as admin.  | [here](https://github.com/beratzorlu/AutoMate/commit/0c606ba4cf32c5a625d95201eff7f06da745ee79) |
| Unresponsive footer. | [here](https://github.com/beratzorlu/AutoMate/commit/e4d1d7a1d1ffe802e82cacfbc4a05d11dc054a30) |
| Consultation frontend render issue. | [here](https://github.com/beratzorlu/AutoMate/commit/4b531cbddf683782b7168eb66540b3f1bc9e3815) |
| Consultation form loop render issue. | [here](https://github.com/beratzorlu/AutoMate/commit/c7dbc7f8b35e05e3d286e784872b67a9883f6199) |
| Card wrap issue. | [here](https://github.com/beratzorlu/AutoMate/commit/162b2bfff80a1ad3b22ee7ec3db0cb2bf798da4c) |
| Application summary card render issue. | [here](https://github.com/beratzorlu/AutoMate/commit/3b5a304272b4be5ea19373b8770ff78d0a9f56ef) |
| Edit view frontend content update issue. | [here](https://github.com/beratzorlu/AutoMate/commit/4848f1c68c68774a8ae5dfb947346e9f35a0de50) |
| cars.py import issue. | [here](https://github.com/beratzorlu/AutoMate/commit/4757863be79691120d3a7a9f841f49b6ebca4b93) |
| ID text capitalization issue. | [here](https://github.com/beratzorlu/AutoMate/commit/dd9bc150e39562fb02b4859dbd776797e222f288) |
| Comment security issue. | [here](https://github.com/beratzorlu/AutoMate/commit/23528285f3d115745b90ccd1e67c005294272159) |
| author_id Null value issue. | [here](https://github.com/beratzorlu/AutoMate/commit/0c0e5e0280444d6805c48daf89c7f92d087b6e3e) |
| Blog page responsivity issue. | [here](https://github.com/beratzorlu/AutoMate/commit/7b054286b982038cca277428d6955ce95a201ac8) |

---

## Deployment

This application has been deployed by using the Heroku cloud platform. Please find below the neccessary procdures to replicate the deployment process.

You can find a [template](https://github.com/Code-Institute-Org/python-essentials-template) prepared by Code Institute that is designed to display this backend application in a modern web browser. This allows the project to be accessible for users without the need of any third party software other than an Internet browser application.

### Local Deployment 

Gitpod IDE is the development environment for this project.

If you wish to make copy of this repository locally, you can clone it by inputting the following code into your preferred integrated development environment (IDE):
- `git clone https://github.com/beratzorlu/AutoMate.git`

As anoher method, you can click below button to create your own workspace using this repository if you are using Gitpod.e

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/beratzorlu/python-quiz)

### Heroku Deployment

This project utilizes the services available at [Heroku](https://www.heroku.com). Heroku is a platform as a service (PaaS) that allows users to build, deploy, and control applications in a cloud environment.

Disclaimer: To be able successfully replicate the Heroku deployment process, it is highly reccomended that users setup an account on the platform prior to following the steps provided below.

- Select *New* in the top-right corner of your Heroku Dashboard after log-in.
- Select navigate to the *Create new app* button from the dropdown menu and select it.
- Assign a unique name to your application.
- Navigate to the *region* dropdown menu and select the region closest to you from either EU or USA. 
- Select *Create App*.
- Navigate to your newly created application and select *Settings*. 
- Click *Reveal Config Vars*.
- Add first *Config Var*.
- Set the value of KEY to `CREDS`, copy and paste the data in your credentials file (ie. creds.json) into the value area.
- Add second *Config Var*.
- Set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- You need to add support to dependencies to be able to successfully deploy application, select *Add Buildpack*.
- The order in which you list your dependencies is critical, select `Python` as the first dependency.
- From the same menu, select `Node.js` after you select `Python`. (You can drag the list items upwards and downwards to change their order if needed.)
- Scroll until you find your desired deployment method, select `Enable Automatic Deploy` to rebuild your project automatically every time you push a new commit. Select `Manual Deployment` to manually deploy from your desired branch on will.*

*If you have selected automatic deployment, your application will only deploy after your first push to the system.

After the completion of this process, Heroku needs two files further to deploy successfully. These are;
    - requirements.txt
    - Procfile

To install your project's requirements use: `pip3 install -r requirements.txt`. 

If you have third party packages in your project the requirements file needs updated, use: `pip3 freeze --local > requirements.txt`

To create your Procfile, use: `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:

- In the Terminal (CLI), connect to Heroku using this: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace <app_name> with your chosen name for your application without the angle-brackets)
- Input commands `git add`, `git commit`, and `git push` to GitHub sequentially.
- Finally, type `git push heroku main` in the terminal to connect to Github.

Alternatively, you can connect to your Github account by following the below steps on Heroku's platform.

- Navigate to your Heroku account dashboard.
- Find the relevant project and click on its icon.
- On the next page, navigate to the `Deploy` subsection.
- Scroll down until you find `Deployment method` and find `Use Github`.
- Finally, input your Github account credentials to complete the process. 

---

## Technologies Used

### Hardware

- Monster Abra A5 V13.4 15.6" Laptop
- Lenovo IdeaPad 3i 14" Laptop
- Samsung VA 1920x1080 144Hz Curved Gaming Monitor
- iPhone 11
- Ipad Air 5th Generation
- Samsung A51

### Software

- Mozilla Firefox: Main browser used for development, testing and device simulation.
- Google Chrome: Secondary browser for testing and device simulation.
- Microsoft Edge: Tertiary browser for testing.
- Firefox Mobile: Mobile testing of the deployed site.
- Chrome Mobile: Mobile testing of the deployed site.
- Safari Mobile: Mobile testing of the deployed site.
- Windows Snip & Sketch: Capturing screenshots for readme and archiving identified bugs.
- Microsoft Snipping Tool: Fallback screen capture software when MS Snip & Sketched became unresponsive.
- DiffChecker: Comparing code to identify issues, solutions and ideas.
- Python Checker: Checking the syntax of Python code.
- ElephantSQL: PosgresSQL database resource.
- Django: Fullstack framework used to build the project
- Bootstrap: Responsive frontend CSS framework used to design the visual aspects of the project.
- Cloudinary: Cloud storage for static files.
- Balsamiq: Wireframe design and rendering.
- Draw.io: Diagram design and rendering.

### Platforms

- GitHub: Version control and site deployment.
- GitPod: Integrated Development Environment (IDE) chosen for this project.
- Google Fonts: Finding and exporting third-party fonts for the website.
- CodePen: For quickly testing out ideas before carrying them to 
DevTools.
- Coolors: For creating a matching colour palette that has appropriate contrast.
- Heroku: Cloud platform used for deploying project.
- Canva: Graphic design platform used for custom visual elements.

### External Modules

| **Name** | **Version** |
| ------- | ------- |
| asgiref | 3.6.0 |
| Babel | 2.12.1 |
| cloudinary | 1.32.0 |
| dj-database-url | 0.5.0 |
| dj3-cloudinary-storage | 0.0.6 |
| Django | 3.2.18 |
| django-allauth | 0.54.0 |
| django-crispy-forms | 1.14.0 |
| django-phonenumber-field | 7.1.0 |
| django-summernote | 0.8.20.0 |
| gunicorn | 20.1.0 |
| oauthlib | 3.2.2 |
| phonenumbers | 8.13.11 |
| psycopg2 | 2.9.6 |
| PyJWT | 2.6.0 |
| python3-openid | 3.2.0 |
| pytz | 2023.3 |
| requests-oauthlib | 1.3.1 |
| sqlparse | 0.4.4 |

---

## Credits and References

### Repositories

- [Code Institute](#): CI's curriculum provided the main knowledge-base required to create and finalize this project. Various academic modules and the tasks available in them helped understand Django before the start of the development process.
    - [Hello Django](#): This walkthrough project provided significant practice for understanding how to implement CRUD functionality to a Django application.
    - [I Think Therefore I Blog](#): While more difficult to fully understand, the concepts demonstrated in this walkthrough project allowed for a deeper understanding of Django admin and site operations. More specifically, pagination was a difficult element to fully implement to this project. The code available here provided the help needed to integrate a pagination system to the project.
- [beratzorlu](https://github.com/beratzorlu/Portfolio-Project-2): I used one of my previous projects to prepare the README.md file for this project. As I already had established a format for this process, I used it as a template for the documentation of this project.
- [adamgilroy](https://github.com/adamgilroy22/tribe/): This is an inspirational project that offers an expansive set of features. Beacuse of this I would like to congratualte Adam Gilroy for his excellent work. Reading through his code helped me understand how to compartmentalize code, add security against unauthorized access to published user content, and how to work class based views.
- [CHCheshire](https://github.com/CHCheshire/Project-blog/tree/main): This project helped me understand managing comments from the frontend when building associated CRUD functionality.
- [stephaniecrocker91](https://github.com/stephaniecrocker91/for-the-love-of-food): This project provided a live perspective towards connecting models from different applications with each other.


### Code Troubleshooting

| Source | Title | URL |
| --- | --- | --- |
| Stack Overflow | delete button | [here](https://stackoverflow.com/questions/68008514/how-i-can-create-a-delete-button-in-django-python) |
| Stack Overflow | delete button #2 | [here](https://stackoverflow.com/questions/46003056/how-to-make-delete-button-in-django) |
| Stack Overflow | backport version issue | [here](https://stackoverflow.com/questions/71712258/error-could-not-build-wheels-for-backports-zoneinfo-which-is-required-to-insta) |
| Stack Overflow | bootstrap header width | [here](https://stackoverflow.com/questions/72279036/why-is-my-boostrap-card-header-not-filling-entire-width-of-the-card) |
| Stack Overflow | bootstrap grid and aside usage | [here](https://stackoverflow.com/questions/36161615/bootstrap-grid-with-html5-sections-and-aside ) |
| Stack Overflow | ajax for liking without page refresh | [here](https://stackoverflow.com/questions/21791037/implement-a-like-this-button-in-django-without-refreshing-page) |
| Stack Overflow | django import js documents | [here](https://stackoverflow.com/questions/30313314/django-how-to-include-javascript-in-template) |
| Stack Overflow | centering cards | [here](https://stackoverflow.com/questions/39031224/how-to-center-cards-in-bootstrap-4) |
| Stack Overflow | center button | [here](https://stackoverflow.com/questions/41664991/bootstrap-4-how-do-i-center-align-a-button) |
| Stack Overflow | prepopulate author dropdown on addpost | [here](https://stackoverflow.com/questions/45221097/add-data-to-django-form-before-it-is-saved/45221181#45221181) |
| Stack Overflow | best image size for bootstrap | [here](https://stackoverflow.com/questions/25554020/bootstrap-carousel-with-photos-optimal-image-size) |
| Stack Overflow | django dropdown | [here](https://stackoverflow.com/questions/31130706/dropdown-in-django-model) |
| Stack Overflow | HTTP referrer | [here](https://stackoverflow.com/questions/4406377/django-request-to-find-previous-referrer) |
| Stack Overflow | unittests | [here](https://stackoverflow.com/questions/51560850/how-to-unit-test-a-post-method-in-python) |
| Stack Overflow | django phonenumberfield | [here](https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-a-phone-number-in-django-models) |
| Stack Overflow | remove crispyforms labels | [here](https://stackoverflow.com/questions/11472495/remove-labels-in-a-django-crispy-forms) |
| Stack Overflow | carousel not working fix | [here](https://stackoverflow.com/questions/48824568/bootstrap-4-carousel-sliders-not-working) |
| Stack Overflow | import django forms | [here](https://stackoverflow.com/questions/56785003/attribute-error-module-django-forms-forms-has-no-attribute-modelform) |
| Stack Overflow | django equalto method | [here](https://stackoverflow.com/questions/20529234/how-to-select-reduce-a-list-of-dictionaries-in-flask-jinja) |
| Stack Overflow | django count of list item | [here](https://stackoverflow.com/questions/40006617/get-count-of-list-items-that-meet-a-condition-with-jinja2) |
| Stack Overflow | only available as class instances issue | [here](https://stackoverflow.com/questions/48613146/python-error-this-method-is-only-available-to-the-class-not-on-instances) |
| Stack Overflow | editing posts on django blog | [here](https://stackoverflow.com/questions/60042351/editing-posts-in-a-django-blog) |
| Stack Overflow | default value set on form | [here](https://stackoverflow.com/questions/70559902/django-how-do-i-set-a-default-value-in-a-form-to-be-the-current-user) |
| Stack Overflow | tuple error indices | [here](https://stackoverflow.com/questions/35359969/typeerror-tuple-indices-must-be-integers-not-str) |
| Stack Overflow | assign default value | [here](https://stackoverflow.com/questions/23718484/django-assign-default-value-to-field-in-modelform) |
| Stack Overflow | placeholder charfield | [here](https://stackoverflow.com/questions/4101258/how-do-i-add-a-placeholder-on-a-charfield-in-django) |
| Stack Overflow | change date format field | [here](https://stackoverflow.com/questions/67538930/how-to-change-date-format-in-a-form-field-django) |
| Stack Overflow | date placeholder | [here](https://stackoverflow.com/questions/39025926/dateinput-how-to-show-placeholder) |
| Stack Overflow | date picker widget | [here](https://stackoverflow.com/questions/41645030/django-date-picker-for-date-of-birth) |
| Stack Overflow | limit blog posts per account – class context method – Django pagination | [here](https://stackoverflow.com/questions/68405198/adding-a-maximum-limit-to-the-number-of-post-using-python) |
| Stack Overflow | dispatch - loginrequired | [here](https://stackoverflow.com/questions/71782596/why-loginrequiredmixin-dont-stop-my-dispatch-flow-when-user-is-not-authenticat) |
| Stack Overflow | delete success message with obj value | [here](https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown) |
| Stack Overflow | how to add custom error pages | [here](https://stackoverflow.com/questions/17662928/django-creating-a-custom-500-404-error-page) |
| Stack Overflow | how to use css in django forms | [here](https://stackoverflow.com/questions/5827590/css-styling-in-django-forms) |
| Stack Overflow | bootstrap card resize | [here](https://stackoverflow.com/questions/65616251/how-to-re-size-my-cards-divs-using-bootstrap) |
| Stack Overflow | relationship with slug and getabsoluteurl | [here](https://stackoverflow.com/questions/35581956/relationship-between-slug-and-get-absolute-url-what-am-i-doing-wrong) |
| GitHub | fix crispy forms label issue | [here](https://github.com/django-crispy-forms/django-crispy-forms/issues/248) |
| Sophyia.me | secret key generate from terminal | [here](https://sophyia.me/the-easist-way-to-create-your-secret-key) |
| Stack Exchange | username length best practice | [here](https://security.stackexchange.com/questions/18516/usernames-should-their-length-be-limited ) |
| Radu | bootstrap footer bottom | [here](https://radu.link/make-footer-stay-bottom-page-bootstrap/) |
| Learn Django | slugify post title | [here](https://learndjango.com/tutorials/django-slug-tutorial) |
| Geeks For Geeks | Django fields | [here](https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/) |
| Adamj | how to use limit integerfield | [here](https://adamj.eu/tech/2021/05/08/django-check-constraints-limit-range-integerfield/ ) |
| W3 Schools | github checkbox markdown | [here](https://www.w3schools.io/file/markdown-checkbox-github/) |
| Geeks For Geeks | how to use typed choice field | [here](https://www.geeksforgeeks.org/typedchoicefield-django-forms/) |
| Geeks For Geeks | form filed custom widgets | [here](https://www.geeksforgeeks.org/django-form-field-custom-widgets/) |
| Codeing Gear | add favicon to django | [here](https://codinggear.blog/django-add-favicon/) |
| Grepper | add class to form field | [here](https://www.grepper.com/answers/564807/Add+class+to+form+field+Django+ModelForm) |
| Medium | crispy forms | [here](https://levelup.gitconnected.com/how-to-make-your-django-forms-look-crispy-78a68000bc3f) |


### Documentation

| Source | Title | URL |
| --- | --- | --- |
| Django | working with forms | [here](https://docs.djangoproject.com/en/3.2/topics/forms/) |
| Django | django's built-in form classes | [here](https://docs.djangoproject.com/en/3.2/ref/forms/api/) |
| Django | working with model forms | [here](https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/) |
| Django | writing views | [here](https://docs.djangoproject.com/en/3.2/topics/http/views/) |
| Django | wandling HTTP requests | [here](https://docs.djangoproject.com/en/3.2/topics/http/) |
| Django | URL dispatcher | [here](https://docs.djangoproject.com/en/3.2/topics/http/urls/) |
| Django | django's messages framework | [here](https://docs.djangoproject.com/en/3.2/ref/contrib/messages/) |
| Django | working with Django templates | [here](https://docs.djangoproject.com/en/3.2/topics/templates/) |
| Django | 	Using the Django ORM | [here](https://docs.djangoproject.com/en/3.2/topics/db/queries/) |
| Django | django's QuerySet API reference | [here](https://docs.djangoproject.com/en/3.2/ref/models/querysets/) |
| Django | template tags and filters | [here](https://docs.djangoproject.com/en/3.2/topics/templates/#tags-and-filters) |
| Django | integer Field | [here](https://docs.djangoproject.com/en/dev/ref/models/fields/#integerfield ) |
| Django | for | [here](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#for) |
| Django | Django User model | [here](https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#django.contrib.auth.models.User) |
| Django | redirects | [here](https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/#redirect) |
| Django | messages | [here](https://docs.djangoproject.com/en/3.2/ref/contrib/messages/) |
| Django | ForeignKey field | [here](https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.ForeignKey) |
| Django | Url dispatcher | [here](https://docs.djangoproject.com/en/3.2/topics/http/urls/ ) |
| Django | form validation | [here](https://docs.djangoproject.com/en/3.2/ref/forms/validation/ ) |
| Django | form fields | [here](https://docs.djangoproject.com/en/4.2/ref/forms/fields/ ) |
| Django | form templates | [here](https://docs.djangoproject.com/en/4.1/topics/forms/#working-with-form-templates) |
| Django PhoneNumberField | django phonenumberfield docs | [here](https://django-phonenumber-field.readthedocs.io/en/latest/reference.html#validator) |
| Mozilla | setTimeout | [here](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout) |
| Bootstrap | methods | [here](https://getbootstrap.com/docs/5.0/components/alerts/#methods) |
| Bootstrap | usage |  [here](https://getbootstrap.com/docs/5.0/components/alerts/#usage ) |
| Bootstrap | carousel examples | [here](https://getbootstrap.com/docs/4.1/examples/carousel/)|
| Bootstrap | login page examples | [here](https://mdbootstrap.com/docs/standard/extended/login/) |
| Bootstrap | blog page examples | [here](https://getbootstrap.com/docs/4.1/examples/blog/) |


### Tutorials

| Source | Title | URL |
| --- | --- | --- |
| YouTube - Web Zone | responsonive grid with bootstrap | [here](https://www.youtube.com/watch?v=ei5-5vcEPz8&t=136s) |
| YouTube - Codemy| add posts | [here](https://www.youtube.com/watch?v=CnaB4Nb0-R8) |
| YouTube - Codemy| comment section | [here](https://www.youtube.com/watch?v=hZrlh4qU4eQ) |
| YouTube - Codemy| delete blog post | [here](https://www.youtube.com/watch?v=8NPOwmtupiI) |
| YouTube - Codemy| update blog post | [here](https://www.youtube.com/watch?v=J7xaESAddDQ) |
| YouTube - Coding Entrepreneurs | Ajax likes | [here](https://www.youtube.com/watch?v=pkPRtQf6oQ8) |
| YouTube - Coding Is Thinking |  delete comments | [here](https://www.youtube.com/watch?v=kuJPMKbN3Yg) |
| YouTube - Django World |  edit and delete button for blog detail page | [here](https://www.youtube.com/watch?v=wFci3tnRNFw) |


### Articles

These article samples were taken from third party resources to prepopulate the website with blogs that present organic content.

- [Jalopnik](https://jalopnik.com/every-car-looks-like-this-thanks-to-a-gigantic-regulato-1849837803): Every Car Looks Like This Thanks to a Gigantic Regulatory Loophole
- [Car Zone](https://www.carzone.ie/motoring-advice/should-you-buy-a-used-electric-car/2933): Should You Buy A Used Electric Car?


### Library Information

- [Car Info](https://www.car.info/en-se/brand): This website presents a database of all car manufacturers in the world. It provided help in preparing the car maker choices tuple that is present in the consultation application submission form.

- [The Python Package Index (PyPI)](https://pypi.org/): PyPI was critical in accessing libraries that added functionality to the project that otherwise would be impossible to feature in the end product.

- [Code Insitute](https://codeinstitute.net/ie/): The theory available in the Code Institute curriculum has been central in successfully setting up and utilizing Google Cloud API services for this project.


### Theory

- [UCD Professional Academy](https://www.ucd.ie/professionalacademy/): I would like to thank UCD PA for their facilitator and masterclass sessions in partnership with Code Insitute. These have been invaluable in better understanding relevant theory and practice elements.

---

## Acknowledgements

I would like to first and foremost thank my mentor, Rohit Sharma, for his dedication to helping me find direction in developing my projects and understand the fundamental considerations in growing as a software developer. Moreover, the tutor support available at Code Institute has been an excellent help in finding solutions to various issues I came across in the development process that I needed help. Lastly, the Slack community at Code Institute has been nothing less than inspirational. I commend their dedication to a constructive culture that strives to help future developers in their struggles towards their software development journey. 

--- 

## Closing Remarks

In closing, the development process in its entirety has doubtless been a highly educative experience. This having been my first time using any kind of full-stack framework to build a web development project, I was introduced to many challenges which at times greatly impeded the development momentum. However, while this may be the case, overcoming the obstacles presented by such issues allowed for understanding how different elements of Django interacted with one another. It is possible to access these learning points through tutorial videos or blog posts. But, my experience shows that one does not truly learn the intricacies of Django until they experience and overcome them themselves. It is possible to argue that this experience isn't unique to the use of Django. The learning points obtained from experiencing and solving problems when using Django provide an opportunity to nurture a development strategy that can translate across many different forms of software development. Thus, if I would take away one key lesson from my experience with this project would be to start from smaller core functionality and slowly expand the project's functional capacity rather than the other way around. If not monitored correctly, the constant addition of tasks and ideas can lead to a long backlog of features that will never become a subject of consideration for the final project.

---
 [Back to Top](#table-of-contents)