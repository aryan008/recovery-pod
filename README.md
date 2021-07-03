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
