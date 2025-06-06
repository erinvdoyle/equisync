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

All html was checked for commented out code. Unfortunately my w3 schools validation check returned issues with the django tags, which I was not anticipating and did not have the time to rewrite within my entire codebase:


![html-validator](/equisync/docs/images/valid-html.png)


### CSS
Test Results CSS  <mark>PASS<mark> 

Due to the validator seemingly taking a dislike to preloaded css via bootstrap, I was unable to run the site without having multiple errors outside of my code. However, I passed each of my app's css files through with no errors to my own code. This was my first tango with separating css into dedicated files for each app and the organization of these files and my classes would have improved with more time. I have made an effort to clean up some of the abandanoned and unused css, but there is still work to be done.

![css-validator](/equisync/docs/images/valid-css.png)

### JavaScript
1. community.js

![community](/equisync/docs/images/js-comm-1.png)

2. reactions.js 

![community reactions](/equisync/docs/images/js-comm-2.png)

3. competitions.js 

![competitions](/equisync/docs/images/js-comp.png)

4. script.js 

![script.js](/equisync/docs/images/js-scriptjs.png)

5. horses.js 

![horses.js](/equisync/docs/images/js-horses.png)

5. users.js 

![users.js](/equisync/docs/images/js-users.png)

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
- calendar_tags.py <mark>PASS<mark> 

![calendar_tags](/equisync/docs/images/comp-pep-1.png)

- admin.py <mark>PASS<mark>

![admin.py](/equisync/docs/images/comp-pep-2.png)

- apps.py <mark>PASS<mark>

![apps.py](/equisync/docs/images/comp-pep-3.png)

- models.py <mark>PASS<mark>

![models.py](/equisync/docs/images/comp-pep-4.png)

- urls.py <mark>PASS<mark>

![urls.py](/equisync/docs/images/comp-pep-5.png)

- utils.py <mark>PASS<mark>

![utils.py](/equisync/docs/images/comp-pep-6.png)

- views.py <mark>PASS<mark>

![views.py](/equisync/docs/images/comp-pep-7.png)

3.  equisync project main
- asgi.py <mark>PASS<mark>

![asgi.py](/equisync/docs/images/eq-pep-1.png)

- InstallCertificates.py <mark>PASS<mark>

![InstallCertificates.py](/equisync/docs/images/eq-pep-2.png)

- settings.py <mark>PASS<mark>

![settings.py](/equisync/docs/images/eq-pep-3.png)

- urls.py <mark>PASS<mark>

![urls.py](/equisync/docs/images/eq-pep-4.png)

- wsgi.py <mark>PASS<mark>

![wsgi.py](/equisync/docs/images/eq-pep-5.png)

- manage.py <mark>PASS<mark>

![manage.py](/equisync/docs/images/eq-pep-6.png)

- models.py <mark>PASS<mark>

![models.py](/equisync/docs/images/eq-pep-7.png)

4. exercise_schedule app
- exercise_tags.py <mark>PASS<mark>

![exercise_tags.py](/equisync/docs/images/ex-pep-1.png)

- admin.py <mark>PASS<mark>

![admin](/equisync/docs/images/ex-pep-2.png)

- apps.py <mark>PASS<mark>

![apps.py](/equisync/docs/images/ex-pep-3.png)

- forms.py <mark>PASS<mark>

![forms.py](/equisync/docs/images/ex-pep-4.png)

- models.py <mark>PASS<mark>

![models](/equisync/docs/images/ex-pep-5.png)

- urls.py <mark>PASS<mark>

![urls](/equisync/docs/images/ex-pep-6.png)

- views.py <mark>PASS<mark>

![views](/equisync/docs/images/ex-pep-7.png)

5. feeding_management app
- admin.py <mark>PASS<mark>

![admin.py](/equisync/docs/images/fm-pep-1.png)

- apps.py <mark>PASS<mark>

![apps.py](/equisync/docs/images/fm-pep-2.png)

- forms.py <mark>PASS<mark>

![forms](/equisync/docs/images/fm-pep-3.png)

- models.py <mark>PASS<mark>

![models](/equisync/docs/images/fm-pep-4.png)

- tables.py <mark>PASS<mark>

![tables](/equisync/docs/images/fm-pep-5.png)

- urls.py <mark>PASS<mark>

![urls](/equisync/docs/images/fm-pep-6.png)

- views.py <mark>PASS<mark>

![views](/equisync/docs/images/fm-pep-7.png)

6. horses app
- admin.py <mark>PASS<mark>

![admin.py](/equisync/docs/images/h-pep-1.png)

- apps.py <mark>PASS<mark>

![apps.py](/equisync/docs/images/h-pep-2.png)

- forms.py <mark>PASS<mark>

![forms](/equisync/docs/images/h-pep-3.png)

- models.py <mark>PASS<mark>

![models](/equisync/docs/images/h-pep-4.png)

- urls.py <mark>PASS<mark>

![urls](/equisync/docs/images/h-pep-5.png)

- views.py <mark>PASS<mark>

![views](/equisync/docs/images/h-pep-6.png)

7. users app
- admin.py <mark>PASS<mark>

![admin.py](/equisync/docs/images/u-pep-1.png)

- apps.py <mark>PASS<mark>

![apps.py](/equisync/docs/images/u-pep-2.png)

- context-processors.py <mark>PASS<mark>

![context-processors](/equisync/docs/images/u-pep-3.png)

- forms.py <mark>PASS<mark>

![forms](/equisync/docs/images/u-pep-4.png)

- models.py <mark>PASS<mark>

![models](/equisync/docs/images/u-pep-5.png)

- signals.py <mark>PASS<mark>

![signals](/equisync/docs/images/u-pep-6.png)

- urls.py <mark>PASS<mark>

![urls](/equisync/docs/images/u-pep-7.png)

- views.py <mark>PASS<mark>

![views](/equisync/docs/images/u-pep-8.png)

## Responsiveness
During development each page was tested using dev tools in Google Chrome. All pages were tested primarily for each screen size between 320px and 1420px, with a consideration of larger desktops as well

|Device|Screen Size|Pass/Fail|Comment|
| --- | --- | --- | ---|
| Iphone 12 | 390x844 | PASS | All sections display correctly. All features work|
| Iphone 13 Pro | 390x844 | PASS | All sections display correctly. All features work|

## Browser Compatibility

|Browser|Result|Pass/Fail|Notes|
| --- | --- | --- | ---|
| Google Chrome | All pages load as expected. All features work as expected | PASS |
| Edge | All pages, load as expected. All features work as expected | PASS |

## Lighthouse

|Page|Validator|Result|
| --- | --- | --- |
| Home |![home](/equisync/docs/images/lh-index.png) | <mark>PASS<mark> |
| Dashboard |![home](/equisync/docs/images/lh-dashboard.png) | <mark>PASS<mark> |
| Horse List |![home](/equisync/docs/images/lh-horses.png) | <mark>PASS<mark> |
| Horse Profiles |![home](/equisync/docs/images/lh-horses2.png) | <mark>PASS<mark> |
| Exercise Schedule |![home](/equisync/docs/images/lh-exercise.png) | <mark>PASS<mark> 
| Horse Exercise Schedule |![home](/equisync/docs/images/lh-exercise2.png) | <mark>PASS<mark> |
| Feeding |![home](/equisync/docs/images/lh-feeding.png) | <mark>PASS<mark> |
| Feeding Profile |![home](/equisync/docs/images/lh-feeding.png) | <mark>PASS<mark> |
| Competition |![home](/equisync/docs/images/lh-comps.png) | <mark>PASS<mark> |
| Competition Details |![home](/equisync/docs/images/lh-comps2.png) | <mark>PASS<mark> |
| Commmunity |![home](/equisync/docs/images/lh-comm.png) | <mark>PASS<mark> |


## Manual Testing

### ✅ Landing Page

| Section     | Test Action                                                                 | Expected Result                                                                 | Pass/Fail |
|-------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------|-----------|
| Intro Modal | Reload landing page, click enter, click X                                   | Modal displays correctly and closes on push of either button                    | PASS      |
| Carousel    | Slides display and change slowly, navigation arrows and indicator buttons work | Carousel changes and navigation works                                           | PASS      |
| Register    | Register a new account                                                      | User is able to register account                                                | PASS      |
| Register    | Register an account with an already used User name                          | User is directed to enter a different user name                                 | PASS      |
| Login       | Log into site and see updated user navbar                                   | Navbar displays login, redirects to dashboard, updates navbar links            | PASS      |
| Logout      | Log out user                                                                | User is successfully logged out                                                 | PASS      |

---

### ✅ User Dashboard

| Section               | Test Action                                                       | Expected Result                                                                 | Pass/Fail |
|-----------------------|--------------------------------------------------------------------|----------------------------------------------------------------------------------|-----------|
| Sidebar               | Navigate to section via sidebar links                             | Page advances to chosen section                                                 | PASS      |
| Sidebar               | User's name is displayed at top                                   | User name displays on top                                                       | PASS      |
| Sidebar               | Retracts at screen sizes < 769px                                  | Sidebar retracts to navbar                                                      | PASS      |
| Your Horses           | Registered horses display                                         | User's horses appear in container                                               | PASS      |
| Your Horses           | User with no horses invited to create profile                     | Link to register a horse appears                                                | PASS      |
| Notifications         | Notifications display with update options                         | Relevant notifications display with buttons                                     | PASS      |
| Appointments          | Scheduled appointments should display                             | Appointments display                                                            | PASS      |
| Feeding Schedule      | Horse feeding chart should link                                   | Registered horse feeding charts display                                         | PASS      |
| Exercise Schedule     | All registered exercise should display                            | Horse exercise schedules display correctly                                      | PASS      |
| Favorited Events      | Favorited events should display                                   | Events display in order                                                         | PASS      |
| Competition Results   | Horse's results should display + edit buttons                     | Results show from newest to oldest with edit/add buttons                        | PASS      |
| Ads & Announcements   | Created ads and announcements should list                         | User's content is listed in dashboard                                           | PASS      |

---

### ✅ Horses

| Section         | Test Action                                                              | Expected Result                                                                 | Pass/Fail |
|-----------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------------|-----------|
| Profile List    | All horse profiles should be listed with clickable names                | Profiles are listed and links lead to correct pages                             | PASS      |
| Add Horse       | User can add horse profile                                               | Horse form works, admin receives approval notification                          | PASS      |
| Horse Profile   | Profile should link to relevant sections or prompt to register horse     | Links and messages appear as intended                                           | PASS      |

---

### ✅ Feeding

| Section            | Test Action                                                            | Expected Result                                                                 | Pass/Fail |
|--------------------|------------------------------------------------------------------------|----------------------------------------------------------------------------------|-----------|
| Feeding Overview   | Table loads all feeding plans with profile links                       | Feeding plans load and links work                                               | PASS      |
| Feeding Profile    | User may view/edit their horse's feeding plan                          | Feeding plan editable and viewable                                              | PASS      |

---

### ✅ Competitions

| Section            | Test Action                                                            | Expected Result                                                                 | Pass/Fail |
|--------------------|------------------------------------------------------------------------|----------------------------------------------------------------------------------|-----------|
| Calendar           | Viewable by month, week, or day                                        | Radio buttons toggle calendar view                                              | PASS      |
| Favoriting Events  | User may favorite a competition                                        | Favorite added and shown on dashboard                                           | PASS      |
| Events             | Add, edit, and view events                                             | Events managed through interface                                                | PASS      |
| Event Details      | Open details when clicked                                              | Details page loads                                                              | PASS      |
| Adding a Horse     | Add a horse and class details to event                                 | Form opens and saves data                                                       | PASS      |
| Horse Results      | Update results for horse                                               | Form works and updates display                                                  | PASS      |

---

### ✅ Community

| Section               | Test Action                                                         | Expected Result                                                                 | Pass/Fail |
|------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------------------|-----------|
| Sales Ads              | Ads display with pagination/comments                               | Pagination and comments render correctly                                        | PASS      |
| Ad Modals              | Click "View Details" to open ad modal                              | Modal opens and displays correct ad data                                        | PASS      |
| Post/Edit Ads          | User can post and edit ads                                          | Ads saved and shown in dashboard                                                | PASS      |
| Announcements Expand   | Click "Read More" to expand announcement                           | Collapsible content displays/retracts                                           | PASS      |
| Post/Edit Announcements| Post and edit forms work as intended                               | Form submits correctly and content updates                                      | PASS      |
| Announcement Emojis    | Emojis show active state and update Most Reacted                   | Background turns purple, console logs clicks, top emoji updates                 | PASS      |
| This Week’s Events     | Use dropdown or buttons to navigate weekly events                  | Weekly calendar updates accordingly                                             | PASS      |
| Post/Edit Events       | Post or edit event to display on calendar                          | Forms work and changes reflected                                                | PASS      |
| Delete Events          | Delete own events                                                   | Button works for user’s own content                                             | PASS      |

### ✅ Exercise

| Section                  | Test Action                                                                 | Expected Result                                                                 | Pass/Fail |
|--------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------|-----------|
| Exercise Calendar        | User can select a week using the dropdown                                  | The correct week displays on the calendar                                       | PASS      |
| Adding Exercise          | User can update their horse's exercise schedule                            | Clicking "Add Exercise" opens the form and it submits correctly                 | PASS      |
| Adding Appointments      | User can update their horse's appointment schedule                         | Clicking "Add Appointment" opens the correct, working form                      | PASS      |
| Calendar Modals          | User clicks green icon to view horse's daily schedule                      | Modal opens showing exercise and appointments for that day                     | PASS      |
| Individual Horse Exercise| User clicks horse's name to view individual chart                          | Page loads changeable chart and exercise data for selected horse               | PASS      |

## User Story Testing

| User Story | Result |
| --- | --- |
| As a developer I want to organize my project with milestones and a Kanban board of issues | Pass |
| As a developer I want to create user stories for different user roles | Pass |
| As a developer I want to design a database schema for my project | Pass |
| As a developer I want to create wireframes for the application | Pass |
| As a developer I want to create a README file with documentation | Pass |
| As a developer I want to set up a Django project | Pass |
| As a developer I want to create and configure a database | Pass |
| As a developer I want to deploy the app early and often | Pass |
| As a site user I want to register an account | Pass |
| As a site user I want to log in and log out of my account | Pass |
| As a site user I want to have a profile created after registration | Pass |
| As a visitor I want to learn about the stable, its owner, and its horses | Pass |
| As a visitor I want to view the calendar of upcoming horseshows | Pass |
| As a visitor I want to view the stable's previous events and search by name or date | Pass |
| As a visitor I want to view the stable community page | Pass |
| As a visitor I want a responsive site design across all devices | Pass |
| As the Barn Manager I want full access while others have role-based access | Pass |
| As the Barn Manager I want a simple data collection system for horse care | Pass |
| As the Barn Manager I want to view each horse's exercise schedule in detail and overviews | Pass |
| As the Barn Manager I want approval rights over community posts | Pass |
| As the Barn Manager I want each horse to have a stored profile | Pass |
| As the Barn Manager I want a show schedule for all horses and individuals | Pass |
| As the Barn Manager I want a calendar for show schedules | Pass |
| As the Barn Manager I want horse schedules manageable by all roles | Pass |
| As the Barn Manager I want to see the full week's schedule for all horses | Pass |
| As the Barn Manager I want feeding schedules stored and visible to all | Pass |
| As the Barn Manager I want to update and group feeding schedules | Pass |
| As an owner I want a community page to view and create posts | Pass |
| As an owner I want clear displays of my horse's routines and schedules | Pass |
| As an owner I want to receive schedule updates by email or sms | Pass |
| As an owner I want weekly/monthly calendar views for competitions | Pass |
| As a rider I want to track performance and stay consistent with horse routines | Pass |
| As a rider I want to interact and trade on the community page | Pass |
| As a staff member I want shared storage of routines to avoid confusion | Pass |
| As a staff member I want a record of my care activities | Pass |
| As a staff member I want to engage and trade on the community page | Pass |
