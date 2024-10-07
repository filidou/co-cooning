# Co-cooning

### The code is provided in the master branch

## Description of Co – cooning
The Co-cooning model is designed to assist users in selecting movies or series based on their preferences, simplifying the often difficult decision-making process. By offering personalized recommendations from a wide range of options, it encourages users to unwind and enjoy a relaxed viewing experience. The name "Co-cooning" reflects its role as a companion in helping users embrace the comfort of cocooning—settling in for a cozy, stress-free movie or series session.
Here's a couple of paragraphs incorporating the points you mentioned:

## Motivation for Developing Co-cooning
Choosing what to watch has become an overwhelming task in today's world of endless streaming options. Often, we find ourselves wasting hours watching trailers, reading plot summaries, and still feeling unsure about what will truly suit our mood or preferences. This not only delays our downtime but also adds stress to what should be a relaxing experience.
The motivation behind developing Co-cooning was to eliminate this frustration. By using a personalized recommendation system, I aimed to create a tool that simplifies the decision-making process, saving time and helping users focus on enjoying their leisure time. Whether it's for a cozy solo night in or a fun group viewing, Co-cooning acts as a trusted partner in finding the perfect movie or series, making cocooning a stress-free, enjoyable experience.
Domain of Co-cooning
The domain of Co-cooning focuses on movie and series recommendation. It asks whether the user wants to watch a movie or series, along with their preferred genre and release year. With these inputs, the bot narrows down options to provide personalized recommendations that suit the user's preferences.



## Features
Co-cooning offers an easy-to-use interface that simplifies the process of selecting movies or series. It provides customized suggestions based on user input, specifically focusing on genre and release year, to tailor recommendations to individual preferences. With its streamlined decision-making process, the bot helps users quickly find something to watch, reducing the time spent searching and maximizing relaxation.
## Installation
To install and run the Co-cooning bot locally, follow these steps:
  - A.	Clone the repository
  - B.	Install the dependencies:
 pip install -r requirements.txt

  - C.	Run the chatbot:
rasa run actions
rasa shell
## Description of scenarios
  - 1st. Movie Recommendation Path: The user requests a movie recommendation, and the bot collects preferences (movie genre and release year) through the form before making a recommendation.
  - 2nd. Series Recommendation Path: Similar to the movie path, but this time the user requests a series recommendation. The bot collects the series genre and release year and provides a suggestion accordingly.
  - 3rd. Sad Path with Rage: This scenario handles cases where the user challenges the bot. After an initial response from the bot, the user persists with another challenge. The bot escalates to a "rage" response and then ends the conversation with a goodbye.
  - 4th. Sad Path with Movie Recommendation: The user initially challenges the bot, but the conversation shifts to asking for a movie recommendation. The bot follows the usual path of collecting movie preferences and providing a recommendation.
  - 5th. Sad Path with Series Recommendation: Similar to the previous path, but the conversation shifts to asking for a series recommendation after the user challenges the bot. The bot collects the necessary series details and makes a suggestion.


## Functionality
Greeting the user:
First interaction with greeting is not necessary for the stories it is implemented in the rules.
- rule: Greet the user
  steps:
  - intent: greet
  - action: utter_greet

This is implemented, also, for the goodbye greet.
- rule: Say goodbye
  steps:
  - intent: goodbye
  - action: utter_goodbye
### Details in the conversation:
Ask for movie
-	Ιntent: ask_movie_recommendation
-	Action: movie_recommendation_form
-	Slot: release_year, movie_genre (e.g., "drama", “2008”)
-	Form: movie_recommendation_form captures location details and stores them in the slots
-	Action: action_recommend_movie
Ask for series
-	Ιntent: ask_series_recommendation
-	Action: series_recommendation_form
-	Slot: release_year, series_genre (e.g., "drama", “2008”)
-	Form: series_recommendation_form captures location details and stores them in the slots
-	Action: action_recommend_series

Challenge with range
Without slots or forms involved
-	intent: bot_challenge
-	action: utter_bot_challenge_response
-	intent: bot_challenge
-	action: utter_rage
-	action: utter_goodbye
Challenge with movie recommendation
-	Ιntent: bot_challenge
-	Action: utter_bot_challenge_response
-	Ιntent: ask_movie_recommendation
-	Action: movie_recommendation_form
-	Slot: release_year, movie_genre (e.g., "drama", “2008”)
-	Form: movie_recommendation_form captures location details and stores them in the slots
-	Action: action_recommend_movie

Challenge with series recommendation
-	Ιntent: bot_challenge
-	Action: utter_bot_challenge_response
-	Ιntent: ask_series_recommendation
-	Action: series_recommendation_form
-	Slot: release_year, series_genre (e.g., "drama", “2008”)
-	Form: series_recommendation_form captures location details and stores them in the slots
-	Action: action_recommend_series

## Forms

movie_recommendation_form: It gathers information about the movie user want to see. It uses for that purpose two slots release_year, movie_genre

series_recommendation_form: It gathers information about the series user want to see. It uses for that purpose two slots release_year, series_genre
## Policies
Implementing the solution for the policy was particularly challenging. It required numerous experiments and careful consideration of different approaches before arriving at a workable solution. The Co-cooning bot utilizes three key Rasa policies to manage conversations effectively. First, the RulePolicy is responsible for handling rule-based interactions, such as activating forms and guiding structured flows. This policy ensures the bot behaves predictably in straightforward scenarios. Next, the MemoizationPolicy remembers exact conversation patterns from the training stories, applying them to ensure consistent responses when the conversation matches previously seen paths. Finally, the TEDPolicy introduces flexibility by using machine learning to predict the next action based on the last five conversation turns. It is trained over 100 epochs and includes a constraint on similarities to help differentiate between similar intents and actions. Together, these policies enable the Co-cooning bot to smoothly handle both predictable interactions and more dynamic, unforeseen conversations.

## Test cases
Movies scenario: 
- User’s input (hi) > Hello Co-cooning is here for you! How can I assist you in finding a movie or TV series? User’s input (movie) > What genre of movies do you prefer?
- User’s input (drama)> What is yor preferred release year ?                                                                                                            - User’s input (2002)> I recommend you watch Drama Queen. It's a Drama movie from 2002, rated 3.2 on IMDb!                                                              - User’s input (bye)> Goodbye and always remember: Get Cozy, Cocoon Up, and Press Play!
Series scenario: 
- User’s input (good morning)> Hello Co-cooning is here for you! How can I assist you in finding a movie or TV series?                                                  - User’s input (series) > What genre of series do you prefer?
- User’s input (drama)> What is yor preferred release year ?                                                                                                            - User’s input (2010)> I recommend you watch Total Drama World Tour. It's a Drama series from 2010–, rated N/A on IMDb!
Challenge scenario: 
- User’s input (are you a bot) > No I am a greenscreen, like those they have in the studios. Do you want me to recommend a movie or a series?                           - User’s input (fu) > I may be just a bot, but challenging me was a mistake. No movies or series for you. Prepare to face my wrath!
Goodbye and always remember: Get Cozy, Cocoon Up, and Press Play!

Movies scenario with challenge: 
- User’s input (are you a bot) > No I am a greenscreen, like those they have in the studios. Do you want me to recommend a movie or a series?                                                                                                                                                      User’s input (series) > movies scenario
Series scenario with challenge: 
- User’s input (are you a human) > No I am a greenscreen, like those they have in the studios. Do you want me to recommend a movie or a series?                                                                                                                                                      User’s input (series) > series scenario
## Challenges
Throughout the development of Co-cooning, I encountered several challenges that tested the bot's design and functionality. One significant hurdle was implementing a "sad path" story that included an utter rage response. This approach ran into issues due to contradictions between the defined stories and the rules governing the chatbot's behavior. The conflicting interactions created confusion in the flow, making it difficult for the bot to respond appropriately. 
For the sad path, I initially set up the bot challenge using a rule because I found it computationally efficient. However, when I wanted to create a scenario where the conversation would stop after the bot challenge to avoid looping, I encountered issues. As a result, I ended up creating three additional scenarios to cover all possible outcomes."
Additionally, integrating the OMDb API presented its own set of challenges, particularly in ensuring that the data fetched aligned with the bot’s goals of simplicity and relevance. Initially, I tried several different APIs related to movies and series, but I encountered issues with privacy settings, high costs, and requests for various personal information. In the end, the OMDb API proved to be the best fit for the bot and its purpose. However, one limitation is that it allows only 1,000 calls per day
On the policy side, another challenge was the generic error messages provided. These messages lacked specificity, making it difficult to identify the exact causes of errors, which complicated the debugging process. 
## Real world data
The choice of real-world data sources for Co-cooning was shaped by the chatbot’s purpose and practical considerations. The goal is to help users quickly choose a movie or series without overwhelming them with too many options or complicated interactions. To align with this philosophy, I opted for the OMDb API for its affordability and straightforward integration. OMDb provides essential data—such as genre and release year—enabling quick and relevant recommendations while maintaining a relaxed user experience. This approach ensures that decision-making remains easy, enjoyable, and efficient. 
Further Steps
Gather more user preferences: Ask users about their favorite movies or series to enhance recommendations.
Specify more explore keys: Include options for users to specify actors and directors.
Range of release year: Instead of a release year of the movie/series the user could provide a range of years.
## Sources
- Github repository for public API’S. Link: https://github.com/public-apis/public-apis
- Rasa Tutorial (YouTubeLink: https://www.youtube.com/watch?v=Ap62n_YAVZ8&ab_channel=Rasa
- Rasa Documentation. Link: https://rasa.com/docs/rasa/
- CoPilot M365 & GPT 4 (use copilot as assistant with the code)

