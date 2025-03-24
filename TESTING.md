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
1. Api app
- serializers.py <mark>PASS<mark>

![serializers](./assets/testing/api-serializers.PNG)

- urls.py <mark>PASS<mark>

![urls](./assets/testing/api-urls.PNG)

- views.py <mark>PASS<mark>

![views](./assets/testing/api-views.PNG)

2. Automarket app
- settings.py <mark>PASS<mark> 

(line too long is part of django standart settings file)

![settings](./assets/testing/automarket-settings.PNG)

- urls.py <mark>PASS<mark>

![urls](./assets/testing/automarket-urls.PNG)

- views.py <mark>PASS<mark>

![views](./assets/testing/automarket-views.PNG)


## Responsiveness
During development each page was tested using dev tools in Google Chrome. The strategy involved ensuring that every page would adapt to various screen sizes beyond a width of 320px, as opposed to relying on fixed device-specific widths.
Further testing was done on mobile to confirm all is working as expected.

|Device|Screen Size|Pass/Fail|Comment|
| --- | --- | --- | ---|
| Iphone 4 | 320x480 | PASS | All sections are displayed correctly. All features work|
| Iphone 12 Pro | 390x844 | PASS | All sections are displayed correctly. All features work|
| Samsung Galaxy s20U | 412x915 | PASS | All sections are displayed correctly. All features work|
| Galaxy Tab S4 | 712x1138| PASS | All sections are displayed correctly. All features work|
| Nest Hub | 1024x600 | PASS | All sections are displayed correctly. All features work|


### Galaxy S20 Ultra
<details><summary>Home</summary> 
 <img src="./assets/testing/responsiveness/Home.jpg"> </details>

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
| Firefox | All pages, load as expected. All features work as expected | PASS | --- |
| Edge | All pages, load as expected. All features work as expected | PASS | During initial testing there was an issue with the hero image on Edge. The reason was that the browser does not support avif files. The file was converted to webp and tested again.  |

## Lighthouse

|Page|Validator|Result|
| --- | --- | --- |
| Home Desktop |![home](./assets/testing/lighthouse/home-d.PNG) | <mark>PASS<mark> |
| Home Mobile |![home](./assets/testing/lighthouse/home-m.PNG) | <mark>PASS<mark> |
| Listings Desktop|![listings](./assets/testing/lighthouse/listings-d.PNG) | <mark>PASS<mark> |
| Listings Mobile|![listings](./assets/testing/lighthouse/listings-m.PNG) | <mark>PASS<mark> |
| Single Listing Desktop|![Single Listing](./assets/testing/lighthouse/single-listing-d.PNG) | <mark>PASS<mark> |
| Single Listing Mobile|![Single Listing](./assets/testing/lighthouse/single-listing-m.PNG) | <mark>PASS<mark> |
| Create Listing Desktop|![Create Listing](./assets/testing/lighthouse/create-listing-d.PNG) | <mark>PASS<mark> |
| Create Listing Mobile|![Create Listing](./assets/testing/lighthouse/create-listing-m.PNG) | <mark>PASS<mark> |
| Edit Listing Desktop|![Create Listing](./assets/testing/lighthouse/edit-listing-d.PNG) | <mark>PASS<mark> |
| Edit Listing Mobile|![Create Listing](./assets/testing/lighthouse/edit-listing-m.PNG) | <mark>PASS<mark> |
| My Profile Desktop|![My Profile](./assets/testing/lighthouse/my-profile-d.PNG) | <mark>PASS<mark> |
| My Profile Mobile|![My Profile](./assets/testing/lighthouse/my-profile-m.PNG) | <mark>PASS<mark> |
| My Listings Desktop|![My Listings](./assets/testing/lighthouse/my-listings-d.PNG) | <mark>PASS<mark> |
| My Listings Mobile|![My Listings](./assets/testing/lighthouse/my-listings-m.PNG) | <mark>PASS<mark> |
| My Favourites Desktop|![My Favourites](./assets/testing/lighthouse/my-favourites-d.PNG) | <mark>PASS<mark> |
| My Favourites Mobile|![My Favourites](./assets/testing/lighthouse/my-favourites-m.PNG) | <mark>PASS<mark> |
| User Account Desktop|![User Account](./assets/testing/lighthouse/user-acc-d.PNG) | <mark>PASS<mark> |
| User Account Mobile|![User Account](./assets/testing/lighthouse/user-acc-m.PNG) | <mark>PASS<mark> |
| User Listings Desktop |![User Listings](./assets/testing/lighthouse/user-acc-listings-d.PNG) | <mark>PASS<mark> |
| User Listings Mobile |![User Listings](./assets/testing/lighthouse/user-acc-m.PNG) | <mark>PASS<mark> |
| Edit Profile Desktop|![Edit Profile](./assets/testing/lighthouse/edit-profile-d.PNG) | <mark>PASS<mark> |
| Edit Profile Mobile|![Edit Profile](./assets/testing/lighthouse/edit-profile-m.PNG) | <mark>PASS<mark> |
| Delete Profile Conf Desktop|![Delete Profile](./assets/testing/lighthouse/delete-profile-d.PNG) | <mark>PASS<mark> |
| Delete Profile Conf Mobile|![Delete Profile](./assets/testing/lighthouse/delete-profile-m.PNG) | <mark>PASS<mark> |
| Profile Deleted Desktop|![Profile Deleted](./assets/testing/lighthouse/profile-delete-success-d.PNG) | <mark>PASS<mark> |
| Profile Deleted Mobile|![Profile Deleted](./assets/testing/lighthouse/profile-delete-success-m.PNG) | <mark>PASS<mark> |
| Delete Listing Conf Desktop|![Delete Listing Conf](./assets/testing/lighthouse/delete-listing-d.PNG) | <mark>PASS<mark> |
| Delete Listing Conf Mobile|![Delete Listing Conf](./assets/testing/lighthouse/delete-listing-m.PNG) | <mark>PASS<mark> |
| Remove Favourite Desktop|![Remove Favourite](./assets/testing/lighthouse/remove-fav-d.PNG) | <mark>PASS<mark> |
| Remove Favourite Mobile|![Remove Favourite](./assets/testing/lighthouse/remove-fav-m.PNG) | <mark>PASS<mark> |
| Log In Desktop|![Log In](./assets/testing/lighthouse/sign-in-d.PNG) | <mark>PASS<mark> |
| Log In Mobile|![Log In](./assets/testing/lighthouse/sign-in-m.PNG) | <mark>PASS<mark> |
| Sign Up Desktop|![Sign Up](./assets/testing/lighthouse/sign-up-d.PNG) | <mark>PASS<mark> |
| Sign Up Mobile|![Sign Up](./assets/testing/lighthouse/sign-up-m.PNG) | <mark>PASS<mark> |
| Sign Out Conf Desktop|![home](./assets/testing/lighthouse/logout-d.PNG) | <mark>PASS<mark> |
| Sign Out Conf Mobile|![home](./assets/testing/lighthouse/logout-m.PNG) | <mark>PASS<mark> |
| Reset Password Enter email Desktop|![Reset Password Enter email](./assets/testing/lighthouse/pass-res-d.PNG) | <mark>PASS<mark> |
| Reset Password Enter email Mobile|![Reset Password Enter email](./assets/testing/lighthouse/pass-res-m.PNG) | <mark>PASS<mark> |
| Reset Password email sent Desktop|![Reset Password email sent](./assets/testing/lighthouse/pass-res-sent-d.PNG) | <mark>PASS<mark> |
| Reset Password email sent Mobile|![Reset Password email sent](./assets/testing/lighthouse/pass-res-sent-m.PNG) | <mark>PASS<mark> |
| Reset Password Enter password Desktop|![Reset Password Enter password](./assets/testing/lighthouse/pass-res-newpass-d.PNG) | <mark>PASS<mark> |
| Reset Password Enter password Mobile|![Reset Password Enter password](./assets/testing/lighthouse/pass-res-newpass-m.PNG) | <mark>PASS<mark> |
| Reset Password Complete Desktop|![Reset Password Complete](./assets/testing/lighthouse/pass-res-complete-d.PNG) | <mark>PASS<mark> |
| Reset Password Complete Mobile|![Reset Password Complete](./assets/testing/lighthouse/pass-res-complete-m.PNG) | <mark>PASS<mark> |
| Profile Deleted Success Desktop |![Profile Deleted Success](./assets/testing/lighthouse/profile-delete-success-d.PNG) | <mark>PASS<mark> |
| Profile Deleted Success Mobile |![Profile Deleted Success](./assets/testing/lighthouse/profile-delete-success-m.PNG) | <mark>PASS<mark> |

## Manual Testing
- Home Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Navbar|Click on logo in Navbar|Redirect to Home |Pass|Navbar present on all pages |
||Click on Home link in Navbar|Redirect to Home |Pass|Navbar present on all pages |
||Click on Listings link in Navbar|Redirect to Listings Page |Pass|Navbar present on all pages |
||Click on Create Listing link in Navbar|Redirect to Create Listing Page |Pass|Navbar present on all pages |
||Click on Profile link in Navbar|Redirect to My Profile Page |Pass|Navbar present on all pages |
||Click on Log Out link in Navbar|Redirect to Create Listing Page |Pass|Navbar present on all pages |
||Click on Login/Sign Up in Navbar|Redirect to Login Page |Pass|Navbar present on all pages |
|Hero section|Open Home page. Ensure the hero section loads as it should|Hero section loads as it should |Pass| |
|Search form|Open the Home page. Ensure the search form section loads as it should|Search form section loads as it should |Pass| |
||Click on each input field. Ensure all choices are loaded.|All input fields appear as they should. |Pass| |
||Search listings by a combination of filters. Ensure the results displayed are accurate with the search filters|All search results match the search criteria |Pass| |
||Select a max year. Ensure the min year cannot exceed the max year|All values of min year that exceed the max year are disabled |Pass| |
||Select min year. Ensure the max year cannot be less than the max year|All values of the max year that are below the min year are disabled |Pass| |
||Select max price. Ensure the min price cannot exceed the max price|All values of min price which exceed the max price are disabled |Pass| |
||Select min price. Ensure the max price cannot be less than the max price|All values of max price which are below min price are disabled |Pass| |
||Click on the search button. Ensure the user is redirected to the listings page|The user is redirected to the listings page with accurate results |Pass| |
|Recent Listings|Open the Home page. Scroll down to recent listings. Ensure the most recent listings are showing by comparing the time added stamp|The most recent listings are displayed |Pass| |
||Open the Create Listing page and create a listing. Ensure it shows as first in the most recent listings section |The added listing is displayed as most recent |Pass| |
|Listing Card| Click on the listing card. Ensure it redirects to the correct single listing page |When clicked each card redirects to the correct single listing page |Pass| |
|| Click on the listing card button. Ensure it redirects to the correct single listing page |When clicked each card button redirects to the correct single listing page |Pass| |
|| Go to the Create Listings page and create a new listing. Ensure the details displayed on the card are accurate |The information displayed on the card is accurate |Pass| |
|Pagination| Click on all of the links in the pagination. Ensure they redirect to the appropriate page. |All links redirect to the correct page. |Pass| |
|Pagination| Use the search form to search listings. Click on all of the links in the pagination. Ensure they redirect to the appropriate page displaying only the search results. |All links redirect to the correct page displaying the correct results. |Pass| |
|Footer|Click on all of the social links in the footer. Ensure each one opens the correct page in a new tab |All links open the correct page in a new tab |Pass| |

- Listings Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|search form|||Pass|Tested on home page|
|listing card|||Pass|Tested on home page|
|Pagination| Click on all of the links in the pagination. Ensure they redirect to the appropriate page. |All links redirect to the correct page. |Pass| |
|Pagination| Use the search form to search listings. Click on all of the links in the pagination. Ensure they redirect to the appropriate page displaying only the search results. |All links redirect to the correct page displaying the correct results. |Pass| |
|Footer|Click on all of the social links in the footer. Ensure each one opens the correct page in a new tab |All links open the correct page in a new tab |Pass| |

- Single Listing Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
| Back button|Open the single listing page. Click on the back button. Ensure it sends you back to the previous page|When clicked the button brings you back to the previous page.|Pass||
|back button|Open the single listing page and the listing to favourites. Click on the back button. Ensure it sends you back to the previous page|When clicked the button does not bring you back to the previous page due to the fact the page reloaded|Fail|This is a known bug.|
|Images section|Click on the main image. Ensure it opens using Lightbox. Ensure arrows appear to navigate through the images|When clicked the images open using lightbox. Arrows appear on the sides and allow you to navigate through the images|Pass||
|Listing details|Ensure all the car specs are accurate with the details used when creating the listing. Ensure all icons display as they should|All icons display as they should, and the information is accurate.|Pass||
|Save to favourites button|Click on the heart icon. Ensure the page reloads, a flash message is displayed with confirmation and the icon changes to full heart|When clicked the page reloads, a flash message is displayed with confirmation and the icon changes to full heart|Pass||
||As not authenticated user, Click on the heart icon. Ensure the page redirects to the login page|When clicked the page redirects to the login page|Pass||
||As an authenticated user, open your listing. Ensure the favourites button does not appear|When visiting your listing the favourites button does not appear|Pass||
|Seller Card|Click on the seller's image. Ensure the link leads to the user's account profile|When clicked redirects to the user's account profile|Pass||
|Email Seller form|Click on the Email Seller button. Ensure a modal pops up with a form to fill in|When clicked, the modal pops up with a form to fill in|Pass||
||Click on the Email Seller button. Ensure The listing title field is populated and read-only. |The listing title field is populated and read-only.|Pass||
||As an authenticated user, ensure the form is prefilled with the user's details|When clicked, a modal pops up with pre-filled form fields for existing details like name and email.|Pass||
||Fill all fields with correct data in the expected format. Click send a message. Ensure an email has been sent with the details entered using a test email address |Email was received with accurate details|Pass||
||Fill all fields with correct data but one. Click send a message. Ensure the form is not submitted and an appropriate message is displayed. Repeat for all fields. |Form did not submit, the appropriate message was displayed|Pass||
|Description|Scroll to the description section. Ensure the accurate description is displayed |The accurate description is displayed|Pass||

- Create listing Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Form|To test car make/model dependancy first select model and ensure there are no drop down options. Then select car make. Ensure the car model field is populated with the correct options for each make|The car model dropdown has no options initially. The car model field is populated with the correct options for each make|Pass||
||Click on each drop down field to ensure correct options are displayed|Correct options are displayed|Pass||
||Fill all fields with correct data in the expected format. Click Submit. Ensure the listing was created by: 1. checking for flash message, 2. Go to Home page and find the card with the new listing |When submitted success flash message is presented. The new listing card appears on the home page's recent listings|Pass||
||Fill all fields with correct data but one. Click Submit. Ensure the form does not submit and appropriate message is displayed. Repeat for all fields. |Form did not submit, appropriate message was displayed|Pass||

- Edit listing Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Form|||Pass|Tested at create listing|
||Open edit listing page. Ensure the form is populated with the correct listing's details|The form is populated with the correct listing's details|Pass||

- My Profile Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Profile Card|Open my profile page. Ensure the image is displaying correctly.|The image is displaying correctly.|Pass||
||Open my profile page. Ensure my details are accurate and are displaying correctly.|My details are accurate and are displaying correctly.|Pass||
|Edit profile button|Click on the edit profile button. Ensure it redirects to the edit profile page.|The edit profile button redirects to the edit profile page.|Pass||
|Delete profile button|Click on the delete profile button. Ensure it redirects to the delete profile page.|The delete profile button redirects to the delete profile page.|Pass||
||Click on my listings link on the sidebar nav. Ensure it redirects to my listings page| Redirects to my listings page|Pass||
||Click on my favourites link on the sidebar nav. Ensure it redirects to my favourites page| Redirects to my favourites page|Pass||

- My Listings Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|My Listings Card|When on the my listings page ensure the listings displayed were created by the authenticated user.|The listings displayed were created by the authenticated user. |Pass||
||Click on the edit button. Ensure it redirects to the edit listing page.|The button redirects to the edit listing page. |Pass||
||Click on the delete button. Ensure it redirects to the delete listing page.|The button redirects to the delete listing page. |Pass||
||Click on the view button. Ensure it redirects to the single listing page.|The button redirects to the single listing page. |Pass||

- My Favourites Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|My Favourites Card|When on the my favourites page ensure the listings displayed were saved by the authenticated user.|The listings displayed were saved by the authenticated user. |Pass||
||Click on the view button. Ensure it redirects to the single listing page.|The button redirects to the single listing page. |Pass||
||Click on the remove button. Ensure it redirects to the remove listing confirmation page.|The button redirects to the remove listing confirmation page. |Pass||


- User Account Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Profile Card|Open the user account page from the seller card on the listing page. Ensure the image is displaying correctly.|The image is displaying correctly.|Pass||
||Open the user account page. Ensure the contact details are accurate and are displaying correctly.|The contact details are accurate and are displaying correctly.|Pass||
||Click on listings link on the sidebar nav. Ensure it redirects to the account listings page| Redirects to account listings page|Pass||

- Account Listings Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|My Listings Card|When on the account listings page ensure the listings displayed were created by the account user.|The listings displayed were created by the account user. |Pass||
||Click on the More Info button. Ensure it redirects to the single listing page.|The button redirects to the single listing page. |Pass||

- Edit/Update Profile Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Back button|Open the edit profile page. Click on the back button. Ensure it sends back to previous page|When clicked the button brings back to previous page.|Pass||
|Form|Open the edit profile page. Ensure the form is pre-filled with the user's details.| The form is pre-filled with the user's details|Pass||
||Fill all fields with correct data in the expected format. Click Submit. Ensure 1. Flash message appears, the user is redirected to their profile, 3. The user's details have been updated |When submitted success flash message is presented, the user is redirected to the profile page and the details are updated.|Pass||
||Fill all fields with correct data but one. Click Submit. Ensure the form does not submit and appropriate message is displayed. Repeat for all fields. |Form did not submit, appropriate message was displayed|Pass||

- Delete Profile Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Go back button|Click on the go back button. Ensure it sends back to previous page |When clicked the button brings back to previous page.|Pass||
|Delete profile|Click on the delete profile button. Ensure it deletes the user account and the user is redirected to the We are sorry to see you go page. |The user is redirected to the We are sorry to see you go page. By checking in the admin pannel can be confirmed the user and the profile were deleted|Pass||

- We are sorry to see you go page.
|Go Home|Click on the go home button. Ensure it redirects to home page |When clicked the button redirects to home page.|Pass||
|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|

- Delete Listing Page 

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Go back button|Click on the go back button. Ensure it sends back to previous page |When clicked the button brings back to previous page.|Pass||
|Delete Listing|Click on the delete listing button. Ensure it deletes the listing and the user is redirected to the my listings page. |The user is redirected to the my listings page. By checking in the admin pannel can be confirmed the was deleted|Pass||

- Remove listing from favourites

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Go back button|Click on the go back button. Ensure it sends back to previous page |When clicked the button brings back to previous page.|Pass||
|Remove button|Click on the Remove button. Ensure it removes the listing from favourites and the user is redirected to the my favourites page. Ensure flash message is displayed |The user is redirected to the my favourites page. Flash message is displayed. By visiting my favourites page can be confirmed that the listing was removed. |Pass||

- Log In page

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Form|Fill all fields with correct data in the expected format. Click Sign In. Ensure Flash message appears and the user is redirected to the home page. To ensure the user is logged in: Open developer tools and navigate to application. On the side select cookies and check for sessionid being added. |When submitted success flash message is presented, the user is redirected to the home page. Sessionid is added to the cookies|Pass||
| | Fill in the form with incorrect details. Ensure the user is not logged in and flash message appears| Flash message appears in red letting the user know they have entered incorrect details. The user is not signed in| Pass| |
| | Click on the forgot password link. ensure it redirects to the reset password page.| The user is redirected to the reset password page| Pass| |
| | Click on the register here link. ensure it redirects to sign up page.| The user is redirected to the sign up page| Pass| |

- Sign Up Page

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Form|Fill all fields with correct data in the expected format. Click Sign Up. Ensure Flash message appears and the user is redirected to the my profile page.|When submitted success flash message is presented, the user is redirected to the my profile page.|Pass||
||Fill all fields with correct data but one. Click Sign Up. Ensure the form does not submit and appropriate message is displayed. Repeat for all fields. |Form did not submit, appropriate message was displayed|Pass||
| | Click on the Already have an account? Log In link. ensure it redirects to the login page.| The user is redirected to the login page| Pass| |


- Sign Out confirmation

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|Go back button|Click on the go back button. Ensure it sends back to previous page |When clicked the button brings back to previous page.|Pass||
|Log out button|Click on the Log out button.To ensure the user is logged out: Open developer tools and navigate to application. On the side select cookies and check for sessionid being removed.The user should be redirected to the the home page. Ensure flash message is displayed |The user is redirected to the home page. Flash message is displayed. Sessionid is removed from cookies.|Pass||

- Reset password

|Section|Test Action|Expected Result|Pass/Fail|Comments|
| ---| ---| ---| ---| ---|
|form|Enter valid email, click on reset password |When submitted, email is sent to the email address with instructions.|Pass||


## User Story Testing
|User Story|Screenshot|Result|
| --- | --- | --- |
| As a developer I can set up a new Django project so that I can create the project's structure | The project was set up successfully| <mark>PASS<mark>  |
