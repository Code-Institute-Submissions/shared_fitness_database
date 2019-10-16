# Shared Fitness Database (Shared Fitness Db)
## Milestone Project Three (Data Centric Development - CI)
By Martin Crowley

### User Experience (UX)
#### Project Purpose
In this project I am focusing on creating a website aimed towards helping people achieve their fitness goals by providing them with a varied database of exercises ranging from Beginner to Advanced levels of difficulty. It will allow users to view the current collection of exercises, as well as expand/fine-tune the collection available by allowing them to add new exercises to the database. They will also be able to edit and delete the exercises they have added to the database (should such action need to be taken).

This project will use a MongoDB database, and the application itself will be set up using the Flask micro web framework.

The primary target audience is anyone that has an interest in the gym and keeping fit. Whether they are new to the world of protein powders and lifting weight, or already an avid gym goer, there will be exercises that cater to all users regardless of their current level of knowledge or fitness.
##### Why would a user want this?
The fitness industry is currently sitting at global industry revenue of around $99.9bn, with 210,000 clubs globally serving 183 million members, and over 7,000 of these gyms based here in the UK. It’s important to note as well that this data is restricted to health clubs only, and doesn’t account for boutique studios, community recreation facilities or gyms located in venues like hotels, etc… Therefore the numbers could in fact, be far greater than the official figures recorded. (Information sourced from: *https://www.wellnesscreatives.com/fitness-industry-statistics-growth/*)

This shows the possible reach, and wide-spread appeal for an application that would allow users to easily navigate and access a database filled with exercises they could follow and incorporate into their workouts, whether they are new to the world of fitness, or just wanting to further expand their current workout regimen.

##### Why is this so special?
The application will give users an easy and accessible way to view information on various exercises, as well as allowing them to save exercises to their user account in a favourite exercises section, therefore allowing them to easily locate exercises that they wish to try/incorporate into their workout.

#### User Experience
The site itself will follow standard web design conventions and so the layout and initial use of the site should feel immediately recognisable to almost all users, with those lacking experience in web browsing finding the website to be self-explanatory and easy to use/navigate.

The Home page will immediately inform the user of the site’s purpose, through the use of a fitness related background image, as well as the site being labelled “Shared Fitness Db”, and the tagline “Find the exercises you need here”. If this doesn’t display the site’s purpose clearly enough, then it will be very apparent from the rest of the information displayed on the home page as to what the site has to offer.

##### User Stories
It is key to think about what the user would require from such a site:
- As a user, I'd like to be able to view a large variety of fitness/gym exercises that I would be able to learn about/try
- As a user, I'd like to add new exercises to the database/website that aren’t currently featured on the website (CREATE)
- As a user, I’d to find out more information about the exercises, including the muscle groups they use, how to do the exercise (step-by-step), equipment used, etc… (READ)
- As a user, I’d like to be able to edit/update an exercise that I have previously added to the website (UPDATE)
- As a user, I’d like to be able to delete an exercise that I have previously added to the website (DELETE)
- As a user, I’d like to be able to easily see any exercises that I previously submitted
- As a user I’d like to be able to save desired exercises to my user account so that they may be easier to find and use when required
- As a user, I’d like for the website to be user-friendly and easy to navigate
- As a user, I’d like to be able to search the database for exercises that match chosen keywords
- As a user, I'd like to be able to access the data and experience all the site has to offer, regardless of device and browser type being used

Whilst the website aims to provide a service for the user and their need ultimately needs to be fulfilled to provide a good user experience, the site will also benefit the Site creator/admin, as they will be able to grow their own knowledge further through the exercises added to the database/site by the users.

##### Design Ideas
When thinking about the layout and the design of the site, I wanted it to look professional and of a high standard, so I used some dark colours (black, dark grey) and some bold colours (White, Orange) so as to make the website stand out and look both professional and memorable. It also has a clean aesthetic, and feels easy and approachable when using it.

I broke the design down into various style decisions:
##### Font
I will be using “Exo 2” for the website’s used font type, as this is a no-frills, modern, professional looking font that is easy to read.
##### Colour Scheme
I have opted for a dark background picture of two dumbbells, and the rest of the site will be of a similar colour scheme. With the grey, white and orange being used to contrast the dark colour of the navbar, footer and background image.
##### Icons
Whilst I would’ve liked to have used the Materialize Icons that were available to use with the Materialize framework, the choice of icons was rather limiting, especially when it came to related icons and ones to use as links to social media. So I opted instead to use Font Awesome for the icons used on the website (*https://fontawesome.com/icons?d=gallery*).

### Wireframes
For my wireframes, I designed these on the website “Moqups” (*https://moqups.com*)

For the most part, the wireframes and the website are fairly similar, with the main differences being that I opted to go for a home screen that allows all execises to be displayed on the home screen, whilst using pagination to limit the number shown per page to stop it being too cluttered (especially on mobile). Whilst I opted on the search page to use a single search bar that uses regular expression and finds instances of the word/s the user has entered in the name of the Exercises, the name of the Muscle Used, the name of the Equipment Required, or the Difficulty listed, and returns all exercises found that match. So if the user typed in “Chest” the exercises that have “Chest” as the muscle being used, would be returned.

For both Mobile and tablet I opted to use a hamburger button in the top left corner, and for Desktop I opted for a more traditional navbar with all the page links displayed on said navbar at the top right. 

These wireframes have been included and are able to be viewed in a separate directory/folder called "Wireframes", which have subdirectories called "Desktop" and "Mobile", with “Desktop” having subdirectories showing wireframes for the pages depending on whether the user is logged in or not.

### Features
#### Current Features
- Feature 1 – Navigation
  - The navigation bar for the website will change both in the way it is displayed and the content it features depending on circumstances.
  - The navigation bar will be displayed as a bar on screen widths that are above 992pixels, anything below this will use a side-nav that will be accessed through clicking on the hamburger button at the left side of the nav-bar.
  - The options displayed on the nav will also change depending on whether the user is logged in (should they have previously registered). If the user has not logged in, they will see the options on the nav to “Register” and “Log In”, whereas if the user is logged in, they will see “Add Exercise”, “My Account” and “Log Out” in their place.
- Feature 2 – Index/Home Page
  - On the index/home page, I am going to display the name of the website and a brief introduction, as well as listing the number of exercises currently on the website (therefore allowing the user to know how large the database is and keep users aware of growth). I will also have all the exercises in the database showing by default at the bottom of the page in cards, with pagination elements allowing these to be cycled through.
- Feature 3 – Search 
  - The search page, will give the user the options to search for a specific exercise by name, or by typing in a muscle type, equipment used or difficulty, and the exercises associated to that particular word will be returned.
- Then clicking on the search button will return the results below the options in the form of cards.
  - Alternatively if the doesn’t enter anything into the search box and the user just clicks the search button, then every exercise in the database will be displayed.
  - This feature will be available to all users, whether registered and logged in, or just browsing the site as a guest user.
- Feature 4 – Register
  - A user can use the site as a guest, and will still be able to use the home page and the search page to their fullest extent to find and read about all the exercises in the database. However they will need to register as a user should they wish to perform any user specific functions such as: add/edit/delete exercises to the website or favourite any exercises and have them display in their own account favourites list.
  - The user information will consist of a username and a password, which get stored in the database, therefore allowing for the users information to be retained for future log ins.
  - Should a user try to register with a username that is already in the database, then a message will display asking them to choose another username.
  - If the user has clicked on the register page by accident and actually meant to go to the log in page, there will be a link at the bottom that will take the user to the log in page.
- Feature 5 – Log In
  - Once a user has registered, they can click on the log in option on the navigation bar, this will then take them to the log in page that will allow them to log in with their user.
  - If the user has previously registered, they will be able to input their username and password, and once checks have been carried out to ensure that the values of those fields are values stored in the database, then the user will be logged in and redirected to the home page with the option to now add exercises to the website, edit or delete exercises they have added, view their account and favourite exercises.
  - If the user has clicked on the log in page by accident and actually meant to go to the register page, there will be a link at the bottom that will take the user to the register page.
- Feature 6 - My Account
  - Once a user is logged in, they are able to view their account, from here they will easily be able to see which exercises they have added to the website, making it easy for them to amend the exercise or delete it should they need to.
  - The user will also be able to see the exercises they have favorited, making it easy to locate particular exercises that you wanted to use for a workout or you just wanted to revisit at a later point.
- Feature 7 – Favourites
  - Each exercise will have a button that you will be able to click on that will add the exercise to your favourites list in your account, this makes it easy to locate at a later point, as you won’t need to go through the search again to find the exercise.
  - This feature will only be available to the user if they have logged in.
- Feature 8 – Flashed Messages
  - I opted to use the flashed messages to inform the user of particular events (for example if they had added an exercise, or if the username they are trying to register already exists). 
  - These flashed messages are displayed just below the navbar at the top the page, just below the navbar. The messages are in bold orange writing, so they will stand out when displayed on the dark background picture, and once the user has read the flashed message and wants to get rid of it, it is as simple as clicking the orange close/X button on the right of the message.
- Feature 9 – Add Exercises
  - The user will be able to add exercises to the database once logged in, this feature will be unavailable for a guest user to carry out unless registered and logged in. The page uses a form consisting of select boxes, input text boxes and a text area. This information is then stored in the database and displayed on the website for all users to view on the home page and in the search page results.
- Feature 10 – Edit/Delete exercises
  - The edit and delete functions can only be carried out by users that are logged in, and on the exercise/s that the user has added to the website themselves. This was to stop the chance of exercises being added by one user and then another user unfairly being able to edit or delete the exercise they hadn’t added themselves.
- Feature 11 - Log Out
  - When a user decides they want to log out of the site, the option to do so is located on the navbar once the user is logged in (it isn’t displayed if the user is not currently logged in) and within the “My Account” page.
  - Once the user click on their account page, they will find the option to log out of the site at the bottom of the page. Should they choose to click the button, they will be taken to another page that will prompt them to confirm they do wish to log out. If they confirm they do, they will be logged out, and returned back to the home page as a guest, with the default nav options available for a guest user (Home, Search, Register, Log In).
#### Future Features
- Feature 1 – Equipment
  - I would in future like to add a separate page on the website that would go into detail on the different types of equipment that is available to use when keeping fit/working out. This could then have my recommendations/reviews for the different types of each equipment type available for purchase from different companies/brands.
  - This would also allow others to come to the website to write about a particular piece/brand of equipment they have used and add it to the site to allow others to get a larger overview of the equipment available and where to get it.
- Feature 2 – Muscles
  - I would in future like to add a separate page on the website that would go into detail on the different muscles used in the human body and further expand on the anatomy of those muscles to enhance the user’s understanding of muscles in the human body, which would solely be for educational purposes and just a fun additional extra.
- Feature 3 – Comments
  - I would like to add a feature in future that would allow for users to add comments on individual exercises already added onto the website. This could allow for users with extensive knowledge to share tips or hints on how certain exercises could be done better or with more variation, to therefore allow each user viewing to gain further insight into how the exercise could be improved upon.
- Feature 4 – Browse button and Sort Options
  - I will implement a browse button and sort options to allow the user to display exercises whilst applying certain filters prior to the search and choosing the number of results shown on screen.

### Technologies Used
The following technologies were used in the design and build of this project.
- Pycharm
  - Pycharm IDE was used to write the HTML, CSS and PYTHON
- Moqups
  - Moqups was used to create the wireframes for the project
- MongoDB/MongoDB Atlas
  - MongoDB was used as the brief states “Build a mangoDB-backed Flask project”. However I also wanted to use MongoDB to further work on and enhance my understanding of document-based (NoSQL) databases.
  - MongoDB Atlas was used for my database.
- Git & GitHub
  - Git used for version control.
  - GitHub used as a remote repository and the hosting of this site.
- Heroku
  - Heroku is used to host the app.

The languages used in this project:
- HTML5 & CSS3
  - HTML5 was the markup language used for the project.
  - CSS3 was used to style the HTML.
- Javascript
- Python
  - Python has been used to run the backend of the application.

There were also many libraries used in this project, which are available to see in the “requirements.txt” file
- Materialize
  - Materialize was used for the CSS framework, as my previous 2 projects used Bootstrap and I felt it would be good to try a new framework to broaden my knowledge and help understand how they differ, therefore allowing me to decide on which is preferred for future projects.
- Flask
  - Flask (is the micro web framework that) was used for the application framework due to the brief stating that it was required.
- Font Awesome
  - Font Awesome was used to provide the website with suitable icons.
- Google Fonts
  - Google Fonts provided the “Exo2” font used throughout the project.
- jQuery
  - jQuery is used in the project to manipulate the DOM, an example of this is the hamburger button on the nav menu for mobile devices(shows/hides the nav menu).
- PyMongo
  - PyMongo enables the python application to access the MongoDB database.
- Jinja
  - Jinja is the templating language used in the project.

### Testing
When testing the website, I carried out testing locally in Pycharm and on Heroku using Chrome developer tools. On chrome developer tools I tested its functionality on simulated devices, in both portrait and the landscape views. The simulated devices that the website was tested on were:
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- iPhone 5/SE
- iPhone 6/7/8
- iPhone 6/7/8 Plus
- iphone X
- iPad
- iPad Pro
- Responsive

I have also tested the website both locally and remotely on actual devices (rather than just simulated ones on Google Chrome tools), these devices consisted of:
- iPhone 6s
- iPhone 7
- iPad (generation 2)
- iPad Pro 
- Sony Xperia Play
- Multiple desktops (various sizes)

Some examples of the physical testing carried out by myself on certain parts of the site include:
- Link to my Github
  - Scrolled to the bottom of the page
  - Clicked on the text “Martin Crowley - (c)2019”
  - This loaded up a new webpage that took me directly to my Github user page/repositories
- Links to social networks (facebook/Instagram)
  - Scrolled to the bottom of the page
  - Clicked on the icons for both facebook and instagram
  - This loaded up a new webpage that took me directly those social networking sites
- Logo in nav and footer
  - Click on the icon at the top and bottom of the page on separate occasions
  - When on a different page it redirected back to the home page, when already on the home page, it just reloaded the home page
- Navbar links (not logged in)
  - On desktop, I clicked on each link on the navbar (home, search, register, log in), and each link took me to the relevant page
  - On mobile, the hamburger button rendered perfectly. I then clicked on the hamburger button in the top left of the screen, and then clicked on each link on the sidenav (home, search, register, log in), and each link to me to the relevant page
- Navbar links (user logged in)
  - On desktop, I clicked on each link on the navbar (home, search, add exercise, my account), and each link took me to the relevant page. Also when log out was clicked, I was logged out and directed back to the home page
  - On mobile, the hamburger button rendered perfectly. I then clicked on the hamburger button in the top left of the screen, and then clicked on each link on the sidenav (home, search, add exercise, my account), and each link to me to the relevant page. Also when log out was clicked, I was logged out and directed back to the home page
- Pagination
  - The pagination on the home page works perfectly and allows the user to change between the pages displaying the total number of exercises. There are 6 exercises being show per pagination page on the home page. This shows the pagination is working correctly as there are currently 48 exercises being displayed on the website, which with 6 exercises per page, gives a current total of 8 full pages of exercises.
  - The pagination on the account page for user added exercises allows the user to change between the pages displaying the exercises they have added themselves. The number of exercises per page is set to 3, and this is working correctly, as I had added 5 exercises on my personal account on the website. This was displayed correctly in the user added exercises pagination, as my account was showing 2 pages, of which the first page had 3 exercises, and the second page had 2 exercises.
  - The pagination on the account page for the users favourite exercises allows the user to change between the pages displaying the exercises they have previously favourited. The number of exercises per page is set to 3, and this is working correctly, as I had 2 exercises favourited on my personal account, which was displayed correctly in the pagination as I only had one page which consisted of 2 exercises I had favourited. I then liked 5 more exercises, and the pages being show went up to 3, of which the third page contained 1 exercise. Therefore the total number of favourite exercises was displaying as 7, which is correct.
- Exercise cards
  - All exercise cards was loading as expected, and were displaying 1 per row on mobile sized screens, 2 per row on tablet sized screens, and 3 per row on desktop sized screens.
  - The pictures were all rendering at the same height in the cards, and the card content was rendering at the same height, to give a symmetrical look to all the cards but also to stop the cards with more or less card content being longer or shorter than others.
  - When clicking on “Find out more…” each card loaded up the page with the information for the specific exercise that was being displayed on the card.
  - The cards consisted of an image of the exercise, the exercise name, the muscle worked, the equipment used and the difficulty of the exercise. All the information rendered as expected and no information was cut off regardless of the device screen size.
- View Exercise
  - I viewed many of the exercises (having clicked “find out more” on the card), and with each exercise being displayed on the screen, all the information stored in the database for that particular exercise was shown on the screen.
  - At the top of the page, the name of the exercise was always displayed, with the name of the user that had added the exercise displayed just below it. The image of the exercise was shown next, with the majority of the information about the exercise located just below that.
  - Below the information was when the functionality and look of the user page changed slightly, as I viewed many exercises as both a guest user (not logged in) and actually logged in as a user.
  - When NOT logged in, each page displayed the exercise name, creator, picture and exercise info, and below the exercise there was just the instructions to carry out the exercise displayed.
  - I then logged in, and all the exercises I viewed now had the same base content available (name, creator, image and information), however below the information, there was now a favourites button displayed, which when clicked, added and removed the exercise from my user favourites (depending on its previous state). Below this was the instructions to carry out the exercise, but below that were the options to edit and/or delete an exercise. However this was only for the exercises I had added to the database myself. When viewing the Skipping exercise (amongst others), which had not been added to the database by me, I was unable to see the edit or delete button. Therefore it showed that the exercise pages were working correctly as it was checking the session username against the username associated to the exercise (who created it).
  - When viewing an exercise I had created, and clicking on the edit or delete buttons, it would then take me to the edit exercise page, or the delete exercise page, depending on which button was clicked.
- Search
  - The search page and function was tested extensively, with me testing it by typing in and searching exercise names, the names of muscles, the names of equipment that is used and with all 3 of the difficulties
  - For example, when typing in “chest” into the search bar and clicking ‘search’, it returned 5 results, this was then checked in the database itself, which confirmed there were 5 exercises in the database that had “chest” listed as the muscle used.
  - There were also cases where the query is being done based on words detected in the exercise name, as well as in the other 3 categories. So for example, when typing in and searching “Back” the search returns 6 results, when there are only 5 back exercises, this is due to one of the exercises (Standing Cable Kickbacks) having the word ‘back’ in it. This proves helpful, as some users might have an idea of the exercise they are looking for but may not remember its full name, therefore allowing them to type in the part they might remember, and have the exercise they were looking for show up as part of the results.
  - When testing based on equipment types, I tested every type of equipment and each number of results returned were the same as the number of documents in the database that had that particular type of equipment as their main equipment needed. For example: when typing “Barbell” into the search bar, when clicking ‘search’, I had 8 results returned, which was the correct number of exercises in the database that had barbell as their equipment_type
  - Testing based on difficulty also came back correct each time, with the search for “Beginner” returning 28 results, the search for “Intermediate” returning 18 results and the search for “Advanced” returning 2 results. Which meant each of these search results were correct as the database had 48 exercises at the time of testing, therefore all 48 were accounted for and matched their respective difficulties.
  - Also, when leaving the search bar blank, the search was intended to return all of the exercises. This worked, and the search returned all of the exercises (which was 48 at the time of testing).
- Register
  - When testing the register page, I initially tried to register with a username that I knew had already been used. This reloaded the register page and displayed a flash message that informed that the username had already been taken and requested that I pick another. Therefore this was working as it should, as it was checking the users collection in the database to see if another user with the same username already existed, and where it did, it would inform the current user trying to register of this and take relevant action.
  - When typing a username in the username box, but leaving the password box empty, upon clicking “create account”, it informed me to “Please fill in this field” underneath the password input.
  - The same also happened when I typed in a password, but didn’t input a username, the form would not submit, and the message was displayed again.
  - Also tested by making both the username and password shorter than the requirements of each field (4 for username, 5 for password), and when trying to submit the form, it would not allow me to and requested that I match the format requested.
  - When the username and password that were entered in cleared the initial checks (that the username wasn’t already being used, that both fields were filled and both had the correct minimum number of characters, and didn’t exceed the maximum number of characters) then the form was able to submit as the user was added into the database and the user was logged in and redirected back to the home page.
  - Also tested the link at the bottom of the page, which successfully redirects to the log in page.
  - When already logged in and trying to access the register page by typing it into the URL, I was returned to the home page and a message was flashed that I had to log out first to try and register a new user
- Log In
  - When testing the log in page, I initially tried to log in with a username that I knew hadn’t been registered yet, and therefore didn’t exist in the database. This reloaded the log in page and displayed a flash message that informed me that the username didn’t exist, and asked me to check the spelling. This is due to it often being a clerical error where a slight spelling mistake may have been made. Therefore this was working as it should, as it was checking the users collection in the database to see if a user with the same username already existed, and if it didn’t, it would inform me of this.
  - When typing a username in the username box, but leaving the password box empty, upon clicking “log in”, it informed me to “Please fill in this field” underneath the password input.
  - The same also happened when I typed in a password, but didn’t input a username, the form would not submit, and the message was displayed again.
  - When the username and password that were entered in cleared the initial checks (that the username was stored in the database, and that the password entered was the password that belonged to that username) then the form was able to submit as the user was logged in and redirected back to the home page.
  - Also tested the link at the bottom of the page, which successfully redirects to the register page.
  - When already logged in and trying to access the log in page by typing it into the URL, I was returned to the home page and a message was flashed that I had to log out first to try and log in as another user
- Add Exercise
  - When filling in the add exercise form, I first deliberately tried to leave each of the required boxes empty, and when trying to submit the form, it wouldn’t allow me to and would show a message that would ask me yet again to “Please fill this field” with the required top most required field that was left unfilled. If this was filled but other required fields weren’t, the message would then display by the next required field with each time the form was submitted.
  - If all required fields were filled, but the unrequired optional fields were left blank, then the form would submit and the exercise would enter the database. When carrying this out, I clicked on the exercise and it just meant that the headings were there, but no information followed the headings. However it still looked neat and tidy and worked as intended.
  - When testing the text area, I had used a JS character counter for the text area, this meant that at the bottom right of the text area, it would show how many characters that had written so far, and also displayed the max number of characters. When writing less than 15 characters a message would display when trying to submit the form that would say “Please lengthen this text to 15 characters of more”. This was working as intended and also showed what was expected.
  - The URL input field has a placeholder that explains what the required URL needs to begin with. When trying to submit a URL that didn’t start with ‘https://’ then a message would pop up under the URL input box and ask for me to “Please match the format requested”.
- Edit Exercise
  - When editing the edit exercise form, all the fields were already filled, so I first deliberately deleted the information that had been written in some of the required boxes so they were empty, and when trying to submit the form, it wouldn’t allow me to and would show a message that would yet again ask me to “Please fill this field”.
  - If all required fields were filled, but the information that had previously been written in the unrequired optional fields was deleted, then the form would submit and the exercise that was stored in the database would be edited and have the new information stored.
  - When clicking on the cancel button, this also worked as planned, as it would return me back to the exercise I was just trying to edit.
- Delete Exercise
  - When trying to delete an exercise (and having previously pressed the “delete button” on an exercise) a page would display that asked if I wanted to deleted the exercise. When clicking “Delete”, the exercise would then be removed from the database, and therefore would no longer exist on the site.
  - When I clicked “Cancel”, it would yet again return me back to the exercise I had just been viewing.
- User Account
  - When logged in and viewing the user account, I was able to see the exercises added by me, as well as the exercises that were favourited by me.
  - The pagination worked on the page and would allow me to view each page for both my added exercises and my favourite exercises.
  - Clicking on the exercise from my pages would take me straight to the exercises so I could view their information.
  - Clicking the log out button at the bottom of the account page logged me out when pressed, and returned me back to the home page.
- Favourite Function
  - The favourite button was only available to see on exercises once I had logged in, once logged in, on each exercise it would have an orange heart that would give me the option to add it to my favourites.
  - When the exercise wasn’t already in my favourites, the text underneath would read “Click to Add to Favourites” and the heart icon would show a broken heart (meaning it wasn’t yet favourited)
  - When the exercise was already in my favourites, the text underneath would read “Click to Remove from Favourites”, and the heart icon would show a heart (meaning it was currently in my favourites) 
- Log Out
  - When clicking “Log Out” from the navbar, I would be logged out of my account and a flashed message would pop up at the top of the screen informing me that I had been logged out. I would also get returned to the home screen whenever I chose to log out.
  - This is the same as when logging out through my user account page, as the log out button at the bottom of the user account page causes the same to happen.
- Family & Friends Testing
  - Once the application was up and running, I asked 4 of the members of my family and 2 friends to register and test the site.
  - Of the 4 family members and 2 friends that tested the site, all said that it was intuitive and easy to use, and that they had no issues with working out what to do or how to use certain functions on the site. I got each member to test all the CRUD operations, and they all created multiple exercises, edited a few they had created, deleted and read exercises too.
  - They also went onto various exercises and favourited the exercises that appealed to them.
  - I also asked for them to go to their user account page and cycle through their added exercises and favourites to see if everything was displaying as expected, to which there were no bugs found and the feedback was very positive.

The devices my friends and family tested on were: 
- iPhone 6s
- iPhone 7
- iPad Pro
- Various desktops

Please note that if you are wishing to test the CRUD operations yourself, you can register as a user, but please don’t use sensitive passwords as they currently are just stored in the database.

Alternatively you can use the guest user that I set up for this pupose:
  - USERNAME: GuestUser
  - PASSWORD: password

#### Known Bugs
When logging in or typing something into an input box, that the user had previously typed into, the autofill options would appear below the input box. If the user clicks on one of these autofill boxes, the background colour would show up as white with black writing, but would take up slightly more space than usual, this effect does not happen if the user types the information in themselves. It doesn’t affect functionality and is just a slight visual bug, of which I am aware of and will fix with future updates.

There is also one bug in the console for an Uncaught TypeError, this is with regards to the JS script provided by code institute to help the select boxes provided by Materialize to function properly. The select boxes do work as they should, so this error doesn't affect functionality.
### Deployment
My application was coded in Pycharm. Once I had created the workspace in Pycharm for my project to be built in, I then turned to GitHub (which is a web-based interface that links with Git and allows you to store and view the different versions of code at the stages it was pushed to the GitHub server) and created a repository for my milestone project, I then went back to Pycharm, and into the terminal I pasted in the Command Line Interface commands that GitHub had provided me with to create a local Git repository and form a link between Git and the GitHub server.
- echo "# practice" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git remote add origin https://github.com/Mcrowley93/shared_fitness_database.git
- git push -u origin master

Once I had done this, I was then able to use git commands in the CLI at various stages to add changes I had made within the workspace, to the staging area (storing files is a 2 step process). This was done using the command: ‘git add ‘which could be followed with the specific file name/s that needed to be added to the staging area (prior to being committed to the repository). Alternatively, when there was a few changes that could be added all at once, the command was followed by a full stop (‘git add .’)

Once changes had been added to the staging area, they then needed to be committed (the 2nd stage of storing files) to the repository using ‘git commit’. However with each commit, I also included a message that explained the reason for each commit to the repository. This was done by using the command: ‘git commit –m “TEXT GOES HERE“ ‘

At this stage, the local Git repository could then be synced with the repository on the GitHub server, which was achieved by using the command: ‘git push’

Once the project/website was in the dedicated GitHub repository, it was then able to be deployed to Heroku. However there were a couple more steps that have to be carried out prior to deploying the project, the first of which was to update my requirements.txt file to ensure the project’s dependencies list was up to date. I also had to create a Procfile, which is a simple text file stored in the root directory of the project that describe the components required to run the application.

I then went to the Heroku dashboard and created a new app called “shared-fitness-database” with Europe as its region. Once the app was created I clicked on the app and went to settings and had to set the Config variables for the PORT, IP, the mongoDB URI string and the secret key for the project. Once these steps were complete I could click on the Deploy tab in the Heroku app dashboard and use the Github deployment method which connects the app to my Github repository, I then turned on automatic deploys, so any changes made to the project that are then pushed to my Github repository are automatically updated on the application once live. All that was left to do was to manually Deploy Branch, this allows you to see a build log for the app being made, but once this step was done the app was deployed on Heroku and was able to be opened and used.

The finished project can be viewed here: **http://shared-fitness-database.herokuapp.com/home**
### Credits
##### Content
Code for the database website/app was written by myself with knowledge I’ve picked up from the code institute course and from personal study.

##### Code used from others
Helped with the code for the try block for my favourite function by Dave Laffan (*https://github.com/steview-d*) 

##### Media
SIDE-NAV BACKGROUND PICTURE: 
*http://www.peakpx.com/593658/grayscale-photograph-of-gym*

DUMBBELLS BACKGROUND PICTURE:
*https://www.pexels.com/photo/dark-dumbbell-fitness-muscle-training-302663/* 

WEBSITE LOGO MADE AT:
*https://www.freelogodesign.org/* 

EXERCISE CARD PICTURES:
*https://upload.wikimedia.org/wikipedia/commons/f/f7/Bench-press-2.png*
*https://upload.wikimedia.org/wikipedia/commons/e/e6/Reverse-grip-bent-over-rows-2.png*
*https://upload.wikimedia.org/wikipedia/commons/0/0c/Squats-2-2.png*
*https://upload.wikimedia.org/wikipedia/commons/8/86/Bicep-hammer-curl-2.png*
*https://upload.wikimedia.org/wikipedia/commons/d/db/Close-grip-ez-bar-curl-2.png*
*https://upload.wikimedia.org/wikipedia/commons/7/73/Push-ups-3-2.png*

The above URLs for images were used for my entries into the website, which were all done using the add exercise form. The images were from Wikimedia, they were free to use and the Author of these pictures is: “Everkinetic”.

All other images on the site were taken from free to use websites and the URLs can be accessed by inspecting the picture and copying the URL stored in its “src”.

##### Acknowledgements
- Spencer Barriball - My Code Institude assigned mentor, for his invaluable knowledge, guidance and advice.
