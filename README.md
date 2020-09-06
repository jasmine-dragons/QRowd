# QRowd
#### Crowd-sourced contact tracing powered by QR codes


## Inspiration
As we slowly readjust to pre-pandemic life, it is essential to monitor the everyday interactions with others that may reinvigorate the Covid-19 virus. If we are not careful with the places we come and go, there is a great possibility that the pandemic will worsen. It is inevitable that the virus will spread without remembering where one came into contact with a Covid-19 positive individual. There is no doubt that we are all victims of the pandemic, indirect or direct. In order to return to a world without the hindrance of Covid-19, we must work together to prevent its further spread.

Contact tracing is a proven method to tackle Covid-19 at its source. By monitoring where individuals have been, both health officials and civilians can shut down infected locations before the virus spreads further. With citizens from all walks of life contributing to an crowd-source contact tracing application, new outbreaks can be suppressed easily. Not only will civilians be able to avoid areas infected by Covid-19 with contact tracing technology, but small businesses can also use the technology to make informed decisions about their own operation. Crowd-sourced contact tracing made simple is the future of public health technology.

## Functionality
There are two primary use cases for QRowd: civilians and local businesses.

After creating an account, users can immediately contribute to a worldwide contact tracing database. Now, every time a user visits a local business or public space, they can use their mobile device to scan the locations QR code. The user will then be prompted to enter their personal user ID. Using geocoding, the user's ID and location will be stored in a database for further reference. These locations are then used to populate an interactive contact tracing map, where a user can view the places they visited along with the times in which they were visited. Because the database is open-sourced, users can also use the map to view the activity at each location they visited, allowing them to determine whether or not they came into contact with a Covid-19 positive individual. However, because the only indentification used is a randomly generated ID, user data is not compromised, ensuring complete privacy and security.

Local businesses can also take advantage of our platform by using it to make informed decisions about their own operation. Instead of creating a user account, local businesses simply request a QR code mapped to their location. Now, whenever a user scans the QR code, the local business will be notified, providing them with direct data regarding the customers and the places they may have come from. If a Covid-19 case is detected at the local business or at a location that one of their customers may have come from, the business may choose to shut down for a period of time, preventing the spread of the virus. Not only will this be beneficial for the business' brand and safety, but it will also protect their customers from falling victim to an infection.

## Build Process
We used a Flask back-end powered by a MongoDB database, in conjunction with an HTML/CSS/Javascript front-end to build out QRowd. First, the web application framework was laid out by creating Flask routes corresponding to each page needed in the site on the app.py file. Within each route, we developed the needed back-end code. For example, within the scan route, which is where users are taken to upon scanning a QR code, contains a MongoDB URI connection that houses the user contact tracing database. After each scan, the corresponding location is appended to the list of locations under the user's ID number. The text input and success pages are implemented in the scan.html and scan_success.html pages, which utilize both CSS and Javascript to create an aesthetic UI/UX.

For the contact tracing map visualization feature (found in the map.html files) we utilize...

## Challenges
The primary challenge that our team faced was the API connections needed for our data visualization feature. Our first choice, the MapBox API, turned out to be much too difficult to master quickly. Trying to configure the backend to work with the API was extremely tought. Therefore, we switched to the Google Maps API because of its ease of use.

## Setup
Your machine will need flask, pymongo, json, geocoder, mapbox, and dotenv to run this code. To get any of these libraries, you can just `pip install [insert library here]` in a terminal window. To run the code, first pull the github to your computer and then navigate to the folder where app.py is. Then open terminal and run the command `flask run`. This will direct you to a localhost website where you can interact with the product.

### Detailed Instructions:
1. Open command prompt
2. Install flask, pymongo, dns, json, and bson using `pip install [library name]`
3. Then download the github repo to your computer
4. Locate the repo in your file explorer
   -- Open command prompt from that folder's search bar by typing cmd into it
5. Then enter `flask run` in the command prompt
6. Copy the localhost link that is outputted and paste it into a web browser
7. Use the application in your browser
