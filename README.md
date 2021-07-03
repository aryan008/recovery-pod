<h1 align = "center">Recovery Pod</h1>

View the live project at the following [link]()

![See how the site looks across the devices]()

We are seeing a massive rise in Athlete’s understanding of how recovery plays an impact in areas such as performance, mood regulation and general wellbeing. Applications such as Whoop, Output Sports and Apex Athlete Series have done phenomenally well in the last number of years in areas such as sleep monitoring, load measuring and performance-based metrics. However, the true use of these sites is often stuck behind a massive paywall and require expensive equipment. 

Although most people that are involved in sports performance often view their recovery as “Am I sore?”, this is only one of the key metrics that have been proven to factor into the recovery equation. Hydration, Sleep, Nutrition, etc. play a huge role in determining an Athlete’s readiness and often willingness to train and are often overlooked by the non-elite.

In response to this, I wanted to create a site that allows the user to figure out “How recovered am I today?” through a form submission with multiple questions, allowing them to visually see their recovery score. They can therefore login every day, fill in this form and plan their training accordingly based on how recovered they are.

The aim of this site is to allow the user of the site to calculate their recovery score. Users will experience:
*	a welcome/about page where the user can create an account/login and view the metrics that the site determines for their score
*	Full CRUD (Create/Read/Update/Delete) functionality
*	a delete account feature
*	password reset feature
*	View external sources of information of the attributes measured
*	Submission of a form which will calculate the user recovery score based on answers to their questions
*	A managing of their profile, which will include their score for the today, as well as an “edit/delete” entry if any mistake on their entry was made 
*	A log out section
*	View the entries of everyone that has an account, including a search bar that users can see all the scores of an entered username
*	A green/yellow/red recovery colouring scheme that allows high-impact colouring across the site

The site is designed to be responsive and accessible across all device sizes, as defined in the testing section of this ReadMe file.
The site is also designed to handle the full suite of user management, as defined in the Information architecture of this ReadMe file.


## Table of Contents
* [Site Owner and Product/Business Goals](#site-owner-and-productbusiness-goals)
* [Developer goals](#developer-goals)
* [First Time Visitor Goals](#first-time-visitor-goals)
* [Returning and Frequent Visitor Goals](#returning-and-frequent-visitor-goals)
* [Attributes measured and their importance](#basic-rules)
* [User Experience (UX)](#user-experience-ux)
  * *The 5 planes of User Experience – Decisions and Reasons*
   1.	[Strategy plane](#strategy-plane)
   2.	[Scope plane](#scope-plane)
   3.	[Structure plane](#structure-plane)
   4.	[Skeleton plane](#skeleton-plane)
   5.	[Surface plane](#surface-plane)
   
  *	[Who/ What/ How](#who-what-how)
  *	[User stories](#user-stories)

* [Design Features](#design-features)
  1.  [Wireframes](#wireframes)
  2.	[Typography](#typography)
  3.	[Colour scheme](#colour-scheme)
  4.	[Imagery](#imagery)
  5.	[Visual Hierarchy](#visual-hierarchy)
  6.	[Features implemented](#features-implemented)
  7.	[Features left to implement](#features-left-to-implement)

* [Design & UX – How do they come together?](#design--ux--how-do-they-come-together)
  * [User goals](#user-goals)
  * [Site owner goals](#site-owner-goals)
  * [Designer goals](#designer-goals)

* [Information Architecture?](#information-architecture)
  * [Sections](#sections)
  * How CSS created an experience
  *	How JS created an experience
  *	How Python created an experience
  *	Site Logic and diagram
  *	User Types and permissions
  *	CRUD Functionality
  *	Mongo DB Database Structure
  *	Metric scoring
  *	Python logic - Brief

* [Technology and Languages used](#technology-and-languages-used)
  *	[Languages](#languages)
  *	[Frameworks, Libraries and Programmes](#frameworks-libraries-and-programmes)

* [Testing](#testing)
  * [Code validation](#code-validation)
  * [Accessibility testing](#accessibility-testing)
  * [Responsive testing](#responsive-testing)
  * [Manual testing](#manual-testing)
  * [Further testing](#further-testing)
  * [Testing user stories from User Experience (UX) section](#testing-user-stories-from-user-experience-ux-section)
  * [Known bugs](#known-bugs)

* [Deployment](#deployment)
  * [Process of deployment](#process-of-deployment)
  * [How to run this project locally](#how-to-run-this-project-locally)

* [Credits](#credits)
  * [Content](#content)
  * [Media](#media)
  * [Code](#code)
  * [Acknowledgements](#acknowledgements)

## Site Owner and Product/Business Goals
As the site owner, the website is to act as a hub for all athletes/users who create an account, allowing them to:
*	Create an account/login with a password reset/delete account feature
*	Have a welcome page where the users can view the attributes measured as well as insights as to what they can experience when they create an account
*	In the welcome page (where the user has not yet created an account), redirect buttons to prompt the user to create an account
*	View in more detail the attributes measured along with “importance” narrative, referencing an external link which the user can click on to read further details of the attribute importance
*	View all entries of other athlete’s including the green/yellow/red scoring of such entries. A search bar function to filter by an athlete’s username is also present
*	A log out function
*	A settings function where the user can change their password
*	A “new entry” feature where the site user can input today’s recovery score via a form asking questions across the attributes measured
*	A “manage profile” function where the user can: see today’s score with appropriate large colouring; edit/delete entry; see the narrative of their score; delete their account if they wish


The site is to achieve the following goals:
1.	The site is presented in an efficient and authentic way so that the users can quickly create an account and log their recovery score
2.	The information on the site is displayed clearly and contain all the information necessary for the user to understand the purpose of the site and how their recovery score is calculated
3.	Provide feedback to the users using colouring of green/yellow/red on today’s recovery score
4.	Is responsive on all device sizes
5.	Utilize Python/JavaScript to allow seamless user transition throughout the site and their profile
6.	Creates a positive experience for the user using colour, imagery and layout
7.	Become a hub for athletes to utilize in determining their recovery metrics
8.	To display the content in a culturally appropriate attested to the audience it is aimed at


## Developer goals
As the developer, the site is to achieve the following goals:
1.	Mar the goals of the site owner and user together
2.	Create a positive experience for both parties using the specifications required by both parties
3.	Achieve responsive design across all devices
4.	Utilize the combination of HTML, CSS, JavaScript and Python to enhance the experience of the user and site owner
5.	Become a hub for athletes to utilize in determining their recovery metrics
6.	Allow “administrator” access to manage user profiles in full


## First-Time Visitor Goals
As a first-time visitor of the site, I want:

1.	My impression of the site to be a positive experience
2.	To understand the main purpose of the site
3.	To provide relevant content related to athlete recovery and the main metrics of score calculation
4.	A clear and unambiguous layout, including a clear recovery score after my form submission
5.	CRUD functionality upon account/entry creation
6.	A quick “create account” feature on landing on the site
7.	An instant feedback loop from form submission to the recovery score of the day
8.	Easy navigation of the site
9.	Built-in safety protocols – single entries, user authentication, appropriate redirects
10.	The ability to edit/delete my entry for the day
11.	The ability to delete my account
12.	To view the recovery score of the day to clearly see how recovered I am
13.	The colours, layout and feel of the site to be of an athlete nature as part of cultural appropriation


## Returning and Frequent Visitor Goals
1.	CRUD functionality on my profile
2.	To explore the more information on the attributes that are measured


## Attributes measured and their importance
The following are the attributes measured by the site:
1.	Cold therapy
2.	Nutrition
3.	Training
4.	Sleep
5.	Stretch
6.	SMR (Self myofascial release)
7.	Feeling
8.	Hydration

The above attributes are present in a “columned” format on the home page of the site, allowing site visitors to see them as the metrics very quickly. On the about page of the site, each of these attributes are broken down further which allow the site user to quickly see narrative of their importance, including a link for further information should the user wish to read more.
From my background in strength & conditioning, these attributes (whilst they are not the exhaustive full list) represent the key list of measurements that many of the top athlete’s around the world measure daily in terms of their recovery. For further information on how the calculation is performed, please see the Information architecture -> Metric scoring section of this ReadMe file.

## User Experience (UX)
### _The 5 planes of User Experience – Decisions and Reasons_
#### Strategy Plane

Question |	Response for site design
-------- | ---------
Is the content culturally appropriate? |	Design will be simplistic in terms of UX and is based on leading athlete load monitoring sites– Dark background and light “pop” information that allow athlete’s to visually see scoring very quickly
Is the content relevant? |	Acting as an athlete hub, only relevant “Recovery” content will be displayed
Can we provide content in an intuitive way? |	The site will have a series of prompts/redirects/buttons and, using Python and JavaScript, will feel interactive to the site user
Is the technology appropriate? |	Since Recovery Pod is essentially a rules-based scoring system with CRUD functionality, Python is the primary source of technology for the site back-end. A combination of CSS and JavaScript will be used for applicable user experience on the front-end
Who is my target audience? |	Athlete’s/general fitness enthusiasts who want to see how recovered they are
Product considerations |	No overload of content/imagery on the site as per appropriation. Recovery Pod is a database-driven CRUD site and hence the content should reflect that. Clear feedback loops from user account creation/CRUD usage/entry creation must be present. Navigation/layout must be easy across all devices for the users

##### Strategy feasibility scoping
Opportunity |	Importance |	Feasibility
-------- | --------- | -----------
Ability to see all entries and search by username | 4 | 5
CRUD functionality on user entry for the day | 5 | 5
Seamlessly move the page when the user “clicks” the button | 5 | 5
Feedback loops on CRUD Functionality | 5 | 5
Feedback loops on form submission | 5 | 5
Daily email reminder to submit an entry | 4 | 2
Instructions on how create an account | 4 | 5
Attributes importance and their sources | 4 | 4
Further inputs for the user to manage – heart rate/ HRV | 3 | 2
Password changing | 5 | 5
Machine learning on user submission – e.g. when you do X, your recovery moves +/-% | 3 | 1
Delete account | 5 | 5
Weekly/monthly recovery score charts/suggestions | 4 | 2
Administrator functionality to manage user profiles | 5 | 5
Pagination on all entries | 3 | 2
User error handling – 404/500 errors, entry duplication safety measures, appropriate redirects on user interaction | 5 | 5

#### Scope Plane
What's in? |	What's out?
-------- | ---------
Ability to see all entries and search by username | Further inputs for the user to manage – heart rate/ HRV
CRUD functionality on user entry for the day | Machine learning on user submission – e.g. when you do X, your recovery moves +/-%
Seamlessly move the page when the user “clicks” the button | Weekly/monthly recovery score charts/suggestions
Feedback loops on CRUD usage | Daily email reminder to submit an entry
Feedback loops on CRUD Functionality | Pagination on all entries
Feedback loops on form submission | Forgot password email reset
Instructions on how create an account
Attributes importance and their sources
Password changing
Delete account
Administrator functionality to manage user profiles
User error handling – 404/500 errors, entry duplication safety measures, appropriate redirects on user interaction

#### Structure Plane
Question |	Response for site design
-------- | ---------
How do I navigate easily? | Navbar is present across all site pages and is fixed to the top. Pages present on the navbar will depend on the following: Unregistered user - On the home page, prompt to create an account/login. The about page is present regardless of user status. Registered user – As above but including navbar links for All entries/ manage profile of the user/ New entry, Log out and User settings page. Administrator – As above but including a navbar link for managing profiles present on the site. Throughout, buttons are present on the appropriate areas to allow the user to bring them to the features they wish to implement on the site.
How is the information presented? | Using athlete style colours/features and text content that allow the user to achieve their goals. Dark background to light interface for a clear separation of colours to the users and their related scores. Clear feedback on the result of form submission and their score for today. Flash feature from Python utilised whenever the user performs CRUD functionality. The buttons through the site pop to the user, clearly demonstrating what will happen should they click on them.
State changes | There is a clear state change at the navbar level depending on the user of the site as previously mentioned – no account, registered user, administrator. Appropriate redirects are present when the user interacts with both the navbar and the buttons of the site, including “reset” after a user searches for a username in the “All entries” page. On form submission, a clear state change redirects the user back to their profile which allows them to see their recovery score for the form they just submitted. Finally, state changes are present on all CRUD function buttons when the user interacts with them along with the Flash messages, tying in with the feedback loop that the user action was performed successfully.
Is the site consistent? | Correct styling and fonts are applied throughout the site, which was achieved using the Jinja templating language feature through Python and HTML. Colouring on the user score for the day and the “all entries” score is consistent between pages.
Is the site predictable? | All navigation is familiar to the user in terms of font/styling consistency.
Is the site appropriately visible? | See the testing/visual hierarchy section of this ReadMe file for visibility testing.
How does the user know to scroll/what to do? | The steps between a “First time visitor” and “First Recovery Score Entry” are adequately displayed and clear for the user.
How does the user if they are recovered? | Upon the day’s form submission, Python will correctly calculate the user’s score based on the form entry selections that they made. This instantaneous recalculation redirects the user back to their profile where their score and appropriate narrative is displayed. The user score, along with the afore mentioned green/yellow/red colouring pattern, displays in a giant circle on their profile. This size/colour emphasis upon form submission is a key feature to the user on whether they are recovered. Please see the Information architecture -> Metric scoring section of this ReadMe file for further information on this.
What if a user makes a mistake on their entry? What if they try to submit twice on the one day? | CRUD functionality is present on the user’s entry that they made for today – if the user wants to edit/delete the entry they just made, buttons are present for the user to perform this action. Note that an “onlick” event occurs to confirm this choice. If the user tries to input another entry, Python logic will determine that “today’s” entry has already been made along with an immediate redirect to the user profile and a flash message. This will prompt the user that the only way to create an entry is either delete the existing one or edit it. Further, if the user tries to edit an entry and has second thoughts – a cancellation button on the edit is presented and the original entry is valid.
How will the user know if they have an entry for today? | When the user views the profile and they have not made an entry for today, a message displays indicating that the user should make today’s entry.
User error – what if it happens? | Providing information to the user if this happens, and how to safely navigate back to the home page.
Information architecture | Using the tree structure with no more than 3 clicks for the user to reach a destination.

#### Skeleton Plane
Question |	Response for site design
-------- | ---------
How will the users get around? | Easy navigation for the user depending on their “status” as mentioned in the structure plane. Using call to action buttons/flash messages along with CRUD functionality that display the correct route the user should take depending on their chosen action.
How will I present the content? | Following industry norms of the header -> content -> footer approach across all pages. Jinja templating allows consistent site content to be present in this regard.
How do I show relevant content? | By making the content audience appropriate as defined by the site user goals. By using representational material/attributes which the user is expects with from previously managing their personal recovery.
How do I make the experience a positive one? | Through listening to the user goals, the content on the webpage is to provide appropriate recovery information for athletes each day that they log in. The use of Jinja templating/Python functionality displays consistent information and styling through the site, with appropriate messages/prompts to the user to “See how recovered you are”. The form submission the user completes daily is simple and consistent, allowing the user to see the metrics the site uses and how they can improve their recovery score over time. The cursor pointer and various text effects will be involved in producing a further positive response from the user. The state changes noted in the structure plane also discuss effects on the result of CRUD uses by the site user.
How do I structure the features and usability? | Non-registered account: Home/About/Login/Create account navbar links and prompt buttons on the home page. Registered user: View all entries,	Submit my own entry,	View my recovery score,	Manage/Edit today’s entry,	Delete account,	Password resetting

#### Surface Plane
Question |	Response for site design
-------- | ---------
What is the visual language? |	Jinja templating as noted above. Colouring as per testing norms, layout is informative, Fonts as per media display standard, images/recovery scores are clear and pop to the user, CTA buttons for site progression, JavaScript for score colouring and “active” page on site.
What is the economy? |	The most important user/owner elements are easily recognised
Readability and consistency |	Each site page is familiar to the user in terms of font/styling consistency

### _Who/ What/ How_
**Who is it for?** Users who want to understand metrics of athlete recovery, see their own recovery scores through form submission and improve their scores over time

**What is it for?** Users who want to recover correctly each day

**How will it achieve this?** Through creating a Recovery Pod site, and through Python/JavaScript/CSS/HTML, allow the user to log their recovery scores and see how recovered they are for the day

### _User Stories_
Performance is dictated by readiness, and this readiness can be boosted by taking the correct measures throughout the day.

Hence, I want a site where I can:
1.	Create my own personal account for the Recovery Pod.
2.	Learn about the attributes of recovery
3.	Navigate easily
4.	See if I’m recovered or not
5.	See other user’s recovery scores
6.	Perform CRUD functionality on my entry for the day
7.	Change my password/delete my account
8.	Login/Logout

#### Wireframes
* Desktop/tablet wireframe - [attached](assets/rm_files/wireframe-desktop.pdf)
* Mobile wireframe - [attached](assets/rm_files/wireframe-mobile.pdf)

#### Typography
Lato is used as the main font on the site, as imported through Google Fonts. Sans-serif is used as the fallback font. According to an article on [perpetual media group](http://www.perpetualmediagroup.ca/tenbestfontsforprintandweb/):
_“The semi-rounded details of the letters give Lato a feeling of warmth, while the strong structure provides stability and seriousness.”_

Further, in this [blog post](https://www.justinmind.com/blog/best-google-web-fonts-website/), Lato is ranked as #1 on the “30 best Google Fonts for your website”. It is known that the designer of this font, Lukasz Dziedzic, _“created Lato to work transparently in body text and also to stand out individually when used in larger-sized titles”_.
With these descriptions in mind, Lato is used for the site design/accompanying text.

#### Colour Scheme
The main colours used on the site are a shade of black and white:
* Background: rgb(46, 45, 45) (grey/black)
* Text colour: rgb(255,255,255) (white)
The reason for this is to achieve a “pop” effect on the icons and text presented, making them appeal more to the screen reader. 

According to [designwebkit](https://designwebkit.com/design/gaming-website-templates-professional-tips-build-game-website/#:~:text=As%20you%20may%20notice%2C%20most,brown%2C%20grey%2C%20and%20khaki.):

_“Most popular websites use dark colour scheme for their websites to create a mystic and engaging ambiance. The most popular colours for such websites are black, brown, grey, and khaki”._

Further colourings used on the site:

Footer links:
* Twitter - rgb(6, 179, 209)
* Facebook - rgb(33, 83, 190)
* Github - rgb(228, 6, 6)

Recovery scores:
* Recovered - rgb(15, 145, 15) (Green)
* Moderate- rgb(216, 216, 39) (Yellow)
* Low - rgb(190, 16, 16) (Red)

Box shadows: rgba(100, 100, 100, 0.877)

Home page circle/ Font awesome icon colouring:
* Cold therapy – rgb(84, 194, 245)
* Stretch – rgb(243, 186, 0)
* Nutrition - rgb(88, 224, 106)
* SMR – rgb(233, 132, 107)
* Training – rgb(255, 244, 93)
* Feeling – rgb(161, 255, 93)
* Sleep – rgb(230, 137, 253)
* Hydration - rgb(0, 166, 243)

#### Imagery
On the home page, a “columned” effect is added to show the attributes names which are measured on the site.
Font Awesome is used to display emoticons on the about page, as well as circle images of each attribute as they are listed.
For the “all entries” page, the green/yellow/red recovery scores are present for each individual user. Similarly, with the user’s entry for the day, the same colouring scheme is applied but on the outside circle which is visually big for user readability and design.
See the credits section of this ReadMe file for all appropriate accreditation of the imagery used.

#### Visual Hierarchy
According to the following article on [Visual Hierarchy](https://www.interaction-design.org/literature/topics/visual-hierarchy):

“Visual hierarchy controls the delivery of the experience. If you have a hard time figuring out where to look on a page, it’s more than likely that its layout is missing a clear visual hierarchy.”

The following characteristics per the article are manipulated (__article narrative in bold__, _developer response in italic_):
* __Size – Users notice larger elements more easily.__ _The CTA buttons to the user are larger than the text elements for the user to visually see where to interact. The recovery score on the manage profile page takes up much of the screen which allows the user to see their result clearly and unambiguously. The “all entries” scores are coordinated to be slightly larger than the text presented in the table._
* __Colour – Bright colours typically attract more attention than muted ones.__ _The contrast between the dark background and bright text attracts the user the read the text more visibly. Colour classes are added at the score level to visibly display to the user whether they are well recovered, moderately recovered or low recovered. See the testing section of this file for contrast testing._
* __Contrast – Dramatically contrasted colours are more eye-catching.__ _As noted above._
* __Repetition – Repeating styles can suggest content is related.__ _The style is repetitive – information for the user follows the same pattern for each page through the use of Jinja templating._
*	__Proximity – Closely placed elements seem related.__ _Content is grouped based on spacing for user readability sectioning. The grouping of the form choices is close as these are the options for user submission, before making way to the singular “Post entry” button. The “Edit entry”/”Delete entry” are grouped beside the user score once they post their form entry, suggesting to the user that these buttons interact with the form they just submitted._
*	__Whitespace – More space around elements draws the eye towards them.__ _Spacing is used effectively according to the hub needs of the product goals._
*	__Texture and Style – Richer textures stand out over flat ones.__ _As noted in the typography section._

#### Features implemented
##### Home Page
*	The site landing/welcoming page welcomes the user to the Recovery Pod, demonstrating that athlete recovery is the outcome of the site
*	The navigation displays a “call to action” for the user to click to create an account/login if they haven’t previously. There is a clear state change through a page redirect when one of these buttons is clicked
*	The attributes that are measured are presented visually through a “wheel effect” and coloured appropriately to pop to the user
*	The page also displays what the site aims to achieve for the user

##### About Page
*	For each attribute, the attribute is named, a coloured font awesome icon is displayed as well as narrative surrounding its choice as an attribute
*	An external link is present for the user to click on to read more about the choice and importance of the attribute

##### Login/Create Account page
*	The user can create an account through a username and password. A prompt is displayed to the user for the password and that the password must be a certain criterion for the password to be accepted to the database – 5 to 15 characters containing only letters and numbers. A user error occurs if the password is not in the requested format.
*	Similarly, the username must be unique for the account to be created and a flash message will appear to the user if that username has already been taken
*	On the login side, the username and password must match the account created details for the user to be logged in. If either do not match, the flash message that appears to the user is that “Either the username or password” do not match in order to prevent brute force entry to the site.

##### Logout/Settings page
*	On clicking the logout page, the user is logged out of the site and redirected to the login page. The navbar displays the original “non-user” navbar links at the top
*	On the settings page, the user can reset their password. Again, the new user password must match the requested format, with a similar error message if this does not correctly happen. 

##### All entries page
*	Once a user is logged in, they can see all the entries created on the site
*	A search bar here allows the user to search by username, along with a reset button to clear the “searched” username and show all entries yet again

##### New entry page
*	If the user does not have an entry for today, they are prompted to select today’s date and fill out the dropdowns for each attribute
*	A comments section provided at the bottom of the form allow the user to post any comments they feel like inputting for the day – e.g. must make more of an effort to stretch after my gym session
*	Upon form submission, the user is redirected back to their profile to view their score for the day

##### Manage profile page
*	After the entry, the resulting score is presented to the user in a coloured circle that is visually large to zone in on their recovery score along with related green/yellow/red colouring
*	Present in this circle are the “Edit entry”/” Delete entry” buttons, allowing the user to perform these actions
*	A narrative is present under the score to tell the user how well recovered they are
*	If the user tries to click on the “New Entry” link in the navbar after todays submission was made, the user is immediately redirected back to the manage profile page and a flash message pops up indicating that today’s entry was already made. This reinforces that should the user want to change this entry; they must do so in the afore mentioned buttons in the circle containing todays score
*	If no entry has been made by the user today, obviously the circle containing the score will not be present on the user’s profile, and they are prompted to go to the new entry link in the navbar to create todays entry
*	Just above the footer at the bottom of the page, the user has the option to entirely delete their account. This will remove their username/password from the database along with all the entries they have ever made on the site. Note that an “onclick” event listener occurs for the user to confirm this action before deletion.
Manage users page (Admin only)
*	Once the administrator is logged in, the navbar will update to allow the administrator to view all profiles on the site
*	Should the admin wish to delete, a “delete user” button beside the username will permanently delete that user from the database, including all their previous entries. Note that an “onclick” event listener occurs for the user to confirm this action before deletion.
*	A search bar at the top will allow the admin to search for a user, similar to the “all entries” page with the search function previously mentioned.

##### Colours & Fonts
*	Background colour is set using a dark style as noted in the colour section, displaying a gamified approach feel to the user
*	Font colour is set in contrast to the background. This gives the effect of user-friendly-readability and gives the “pop” sensation of text overlapping the dark background
*	Lato is used as the playful text of choice for the site, providing a sense of warmth to the user, while the strong structure provides stability and seriousness.
*	The recovery green/yellow/red recovery scores throughout the site adhere to human nature – green is good, yellow is moderate, and red is bad

##### Layout
*	The site’s page is structured visually (font/colouring/areas/form) consistently throughout after each navigation choice by the user, creating a common theme for the site along with Jinja templating. The hierarchy presented tells the user extremely quickly where to look on a page, where to click and how to navigate their profile.

#### Features left to implement
*	Further inputs for the user to manage – heart rate/ HRV
*	Machine learning on user submission – e.g. when you do X, your recovery moves +/-%
*	Forgot your password? Reset feature
*	Weekly/monthly recovery score charts/suggestions
*	Daily email reminder to submit an entry
*	Pagination on all entries and manage users page

## Design & UX – How do they come together?

### User goals

User Goal | Feature(s)/ Content in response | Goal Met?
-------- | --------- | --------
(1)|	Colour/Font/Layout/Scoring structure. Responsive button elements and appropriate redirects/CRUD messages. Clear call to action on user progression from site landing to entry submission.|	Yes
(2)|	Displayed on the landing “home” page|	Yes
(3)|	Content on the “home”/ “about” page related to user recovery and appropriate narration. Main attributes and their importance listed on both pages|	Yes
(4)|	Colour/Font/Layout/Scoring structure. On form submission for the day, redirect to user profile and large circle showing today’s result with appropriate colouring scheme.|	Yes
(5)|	Users can create an entry, edit their entry, delete their entry, read their entry. Delete account/ password edit feature also available.|	Yes
(6)|	Site landing page has (once user not logged in) buttons to redirect to login/ create an account|	Yes
(7)|	Flash message present that todays entry has been made after form submission followed by an immediate redirect to user profile to view their score.|	Yes
(8)|	Navbar present at the top of each page. Use of JavaScript to apply an “active” class to show the user what page they’re on. Registered/logged in users see the full suite of pages available on the site. 404 and 500 error handing applied for any issues with the site where the user is redirected back to the site should these errors occur. User submission navigation prompts are present whether the user has/ has not submitted today’s score.|	Yes
(9)|	User authentication used on login/ create an account where the username is checked for a username of that name in the database. Passwords must match a specified format. Flash error messages are displayed on both points above if either show as an error. Double entry attempts by the user on the same day are prevented via a redirect back to today’s score and profile, prompting the user to use the designated buttons to interact with their entry.|	Yes
(10)|	As part of CRUD functionality and noted above, this is present|	Yes
(11)|	Account deletion is present on the user’s profile page through a button|	Yes
(12)|	Available on the user’s profile page should a submission be made on the day. If the user has yet to make an entry, narrative appears on the profile page that they have not made today’s entry yet and should make that entry now.|	Yes
(13)|	Noted as part of the visual hierarchy section above.|	Yes

### Site owner goals

User Goal | Feature(s)/ Content in response | Goal Met?
-------- | --------- | --------
(a)|	Clear call to action on user progression from site landing to entry submission, indicative through display of CTA buttons on the landing “home” page|	Yes
(b)|	Attributes and their measurement/importance noted in both the home and about page|	Yes
(c)|	Utilizing JavaScript to apply green/yellow/red colourings on both the user’s personal score for the day and all the entries made on the site.|	Yes
(d)|	Responsive design build using media queries in CSS. Tested as part of testing section below.|	Yes
(e)|	Utilizing of Flask/Jinja/JQuery and appropriate redirects for site progression. See the Information Architecture section below for further details|	Yes
(f)|	Clear contrast effect between background & foreground text/images, including score colouring application as noted in the outset|	Yes
(g)|	Allows users to see all athlete entries ever made and pit their scores against others|	Yes
(h)|	As above point (f)|	Yes

### Designer goals

User Goal | Feature(s)/ Content in response | Goal Met?
-------- | --------- | --------
(1)|	Noted above.|	Yes
(2)|	Noted above.|	Yes
(3)|	Noted above.|	Yes
(4)|	Noted above – JavaScript/Python features noted below.|	Yes
(5)|	Noted above.|	Yes
(6)|	Administrator access to manage profiles on the database present on admin login. A safety feature is added to not show the “delete account” button to the admin, in case they accidentally delete their account.|	Yes

## Information architecture

### How CSS created an experience
#### Responsive styling

CSS and media queries were used in the style.css file to make a responsive web application for all screen sizes. This has been tested in the testing section below as part of responsive testing. The following media query sizes were used:
*	max-width:1037px
*	max-width:796px
*	max-width:562px
*	max-width:460px
*	max-width:400px

_Note that as part of response testing in the testing section below, the above CSS media rules passed all visual review by the developer._

#### Hover effects
CSS was used to add a cursor pointer to further engage the site user into clicking the buttons presented.

#### Button effects
CSS was used to display buttons accordingly with site users in mind.
*	Blue button – search
*	Red button – reset/delete (with the exception of a site visitor “Create account” button for visual hierarchy purposes)
*	Green button – Log in/Create account/ Post entry/ Edit entry

### How JS created an experience
The JavaScript code created by the site designer is contained within the below JavaScript Code Library files. Note that the key features provided to the user are detailed below where appropriate as an actual feature, not just JS logic.

JavaScript Library – LINK
See the attached [link](testing_results.md) for the screenshot results of JSHint on the below Javascript code. This is also noted in the testing section of this README file.

#### Feature 1 – Active Class
Ensuring that the navbar updates to an underlining “Active” class when the site user/visitor/administrator is on a particular page. This will underline the navbar “page” that the user is on, and when the user changes the page, it will automatically remove the class and reapply to the current window location href.

#### Feature 2 – Recovery score all users
This JS feature will look in all the entries that users have created and apply styling to them depending on their score. If the user’s score is greater than or equal to 70, the class of “recovered” is applied. If the user’s score is greater than or equal to 50, the class of “moderate” is applied. Below this the class of “low” is applied.

#### Feature 3 – Recovery score current entry of user
This JS feature will look at today’s entry submitted by the user and apply styling to the outside circle depending on the score calculated. If the user’s score is greater than or equal to 70, the class of “recovered” is applied. If the user’s score is greater than or equal to 50, the class of “moderate” is applied. Below this the class of “low” is applied.

#### Feature 4 – Password reset check
This JS feature checks that the password reset feature works appropriately. If the new and confirm passwords do not match each other, an error is presented to the user explaining what has happened.

Each individual feature has been fully documented adhering to the following JSDoc framework.

### How Python created an experience
Python, along with the libraries noted below, create an experience for the user.

(1)	Use of Jinja templating language. The use of the Jinja templating language allows the site to become of the same structure and hierarchy. On design, I created a “base.html” page which acts as the springboard for all other pages. Fonts/Structure/Colouring/Navbar all act as a platform which the descendent pages all pull from

(2)	Use of Flash messages. Flash messages are used throughout the site upon user interaction:
-	Profile page name
-	Account creation messages
-	Password change messages
-	Form recovery entry CRUD messages
-	Account deletion messages

(3)	Use of Mongo DB and it’s interaction. As per the Mongo DB Database Structure section below, data is stored and pulled from Mongo DB throughout the site across 4 collections. Indexes are created on two collections in order to allow the users to search by username. Database management is integral to the CRUD functionality of the site and as per the testing section below, all CRUD functionality has been tested with Mongo DB where the appropriate interface is present for the user.

(4)	Display of JSON information. The “about” page displays information on each of the eight attributes, along with further reading, information text, font awesome icons, image sources and alt tags. Python allows this information to be read from the JSON file and present visually to the site visitor/user.

(5)	Security. Python’s Werkzeug library allows the user to create a hashed password on site creation and consequently change their password should they wish.

(6)	Error handing. 404 & 500 error handling templates have been managed and monitored through the site, allowing the user to safely navigate back towards the site should these errors occur

(7)	Score calculation – see the Metric Scoring section below

### Site Logic and diagram
The game logic was developed using Python, Flask, PyMongo, Json, Werkzeug, Heroku, JavaScript and JQuery. Jinja templating language was utilised in the creation of the site.
When a visitor lands on the site, they can read both the home and about page. They also have an option to login or create an account.
Once they have created this account/ logged in, the site navbar allows them to:
*	Create today’s entry
*	View all entries of all users
*	View their profile and recovery score
*	Edit/delete the entry they made today
*	Delete their account
*	Create a new password
*	Log out

If the administrator is logged in, they will have all of the above features but will have a special “Manage Users” section, where they can view all users that use the site and delete their profiles as they wish.

See below for a diagram of the site logic.

### User Types and permissions
There are three types of users that this website is designed for:

#### Visitor
A visitor is anyone who navigates to this website and can see home & about pages. Visitors can view the attributes, their importance, the about page and they can register for an account/login. The page is fully functional for read only access for visitors.

#### User
A visitor who registers for an account automatically becomes a "user". Users have the same rights as visitors, plus they have access to a see all the entries ever created, their own profile, creation of today’s score through a form, change their password and log out. Users have full CRUD functionality on their own entries for today, as well as the ability to delete their account and all entries.

#### Admin
Administrators have all the rights of a user, but they also have the right to manage the profiles of other users. They can delete any user except themselves. This is a security feature so that an administrator doesn't accidentally delete their own account.

### CRUD - Create, Read, Update and Delete
As part of the milestone project, we must demonstrate that our application can perform CRUD operations.

User type | Create |	Read |	Update |	Delete
-------- | --------- | -------- | -------- | --------
Visitor|	No|	Yes|	No|	No|
User|	Yes|	Yes|	Yes|	Yes – own profile/entry
Admin|	Yes|	Yes|	Yes|	Yes – other profiles

As seen in the table above, all CRUD functionality is present in the application, however, CRUD operations are restricted to some user types.

#### Create
Narrative|User|Admin|Visitor
-------- | --------- | -------- | --------
Account creation|Yes|Yes|Yes
Individual entry|Yes|Yes|No
Password change|Yes|Yes|No

#### Read
Narrative|User|Admin|Visitor
-------- | --------- | -------- | --------
Home/About Page|Yes|Yes|Yes
All entries|Yes|Yes|No
User profile|Yes|Yes|No
User score|Yes|Yes|No
Manage users|No|Yes|No

#### Update
Narrative|User|Admin|Visitor
-------- | --------- | -------- | --------
Password|Yes|Yes|No
Individual entry|Yes|Yes|No

#### Delete
Narrative|User|Admin|Visitor
-------- | --------- | -------- | --------
Account|Yes|No|No
Individual entry|Yes|Yes|No
Manage users|No|Yes|No

### Mongo DB Database Structure
The database used for this project is MongoDB. The main database contains four collections.
*	Attributes
*	Entries
*	Recovery
*	Users
Throughout the Python app.py file, various Mongo DB requests are made to get the appropriate information from the database and rendered to their appropriate html pages.

#### Attributes
This collection contains the eight attribute names upon which the site calculates scores on user submission.
As per below, this collection contains the following structure for the eight attributes:
* __id: ObjectId
* attribute_name: String

#### Users
This collection stores the usernames and passwords of all site members who create an account.
As per below, this collection contains the following structure for each user:
* __id: ObjectId
* username: String
* password: String

Note that the password is hashed as using the werkzeug.security --> generate_password_hash/check_password_hash libraries in Python

#### Recovery
This collection contains the eight attribute names/timeframes/narrative and three options for each on the user entry form, upon which the site calculates scores on user submission.
As per below, this collection contains the following structure for the eight attributes:
* __id: ObjectId
* timeframe: String
* attribute_name: String
* narrative: String
* option_one: String
* option_two: String
* option_three: String

#### Entries
This collection stores the entries made by the users on today’s recovery score calculation on form submission.
As per below, this collection contains the following structure for each user submission:
* __id: ObjectId
* Option_choice: Array
* created_by: String
* user_chosen_date: String
* submission_date: String
* comment_text: String
* name: ObjectId
* score: Int32

#### Mongo DB – Search Functionality
In both the “All entries” and “Manage Users” page, an index was created in Mongo DB to facilitate site users to search.

##### Users collection
An index was created on the username, allowing the site administrator to search by Username.

##### Entries collection
An index was created on the created_by, allowing the site users to search by Username.

### Metric Scoring
As noted above, recovery is calculated on a user-by-user basis by a user-submitted form. Python functionality noted in the code itself maintains the “present” status of this form submission – the user should submit the entry for today to see their score. 
*	If the user tries to submit an entry if they have already created one for today, a flash message will appear explaining they have already made an entry and to “edit”/ “delete” this entry if they want
*	If no entry has been made for today, the “new entry” page will show the form to be submitted

On this form to be completed, it begins with a date picker in which the user is asked to select today’s date. Once filled in, the user can view all the narrative/options for each of the eight attributes and importantly their specific options for that attribute. The use of Jinja templating allows the form to be successfully generated by looking through the “recovery” collection in Mongo DB and populating the form. The user can then add any comments here before posting the entry to the Mongo DB entries collection.
Using error handling in Python as documented in the app.py file, a score is then calculated for the user which then redirects them back to their profile and their recovery score for the day.
The makeup of this scoring matrix and calculation basis is through using a python dictionary for each attribute’s option selection and related score, and then totalling them up. Note that the score has been set up to never exceed 100%.

Before delving into the makeup of these dictionaries, it must be mentioned that not all attributes are created equal. As an example, the attribute of sleep is more heavily weighted scoring wise than say feeling. If a user entered a top score on both, they would get scores of 25% and 10% respectively. This “weighting” allows the users to focus on the “big hitters” of recovery and affirms the age-old wisdom of sleep is paramount. See the below following dictionaries for further information:

As part of test #2 in the testing section below, if a user were to select the “best” option for each attribute, they would get a recovery score of 100%. Similarly with test #3, if the user were to select the “worst” options, their score would be 32%.

In terms of the above and the related colourings on the site, test #4 below provides some insight. The colouring schemes on recovery percentage are:
*	Green --> 70%+ --> Fully recovered
*	Yellow --> 50%+ --> Moderately recovered
*	Red --> less than 50% --> Low recovery
This colouring scheme will apply to both the user’s entry for the day and all entries as per that specific page.
Please see the app.py in the code for further information of the form entry and it’s calculation for each user, including KeyError/IndexError checks and edit/delete entries.

