Go back to [README.md](/README.md)

# Testing
- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#JavaScript)
    - [Python](#python)
- [Responsiveness](#Responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Lighthouse](#Lighthouse)
- [Manual Testing](#manual-testing)
- [User Story Testing](#user-story-testing)

## Code Validation
### HTML
|Page|Validator|Result|
| --- | --- | --- |
| Home |![home](./assets/testing/html-validator/home.PNG) | <mark>PASS<mark> |



### CSS
Test Results CSS  <mark>PASS<mark> 

![css-validator](./assets/testing/css-validator.PNG)

### JavaScript
1. listing_form.js <mark>PASS<mark> 

![listing_form](./assets/testing/listing_form.PNG)

2. search.js <mark>PASS<mark>

The initial test showed variable not declared. This was fixed.
![search](./assets/testing/search.PNG)

### Python
1. community App
- ads/forms.py <mark>PASS<mark>

![ads/forms](/equisync/docs/images/comm-pep-1.png)

- ads/models.py <mark>PASS<mark>

![ads/models](/equisync/docs/images/comm-pep-2.png)

- ads/views.py <mark>PASS<mark>

![ads/views](/equisync/docs/images/comm-pep-3.png)

- announcements/forms.py <mark>PASS<mark>

![announcements/forms](/equisync/docs/images/comm-pep-4.png)

- announcements/models.py <mark>PASS<mark>

![announcements/models](/equisync/docs/images/comm-pep-5.png)

- announcements/views.py <mark>PASS<mark>

![announcements/views](/equisync/docs/images/comm-pep-6.png)

- dict_filters.py <mark>PASS<mark>

![dict_filters](/equisync/docs/images/comm-pep-7.png)

- reaction_tags.py <mark>PASS<mark>

![reaction_tags](/equisync/docs/images/comm-pep-8.png)

- admin.py <mark>PASS<mark>

![admin.py](/equisync/docs/images/comm-pep-9.png)

- apps.py <mark>PASS<mark>

![apps.py](/equisync/docs/images/comm-pep-10.png)

- filters.py <mark>PASS<mark>

![filters.py](/equisync/docs/images/comm-pep-11.png)

- forms.py <mark>PASS<mark>

![forms.py](/equisync/docs/images/comm-pep-12.png)

- models.py <mark>PASS<mark>

![models.py](/equisync/docs/images/comm-pep-13.png)

- signals.py <mark>PASS<mark>

![signals.py](/equisync/docs/images/comm-pep-14.png)

- urls.py <mark>PASS<mark>

![urls.py](/equisync/docs/images/comm-pep-15.png)

- views_reactions.py <mark>PASS<mark>

![views_reactions.py](/equisync/docs/images/comm-pep-16.png)

- views.py <mark>PASS<mark>

![views.py](/equisync/docs/images/comm-pep-17.png)

2. competitions app
- settings.py <mark>PASS<mark> 

![settings](./assets/testing/automarket-settings.PNG)

- urls.py <mark>PASS<mark>

![urls](./assets/testing/automarket-urls.PNG)

- views.py <mark>PASS<mark>

![views](./assets/testing/automarket-views.PNG)

3.  equisync project main
- settings.py <mark>PASS<mark> 

![settings](./assets/testing/automarket-settings.PNG)

4. exercise_schedule app
- settings.py <mark>PASS<mark> 

![settings](./assets/testing/automarket-settings.PNG)

5. feeding_management app
- settings.py <mark>PASS<mark> 

![settings](./assets/testing/automarket-settings.PNG)

6. horses app
- settings.py <mark>PASS<mark> 

![settings](./assets/testing/automarket-settings.PNG)

7. users app
- settings.py <mark>PASS<mark> 

![settings](./assets/testing/automarket-settings.PNG)

## Responsiveness
During development each page was tested using dev tools in Google Chrome. The strategy involved ensuring that every page would adapt to various screen sizes beyond a width of 320px, as opposed to relying on fixed device-specific widths.
Further testing was done on mobile to confirm all is working as expected.

|Device|Screen Size|Pass/Fail|Comment|
| --- | --- | --- | ---|
| Iphone 12 | 320x480 | PASS | All sections are displayed correctly. All features work|
| Iphone 13 Pro | 390x844 | PASS | All sections are displayed correctly. All features work|



### Galaxy S20 Ultra
<details><summary>Home</summary><img src="./assets/testing/responsiveness/Home.jpg"> </details>
<details><summary>Listings</summary> <img src="./assets/testing/responsiveness/Listings.jpg"></details>
<details><summary>Single Listing</summary><img src="./assets/testing/responsiveness/single-listing-page.jpg"></details>
<details><summary>Gallery</summary><img src="./assets/testing/responsiveness/gallery.jpg"></details>
<details><summary>Create Listing</summary><img src="./assets/testing/responsiveness/Create-listing.jpg"></details>
<details><summary>My Profile</summary><img src="./assets/testing/responsiveness/my-profile.jpg"></details>
<details><summary>My Favourites</summary><img src="./assets/testing/responsiveness/my-favourites.jpg"></details>
<details><summary>My Listings</summary><img src="./assets/testing/responsiveness/my-listings.jpg"></details>
<details><summary>Remove Favourite</summary><img src="./assets/testing/responsiveness/remove-fav-conf.jpg"></details>
<details><summary>500 Page</summary><img src="./assets/testing/responsiveness/500-page.jpg"></details>
<details><summary>Log In</summary><img src="./assets/testing/responsiveness/Sign-in.jpg"></details>
<details><summary>Sign Up</summary><img src="./assets/testing/responsiveness/Sign-up.jpg"></details>


## Browser Compatibility


|Browser|Result|Pass/Fail|Notes|
| --- | --- | --- | ---|
| Google Chrome | All pages, load as expected. All features work as expected | PASS | --- |
| Edge | All pages, load as expected. All features work as expected | PASS | During initial testing there was an issue with the hero image on Edge. The reason was that the browser does not support avif files. The file was converted to webp and tested again.  |

## Lighthouse

|Page|Validator|Result|
| --- | --- | --- |
| Home Desktop |![home](./assets/testing/lighthouse/home-d.PNG) | <mark>PASS<mark> |


## Manual Testing
- Home Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Navbar|Click on logo in Navbar|Redirect to Home |Pass|


## User Story Testing
| User Story | Screenshot | Result |
| --- | --- | --- |
| As a developer I want to organize my project with milestones and a Kanban board of issues |  |  |
| As a developer I want to create user stories for different user roles |  |  |
| As a developer I want to design a database schema for my project |  |  |
| As a developer I want to create wireframes for the application |  |  |
| As a developer I want to create a README file with documentation |  |  |
| As a developer I want to set up a Django project |  |  |
| As a developer I want to create and configure a database |  |  |
| As a developer I want to deploy the app early and often |  |  |
| As a site user I want to register an account |  |  |
| As a site user I want to log in and log out of my account |  |  |
| As a site user I want to have a profile created after registration |  |  |
| As a visitor I want to learn about the stable, its owner, and its horses |  |  |
| As a visitor I want to contact the manager |  |  |
| As a visitor I want to view the calendar of upcoming horseshows |  |  |
| As a visitor I want to view the stable's previous events and search by name or date |  |  |
| As a visitor I want to view the stable community page |  |  |
| As a visitor I want a responsive site design across all devices |  |  |
| As the Barn Manager I want an admin dashboard to manage user updates |  |  |
| As the Barn Manager I want full access while others have role-based access |  |  |
| As the Barn Manager I want a simple data collection system for horse care |  |  |
| As the Barn Manager I want to view each horse's exercise schedule in detail and overviews |  |  |
| As the Barn Manager I want to quickly share horse data via email or text |  |  |
| As the Barn Manager I want approval rights over community posts |  |  |
| As the Barn Manager I want each horse to have a stored profile |  |  |
| As the Barn Manager I want a show schedule for all horses and individuals |  |  |
| As the Barn Manager I want a calendar for show schedules |  |  |
| As the Barn Manager I want horse schedules manageable by all roles |  |  |
| As the Barn Manager I want to see the full week's schedule for all horses |  |  |
| As the Barn Manager I want feeding schedules stored and visible to all |  |  |
| As the Barn Manager I want to update and group feeding schedules |  |  |
| As an owner I want a community page to view and create posts |  |  |
| As an owner I want clear displays of my horse's routines and schedules |  |  |
| As an owner I want to receive schedule updates by email or sms |  |  |
| As an owner I want weekly/monthly calendar views for competitions |  |  |
| As a rider I want to track performance and stay consistent with horse routines |  |  |
| As a rider I want to interact and trade on the community page |  |  |
| As a staff member I want shared storage of routines to avoid confusion |  |  |
| As a staff member I want a record of my care activities |  |  |
| As a staff member I want to engage and trade on the community page |  |  |

