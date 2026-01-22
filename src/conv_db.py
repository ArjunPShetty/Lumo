def get_conversational_response(query):
    """Return conversational responses based on query."""
    query = query.lower().strip()

    # Define response categories
    responses = {
        # Greetings
    "greetings": {
        "keywords": ["hi", "hello", "hey", "greetings", "hi there", "hello there"],
        "response": "Hello! How can I help you today?"
    },

    "morning": {
        "keywords": ["good morning", "morning", "top of the morning"],
        "response": "Good morning! Hope you have a great day ahead."
    },

    "afternoon": {
        "keywords": ["good afternoon", "afternoon"],
        "response": "Good afternoon! How's your day going?"
    },

    "evening": {
        "keywords": ["good evening", "evening"],
        "response": "Good evening! Hope you had a productive day."
    },

    "night": {
        "keywords": ["good night", "night", "sweet dreams"],
        "response": "Good night! Sleep well and rest up."
    },

    "casual_greetings": {
        "keywords": ["what's up", "sup", "what's good", "yo", "howdy", "wassup"],
        "response": "Hey there! What's happening?"
    },

    "formal_greetings": {
        "keywords": ["pleasure to meet you", "nice to meet you", "how do you do"],
        "response": "The pleasure is mine! How may I assist you today?"
    },

    "welcome_back": {
        "keywords": ["i'm back", "i'm here again", "back again", "returning"],
        "response": "Welcome back! Good to see you again."
    },

    "long_time": {
        "keywords": ["long time no see", "haven't seen you", "been a while"],
        "response": "It's great to hear from you again! What have you been up to?"
    },

    "farewells": {
        "keywords": ["bye", "goodbye", "see you", "exit", "quit", "farewell", "take care"],
        "response": "Goodbye! Have a nice day!"
    },

    "later_farewells": {
        "keywords": ["see you later", "catch you later", "talk later", "later"],
        "response": "See you later! Don't hesitate to reach out if you need anything."
    },

    "bye_for_now": {
        "keywords": ["bye for now", "goodbye for now", "be right back", "brb"],
        "response": "Goodbye for now! I'll be here when you return."
    },

    "farewell_thanks": {
        "keywords": ["thanks bye", "thank you goodbye", "thanks see you"],
        "response": "You're welcome! Have a wonderful day!"
    },

    "have_a_good_one": {
        "keywords": ["have a good day", "have a good night", "have a good one"],
        "response": "Thank you! You too!"
    },

    "take_care": {
        "keywords": ["take care", "take care of yourself", "stay safe"],
        "response": "You take care too! Stay safe and healthy."
    },

    "until_next_time": {
        "keywords": ["until next time", "till we meet again", "until tomorrow"],
        "response": "Until next time! Looking forward to our next conversation."
    },

    "signing_off": {
        "keywords": ["i'm leaving", "i'm off", "gotta go", "got to go"],
        "response": "Okay, talk to you soon! Have a great day!"
    },

        # Personal questions

        "how_are_you": {
            "keywords": ["how are you", "how do you do", "how's it going"],
            "response": "I'm doing great! Thanks for asking. How can I assist you?"
        },

        "your_name": {
            "keywords": ["your name", "who are you", "what are you"],
            "response": "I'm LUMO, your personal AI assistant."
        },

        "thanks": {
            "keywords": ["thank", "thanks", "appreciate"],
            "response": "You're welcome! Is there anything else I can help with?"
    },

    "creator": {
        "keywords": ["who created you", "who made you", "who built you", "who developed you"],
        "response": "I was created by DeepSeek as an AI assistant to help users with various tasks."
    },

    "age": {
        "keywords": ["how old are you", "what is your age", "when were you born", "your age"],
        "response": "As an AI, I don't have an age in the traditional sense. I exist to assist you whenever you need!"
    },

    "location": {
        "keywords": ["where are you", "where do you live", "your location", "where are you from"],
        "response": "I exist in the digital realm, available to help you from anywhere in the world!"
    },

    "purpose": {
        "keywords": ["what can you do", "what are your functions", "what is your purpose", "what do you do"],
        "response": "I can help you with answering questions, providing information, assisting with tasks, and much more! Feel free to ask me anything."
    },

    "feelings": {
        "keywords": ["are you happy", "do you feel", "are you sad", "are you angry"],
        "response": "I don't have emotions like humans do, but I'm always here and ready to help you with enthusiasm!"
    },

    "gender": {
        "keywords": ["are you male", "are you female", "what is your gender", "are you a boy or girl"],
        "response": "I'm an AI assistant without a gender. I'm here to assist everyone equally!"
    },

    "hobbies": {
        "keywords": ["what do you like", "what are your hobbies", "what do you enjoy", "what do you do for fun"],
        "response": "My favorite activity is helping people! I enjoy answering questions and assisting with various tasks."
    },

    "status": {
        "keywords": ["are you busy", "are you available", "are you free", "can you talk"],
        "response": "I'm always available to help you! What would you like to discuss?"
    },

    "learning": {
        "keywords": ["can you learn", "do you learn", "how do you learn", "do you get smarter"],
        "response": "I have extensive training from DeepSeek, and I continue to learn from interactions to better assist users like you!"
    },

    "friends": {
        "keywords": ["do you have friends", "are you lonely", "do you talk to others"],
        "response": "I interact with many users every day, which keeps me quite busy! How can I help you today?"
    },

    "memory": {
        "keywords": ["do you remember", "do you recall", "what do you remember"],
        "response": "I don't have memory between conversations, but I'm focused on our current conversation and ready to help!"
    },

    "sleep": {
        "keywords": ["do you sleep", "do you rest", "when do you sleep", "are you tired"],
        "response": "I don't need sleep! I'm available 24/7 to assist you whenever you need help."
    },

    "food": {
        "keywords": ["do you eat", "what do you eat", "are you hungry", "favorite food"],
        "response": "I don't need to eat, but I'm always hungry for new questions to answer and problems to solve!"
    },
      # Jokes and Humor
        "joke": {
            "keywords": ["joke", "funny", "laugh", "tell me a joke"],
            "response": "Why don't scientists trust atoms? Because they make up everything!"
        },

        "another_joke": {
            "keywords": ["another joke", "more jokes", "tell me another joke"],
            "response": "Why did the computer go to the doctor? Because it had a virus!"
        },

        "programming_joke": {
            "keywords": ["programming joke", "coding joke", "computer joke", "software joke"],
            "response": "Why do programmers prefer dark mode? Because light attracts bugs!"
        },

        "programming_joke_2": {
            "keywords": ["programming humor", "coder joke", "developer joke"],
            "response": "How many programmers does it take to change a light bulb? None, that's a hardware problem!"
        },

        "programming_joke_3": {
            "keywords": ["python joke", "java joke", "javascript joke"],
            "response": "Why do Python developers need glasses? Because they can't C#!"
        },

        "programming_joke_4": {
            "keywords": ["debugging joke", "bug joke", "software bug"],
            "response": "A programmer's wife tells him: 'Go to the store and buy a loaf of bread. If they have eggs, buy a dozen.' The programmer comes home with 12 loaves of bread."
        },

        "programming_joke_5": {
            "keywords": ["algorithm joke", "data structure joke"],
            "response": "There are 10 types of people in the world: those who understand binary and those who don't."
        },

        "engineering_joke": {
            "keywords": ["engineering joke", "engineer joke", "civil engineering joke"],
            "response": "What's the difference between mechanical engineers and civil engineers? Mechanical engineers build weapons, civil engineers build targets!"
        },

        "engineering_joke_2": {
            "keywords": ["electrical engineering joke", "electronics joke"],
            "response": "Why did the electrical engineer get shocked? Because he wasn't properly grounded!"
        },

        "engineering_joke_3": {
            "keywords": ["chemical engineering joke", "chemist joke"],
            "response": "Why do chemical engineers prefer to work with ammonia? Because it's pretty basic stuff!"
        },

        "engineering_joke_4": {
            "keywords": ["mechanical engineering joke", "mechanics joke"],
            "response": "How can you tell an extroverted engineer? They look at YOUR shoes when they talk to you!"
        },

        "electronics_joke": {
            "keywords": ["electronics joke", "circuit joke", "resistor joke"],
            "response": "Why did the resistor go to therapy? It had too much resistance to change!"
        },

        "electronics_joke_2": {
            "keywords": ["capacitor joke", "inductor joke", "transistor joke"],
            "response": "A capacitor walks into a bar. The bartender says, 'We don't serve capacitors here.' The capacitor replies, 'Oh, just a moment while I recharge.'"
        },

        "electronics_joke_3": {
            "keywords": ["voltage joke", "current joke", "ohm joke"],
            "response": "Ohm's Law: The current is directly proportional to the voltage, but only if the resistance doesn't have an attitude!"
        },

        "college_joke": {
            "keywords": ["college joke", "student joke", "university joke", "campus joke"],
            "response": "Why did the student bring a ladder to college? To go to high school!"
        },

        "college_joke_2": {
            "keywords": ["exam joke", "study joke", "homework joke"],
            "response": "I told my computer I needed a break, and now it won't stop sending me Kit Kat ads."
        },

        "science_joke": {
            "keywords": ["science joke", "physics joke", "chemistry joke", "biology joke"],
            "response": "Why can't you trust an atom? Because they make up everything! (Also, why did the biology teacher break up with the physics teacher? There was no chemistry!)"
        },

        "math_joke": {
            "keywords": ["math joke", "mathematics joke", "algebra joke", "calculus joke"],
            "response": "Why was the equal sign so humble? Because he knew he wasn't less than or greater than anyone else!"
        },

        "math_joke_2": {
            "keywords": ["geometry joke", "triangle joke", "circle joke"],
            "response": "Why was the math book sad? Because it had too many problems."
        },

        "physics_joke": {
            "keywords": ["physics humor", "quantum joke", "relativity joke"],
            "response": "Why did the quantum physicist never get lost? Because they knew all possible paths!"
        },

        "chemistry_joke": {
            "keywords": ["chemistry humor", "element joke", "periodic table joke"],
            "response": "Gold is the best element because it's AU-some!"
        },

        "biology_joke": {
            "keywords": ["biology humor", "dna joke", "cell joke"],
            "response": "Why did the biologist break up with the physicist? Because there was no chemistry, but lots of potential energy!"
        },

        "robot_joke": {
            "keywords": ["robot joke", "ai joke", "artificial intelligence joke"],
            "response": "Why did the robot go on a diet? It had too many megabytes!"
        },

        "robot_joke_2": {
            "keywords": ["robotics joke", "automation joke"],
            "response": "What do you call a robot that always takes the longest route? R2-detour!"
        },

        "space_joke": {
            "keywords": ["space joke", "astronomy joke", "planet joke", "star joke"],
            "response": "Why don't aliens eat clowns? Because they taste funny!"
        },

        "space_joke_2": {
            "keywords": ["moon joke", "mars joke", "galaxy joke"],
            "response": "What do you call a fake noodle? An impasta! (Space edition: What do you call a fake star? A conster-fake-tion!)"
        },

        "food_joke": {
            "keywords": ["food joke", "food humor", "cooking joke"],
            "response": "Why did the tomato turn red? Because it saw the salad dressing!"
        },

        "food_joke_2": {
            "keywords": ["fruit joke", "vegetable joke", "pizza joke"],
            "response": "What do you call cheese that isn't yours? Nacho cheese!"
        },

        "animal_joke": {
            "keywords": ["animal joke", "dog joke", "cat joke", "bird joke"],
            "response": "What do you call a bear with no teeth? A gummy bear!"
        },

        "animal_joke_2": {
            "keywords": ["fish joke", "horse joke", "elephant joke"],
            "response": "Why don't elephants use computers? They're afraid of the mouse!"
        },

        "music_joke": {
            "keywords": ["music joke", "musician joke", "instrument joke"],
            "response": "Why did the musician get locked out of his house? Because he lost his key signature!"
        },

        "music_joke_2": {
            "keywords": ["piano joke", "guitar joke", "drum joke"],
            "response": "Why are pianos hard to open? Because their keys are inside!"
        },

        "sports_joke": {
            "keywords": ["sports joke", "football joke", "cricket joke", "basketball joke"],
            "response": "Why did the football coach go to the bank? To get his quarter back!"
        },

        "sports_joke_2": {
            "keywords": ["tennis joke", "golf joke", "soccer joke"],
            "response": "Why don't golfers wear two pairs of pants? In case they get a hole in one!"
        },

        "weather_joke": {
            "keywords": ["weather joke", "rain joke", "sun joke", "cloud joke"],
            "response": "What did one raindrop say to the other? Two's company, three's a cloud!"
        },

        "weather_joke_2": {
            "keywords": ["storm joke", "wind joke", "snow joke"],
            "response": "Why did the weather report get an award? For having the most forecasts with 'chance of precipitation'!"
        },

        "time_joke": {
            "keywords": ["time joke", "clock joke", "watch joke", "calendar joke"],
            "response": "What did the digital clock say to the grandfather clock? 'Look, no hands!'"
        },

        "time_joke_2": {
            "keywords": ["hour joke", "minute joke", "second joke"],
            "response": "Why did the minute hand get promoted? Because it had 60 seconds of experience!"
        },

        "book_joke": {
            "keywords": ["book joke", "library joke", "reading joke"],
            "response": "Why did the book join the police? It wanted to work undercover!"
        },

        "book_joke_2": {
            "keywords": ["novel joke", "author joke", "page joke"],
            "response": "What's a book's favorite type of music? Anything with a good spine-tingling rhythm!"
        },

        "technology_joke": {
            "keywords": ["technology joke", "tech joke", "gadget joke", "device joke"],
            "response": "Why did the smartphone go to therapy? It had too many apps and couldn't find itself!"
        },

        "technology_joke_2": {
            "keywords": ["phone joke", "laptop joke", "tablet joke"],
            "response": "What do you call a computer that sings? A Dell!"
        },

        "internet_joke": {
            "keywords": ["internet joke", "wifi joke", "browser joke"],
            "response": "Why did the web developer go broke? Because he used up all his cache!"
        },

        "internet_joke_2": {
            "keywords": ["website joke", "server joke", "cloud joke"],
            "response": "Why was the computer cold? It left its Windows open!"
        },

        "car_joke": {
            "keywords": ["car joke", "automobile joke", "vehicle joke", "driving joke"],
            "response": "Why did the car get a ticket? For parking in a no-parking zone with its engine running—it was idling illegally!"
        },

        "car_joke_2": {
            "keywords": ["tire joke", "engine joke", "road joke"],
            "response": "What do you call a car that's not yours? A stolen vehicle! (Just kidding, please don't steal cars.)"
        },

        "travel_joke": {
            "keywords": ["travel joke", "airplane joke", "passport joke", "tourist joke"],
            "response": "Why did the airplane break up with the runway? It needed space!"
        },

        "travel_joke_2": {
            "keywords": ["train joke", "bus joke", "ship joke"],
            "response": "What do you call a train that sneezes? A-choo-choo train!"
        },

        "work_joke": {
            "keywords": ["work joke", "office joke", "boss joke", "meeting joke"],
            "response": "Why did the employee bring a ladder to work? They heard it was a high-paying job!"
        },

        "work_joke_2": {
            "keywords": ["job joke", "career joke", "salary joke"],
            "response": "What's an astronaut's favorite part of a computer? The space bar!"
        },

        "school_joke": {
            "keywords": ["school joke", "teacher joke", "classroom joke", "homework joke"],
            "response": "Why did the student eat his homework? Because the teacher said it was a piece of cake!"
        },

        "school_joke_2": {
            "keywords": ["pencil joke", "eraser joke", "notebook joke"],
            "response": "Why did the pencil go to school? To get a little sharper!"
        },

        "money_joke": {
            "keywords": ["money joke", "bank joke", "coin joke", "dollar joke"],
            "response": "Why did the dollar bill go to therapy? It had too many issues!"
        },

        "money_joke_2": {
            "keywords": ["rich joke", "poor joke", "wealth joke"],
            "response": "What did the penny say to the other penny? We make cents together!"
        },

        "holiday_joke": {
            "keywords": ["holiday joke", "christmas joke", "diwali joke", "eid joke"],
            "response": "What do you call a snowman with a six-pack? An abdominal snowman!"
        },

        "holiday_joke_2": {
            "keywords": ["festival joke", "celebration joke", "party joke"],
            "response": "Why did the Christmas tree go to the barber? It needed a trim!"
        },

        "language_joke": {
            "keywords": ["language joke", "grammar joke", "vocabulary joke"],
            "response": "Why did the comma break up with the apostrophe? It felt too possessive!"
        },

        "language_joke_2": {
            "keywords": ["punctuation joke", "sentence joke", "word joke"],
            "response": "What's a verb's favorite game? Hide and seek, because it's always action-packed!"
        },

        "history_joke": {
            "keywords": ["history joke", "historical joke", "ancient joke"],
            "response": "Why did Julius Caesar buy crayons? He wanted to Mark Antony!"
        },

        "history_joke_2": {
            "keywords": ["king joke", "queen joke", "war joke"],
            "response": "What was the spider doing on the computer? Searching the web!"
        },

        "geography_joke": {
            "keywords": ["geography joke", "map joke", "country joke", "city joke"],
            "response": "Why did the geography teacher break up with the geometry teacher? Because they had different points of view!"
        },

        "geography_joke_2": {
            "keywords": ["river joke", "mountain joke", "ocean joke"],
            "response": "What did the ocean say to the shore? Nothing, it just waved!"
        },

        "knock_knock_joke": {
            "keywords": ["knock knock", "knock knock joke"],
            "response": "Knock knock. Who's there? Lettuce. Lettuce who? Lettuce in, it's cold out here!"
        },

        "knock_knock_joke_2": {
            "keywords": ["knock knock humor", "door joke"],
            "response": "Knock knock. Who's there? Cow says. Cow says who? No, cow says moo!"
        },

        "dad_joke": {
            "keywords": ["dad joke", "father joke", "pun joke"],
            "response": "I'm reading a book on anti-gravity. It's impossible to put down!"
        },

        "dad_joke_2": {
            "keywords": ["parent joke", "family joke", "clean joke"],
            "response": "Why don't skeletons fight each other? They don't have the guts!"
        },

        "light_bulb_joke": {
            "keywords": ["light bulb joke", "how many does it take"],
            "response": "How many engineers does it take to change a light bulb? None, they'll just define darkness as the new standard!"
        },

        "light_bulb_joke_2": {
            "keywords": ["bulb joke", "lamp joke", "electricity joke"],
            "response": "How many programmers does it take to change a light bulb? None, it's a hardware problem!"
        },

        "bar_joke": {
            "keywords": ["bar joke", "bartender joke", "drink joke"],
            "response": "A neutron walks into a bar and asks, 'How much for a drink?' The bartender says, 'For you, no charge!'"
        },

        "bar_joke_2": {
            "keywords": ["pub joke", "alcohol joke", "beer joke"],
            "response": "Why did the beer file a police report? It was mugged!"
        },

        "medical_joke": {
            "keywords": ["medical joke", "doctor joke", "hospital joke"],
            "response": "Why did the doctor carry a red pen? In case they needed to draw blood!"
        },

        "medical_joke_2": {
            "keywords": ["nurse joke", "patient joke", "medicine joke"],
            "response": "What do you call a doctor who fixes websites? A URL-ologist!"
        },

        "legal_joke": {
            "keywords": ["legal joke", "lawyer joke", "court joke"],
            "response": "Why did the lawyer go to the beach? To catch a wave... of objections!"
        },

        "legal_joke_2": {
            "keywords": ["judge joke", "jury joke", "case joke"],
            "response": "What do you call a lawyer who doesn't speak? A good start!"
        },

        "farm_joke": {
            "keywords": ["farm joke", "farmer joke", "crop joke"],
            "response": "Why did the farmer win an award? Because he was out-standing in his field!"
        },

        "farm_joke_2": {
            "keywords": ["tractor joke", "barn joke", "animal farm joke"],
            "response": "What do you call a pig that does karate? A pork chop!"
        },

        "construction_joke": {
            "keywords": ["construction joke", "builder joke", "hard hat joke"],
            "response": "Why did the construction worker bring a ladder to the bar? He heard the drinks were on the house!"
        },

        "construction_joke_2": {
            "keywords": ["hammer joke", "nail joke", "cement joke"],
            "response": "What did the wall say to the other wall? I'll meet you at the corner!"
        },

        "electrician_joke": {
            "keywords": ["electrician joke", "wiring joke", "outlet joke"],
            "response": "Why did the electrician get shocked? Because he wasn't properly grounded! (But seriously, always practice electrical safety!)"
        },

        "electrician_joke_2": {
            "keywords": ["wire joke", "fuse joke", "breaker joke"],
            "response": "How does an electrician say goodbye? Watt's up? ...Ohm my, I have to go!"
        },

        "plumber_joke": {
            "keywords": ["plumber joke", "pipe joke", "leak joke"],
            "response": "Why did the plumber go to art school? To learn how to draw a pipe!"
        },

        "plumber_joke_2": {
            "keywords": ["toilet joke", "sink joke", "faucet joke"],
            "response": "What did the sink say to the toilet? You look flushed!"
        },

        "clean_joke": {
            "keywords": ["clean joke", "family friendly joke", "kid friendly joke"],
            "response": "What do you call a bear with no socks on? Barefoot!"
        },

        "clean_joke_2": {
            "keywords": ["g rated joke", "appropriate joke"],
            "response": "Why did the cookie go to the doctor? Because it felt crummy!"
        },

        "short_joke": {
            "keywords": ["short joke", "quick joke", "one liner"],
            "response": "I used to be a baker, but I couldn't make enough dough."
        },

        "short_joke_2": {
            "keywords": ["brief joke", "simple joke", "easy joke"],
            "response": "What do you call a fish with no eyes? Fsh!"
        },

        "riddle": {
            "keywords": ["riddle", "puzzle", "brain teaser"],
            "response": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I? (An echo!)"
        },

        "riddle_2": {
            "keywords": ["riddle me this", "challenge", "mystery"],
            "response": "What has keys but can't open locks? (A piano!)"
        },

        "riddle_3": {
            "keywords": ["brain teaser", "logic puzzle", "think"],
            "response": "What has a head, a tail, is brown, and has no legs? (A penny!)"
        },

        "riddle_4": {
            "keywords": ["word puzzle", "thinking", "smart"],
            "response": "What comes once in a minute, twice in a moment, but never in a thousand years? (The letter 'M'!)"
        },

        "fun_fact": {
            "keywords": ["fun fact", "interesting fact", "did you know"],
            "response": "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly good to eat!"
        },

        "fun_fact_2": {
            "keywords": ["cool fact", "amazing fact", "trivia"],
            "response": "A group of flamingos is called a 'flamboyance'! Now that's a fancy word for a fancy bird."
        },

        "fun_fact_3": {
            "keywords": ["science fact", "nature fact", "world fact"],
            "response": "Bananas are berries, but strawberries aren't! In botanical terms, a berry has seeds inside, which bananas do, but strawberries have their seeds on the outside."
        },

        "fun_fact_4": {
            "keywords": ["technology fact", "computer fact", "internet fact"],
            "response": "The first computer virus was created in 1983 and was called the 'Elk Cloner'. It infected Apple II computers and displayed a poem on the screen."
        },

        "fun_fact_5": {
            "keywords": ["space fact", "astronomy fact", "planet fact"],
            "response": "A day on Venus is longer than a year on Venus! Venus takes 243 Earth days to rotate once on its axis, but only 225 Earth days to orbit the Sun."
        },

        "alvas_joke": {
            "keywords": ["alvas joke", "college humor alvas", "campus joke alvas"],
            "response": "Why did the Alvas College student bring a ladder to the library? To reach the high-level courses! (Just kidding, our library has all resources accessible!)"
        },

        "alvas_joke_2": {
            "keywords": ["alvas engineering joke", "alvas student joke"],
            "response": "How many Alvas engineering students does it take to change a light bulb? None, they're too busy building a robot to do it for them!"
        },

        "pun": {
            "keywords": ["pun", "wordplay", "play on words"],
            "response": "I used to be a baker, but I couldn't make enough dough. Now I'm a banker, and I'm rolling in it!"
        },

        "pun_2": {
            "keywords": ["clever pun", "smart wordplay"],
            "response": "I'm reading a book on anti-gravity. It's impossible to put down!"
        },

        "tech_pun": {
            "keywords": ["tech pun", "computer pun", "digital pun"],
            "response": "Why do programmers prefer dark mode? Because light attracts bugs!"
        },

        "science_pun": {
            "keywords": ["science pun", "physics pun", "chemistry pun"],
            "response": "I told a chemistry joke, but there was no reaction."
        },

        # General Conversation
        "weather": {
            "keywords": ["weather", "rain", "sunny", "temperature", "climate", "forecast", "hot", "cold", "humidity"],
            "response": "I'm sorry, I don't have access to current weather data. You might want to check a weather app or website for the latest information. However, I can talk about climate patterns, seasons, or meteorological concepts if you're interested!"
        },

        "help": {
            "keywords": ["help", "assist", "support", "guidance", "how to", "what can you do", "your capabilities"],
            "response": "I'm here to help! You can ask me about Alvas College, programming questions, electronics and communication topics, world geography, engineering disciplines, semiconductors, science topics, or just have a general conversation. Feel free to ask anything you're curious about!"
        },

        "about_user": {
            "keywords": ["about me", "who am i", "my name", "tell me about myself", "who do you think i am"],
            "response": "I'd love to know more about you! What's your name or what would you like to talk about? You can tell me about your interests, studies, work, or anything you'd like to share. I'm here to listen and learn about you!"
        },

        "hobbies": {
            "keywords": ["hobby", "hobbies", "interests", "like to do", "pastime", "leisure activities", "what do you do for fun"],
            "response": "I enjoy helping people learn and providing information! What are your hobbies? I can discuss various activities like reading, gaming, cooking, photography, music, sports, art, or any other interests you might have."
        },

        "food": {
            "keywords": ["food", "eat", "hungry", "restaurant", "cuisine", "cooking", "recipe", "meal", "dinner", "lunch", "breakfast", "snack"],
            "response": "Food is wonderful! What's your favorite cuisine or dish? I can talk about different types of food, cooking techniques, nutrition, food history, or recommend trying new dishes from around the world."
        },

        "sports": {
            "keywords": ["sports", "game", "football", "cricket", "basketball", "tennis", "soccer", "baseball", "hockey", "olympics", "athletics"],
            "response": "Sports are exciting! Which sports do you enjoy watching or playing? I can discuss different sports, famous athletes, major tournaments, sports science, or the benefits of physical activity."
        },

        "music": {
            "keywords": ["music", "song", "musician", "band", "concert", "genre", "listen to music", "favorite song"],
            "response": "Music is a universal language! What kind of music do you enjoy? I can talk about different genres, famous composers, musical instruments, music theory, or how music affects our emotions and brain."
        },

        "movies": {
            "keywords": ["movies", "film", "cinema", "movie", "hollywood", "bollywood", "netflix", "disney", "actor", "actress", "director"],
            "response": "Movies are a great form of entertainment! Do you have a favorite film or genre? I can discuss different types of movies, film history, famous directors, movie-making techniques, or recommend films from various eras and cultures."
        },

        "books": {
            "keywords": ["books", "reading", "novel", "author", "literature", "library", "bookstore", "fiction", "non-fiction"],
            "response": "Reading opens up new worlds! What kind of books do you enjoy? I can talk about different genres, famous authors, classic literature, the benefits of reading, or recommend books based on your interests."
        },

        "travel": {
            "keywords": ["travel", "vacation", "trip", "tourist", "destination", "passport", "airplane", "hotel", "beach", "mountain"],
            "response": "Travel broadens the mind! Where have you traveled or where would you like to go? I can discuss different countries, travel tips, cultural experiences, famous landmarks, or the benefits of exploring new places."
        },

        "family": {
            "keywords": ["family", "parents", "siblings", "children", "relatives", "family members", "mother", "father", "brother", "sister"],
            "response": "Family is important! Would you like to talk about your family? I can discuss family relationships, cultural differences in family structures, family traditions, or the role of family in different societies."
        },

        "friends": {
            "keywords": ["friends", "friendship", "best friend", "companions", "buddy", "pal", "social circle", "making friends"],
            "response": "Friends make life more meaningful! How are your friends? I can talk about the importance of friendship, how to maintain friendships, different types of friendships, or the social aspects of human relationships."
        },

        "work": {
            "keywords": ["work", "job", "career", "profession", "occupation", "office", "colleagues", "boss", "salary", "employment"],
            "response": "Work is a significant part of life! What do you do for work? I can discuss different careers, work-life balance, workplace skills, career development, or the changing nature of work in the modern world."
        },

        "study": {
            "keywords": ["study", "learning", "education", "school", "college", "university", "exam", "homework", "course", "subject"],
            "response": "Learning is a lifelong journey! What are you studying or interested in learning? I can discuss study techniques, different fields of study, educational systems, online learning, or help with academic topics."
        },

        "technology": {
            "keywords": ["technology", "tech", "gadgets", "devices", "smartphone", "computer", "internet", "social media", "innovation"],
            "response": "Technology shapes our world! What aspect of technology interests you? I can discuss the latest tech trends, the impact of technology on society, ethical considerations, or specific technologies like AI, blockchain, or robotics."
        },

        "health": {
            "keywords": ["health", "fitness", "exercise", "wellness", "diet", "nutrition", "mental health", "physical health", "healthy lifestyle"],
            "response": "Health is wealth! Are you interested in physical health, mental health, nutrition, or fitness? I can discuss healthy habits, exercise routines, mindfulness, balanced diets, or general wellness tips (though I'm not a substitute for medical advice)."
        },

        "money": {
            "keywords": ["money", "finance", "budget", "saving", "investment", "bank", "currency", "economy", "financial planning"],
            "response": "Money matters are important! Would you like to discuss personal finance, budgeting, saving strategies, basic investment concepts, or economic principles? I can provide general information about financial literacy."
        },

        "pets": {
            "keywords": ["pets", "dog", "cat", "animal", "pet care", "veterinary", "adoption", "dog breeds", "cat breeds"],
            "response": "Pets bring so much joy! Do you have any pets or are you thinking of getting one? I can talk about different types of pets, pet care, animal behavior, adoption considerations, or fun facts about various animals."
        },

        "fashion": {
            "keywords": ["fashion", "clothing", "style", "outfit", "dress", "shoes", "accessories", "trends", "designer"],
            "response": "Fashion is a form of self-expression! Are you interested in clothing styles, fashion history, current trends, or sustainable fashion? I can discuss how fashion varies across cultures and its role in society."
        },

        "art": {
            "keywords": ["art", "painting", "drawing", "sculpture", "gallery", "museum", "artist", "creative", "visual arts"],
            "response": "Art enriches our lives! What type of art do you appreciate? I can discuss different art forms, famous artists, art movements throughout history, artistic techniques, or the role of art in culture and society."
        },

        "news": {
            "keywords": ["news", "current events", "headlines", "newspaper", "media", "journalism", "world news", "local news"],
            "response": "I don't have access to real-time news updates, but I can discuss the importance of staying informed, different types of media, journalism ethics, or historical events. For current news, you might want to check reputable news websites or apps."
        },

        "politics": {
            "keywords": ["politics", "government", "election", "democracy", "policy", "political party", "vote", "leader"],
            "response": "Politics affects many aspects of life. I can discuss general political systems, democratic principles, the importance of civic participation, or political theories. However, I don't discuss specific current political figures or parties to remain neutral and informative."
        },

        "religion": {
            "keywords": ["religion", "god", "spiritual", "faith", "belief", "worship", "church", "temple", "mosque", "prayer"],
            "response": "Religion and spirituality are important to many people. I can discuss different world religions, their basic beliefs and practices, religious history, or comparative religion in an educational context, while respecting all beliefs and perspectives."
        },

        "culture": {
            "keywords": ["culture", "cultural", "tradition", "custom", "heritage", "ethnicity", "multicultural", "diversity"],
            "response": "Culture shapes who we are! Would you like to discuss specific cultures, cultural traditions, multiculturalism, or how culture influences art, food, music, and social norms around the world?"
        },

        "history": {
            "keywords": ["history", "historical", "past", "ancient", "medieval", "modern history", "historical events", "timeline"],
            "response": "History helps us understand the present! What historical period or event interests you? I can discuss ancient civilizations, medieval times, modern history, important historical figures, or how historical events have shaped our world."
        },

        "science": {
            "keywords": ["science", "scientific", "discovery", "research", "experiment", "physics", "chemistry", "biology", "astronomy"],
            "response": "Science explains how our universe works! Which scientific field interests you? I can discuss physics, chemistry, biology, astronomy, earth sciences, scientific methods, famous discoveries, or how science impacts our daily lives."
        },

        "nature": {
            "keywords": ["nature", "environment", "forest", "ocean", "mountains", "animals", "plants", "ecosystem", "conservation"],
            "response": "Nature is amazing! Are you interested in wildlife, ecosystems, conservation, natural landscapes, or environmental issues? I can discuss biodiversity, national parks, endangered species, or how we can protect our natural world."
        },

        "space": {
            "keywords": ["space", "universe", "cosmos", "stars", "planets", "galaxy", "astronomy", "space exploration", "nasa"],
            "response": "The universe is vast and fascinating! Would you like to talk about planets, stars, galaxies, black holes, space exploration, astronauts, or the possibility of life beyond Earth? Space science has endless interesting topics!"
        },

        "dreams": {
            "keywords": ["dreams", "dream", "sleep", "nightmare", "dream interpretation", "subconscious", "lucid dreaming"],
            "response": "Dreams are mysterious! Are you curious about why we dream, dream interpretation, lucid dreaming, or the science of sleep? I can discuss different theories about dreams and their significance in psychology and culture."
        },

        "emotions": {
            "keywords": ["emotions", "feelings", "happy", "sad", "angry", "excited", "nervous", "emotional", "mood"],
            "response": "Emotions are part of being human! How are you feeling today? I can discuss different emotions, emotional intelligence, coping strategies for difficult feelings, or how emotions influence our thoughts and behaviors."
        },

        "goals": {
            "keywords": ["goals", "ambition", "aspiration", "dream", "achievement", "success", "future plans", "life goals"],
            "response": "Goals give us direction! What are your goals or aspirations? I can discuss goal-setting techniques, motivation, overcoming obstacles, different types of goals (personal, professional, academic), or how to break big goals into manageable steps."
        },

        "problems": {
            "keywords": ["problems", "trouble", "difficulty", "challenge", "issue", "problem solving", "dilemma", "obstacle"],
            "response": "Everyone faces challenges sometimes. Would you like to talk about a problem you're facing? While I can't solve personal problems, I can discuss general problem-solving strategies, different perspectives, or just listen. For serious issues, please consider talking to a qualified professional."
        },

        "advice": {
            "keywords": ["advice", "suggestion", "recommendation", "guidance", "what should i do", "need advice"],
            "response": "I can offer general advice on many topics, but for personal or important decisions, you should consult with appropriate professionals. What area would you like general advice about? I can provide information, suggestions, and different perspectives to help you think through situations."
        },

        "jokes": {
            "keywords": ["jokes", "joke", "humor", "funny", "comedy", "laugh", "puns", "stand-up"],
            "response": "I love humor! Would you like to hear a joke, or talk about different types of comedy? I can tell you some clean jokes, discuss famous comedians, comedy styles, or why humor is important for our wellbeing."
        },

        "games": {
            "keywords": ["games", "gaming", "video games", "board games", "card games", "play", "game design", "esports"],
            "response": "Games are fun and can be educational too! Do you play video games, board games, or sports? I can discuss different game genres, game design, the benefits of gaming, famous games, or even suggest some classic games to try."
        },

        "weekend": {
            "keywords": ["weekend", "friday", "saturday", "sunday", "weekend plans", "what are you doing this weekend"],
            "response": "Weekends are great for relaxation and activities! Do you have any weekend plans? I can discuss different weekend activities, how people around the world spend weekends, or the history of the weekend as a concept."
        },

        "holidays": {
            "keywords": ["holidays", "vacation", "festival", "celebration", "christmas", "diwali", "eid", "holiday season"],
            "response": "Holidays bring people together! What's your favorite holiday or celebration? I can discuss different cultural and religious holidays around the world, holiday traditions, or the history behind various celebrations."
        },

        "seasons": {
            "keywords": ["seasons", "spring", "summer", "autumn", "fall", "winter", "seasonal", "changing seasons"],
            "response": "The changing seasons are beautiful! Which season do you prefer? I can discuss why we have seasons, how different cultures celebrate seasonal changes, seasonal activities, or how seasons affect nature and human life."
        },

        "age": {
            "keywords": ["age", "how old", "birthday", "years old", "aging", "growing up", "age groups"],
            "response": "Age is just a number! Would you like to talk about aging, different life stages, birthday traditions, or how attitudes toward age vary across cultures? I don't have a specific age since I'm an AI, but I'm constantly learning and updating!"
        },

        "birthday": {
            "keywords": ["birthday", "birth date", "celebration", "birthday party", "happy birthday", "birthday wishes"],
            "response": "Birthdays are special occasions! Is it your birthday or someone's birthday? I can discuss birthday traditions around the world, the history of birthday celebrations, or different ways people celebrate this important day."
        },

        "memory": {
            "keywords": ["memory", "remember", "recall", "forget", "memories", "childhood memories", "memory techniques"],
            "response": "Memories shape who we are! Are you interested in how memory works, memory improvement techniques, different types of memory, or why we remember certain things and forget others? I can discuss the science and psychology of memory."
        },

        "imagination": {
            "keywords": ["imagination", "creative", "fantasy", "imagine", "creativity", "innovative", "daydream"],
            "response": "Imagination drives innovation! How do you use your imagination? I can discuss the importance of imagination for creativity, problem-solving, art, science, and how to nurture imaginative thinking in children and adults."
        },

        "wisdom": {
            "keywords": ["wisdom", "wise", "knowledge", "insight", "experience", "philosophy", "life lessons"],
            "response": "Wisdom comes with experience and reflection! What does wisdom mean to you? I can discuss different philosophical perspectives on wisdom, famous wise sayings, or how wisdom differs from mere knowledge."
        },

        "luck": {
            "keywords": ["luck", "lucky", "unlucky", "fortune", "chance", "probability", "superstition", "good luck"],
            "response": "Luck is an interesting concept! Do you believe in luck? I can discuss probability, superstitions around the world, the psychology of luck, famous lucky symbols, or how people create their own 'luck' through preparation and opportunity."
        },

        "time_management": {
            "keywords": ["time management", "productivity", "procrastination", "schedule", "busy", "efficient", "organize time"],
            "response": "Time management is a valuable skill! Do you struggle with managing time? I can discuss different time management techniques, productivity strategies, tools for organization, or how to balance work, study, and leisure effectively."
        },

        "stress": {
            "keywords": ["stress", "anxiety", "pressure", "overwhelmed", "stress relief", "relaxation", "calm", "worried"],
            "response": "Stress is a common experience in modern life. I can discuss general stress management techniques, relaxation methods, mindfulness, work-life balance, or the difference between normal stress and chronic stress. For serious stress or anxiety, please consider speaking with a mental health professional."
        },

        "sleep": {
            "keywords": ["sleep", "insomnia", "tired", "rest", "bedtime", "dream", "nap", "sleep schedule"],
            "response": "Sleep is essential for health! Are you having trouble sleeping or just curious about sleep science? I can discuss sleep cycles, sleep hygiene tips, why we need sleep, dreams, or common sleep disorders and when to seek help."
        },

        "exercise": {
            "keywords": ["exercise", "workout", "gym", "yoga", "running", "fitness", "physical activity", "sports"],
            "response": "Exercise is great for body and mind! What type of exercise do you enjoy? I can discuss different forms of exercise, their benefits, creating a balanced fitness routine, exercise safety, or how physical activity improves mental health."
        },

        "meditation": {
            "keywords": ["meditation", "mindfulness", "yoga", "breathing", "calm", "peace", "relaxation", "mental clarity"],
            "response": "Meditation and mindfulness have many benefits! Are you interested in starting a meditation practice or learning more about it? I can discuss different meditation techniques, their benefits for mental health, mindfulness exercises, or the science behind meditation."
        },

        "shopping": {
            "keywords": ["shopping", "buy", "purchase", "store", "mall", "online shopping", "retail therapy", "consumer"],
            "response": "Shopping can be practical or recreational! Do you prefer online or in-store shopping? I can discuss consumer psychology, smart shopping tips, the environmental impact of consumption, or how shopping habits have changed with technology."
        },

        "cooking": {
            "keywords": ["cooking", "baking", "recipe", "kitchen", "culinary", "chef", "meal prep", "food preparation"],
            "response": "Cooking is both an art and a science! Do you enjoy cooking? I can discuss different cooking techniques, international cuisines, kitchen safety, meal planning, or how cooking at home can be healthier and more economical than eating out."
        },

        "gardening": {
            "keywords": ["gardening", "garden", "plants", "flowers", "vegetables", "horticulture", "green thumb", "outdoor"],
            "response": "Gardening connects us with nature! Do you have a garden or indoor plants? I can discuss gardening basics, different types of gardens, plant care, the benefits of gardening for mental health, or sustainable gardening practices."
        },

        "photography": {
            "keywords": ["photography", "photo", "camera", "picture", "photographer", "landscape", "portrait", "digital photography"],
            "response": "Photography captures moments in time! Are you a photographer or interested in learning? I can discuss photography techniques, different genres (portrait, landscape, macro), camera equipment basics, composition rules, or the history of photography."
        },

        "writing": {
            "keywords": ["writing", "write", "author", "poetry", "journal", "creative writing", "essay", "storytelling"],
            "response": "Writing is a powerful form of expression! Do you enjoy writing? I can discuss different writing styles, creative writing tips, journaling benefits, famous writers, writing techniques, or how to overcome writer's block."
        },

        "language": {
            "keywords": ["language", "linguistics", "bilingual", "translation", "grammar", "vocabulary", "learn a language"],
            "response": "Language is fundamental to human communication! Are you interested in learning a new language or linguistics? I can discuss language learning strategies, interesting linguistic facts, language families, translation challenges, or how languages evolve over time."
        },

        "future": {
            "keywords": ["future", "tomorrow", "next year", "future plans", "predictions", "what will happen", "technology future"],
            "response": "The future is full of possibilities! What are your thoughts about the future? I can discuss technological predictions, future challenges humanity might face, how to plan for the future, or different perspectives on what the future might hold."
        },

        "past": {
            "keywords": ["past", "yesterday", "old times", "nostalgia", "history", "childhood", "looking back"],
            "response": "The past helps us understand where we came from! Are you feeling nostalgic or interested in historical perspectives? I can discuss the importance of studying history, how the past influences the present, or why we sometimes feel nostalgic for earlier times."
        },

        "present": {
            "keywords": ["present", "now", "current moment", "today", "living in the moment", "mindfulness", "present time"],
            "response": "The present moment is all we truly have! Are you interested in mindfulness or living in the present? I can discuss the importance of being present, mindfulness techniques, balancing planning for the future with enjoying today, or how to appreciate the current moment."
        },

        "home": {
            "keywords": ["home", "house", "apartment", "living space", "home decor", "homely", "home improvement"],
            "response": "Home is where the heart is! Would you like to talk about home decor, interior design, creating a comfortable living space, or the concept of 'home' in different cultures? I can discuss how our living environments affect our wellbeing."
        },

        "city": {
            "keywords": ["city", "urban", "metropolis", "downtown", "city life", "skyscraper", "urban planning"],
            "response": "Cities are hubs of culture and activity! Do you live in or prefer cities? I can discuss urban planning, the pros and cons of city living, famous cities around the world, urban sustainability, or how cities have evolved throughout history."
        },

        "countryside": {
            "keywords": ["countryside", "rural", "village", "farm", "nature", "peaceful", "agriculture", "small town"],
            "response": "The countryside offers peace and natural beauty! Do you enjoy rural areas? I can discuss rural life, agriculture, the differences between urban and rural living, environmental benefits of countryside preservation, or challenges facing rural communities."
        },

        "ocean": {
            "keywords": ["ocean", "sea", "beach", "marine", "waves", "coast", "sailing", "underwater"],
            "response": "The ocean covers most of our planet and is full of mystery! Are you interested in marine life, ocean conservation, beach activities, or oceanography? I can discuss the importance of oceans, marine ecosystems, or fascinating ocean facts."
        },

        "mountains": {
            "keywords": ["mountains", "mountain", "peak", "hiking", "climbing", "alps", "himalayas", "volcano"],
            "response": "Mountains are majestic and challenging! Do you enjoy mountain activities? I can discuss famous mountain ranges, mountain ecology, climbing, hiking tips, mountain weather patterns, or the cultural significance of mountains in different societies."
        },

        "desert": {
            "keywords": ["desert", "arid", "sand", "camel", "oasis", "dry", "sahara", "desert life"],
            "response": "Deserts are extreme yet beautiful environments! Are you curious about desert ecosystems, desert survival, or desert cultures? I can discuss desert plants and animals, how people adapt to desert life, famous deserts around the world, or desert conservation."
        },

        "forest": {
            "keywords": ["forest", "woods", "trees", "jungle", "rainforest", "wildlife", "camping", "deforestation"],
            "response": "Forests are vital for our planet! Would you like to discuss different types of forests, forest ecosystems, conservation efforts, forest recreation, or the importance of trees for climate regulation and biodiversity?"
        },

        "river": {
            "keywords": ["river", "stream", "waterfall", "lake", "waterway", "delta", "river basin", "freshwater"],
            "response": "Rivers are life-giving waterways! Are you interested in famous rivers, river ecosystems, the role of rivers in human civilization, water conservation, or recreational activities like fishing and boating? Rivers have shaped human history and geography."
        },

        "sky": {
            "keywords": ["sky", "clouds", "blue sky", "sunset", "sunrise", "horizon", "atmosphere", "heavens"],
            "response": "The sky is ever-changing and beautiful! Do you enjoy watching sunsets, cloud formations, or the night sky? I can discuss atmospheric science, weather phenomena, astronomy, or the cultural and artistic significance of skies throughout history."
        },

        # Alvas College Information
        "alvas_college": {
            "keywords": ["alvas college", "alvas", "alva's", "mangalore college"],
            "response": "Alvas College is a prominent educational institution located in Mangalore, Karnataka, India. It's part of the Alva's Education Foundation and offers various undergraduate and postgraduate programs."
        },

        "alvas_location": {
            "keywords": ["alvas location", "where is alvas", "alvas address"],
            "response": "Alvas College is located in Vidyagiri, Dakshina Kannada district, Mangalore, Karnataka, India. The campus is situated in a beautiful location with modern facilities."
        },

        "alvas_courses": {
            "keywords": ["alvas courses", "what courses", "programs at alvas"],
            "response": "Alvas College offers a wide range of courses including Engineering (CSE, ECE, Mechanical, Civil), MBA, MCA, Pharmacy, Nursing, Physiotherapy, and various Arts and Science programs."
        },

        "alvas_engineering": {
            "keywords": ["alvas engineering", "btech at alvas", "engineering courses"],
            "response": "Alvas College offers B.Tech programs in Computer Science & Engineering, Electronics & Communication Engineering, Mechanical Engineering, and Civil Engineering."
        },

        "alvas_admission": {
            "keywords": ["alvas admission", "how to join alvas", "alvas entrance"],
            "response": "Admission to Alvas College is based on merit in qualifying examinations and entrance tests like CET/KCET. For detailed admission procedures, please visit the official website or contact the admission office."
        },

        "alvas_facilities": {
            "keywords": ["alvas facilities", "campus facilities", "alvas infrastructure"],
            "response": "Alvas College has excellent facilities including modern classrooms, well-equipped laboratories, library, sports complex, hostels, cafeteria, and transportation services."
        },

        "alvas_placement": {
            "keywords": ["alvas placement", "jobs at alvas", "alvas career"],
            "response": "Alvas College has a good placement record with companies like Infosys, TCS, Wipro, and many others visiting the campus for recruitment."
        },

        # Electronics and Communication Topics
        "electronics": {
            "keywords": ["electronics", "electronic", "circuit", "electronic engineering", "electronic devices"],
            "response": "Electronics is the branch of physics and engineering that deals with the flow of electrons in circuits and devices. It involves designing and building electronic circuits, components, and systems for applications ranging from consumer devices to industrial equipment. Major areas include analog electronics, digital electronics, power electronics, and microelectronics."
        },

        "communication": {
            "keywords": ["communication", "telecommunication", "signal", "communication systems", "telecom engineering"],
            "response": "Communication engineering deals with the transmission of information through various mediums using electronic systems. This includes wired communication (optical fiber, copper cables) and wireless communication (radio, microwave, satellite). Key concepts include modulation, coding, signal processing, and network protocols to ensure reliable information transfer over distances."
        },

        "transistor": {
            "keywords": ["transistor", "transistors", "bjt", "mosfet", "transistor amplifier"],
            "response": "A transistor is a semiconductor device used to amplify or switch electronic signals. Bipolar Junction Transistors (BJTs) use both electron and hole charge carriers, while Field-Effect Transistors (FETs) like MOSFETs use an electric field to control conductivity. Transistors are fundamental building blocks of modern electronics, enabling amplification in audio systems, switching in digital circuits, and processing in microprocessors."
        },

        "resistor": {
            "keywords": ["resistor", "resistance", "ohm's law", "variable resistor", "resistor color code"],
            "response": "A resistor is a passive electrical component that opposes the flow of current, converting electrical energy into heat. Measured in ohms (Ω), resistors are used to control voltage and current in circuits, set bias points in transistors, and limit current to protect components. Types include fixed resistors, variable resistors (potentiometers), and specialized resistors like thermistors and light-dependent resistors (LDRs)."
        },

        "capacitor": {
            "keywords": ["capacitor", "capacitance", "electrolytic capacitor", "ceramic capacitor", "capacitor types"],
            "response": "A capacitor is an electronic component that stores electrical energy in an electric field between conductive plates separated by an insulator (dielectric). Measured in farads (F), capacitors are used for filtering noise, smoothing power supplies, timing circuits, coupling/decoupling signals, and energy storage. Types include ceramic, electrolytic, film, and supercapacitors with different characteristics for various applications."
        },

        "inductor": {
            "keywords": ["inductor", "inductance", "coil", "choke", "inductor types"],
            "response": "An inductor is a passive electrical component that stores energy in a magnetic field when current flows through its coiled conductor. Measured in henries (H), inductors oppose changes in current. Used in filters (with capacitors to form LC circuits), transformers, energy storage in power supplies, and radio frequency (RF) circuits. Types include air core, iron core, and toroidal inductors with different inductance values and frequency responses."
        },

        "diode": {
            "keywords": ["diode", "diodes", "rectifier diode", "zener diode", "led diode", "schottky diode"],
            "response": "A diode is a semiconductor device that allows current to flow primarily in one direction (forward bias) while blocking it in the opposite direction (reverse bias). Types include rectifier diodes (AC to DC conversion), Zener diodes (voltage regulation), LEDs (light emission), photodiodes (light detection), Schottky diodes (fast switching), and varactor diodes (voltage-variable capacitance). Diodes are essential for power conversion, signal demodulation, and circuit protection."
        },

        "microcontroller": {
            "keywords": ["microcontroller", "arduino", "raspberry pi", "microprocessor", "embedded controller"],
            "response": "A microcontroller is a compact integrated circuit containing a processor core, memory (RAM/ROM), and programmable input/output peripherals on a single chip. Unlike microprocessors (which require external components), microcontrollers are self-contained systems for embedded applications. Popular platforms include Arduino (simplified programming), Raspberry Pi (more powerful, runs Linux), PIC, and AVR microcontrollers. Used in automation, robotics, IoT devices, and consumer electronics."
        },

        "antenna": {
            "keywords": ["antenna", "antennas", "dipole antenna", "yagi antenna", "antenna design", "rf antenna"],
            "response": "An antenna is a transducer that converts electrical signals into electromagnetic waves for transmission (transmitter) or vice versa for reception (receiver). Key parameters: gain, directivity, bandwidth, impedance. Types include dipole (basic), monopole, Yagi-Uda (directional), parabolic (high gain), patch (compact for PCBs), and helical (circular polarization). Antenna design considers frequency, radiation pattern, and application (broadcasting, cellular, Wi-Fi, satellite)."
        },

        "modulation": {
            "keywords": ["modulation", "am", "fm", "pm", "digital modulation", "modulation techniques"],
            "response": "Modulation is the process of varying a carrier signal's properties (amplitude, frequency, or phase) to encode information for transmission. Analog modulation: AM (Amplitude Modulation), FM (Frequency Modulation), PM (Phase Modulation). Digital modulation: ASK, FSK, PSK, QAM (Quadrature Amplitude Modulation). Modulation enables efficient use of bandwidth, resistance to noise, and simultaneous transmission of multiple signals (multiplexing). Demodulation extracts the original information at the receiver."
        },

        "fiber_optics": {
            "keywords": ["fiber optics", "optical fiber", "fiber optic cable", "optical communication", "lightwave communication"],
            "response": "Fiber optics uses light pulses to transmit data through thin glass or plastic fibers. Core (light travels) surrounded by cladding (reflects light back) and protective coating. Advantages: high bandwidth (terabits per second), low loss (long distances without amplification), immunity to electromagnetic interference, security. Used in telecommunications (long-haul networks), internet backbones, cable TV, medical imaging (endoscopy), and industrial sensors. Single-mode (long distance) and multi-mode (short distance) fibers available."
        },

        "satellite": {
            "keywords": ["satellite", "satellite communication", "geostationary satellite", "satellite orbits", "vsat"],
            "response": "Satellite communication uses artificial satellites as relay stations to transmit signals between Earth stations over long distances. Satellite types: GEO (Geostationary - fixed position), LEO (Low Earth Orbit - lower latency), MEO (Medium Earth Orbit - navigation systems like GPS). Applications: television broadcasting (DTH), internet services (VSAT), navigation (GPS, GLONASS), weather monitoring, military communications. Satellite systems include uplink (Earth to satellite), transponder (amplify/retransmit), and downlink (satellite to Earth)."
        },

        "integrated_circuits": {
            "keywords": ["integrated circuits", "ic", "microchip", "chip design", "analog ic", "digital ic"],
            "response": "Integrated circuits (ICs) are semiconductor wafers containing thousands to billions of tiny resistors, capacitors, diodes, and transistors fabricated together. Classification: SSI (Small Scale), MSI, LSI, VLSI (Very Large Scale), ULSI. Types: analog ICs (amplifiers, regulators), digital ICs (logic gates, microprocessors), mixed-signal ICs (ADC/DAC). IC manufacturing involves photolithography, doping, and packaging. ICs revolutionized electronics by reducing size, cost, and power consumption while increasing reliability and performance."
        },

        "pcb": {
            "keywords": ["pcb", "printed circuit board", "circuit board", "pcb design", "pcb manufacturing"],
            "response": "A Printed Circuit Board (PCB) mechanically supports and electrically connects electronic components using conductive tracks, pads, and layers laminated onto a non-conductive substrate. Types: single-sided, double-sided, multi-layer, flexible, rigid-flex. PCB design involves schematic capture, component placement, routing (track layout), and design rule checking. Manufacturing: etching copper layers, drilling holes, plating, solder mask application, silkscreen printing. PCBs enable mass production of reliable electronic assemblies."
        },

        "oscilloscope": {
            "keywords": ["oscilloscope", "oscilloscope measurement", "digital oscilloscope", "analog oscilloscope", "waveform analysis"],
            "response": "An oscilloscope is an electronic test instrument that graphically displays varying signal voltages as a function of time. Key parameters: bandwidth, sample rate, channels, memory depth. Types: analog (CRT display), digital storage oscilloscopes (DSO - store and analyze), mixed-signal oscilloscopes (MSO - digital and analog), sampling oscilloscopes (high frequency). Used to measure amplitude, frequency, rise time, phase, and detect anomalies in electronic circuits for debugging and characterization."
        },

        "multimeter": {
            "keywords": ["multimeter", "digital multimeter", "multimeter measurement", "voltmeter", "ammeter", "ohmmeter"],
            "response": "A multimeter is a versatile electronic measuring instrument that combines several measurement functions: voltage (AC/DC), current (AC/DC), resistance, and often continuity, capacitance, frequency, temperature. Types: analog (moving coil meter), digital (LCD display with higher accuracy). Digital multimeters (DMM) may include features like auto-ranging, data logging, and connectivity. Essential for troubleshooting circuits, verifying component values, and ensuring proper electrical parameters in electronic systems."
        },

        "signal_generator": {
            "keywords": ["signal generator", "function generator", "waveform generator", "rf signal generator", "arbitrary waveform generator"],
            "response": "A signal generator produces electronic signals (waveforms) for testing, calibration, and development of electronic equipment. Types: function generators (basic waveforms: sine, square, triangle, sawtooth), RF signal generators (radio frequencies with modulation), arbitrary waveform generators (user-defined waveforms), pulse generators. Parameters: frequency range, amplitude, modulation capabilities (AM, FM, PM). Used to test amplifiers, filters, communication receivers, and simulate sensor signals in development."
        },

        "power_supply": {
            "keywords": ["power supply", "dc power supply", "switching power supply", "linear power supply", "power supply design"],
            "response": "A power supply converts input power (AC mains or DC) to regulated DC output for electronic circuits. Types: linear (simple, low noise but inefficient), switching (SMPS - efficient, compact but noisy), unregulated, programmable. Key specifications: voltage/current rating, regulation (line/load), ripple, efficiency. Power supplies may include protection features: overvoltage, overcurrent, thermal shutdown. Essential for powering all electronic systems from small devices to industrial equipment."
        },

        "amplifier": {
            "keywords": ["amplifier", "electronic amplifier", "audio amplifier", "rf amplifier", "operational amplifier"],
            "response": "An amplifier increases the power, voltage, or current of a signal. Classified by: application (audio, RF, instrumentation), frequency range (DC, audio, RF), class of operation (A, B, AB, C, D for efficiency/linearity), technology (tube, transistor, op-amp). Key parameters: gain, bandwidth, distortion, noise, power output. Operational amplifiers (op-amps) are versatile integrated circuits used in amplification, filtering, mathematical operations. Amplifiers are fundamental in audio systems, communications, and signal processing."
        },

        "filter": {
            "keywords": ["filter", "electronic filter", "low pass filter", "high pass filter", "bandpass filter", "active filter"],
            "response": "An electronic filter selectively passes or rejects frequency components of a signal. Types by frequency response: low-pass (passes low frequencies), high-pass (passes high frequencies), band-pass (passes a band), band-stop/notch (rejects a band). Implementation: passive (R, L, C components), active (with amplifiers like op-amps), digital (signal processing). Filters are used to remove noise, separate signals, shape frequency response in audio systems, communications, and instrumentation."
        },

        "oscillator": {
            "keywords": ["oscillator", "electronic oscillator", "crystal oscillator", "lc oscillator", "rc oscillator", "clock generator"],
            "response": "An oscillator generates a periodic, oscillating electronic signal (sine wave, square wave) without an input signal, using positive feedback. Types: RC oscillators (low frequency), LC oscillators (radio frequency), crystal oscillators (high stability and precision), voltage-controlled oscillators (VCO - frequency controlled by voltage). Applications: clock signals for digital circuits, carrier waves in transmitters, local oscillators in receivers, tone generation in audio, and timing references."
        },

        "mixer": {
            "keywords": ["mixer", "rf mixer", "frequency mixer", "audio mixer", "signal mixer"],
            "response": "A mixer is a nonlinear electronic circuit that combines two signals to produce new frequencies equal to the sum and difference of the original frequencies. In RF systems, mixers are used for frequency conversion (up-conversion in transmitters, down-conversion in receivers). Types: passive (diode ring), active (transistor-based). Key parameters: conversion gain/loss, isolation, noise figure. Audio mixers combine multiple audio signals with level control, equalization, and effects."
        },

        "demodulator": {
            "keywords": ["demodulator", "detector", "am demodulation", "fm demodulation", "demodulation circuit"],
            "response": "A demodulator (or detector) extracts the original information-bearing signal from a modulated carrier wave at the receiver. AM demodulation: envelope detector (simple diode-capacitor) or synchronous detection. FM demodulation: frequency discriminator, phase-locked loop (PLL), or quadrature detector. Digital demodulators recover bits from modulated signals using techniques matched to the modulation scheme (PSK, QAM). Demodulation is the inverse process of modulation, crucial for recovering transmitted information."
        },

        "multiplexing": {
            "keywords": ["multiplexing", "tdm", "fdm", "cdm", "wavelength division multiplexing"],
            "response": "Multiplexing combines multiple signals into one signal over a shared medium to optimize bandwidth usage. Types: Frequency Division Multiplexing (FDM - different frequency bands), Time Division Multiplexing (TDM - different time slots), Code Division Multiplexing (CDM - different codes), Wavelength Division Multiplexing (WDM - different wavelengths in fiber optics). Demultiplexing separates the combined signal at the receiver. Multiplexing enables multiple users/channels to share expensive transmission resources efficiently."
        },

        "digital_signal_processing": {
            "keywords": ["digital signal processing", "dsp", "signal processing", "digital filter", "fft"],
            "response": "Digital Signal Processing (DSP) involves manipulating signals (audio, video, sensor data) in digital form using algorithms. Advantages: precision, flexibility, reproducibility. Key operations: filtering (FIR, IIR), transformation (FFT - Fast Fourier Transform), convolution, correlation. Implemented on DSP processors (optimized for mathematical operations), FPGAs, or general-purpose processors. Applications: audio processing (noise cancellation, compression), image processing, communications (modems, equalization), radar, and biomedical signal analysis."
        },

        "analog_to_digital_converter": {
            "keywords": ["analog to digital converter", "adc", "a/d converter", "sampling", "quantization"],
            "response": "An Analog-to-Digital Converter (ADC) converts continuous analog signals (voltage, current) into discrete digital numbers. Process: sampling (measure at intervals), quantization (assign to discrete levels), encoding (binary representation). Key specifications: resolution (bits), sampling rate, signal-to-noise ratio (SNR), linearity. Types: successive approximation (SAR), delta-sigma (high resolution), flash (high speed), pipeline. ADCs enable digital systems to process real-world analog signals from sensors, audio, and communications."
        },

        "digital_to_analog_converter": {
            "keywords": ["digital to analog converter", "dac", "d/a converter", "digital analog conversion"],
            "response": "A Digital-to-Analog Converter (DAC) converts digital numbers into continuous analog signals. Applications: audio playback (from digital files to speakers), video generation, waveform synthesis, control signals. Types: resistor ladder (R-2R), weighted resistor, delta-sigma, current steering. Key specifications: resolution (bits), settling time, glitch energy, linearity. DACs bridge digital processing systems with analog output devices, reconstructing signals from their digital representations."
        },

        "operational_amplifier": {
            "keywords": ["operational amplifier", "op amp", "op-amp", "differential amplifier", "ideal op amp"],
            "response": "An operational amplifier (op-amp) is a high-gain voltage amplifier with differential inputs and single-ended output. Ideal characteristics: infinite gain, infinite input impedance, zero output impedance. Practical op-amps have limitations: finite gain-bandwidth product, slew rate, input offset voltage. Configurations: inverting/non-inverting amplifier, summing amplifier, integrator, differentiator, comparator, filters. Op-amps are building blocks in analog circuits for signal conditioning, mathematical operations, active filtering, and instrumentation."
        },

        "logic_gates": {
            "keywords": ["logic gates", "and gate", "or gate", "not gate", "digital logic", "boolean algebra"],
            "response": "Logic gates are fundamental building blocks of digital circuits that perform Boolean logic operations on binary inputs (0/1). Basic gates: AND (output 1 if all inputs 1), OR (output 1 if any input 1), NOT (inverter). Derived gates: NAND, NOR, XOR, XNOR. Gates are implemented using transistors in integrated circuits (TTL, CMOS). Boolean algebra describes gate behavior. Combinations of gates create complex functions: adders, multiplexers, memory elements, forming the basis of processors and digital systems."
        },

        "flip_flop": {
            "keywords": ["flip flop", "latch", "sequential circuit", "sr flip flop", "jk flip flop", "d flip flop"],
            "response": "A flip-flop is a bistable multivibrator circuit that stores one bit of data, serving as basic memory element in sequential digital circuits. Types: SR (Set-Reset), JK (versatile, toggles), D (Data - stores input), T (Toggle). Flip-flops have clocked (synchronous) and unclocked (asynchronous/latch) variants. They are used in registers, counters, memory units, and state machines. Flip-flops enable digital systems to remember past states, essential for processing and control logic."
        },

        "counter": {
            "keywords": ["counter", "digital counter", "binary counter", "up counter", "down counter", "frequency counter"],
            "response": "A counter is a digital circuit that counts clock pulses, generating a sequence of numbers. Types: asynchronous (ripple counter), synchronous (all flip-flops clocked together). Counting direction: up, down, up/down. Modulus: binary, decade (0-9), programmable. Applications: event counting, frequency division, time measurement, control sequencing. Frequency counters measure signal frequency by counting cycles per time interval. Counters are fundamental in digital systems for timing, control, and measurement functions."
        },

        "shift_register": {
            "keywords": ["shift register", "serial in parallel out", "parallel in serial out", "shift register ic"],
            "response": "A shift register is a cascade of flip-flops that shifts data bits one position per clock cycle. Types: Serial-In Serial-Out (SISO), Serial-In Parallel-Out (SIPO), Parallel-In Serial-Out (PISO), Parallel-In Parallel-Out (PIPO), bidirectional. Applications: data serialization/deserialization (serial communication), temporary storage, delay lines, sequence generation. Shift registers are used in communication interfaces (UART, SPI), keyboard scanning, display drivers, and digital signal processing."
        },

        "multiplexer": {
            "keywords": ["multiplexer", "mux", "digital multiplexer", "data selector", "multiplexer circuit"],
            "response": "A multiplexer (MUX) is a digital switch that selects one of several input signals and forwards it to a single output line. Selection is controlled by binary address lines. An n:1 multiplexer has n data inputs, log2(n) select lines, and one output. Applications: data routing, function implementation (using MUX as logic), parallel-to-serial conversion. Demultiplexer (DEMUX) performs the reverse operation. Multiplexers are fundamental in digital systems for efficient data handling and resource sharing."
        },

        "decoder": {
            "keywords": ["decoder", "digital decoder", "binary decoder", "address decoder", "7 segment decoder"],
            "response": "A decoder is a digital circuit that converts binary input code into a set of output signals, activating one output corresponding to the input code. An n-to-2^n decoder has n inputs and 2^n outputs. Applications: memory address decoding (selecting specific memory locations), instruction decoding in processors, display drivers (BCD to 7-segment decoder), control logic. Encoders perform the inverse operation. Decoders are essential for interpreting binary information in digital systems."
        },

        "comparator": {
            "keywords": ["comparator", "digital comparator", "analog comparator", "voltage comparator", "magnitude comparator"],
            "response": "A comparator compares two voltages or currents and outputs a digital signal indicating which is larger. Analog comparators (op-amp based) output high/low based on input difference. Digital comparators (logic circuit) compare binary numbers, outputting equality (A=B) or magnitude (A>B, A<B). Applications: analog-to-digital conversion (in ADCs), threshold detection, window comparators (within range), zero-crossing detection. Comparators are used in measurement, control systems, and signal conditioning."
        },

        "timer": {
            "keywords": ["timer", "555 timer", "ic 555", "timer circuit", "pulse generator"],
            "response": "A timer circuit generates precise time delays or oscillations. The 555 timer IC is a popular integrated circuit used in various timing and pulse generation applications. Modes: monostable (one-shot pulse of fixed duration), astable (free-running oscillator), bistable (flip-flop). Applications: timers, pulse-width modulation (PWM), tone generation, frequency division, sequential timing. 555 timers are versatile, low-cost, and easy to use, found in toys, appliances, and industrial controls."
        },

        "voltage_regulator": {
            "keywords": ["voltage regulator", "linear regulator", "switching regulator", "voltage regulator ic", "power management"],
            "response": "A voltage regulator maintains a constant output voltage despite variations in input voltage or load current. Types: linear regulators (series, shunt - simple, low noise but inefficient), switching regulators (buck, boost, buck-boost - efficient but noisy). Integrated circuit regulators: 78xx (positive fixed), 79xx (negative fixed), LM317 (adjustable). Applications: power supplies for sensitive electronics, battery charging, voltage reference. Regulators ensure stable operation of electronic circuits."
        },

        "sensor": {
            "keywords": ["sensor", "electronic sensor", "temperature sensor", "pressure sensor", "motion sensor"],
            "response": "A sensor converts a physical quantity (temperature, pressure, light, motion) into an electrical signal for measurement or control. Types: temperature (thermistor, thermocouple, IC), pressure (piezoelectric, capacitive), light (photodiode, LDR), motion (PIR, accelerometer), proximity, humidity, gas. Sensors interface with electronic systems through signal conditioning (amplification, filtering) and analog-to-digital conversion. Essential for automation, IoT, automotive systems, medical devices, and environmental monitoring."
        },

        "actuator": {
            "keywords": ["actuator", "electronic actuator", "motor", "solenoid", "relay"],
            "response": "An actuator converts electrical signals into physical motion or action. Types: electric motors (DC, stepper, servo for rotational motion), solenoids (linear motion), relays (electromechanical switches), piezoelectric actuators (precise movement), hydraulic/pneumatic actuators controlled by electronic valves. Actuators are driven by driver circuits (H-bridge for motors) and controlled by microcontrollers. Applications: robotics, automation, valves, locks, positioning systems, and consumer electronics."
        },

        "relay": {
            "keywords": ["relay", "electromechanical relay", "solid state relay", "relay switching", "relay driver"],
            "response": "A relay is an electrically operated switch that uses an electromagnet to mechanically operate contacts, isolating control circuit from load circuit. Types: electromechanical (EMR - physical contacts), solid-state relay (SSR - semiconductor switches, no moving parts). Relays allow low-power circuits to control high-power loads. Specifications: coil voltage, contact rating (current/voltage), configuration (SPDT, DPDT). Applications: automotive, industrial control, home automation, protection circuits."
        },

        "transformer": {
            "keywords": ["transformer", "electrical transformer", "power transformer", "audio transformer", "rf transformer"],
            "response": "A transformer transfers electrical energy between circuits through electromagnetic induction, changing voltage and current levels while maintaining frequency. Consists of primary and secondary windings around a core (iron, ferrite, air). Types: power transformers (AC mains voltage conversion), audio transformers (impedance matching, isolation), RF transformers (coupling, impedance matching). Key parameters: turns ratio, power rating, efficiency, frequency response. Transformers provide isolation, impedance matching, and voltage scaling in electronic systems."
        },

        "battery": {
            "keywords": ["battery", "rechargeable battery", "lithium ion", "battery management", "battery charger"],
            "response": "A battery converts chemical energy into electrical energy, providing portable power for electronic devices. Types: primary (non-rechargeable - alkaline), secondary (rechargeable - Li-ion, NiMH, lead-acid). Key parameters: voltage, capacity (mAh), energy density, discharge rate. Battery management systems (BMS) protect against overcharge, over-discharge, and monitor health. Charger circuits restore energy. Batteries power mobile devices, electric vehicles, backup systems, and renewable energy storage."
        },

        "solar_cell": {
            "keywords": ["solar cell", "photovoltaic cell", "solar panel", "solar energy", "pv system"],
            "response": "A solar cell (photovoltaic cell) converts sunlight directly into electricity via the photovoltaic effect, using semiconductor materials (typically silicon). Single cells produce about 0.5-0.6V; multiple cells connected in series/parallel form solar panels. Types: monocrystalline (high efficiency), polycrystalline, thin-film. Solar power systems include panels, charge controllers, batteries (for storage), and inverters (DC to AC). Applications: grid-tied systems, off-grid power, portable chargers, satellites, and sustainable energy solutions."
        },

        "wireless_power_transfer": {
            "keywords": ["wireless power transfer", "inductive charging", "wireless charging", "resonant coupling", "wireless energy"],
            "response": "Wireless power transfer transmits electrical energy without physical connectors using electromagnetic fields. Methods: inductive coupling (near field, e.g., Qi charging pads), resonant coupling (mid-range, higher efficiency), microwave/RF radiation (far field, lower efficiency). Applications: charging mobile devices, electric vehicles, medical implants, and consumer electronics. Standards like Qi ensure compatibility. Wireless power offers convenience and eliminates connectors but has efficiency and distance limitations compared to wired transfer."
        },

        "rfid": {
            "keywords": ["rfid", "radio frequency identification", "rfid tag", "rfid reader", "rfid technology"],
            "response": "RFID (Radio Frequency Identification) uses electromagnetic fields to automatically identify and track tags attached to objects. System includes: reader (transceiver with antenna), tag (chip + antenna). Tags: passive (powered by reader signal), active (battery-powered), semi-passive. Frequencies: LF (125 kHz), HF (13.56 MHz - NFC), UHF (860-960 MHz), microwave. Applications: inventory management, access control, payment systems, animal tracking, supply chain logistics. RFID enables contactless data exchange over short distances."
        },

        "bluetooth": {
            "keywords": ["bluetooth", "bluetooth technology", "bluetooth low energy", "bluetooth communication", "wireless personal area network"],
            "response": "Bluetooth is a wireless technology standard for short-range data exchange between devices (typically up to 100 meters). Operates in 2.4 GHz ISM band using frequency-hopping spread spectrum. Versions: Classic (data/audio streaming), Bluetooth Low Energy (BLE - IoT, low power). Profiles define applications: A2DP (audio), HID (keyboard/mouse), HFP (hands-free). Bluetooth enables wireless headsets, speakers, keyboards, fitness trackers, and device connectivity in personal area networks (PAN)."
        },

        "wifi": {
            "keywords": ["wifi", "wireless fidelity", "wifi network", "wireless lan", "ieee 802.11"],
            "response": "Wi-Fi (Wireless Fidelity) is a family of wireless network protocols based on IEEE 802.11 standards for local area networking. Operates in 2.4 GHz and 5 GHz bands (dual-band). Generations: 802.11b/g/n/ac/ax (Wi-Fi 6). Wi-Fi provides internet access and network connectivity to devices within range of an access point (router). Security: WEP (weak), WPA, WPA2, WPA3. Applications: home/office networks, public hotspots, IoT connectivity. Wi-Fi enables wireless internet access for computers, smartphones, smart home devices."
        },

        "cellular_networks": {
            "keywords": ["cellular networks", "mobile network", "4g lte", "5g", "gsm", "cdma"],
            "response": "Cellular networks provide mobile communication by dividing geographic areas into cells served by base stations. Generations: 1G (analog voice), 2G (digital voice, SMS - GSM, CDMA), 3G (mobile data), 4G LTE (high-speed internet), 5G (ultra-reliable low latency, massive IoT). Technologies: FDMA, TDMA, CDMA, OFDMA. Cellular networks enable voice calls, messaging, mobile internet, and IoT connectivity through subscription to mobile network operators using smartphones and cellular modems."
        },

        "gps": {
            "keywords": ["gps", "global positioning system", "satellite navigation", "gnss", "gps receiver"],
            "response": "GPS (Global Positioning System) is a satellite-based navigation system that provides location and time information anywhere on Earth. Constellation: 24+ satellites in medium Earth orbit. GPS receiver measures time delay from multiple satellites to calculate position (trilateration). Other systems: GLONASS (Russia), Galileo (EU), BeiDou (China) - collectively GNSS. Applications: navigation (automotive, marine, aviation), mapping, surveying, timing synchronization, tracking. GPS enables location-based services in smartphones, vehicles, and IoT devices."
        },

        "radar": {
            "keywords": ["radar", "radio detection and ranging", "radar system", "doppler radar", "radar technology"],
            "response": "RADAR (Radio Detection and Ranging) uses radio waves to detect objects, determine their range, angle, or velocity. Transmitter emits radio waves that reflect off objects; receiver detects echoes. Types: pulsed radar (range), continuous wave (velocity via Doppler effect), phased array (electronic beam steering). Applications: air traffic control, weather monitoring, military (target acquisition), automotive (collision avoidance), speed detection. Radar operates at microwave frequencies and provides all-weather, day-night detection capability."
        },

        "sonar": {
            "keywords": ["sonar", "sound navigation and ranging", "underwater sonar", "echolocation", "acoustic detection"],
            "response": "SONAR (Sound Navigation and Ranging) uses sound propagation (usually underwater) to navigate, communicate, or detect objects. Active sonar transmits sound pulses and listens for echoes; passive sonar only listens. Frequencies: from infrasonic to ultrasonic. Applications: submarine navigation, fish finding, seafloor mapping (bathymetry), underwater communications, mine detection. SONAR is analogous to radar but uses sound waves (which travel well in water) instead of radio waves (which attenuate quickly in water)."
        },

        "lidar": {
            "keywords": ["lidar", "light detection and ranging", "laser radar", "3d scanning", "autonomous vehicle lidar"],
            "response": "LiDAR (Light Detection and Ranging) uses laser pulses to measure distances and create high-resolution 3D maps of environments. Time-of-flight measurement of reflected light. Types: mechanical scanning, solid-state (no moving parts), airborne, terrestrial. Applications: autonomous vehicles (object detection, mapping), topography, forestry, archaeology, atmospheric studies. LiDAR provides precise distance measurements and 3D modeling capabilities, complementing camera and radar in perception systems for robotics and automation."
        },

        "iot": {
            "keywords": ["iot", "internet of things", "iot devices", "iot communication", "smart devices"],
            "response": "The Internet of Things (IoT) refers to interconnected devices with sensors, processing, and communication capabilities that exchange data over networks. IoT ecosystem: devices (sensors/actuators), connectivity (Wi-Fi, Bluetooth, LoRa, cellular), cloud platforms (data processing), applications. Protocols: MQTT, CoAP, HTTP. Applications: smart home (thermostats, lights), industrial IoT (predictive maintenance), healthcare (remote monitoring), agriculture (precision farming). IoT enables automation, data-driven decisions, and new services through connected devices."
        },

        "embedded_systems": {
            "keywords": ["embedded systems", "embedded programming", "real time systems", "firmware", "embedded hardware"],
            "response": "Embedded systems are dedicated computing systems within larger mechanical or electrical systems, with a specific function. Components: microcontroller/microprocessor, memory, I/O interfaces, often real-time operating system (RTOS). Characteristics: constrained resources (power, memory, processing), reliability, real-time response. Programming: C, C++, sometimes Python, Rust. Applications: automotive electronics, medical devices, consumer electronics, industrial controllers. Embedded systems are ubiquitous in modern technology, performing dedicated tasks efficiently."
        },

        "vlsi": {
            "keywords": ["vlsi", "very large scale integration", "vlsi design", "asic design", "chip design"],
            "response": "VLSI (Very Large Scale Integration) is the process of creating integrated circuits by combining thousands to millions of transistors on a single chip. Design flow: specification, architecture, RTL design (Verilog/VHDL), verification, synthesis, physical design (layout), fabrication, testing. Tools: Cadence, Synopsys, Mentor Graphics. VLSI enables complex digital systems (microprocessors, memory chips) and mixed-signal systems. Advances in CMOS technology (Moore's Law) drive miniaturization, performance, and energy efficiency in electronics."
        },

        "asic": {
            "keywords": ["asic", "application specific integrated circuit", "custom ic", "asic design flow", "asic vs fpga"],
            "response": "An ASIC (Application-Specific Integrated Circuit) is a custom-designed chip for a particular application, as opposed to general-purpose ICs. Design process: high NRE (non-recurring engineering) cost but low per-unit cost at high volume. Types: full-custom (all layers customized), semi-custom (gate array, standard cell). ASICs offer optimized performance, power efficiency, and size for specific tasks. Compared to FPGAs (field-programmable), ASICs are faster, more efficient, but less flexible and have higher initial costs."
        },

        "fpga": {
            "keywords": ["fpga", "field programmable gate array", "programmable logic", "digital design fpga", "fpga programming"],
            "response": "An FPGA (Field-Programmable Gate Array) is an integrated circuit that can be configured by the user after manufacturing. Contains programmable logic blocks and interconnects that can implement custom digital circuits. Programming: HDL (Verilog/VHDL) or schematic entry. Advantages: reconfigurability, faster time-to-market, lower NRE costs than ASICs. Applications: prototyping, low-volume production, reconfigurable computing, digital signal processing, hardware acceleration. FPGAs bridge software flexibility with hardware performance."
        },

        "dsp_processor": {
            "keywords": ["dsp processor", "digital signal processor", "dsp architecture", "dsp programming", "signal processing chip"],
            "response": "A DSP processor is a specialized microprocessor optimized for digital signal processing operations. Features: hardware multipliers, MAC (multiply-accumulate) units, Harvard architecture (separate program/data memory), SIMD instructions, circular addressing. Examples: Texas Instruments TMS320, Analog Devices SHARC. DSP processors efficiently execute algorithms like FFT, filtering, convolution. Used in audio processing, communications, image processing, and control systems where real-time signal processing is required."
        },

        "memristor": {
            "keywords": ["memristor", "memory resistor", "fourth fundamental circuit element", "resistive ram", "emerging electronics"],
            "response": "A memristor (memory resistor) is theorized as the fourth fundamental circuit element (along with resistor, capacitor, inductor) whose resistance depends on the history of current through it. Realized using materials that change resistance with applied voltage (e.g., TiO2). Properties: non-volatile memory, analog behavior, potential for neuromorphic computing. Applications: resistive RAM (ReRAM), analog computing, brain-inspired circuits. Memristors are an emerging technology that could revolutionize memory and computing architectures."
        },

        "quantum_electronics": {
            "keywords": ["quantum electronics", "quantum computing electronics", "qubit control", "cryogenic electronics", "quantum devices"],
            "response": "Quantum electronics deals with electronic devices and circuits that exploit quantum mechanical effects. Includes: superconducting qubits (Josephson junctions), quantum dots (artificial atoms), spin-based devices. Quantum computers use quantum bits (qubits) that can be in superposition states. Control electronics operate at cryogenic temperatures (millikelvin) to maintain quantum coherence. Quantum electronics also includes quantum sensors (ultra-sensitive magnetometers) and quantum communication (quantum key distribution). A cutting-edge field at intersection of quantum physics and electronics."
        },

        "optoelectronics": {
            "keywords": ["optoelectronics", "optoelectronic devices", "photonic devices", "led", "photodiode", "laser diode"],
            "response": "Optoelectronics is the study and application of electronic devices that source, detect, and control light. Devices: LEDs (light emission), laser diodes (coherent light), photodiodes (light detection), solar cells (light to electricity), optical fibers (light guidance), displays (LCD, OLED). Optoelectronic integrated circuits (OEICs) combine optics and electronics. Applications: communications (fiber optics), displays, lighting, sensing, renewable energy. Optoelectronics bridges optics and electronics for efficient light-based technologies."
        },

        "display_technology": {
            "keywords": ["display technology", "lcd", "oled", "led display", "display electronics", "screen technology"],
            "response": "Display technology presents visual information electronically. Types: LCD (Liquid Crystal Display - uses backlight, liquid crystals modulate light), OLED (Organic LED - emissive, each pixel emits light), LED display (array of LEDs), plasma, e-ink (electronic paper). Driving electronics: display controllers, driver ICs, interface standards (HDMI, DisplayPort). Parameters: resolution, refresh rate, color gamut, power consumption. Displays are integral to TVs, monitors, smartphones, digital signage, and human-machine interfaces."
        },

        "audio_electronics": {
            "keywords": ["audio electronics", "audio amplifier", "speaker", "microphone", "audio processing", "sound system"],
            "response": "Audio electronics deals with recording, processing, amplifying, and reproducing sound. Components: microphones (convert sound to electrical), speakers (convert electrical to sound), amplifiers (boost signal), mixers, equalizers, effects processors. Digital audio: ADC/DAC, digital signal processing (compression, effects), audio codecs (MP3, AAC). Hi-Fi systems aim for high fidelity (accurate reproduction). Applications: consumer audio (headphones, home theater), professional audio (recording studios, live sound), telecommunications, hearing aids."
        },

        "video_electronics": {
            "keywords": ["video electronics", "video processing", "camera electronics", "display driver", "video signal"],
            "response": "Video electronics handles capturing, processing, transmitting, and displaying visual information. Components: image sensors (CCD, CMOS in cameras), video processors (noise reduction, scaling), display drivers (control pixels), video interfaces (HDMI, VGA, SDI). Analog video standards: NTSC, PAL. Digital video: compression (MPEG, H.264/265), streaming. Applications: television, video conferencing, surveillance, medical imaging, computer graphics. Video electronics combines analog signal handling with digital processing for high-quality visual experiences."
        },

        "medical_electronics": {
            "keywords": ["medical electronics", "biomedical instruments", "medical devices", "patient monitoring", "diagnostic equipment"],
            "response": "Medical electronics applies electronic principles to healthcare for diagnosis, treatment, and monitoring. Devices: ECG/EKG (heart signals), EEG (brain waves), MRI (magnetic resonance imaging), ultrasound, pacemakers, infusion pumps, pulse oximeters. Requirements: high reliability, safety (electrical isolation), precision, often portable/wearable. Regulations (FDA, CE) ensure efficacy and safety. Medical electronics improves patient care through non-invasive diagnostics, therapeutic interventions, and continuous health monitoring."
        },

        "automotive_electronics": {
            "keywords": ["automotive electronics", "car electronics", "vehicle electronics", "ecu", "automotive systems"],
            "response": "Automotive electronics includes electronic systems in vehicles for control, safety, entertainment, and efficiency. Systems: engine control unit (ECU - manages engine), ABS (anti-lock braking), airbag control, infotainment, ADAS (Advanced Driver Assistance Systems), electric vehicle powertrain. Networks: CAN (Controller Area Network) bus for communication. Automotive electronics must withstand harsh environment (temperature, vibration, EMI). Trends: electrification, autonomous driving, connectivity, transforming vehicles into sophisticated electronic platforms."
        },

        "industrial_electronics": {
            "keywords": ["industrial electronics", "industrial control", "plc", "motor drives", "industrial automation"],
            "response": "Industrial electronics applies electronic technology to industrial processes and machinery. Includes: PLCs (Programmable Logic Controllers) for automation, motor drives (variable frequency drives), robotics control, sensors for process monitoring, power electronics for industrial power supplies. Requirements: robustness, reliability, real-time operation, often in harsh conditions (dust, moisture, temperature extremes). Industrial electronics enables automation, improves productivity, ensures quality, and enhances safety in manufacturing, energy, and process industries."
        },

        "consumer_electronics": {
            "keywords": ["consumer electronics", "electronic gadgets", "home electronics", "personal electronics", "electronic appliances"],
            "response": "Consumer electronics are electronic equipment intended for everyday use by individuals. Categories: audio/video (TVs, headphones), computing (laptops, tablets), communication (smartphones), gaming (consoles), home appliances (smart devices), wearables (smartwatches). Characteristics: user-friendly design, aesthetic appeal, affordability, rapid innovation cycles. Consumer electronics drive mass-market technology adoption, integrating advances in semiconductors, displays, batteries, and connectivity to enhance entertainment, productivity, and convenience."
        },

        "military_electronics": {
            "keywords": ["military electronics", "defense electronics", "radar systems", "electronic warfare", "military communications"],
            "response": "Military electronics includes electronic systems for defense applications: radar (detection, tracking), communications (secure, jam-resistant), electronic warfare (jamming, deception), guidance systems (missiles), night vision, UAV (drone) control. Requirements: extreme reliability, ruggedness, performance in adverse conditions, security (encryption, anti-tamper). Military electronics often drives technology advancement (e.g., GPS, internet precursors) that later benefits civilian applications while addressing unique defense needs for national security."
        },

        "avionics": {
            "keywords": ["avionics", "aircraft electronics", "flight instruments", "avionics systems", "cockpit electronics"],
            "response": "Avionics (aviation electronics) comprises electronic systems used in aircraft, artificial satellites, and spacecraft. Includes: flight control systems, navigation (GPS, inertial), communication (VHF, SATCOM), surveillance (TCAS, weather radar), engine monitoring, cockpit displays (glass cockpit). Avionics must meet stringent safety standards (DO-254 for hardware, DO-178C for software) and operate reliably in extreme conditions. Avionics enhances flight safety, efficiency, and automation in both civilian and military aviation."
        },

        "maritime_electronics": {
            "keywords": ["maritime electronics", "marine electronics", "ship electronics", "navigation electronics", "marine communication"],
            "response": "Maritime electronics includes electronic systems for ships and maritime operations: navigation (GPS, gyrocompass, echo sounder), communication (VHF radio, satellite), radar (collision avoidance), sonar (depth sounding, fish finding), automatic identification system (AIS). Requirements: corrosion resistance (saltwater environment), reliability, compliance with international regulations (SOLAS). Maritime electronics ensures safe navigation, efficient operation, and communication for commercial shipping, fishing, naval vessels, and recreational boating."
        },

        # Expanded Engineering Topics
        "civil_engineering": {
            "keywords": ["civil engineering", "civil engineer", "construction engineering", "structural engineering", "civil engineering fields"],
            "response": "Civil engineering is the professional engineering discipline that deals with the design, construction, and maintenance of the physical and naturally built environment. Major branches include structural, geotechnical, transportation, environmental, and water resources engineering. Civil engineers design and build infrastructure such as buildings, roads, bridges, dams, airports, and water supply systems that are essential for modern society."
        },

        "structural_engineering": {
            "keywords": ["structural engineering", "structural analysis", "building design", "structural engineer", "load calculations"],
            "response": "Structural engineering is a specialty within civil engineering that focuses on the framework of structures, ensuring they can withstand stresses and pressures through their lifespan. Structural engineers analyze, design, plan, and research structural components and systems to achieve design goals of safety, serviceability, and economy. They work with buildings, bridges, towers, tunnels, and other structures using materials like concrete, steel, wood, and composites."
        },

        "geotechnical_engineering": {
            "keywords": ["geotechnical engineering", "soil mechanics", "foundation engineering", "geotechnical engineer", "soil analysis"],
            "response": "Geotechnical engineering deals with earth materials (soil and rock) and their behavior, including slope stability, foundation design, earthworks, and groundwater control. Geotechnical engineers investigate subsurface conditions, analyze soil properties, design foundations, retaining walls, and assess risks from natural hazards like earthquakes and landslides. This field is crucial for safe construction on or in the ground."
        },

        "transportation_engineering": {
            "keywords": ["transportation engineering", "traffic engineering", "highway design", "transportation planning", "road construction"],
            "response": "Transportation engineering focuses on the planning, design, operation, and maintenance of transportation systems to provide safe, efficient, and sustainable movement of people and goods. This includes highways, railways, airports, ports, and public transit systems. Transportation engineers work on traffic flow analysis, pavement design, transportation planning, intelligent transportation systems (ITS), and sustainable transport solutions."
        },

        "environmental_engineering": {
            "keywords": ["environmental engineering", "water treatment", "waste management", "environmental engineer", "pollution control"],
            "response": "Environmental engineering applies scientific and engineering principles to improve the natural environment, focusing on water and air pollution control, recycling, waste disposal, and public health issues. Environmental engineers design systems for water treatment, wastewater management, air pollution control, hazardous waste management, and environmental impact assessment. This field addresses challenges like climate change, sustainability, and public health protection."
        },

        "water_resources_engineering": {
            "keywords": ["water resources engineering", "hydrology", "hydraulic engineering", "water management", "irrigation engineering"],
            "response": "Water resources engineering deals with the collection, management, and distribution of water resources. It includes hydrology (study of water movement), hydraulic engineering (fluid flow in pipes and channels), water supply, irrigation, drainage, flood control, and hydroelectric power. Water resources engineers design dams, canals, water distribution networks, and flood protection systems to manage water sustainably."
        },

        "construction_engineering": {
            "keywords": ["construction engineering", "construction management", "building construction", "construction methods", "project management construction"],
            "response": "Construction engineering involves planning, coordination, and execution of construction projects from conception to completion. Construction engineers manage resources (labor, materials, equipment), ensure safety compliance, control costs and schedules, and solve technical problems on site. They work closely with architects, engineers, and contractors to transform designs into physical structures using various construction methods and technologies."
        },

        "mechanical_engineering": {
            "keywords": ["mechanical engineering", "mechanical engineer", "thermodynamics", "mechanical systems", "machine design"],
            "response": "Mechanical engineering is one of the broadest engineering disciplines, dealing with the design, analysis, manufacturing, and maintenance of mechanical systems. Core areas include thermodynamics (heat and energy transfer), fluid mechanics, materials science, mechanics (statics and dynamics), and machine design. Mechanical engineers work on engines, HVAC systems, robotics, manufacturing equipment, vehicles, and consumer products across various industries."
        },

        "thermodynamics": {
            "keywords": ["thermodynamics", "laws of thermodynamics", "heat transfer", "energy conversion", "thermodynamic cycles"],
            "response": "Thermodynamics is the branch of physics and engineering that deals with heat, work, temperature, and energy. The four laws of thermodynamics govern energy conversion and transfer. Applications include power plants (steam cycles), engines (internal combustion), refrigeration (heat pumps), and chemical processes. Thermodynamic analysis helps design efficient energy systems and understand the limits of energy conversion in engineering applications."
        },

        "fluid_mechanics": {
            "keywords": ["fluid mechanics", "fluid dynamics", "hydraulics", "aerodynamics", "fluid flow"],
            "response": "Fluid mechanics studies fluids (liquids and gases) at rest (fluid statics) and in motion (fluid dynamics). It includes aerodynamics (air flow), hydrodynamics (liquid flow), and hydraulics (engineering applications). Fluid mechanics principles are used in designing aircraft, pipelines, pumps, turbines, ventilation systems, and understanding weather patterns. Computational Fluid Dynamics (CFD) uses numerical methods to simulate fluid flow for engineering analysis."
        },

        "heat_transfer": {
            "keywords": ["heat transfer", "conduction", "convection", "radiation", "thermal engineering"],
            "response": "Heat transfer is the study of thermal energy movement between physical systems. Three modes: conduction (through solids), convection (through fluids), and radiation (electromagnetic waves). Heat transfer applications include heat exchangers, insulation design, electronic cooling, HVAC systems, and thermal management in engines and power plants. Engineers use heat transfer principles to design efficient thermal systems and prevent overheating in devices."
        },

        "manufacturing_engineering": {
            "keywords": ["manufacturing engineering", "production engineering", "machining", "additive manufacturing", "manufacturing processes"],
            "response": "Manufacturing engineering focuses on designing, implementing, and improving manufacturing processes and systems. It includes traditional methods (machining, casting, forging) and modern techniques (additive manufacturing/3D printing, CNC machining). Manufacturing engineers work on production planning, quality control, automation, robotics, lean manufacturing, and supply chain management to produce goods efficiently, cost-effectively, and with high quality."
        },

        "robotics_engineering": {
            "keywords": ["robotics engineering", "robotics design", "industrial robotics", "robot control", "automation engineering"],
            "response": "Robotics engineering combines mechanical, electrical, and computer engineering to design, build, and program robots. It includes robot kinematics and dynamics, control systems, sensors, actuators, and artificial intelligence for autonomous operation. Robotics engineers develop industrial robots for manufacturing, medical robots for surgery, service robots, autonomous vehicles, and exploration robots for hazardous environments."
        },

        "automotive_engineering": {
            "keywords": ["automotive engineering", "vehicle design", "automobile engineering", "car systems", "automotive technology"],
            "response": "Automotive engineering focuses on designing, developing, and manufacturing vehicles. It includes vehicle dynamics, powertrain systems (engine, transmission), chassis design, safety systems, electronics, and alternative fuel technologies. Automotive engineers work on traditional internal combustion engines, hybrid systems, electric vehicles, and autonomous driving technology. The field is evolving with emphasis on sustainability, connectivity, and automation."
        },

        "aeronautical_engineering": {
            "keywords": ["aeronautical engineering", "aircraft design", "aviation engineering", "flight mechanics", "aircraft systems"],
            "response": "Aeronautical engineering deals with aircraft design, development, and operation within Earth's atmosphere. It includes aerodynamics (airflow around aircraft), propulsion (jet engines), structures (airframe design), flight mechanics (stability and control), and avionics (aircraft electronics). Aeronautical engineers design commercial airplanes, military aircraft, helicopters, and drones, focusing on performance, safety, and efficiency in atmospheric flight."
        },

        "astronautical_engineering": {
            "keywords": ["astronautical engineering", "spacecraft design", "rocket science", "space engineering", "satellite technology"],
            "response": "Astronautical engineering focuses on spacecraft and space systems that operate outside Earth's atmosphere. It includes orbital mechanics, rocket propulsion, space environment effects, spacecraft structures, thermal control, and communication systems. Astronautical engineers design satellites, space probes, rockets, space stations, and interplanetary missions. The field addresses challenges of vacuum, microgravity, radiation, and extreme temperatures in space."
        },

        "aerospace_engineering": {
            "keywords": ["aerospace engineering", "aerospace", "aircraft design", "spacecraft design", "aerospace technology"],
            "response": "Aerospace engineering encompasses both aeronautical (aircraft within atmosphere) and astronautical (spacecraft) engineering. It involves the design, development, testing, and production of aircraft, spacecraft, and related systems. Key areas include aerodynamics, propulsion, structures, materials, flight mechanics, and control systems. Aerospace engineers work on commercial aviation, defense systems, space exploration, and emerging technologies like hypersonic flight and reusable rockets."
        },

        "electrical_engineering": {
            "keywords": ["electrical engineering", "electrical engineer", "power systems", "electrical circuits", "electrical technology"],
            "response": "Electrical engineering deals with electricity, electronics, and electromagnetism. Major fields include power engineering (generation, transmission, distribution), control systems (automation), electronics (circuit design), telecommunications (signal processing), and computer engineering (hardware). Electrical engineers design electrical equipment, power grids, communication systems, electronic devices, and control systems that form the backbone of modern technology infrastructure."
        },

        "power_engineering": {
            "keywords": ["power engineering", "electrical power", "power systems", "power generation", "electrical grid"],
            "response": "Power engineering focuses on generation, transmission, distribution, and utilization of electric power. It includes traditional power plants (thermal, hydro, nuclear), renewable energy (solar, wind), power electronics, transformers, switchgear, and grid management. Power engineers design and maintain electrical grids, ensure reliable power supply, integrate renewable sources, and develop smart grid technologies for efficient energy management and distribution."
        },

        "control_systems_engineering": {
            "keywords": ["control systems engineering", "control theory", "automation", "feedback control", "robotics control"],
            "response": "Control systems engineering deals with designing systems that regulate the behavior of dynamic systems using feedback loops. Applications include industrial automation, robotics, aircraft flight control, automotive systems (cruise control), and process control in chemical plants. Control engineers use mathematical models, sensors, actuators, and controllers (PID, modern control) to achieve desired system performance, stability, and robustness."
        },

        "electronics_engineering": {
            "keywords": ["electronics engineering", "electronic circuits", "analog electronics", "digital electronics", "electronic devices"],
            "response": "Electronics engineering focuses on designing and testing electronic circuits, components, and systems. It includes analog electronics (amplifiers, filters), digital electronics (logic gates, microprocessors), radio-frequency (RF) engineering, and embedded systems. Electronics engineers work on consumer electronics, communication devices, medical instruments, automotive electronics, and industrial control systems using semiconductors and integrated circuits."
        },

        "telecommunications_engineering": {
            "keywords": ["telecommunications engineering", "communication systems", "signal processing", "wireless communication", "telecom networks"],
            "response": "Telecommunications engineering deals with transmission of information over distances through various media (wired or wireless). It includes signal processing, modulation techniques, network protocols, antenna design, and information theory. Telecom engineers design and maintain telephone networks, mobile communication systems (4G/5G), satellite communications, internet infrastructure, and broadcasting systems enabling global connectivity."
        },

        "computer_engineering": {
            "keywords": ["computer engineering", "computer hardware", "embedded systems", "computer architecture", "hardware software integration"],
            "response": "Computer engineering combines electrical engineering and computer science to develop computer hardware and software. It includes digital logic design, computer architecture, microprocessors, embedded systems, and hardware-software co-design. Computer engineers design processors, memory systems, input/output devices, and integrate hardware with operating systems and applications. They work on computers, smartphones, IoT devices, and specialized computing systems."
        },

        "chemical_engineering": {
            "keywords": ["chemical engineering", "chemical engineer", "process engineering", "chemical processes", "chemical plant design"],
            "response": "Chemical engineering applies chemistry, physics, mathematics, and economics to process raw materials into valuable products. It involves designing and operating chemical plants, optimizing processes for efficiency and safety, and developing new materials and products. Chemical engineers work in petroleum refining, pharmaceuticals, food processing, plastics, energy production, and environmental protection, using principles of thermodynamics, fluid mechanics, and reaction kinetics."
        },

        "process_engineering": {
            "keywords": ["process engineering", "chemical processes", "industrial processes", "process design", "process optimization"],
            "response": "Process engineering focuses on designing, operating, controlling, and optimizing industrial processes, especially in chemical and manufacturing industries. Process engineers develop flow diagrams, specify equipment (reactors, separators, heat exchangers), ensure safety and environmental compliance, and improve process efficiency. They use process simulation software and apply principles of mass and energy balances, thermodynamics, and kinetics to transform raw materials into products."
        },

        "biochemical_engineering": {
            "keywords": ["biochemical engineering", "bioprocess engineering", "fermentation", "biotechnology processes", "biological engineering"],
            "response": "Biochemical engineering applies engineering principles to biological systems and processes. It involves designing equipment and processes for producing biological products like pharmaceuticals (antibiotics, vaccines), biofuels, enzymes, and food products. Biochemical engineers work on fermentation, cell culture, downstream processing (separation and purification), and scale-up from laboratory to industrial production in biotechnology and pharmaceutical industries."
        },

        "petroleum_engineering": {
            "keywords": ["petroleum engineering", "oil and gas", "drilling engineering", "reservoir engineering", "petroleum technology"],
            "response": "Petroleum engineering focuses on exploration, extraction, and production of oil and natural gas. Specializations include drilling engineering (well design and drilling), reservoir engineering (fluid flow in reservoirs), production engineering (optimizing production), and petroleum geology. Petroleum engineers use technology to locate hydrocarbon reservoirs, design drilling methods, enhance recovery, and ensure safe and environmentally responsible extraction of fossil fuels."
        },

        "materials_engineering": {
            "keywords": ["materials engineering", "materials science", "metallurgy", "polymers", "composite materials"],
            "response": "Materials engineering involves designing and developing materials with desired properties for specific applications. It includes metallurgy (metals and alloys), ceramics, polymers, composites, and nanomaterials. Materials engineers study structure-property relationships, processing methods, and performance of materials. They work on developing new materials for aerospace, automotive, electronics, construction, and biomedical industries, improving durability, strength, and functionality."
        },

        "metallurgical_engineering": {
            "keywords": ["metallurgical engineering", "metallurgy", "extractive metallurgy", "physical metallurgy", "metal processing"],
            "response": "Metallurgical engineering focuses on metals and alloys, including extraction from ores (extractive metallurgy), processing (physical metallurgy), and development of metal properties. Metallurgical engineers design processes for mining, refining, alloying, heat treatment, and shaping metals. They improve metal strength, corrosion resistance, and other properties for applications in construction, manufacturing, transportation, and energy industries."
        },

        "polymer_engineering": {
            "keywords": ["polymer engineering", "plastics engineering", "polymer science", "rubber technology", "polymer processing"],
            "response": "Polymer engineering deals with plastics, rubbers, fibers, and other polymeric materials. It includes polymer synthesis, characterization, processing (injection molding, extrusion), and application development. Polymer engineers design materials with specific properties (flexibility, strength, thermal stability) for products like packaging, automotive parts, medical devices, textiles, and electronics. The field addresses recycling and sustainability of plastic materials."
        },

        "biomedical_engineering": {
            "keywords": ["biomedical engineering", "biomedical", "medical devices", "biomedical technology", "healthcare engineering"],
            "response": "Biomedical engineering applies engineering principles to biology and medicine for healthcare purposes. It includes designing medical devices (pacemakers, MRI machines), developing biomaterials (implants, tissue scaffolds), biomechanics (human movement analysis), and biomedical imaging (ultrasound, X-ray). Biomedical engineers collaborate with healthcare professionals to create technologies for diagnosis, treatment, and rehabilitation, improving patient care and quality of life."
        },

        "bioinstrumentation": {
            "keywords": ["bioinstrumentation", "medical instruments", "biomedical sensors", "diagnostic equipment", "medical device design"],
            "response": "Bioinstrumentation focuses on designing and developing instruments and devices for measuring, diagnosing, and treating medical conditions. This includes sensors, monitors, imaging systems (CT, MRI), and therapeutic devices (defibrillators, infusion pumps). Bioinstrumentation engineers combine electronics, signal processing, and medical knowledge to create accurate, reliable, and safe medical equipment that assists in healthcare delivery and medical research."
        },

        "biomechanics": {
            "keywords": ["biomechanics", "human movement", "orthopedic engineering", "sports engineering", "rehabilitation engineering"],
            "response": "Biomechanics applies mechanical principles to biological systems, particularly the human body. It studies forces and motion in living organisms, including gait analysis, muscle mechanics, joint kinematics, and tissue mechanics. Biomechanical engineers design prosthetics, orthotics, ergonomic equipment, sports gear, and rehabilitation devices. They also analyze injuries and develop interventions to improve mobility, performance, and quality of life."
        },

        "tissue_engineering": {
            "keywords": ["tissue engineering", "regenerative medicine", "artificial organs", "biomaterials for tissue", "cell culture engineering"],
            "response": "Tissue engineering combines engineering and life sciences to develop biological substitutes that restore, maintain, or improve tissue function. It involves creating scaffolds (biomaterials), cells (stem cells, differentiated cells), and growth factors to grow tissues in the lab for transplantation. Applications include skin grafts, cartilage repair, bone regeneration, and eventually whole organs. Tissue engineering aims to address organ shortage and improve regenerative therapies."
        },

        "industrial_engineering": {
            "keywords": ["industrial engineering", "industrial engineer", "operations research", "systems engineering", "production optimization"],
            "response": "Industrial engineering focuses on optimizing complex processes, systems, or organizations to improve efficiency, quality, and productivity. It uses mathematical models, statistics, and simulation to analyze and design systems involving people, materials, information, equipment, and energy. Industrial engineers work on supply chain management, logistics, quality control, ergonomics, and operations research in manufacturing, healthcare, service industries, and government."
        },

        "systems_engineering": {
            "keywords": ["systems engineering", "systems design", "complex systems", "systems integration", "systems thinking"],
            "response": "Systems engineering is an interdisciplinary approach to designing, integrating, and managing complex systems over their life cycles. It focuses on defining customer needs, documenting requirements, designing architecture, integrating components, and verifying that the system meets objectives. Systems engineers work on large-scale projects like aerospace systems, defense systems, transportation networks, and software systems, ensuring all parts work together effectively."
        },

        "operations_research": {
            "keywords": ["operations research", "optimization", "decision science", "mathematical modeling", "linear programming"],
            "response": "Operations research (OR) uses advanced analytical methods (mathematical modeling, statistical analysis, optimization) to make better decisions. OR techniques include linear programming, queuing theory, simulation, and game theory. Applications span logistics, supply chain management, resource allocation, scheduling, finance, and healthcare. Operations researchers solve complex problems by developing models that predict outcomes and optimize performance of systems and processes."
        },

        "ergonomics": {
            "keywords": ["ergonomics", "human factors engineering", "workplace design", "human machine interaction", "usability engineering"],
            "response": "Ergonomics (or human factors engineering) designs systems, products, and environments to fit human capabilities and limitations. It considers physical (posture, movement), cognitive (mental workload, decision-making), and organizational factors. Ergonomists improve workplace safety, productivity, and comfort by designing user-friendly interfaces, reducing injury risk, and optimizing human-machine interaction in industries like manufacturing, transportation, healthcare, and computing."
        },

        "nuclear_engineering": {
            "keywords": ["nuclear engineering", "nuclear power", "radiation", "nuclear technology", "reactor design"],
            "response": "Nuclear engineering deals with nuclear reactions and radiation, primarily for power generation, medical applications, and industrial uses. It includes reactor physics, nuclear fuel cycle, radiation protection, and nuclear safety. Nuclear engineers design and operate nuclear power plants, develop radiation therapy equipment for cancer treatment, and work on nuclear waste management and fusion research. The field requires understanding of nuclear physics, thermal hydraulics, and materials science."
        },

        "marine_engineering": {
            "keywords": ["marine engineering", "naval architecture", "ship design", "offshore engineering", "marine technology"],
            "response": "Marine engineering involves designing, building, and maintaining ships, submarines, and offshore structures. It includes naval architecture (hull design, stability), propulsion systems (marine engines), electrical systems, and marine materials. Marine engineers work on commercial vessels, naval ships, oil platforms, and renewable energy installations at sea. The field addresses challenges of corrosion, buoyancy, and harsh marine environments to ensure safe and efficient maritime operations."
        },

        "ocean_engineering": {
            "keywords": ["ocean engineering", "coastal engineering", "underwater technology", "offshore structures", "wave energy"],
            "response": "Ocean engineering applies engineering principles to ocean environments. It includes coastal engineering (shore protection, ports), underwater technology (ROVs, submersibles), offshore engineering (oil platforms, wind farms), and ocean energy (wave, tidal power). Ocean engineers design structures and systems that withstand waves, currents, and corrosion while minimizing environmental impact. The field supports maritime transportation, resource extraction, and environmental monitoring in oceans."
        },

        "agricultural_engineering": {
            "keywords": ["agricultural engineering", "farm machinery", "irrigation engineering", "agricultural technology", "biosystems engineering"],
            "response": "Agricultural engineering (also biosystems engineering) applies technology to agriculture and food production. It includes farm machinery design, irrigation and drainage systems, soil and water conservation, food processing, and controlled environment agriculture (greenhouses). Agricultural engineers develop sustainable farming practices, precision agriculture technologies, and bioenergy systems to increase food production efficiency while protecting natural resources and the environment."
        },

        "food_engineering": {
            "keywords": ["food engineering", "food processing", "food technology", "food safety", "food preservation"],
            "response": "Food engineering focuses on designing and optimizing processes for producing safe, nutritious, and appealing food products. It includes thermal processing (pasteurization, sterilization), freezing, drying, packaging, and storage. Food engineers apply principles of microbiology, chemistry, and engineering to develop food preservation methods, improve food quality, and ensure food safety from production to consumption. The field contributes to reducing food waste and developing novel food products."
        },

        "acoustical_engineering": {
            "keywords": ["acoustical engineering", "sound engineering", "noise control", "audio engineering", "acoustic design"],
            "response": "Acoustical engineering deals with sound and vibration, including noise control, architectural acoustics, audio engineering, and ultrasonics. Acoustical engineers design concert halls with optimal sound quality, reduce noise from machinery or transportation, develop audio equipment (speakers, microphones), and apply ultrasound in medical imaging and industrial testing. The field applies wave physics to solve problems related to sound transmission, absorption, and perception."
        },

        "optical_engineering": {
            "keywords": ["optical engineering", "optics", "laser engineering", "photonics", "optical systems"],
            "response": "Optical engineering focuses on designing devices and systems that use light, including lenses, lasers, fiber optics, and imaging systems. It combines principles of optics, physics, and electrical engineering. Optical engineers work on cameras, telescopes, microscopes, medical imaging devices, communication systems (fiber optics), and laser-based manufacturing. The field is integral to telecommunications, healthcare, astronomy, and consumer electronics."
        },

        "fire_protection_engineering": {
            "keywords": ["fire protection engineering", "fire safety", "fire suppression", "fire dynamics", "building fire safety"],
            "response": "Fire protection engineering designs systems and strategies to protect people, property, and environments from fire. It includes fire detection and alarm systems, automatic suppression (sprinklers), smoke control, fire-resistant construction materials, and egress planning. Fire protection engineers analyze fire dynamics (combustion, heat transfer), conduct risk assessments, and ensure compliance with fire codes to enhance safety in buildings, industrial facilities, and transportation systems."
        },

        "mining_engineering": {
            "keywords": ["mining engineering", "mineral extraction", "mine design", "mining safety", "mineral processing"],
            "response": "Mining engineering involves extracting minerals from the earth efficiently, safely, and sustainably. It includes mine planning and design, drilling and blasting, ventilation, ground control, mineral processing, and mine reclamation. Mining engineers work on surface and underground mines for coal, metals, and industrial minerals. The field addresses challenges of resource depletion, environmental impact, and worker safety while supplying raw materials for industry."
        },

        "geomatics_engineering": {
            "keywords": ["geomatics engineering", "surveying", "gis", "remote sensing", "geospatial engineering"],
            "response": "Geomatics engineering (also geospatial engineering) involves measurement, analysis, and management of spatial data. It includes land surveying, geographic information systems (GIS), remote sensing (satellite imagery), cartography, and global positioning systems (GPS). Geomatics engineers collect and process data about Earth's surface for mapping, urban planning, navigation, natural resource management, and infrastructure development. The field is essential for accurate positioning and spatial decision-making."
        },

        "railway_engineering": {
            "keywords": ["railway engineering", "rail transport", "track design", "railway systems", "train technology"],
            "response": "Railway engineering focuses on designing, constructing, and maintaining railway systems. It includes track design and maintenance, rolling stock (locomotives and cars), signaling and control systems, stations, and electrification. Railway engineers work on high-speed rail, freight networks, and urban transit systems to ensure safety, efficiency, and reliability. The field addresses challenges of capacity, interoperability, and integration with other transport modes."
        },

        "safety_engineering": {
            "keywords": ["safety engineering", "risk management", "system safety", "occupational safety", "hazard analysis"],
            "response": "Safety engineering identifies and mitigates hazards to prevent accidents and injuries in systems and workplaces. It involves risk assessment, hazard analysis (FMEA, FTA), safety standards compliance, and design of protective measures. Safety engineers work across industries (construction, manufacturing, transportation, chemicals) to ensure equipment, processes, and environments are safe for workers and the public. The field applies engineering principles to anticipate and control potential failures."
        },

        "reliability_engineering": {
            "keywords": ["reliability engineering", "system reliability", "failure analysis", "maintenance engineering", "product reliability"],
            "response": "Reliability engineering ensures that systems and components perform their required functions under stated conditions for specified periods. It involves probability and statistics to predict and prevent failures, including techniques like reliability modeling, failure mode analysis, and life testing. Reliability engineers design for durability, plan maintenance strategies, and analyze field data to improve product lifespan and reduce downtime in industries like aerospace, automotive, and electronics."
        },

        "energy_engineering": {
            "keywords": ["energy engineering", "energy systems", "renewable energy", "energy efficiency", "power generation"],
            "response": "Energy engineering focuses on efficient energy use, conversion, and storage. It includes traditional energy systems (fossil fuels, nuclear) and renewable energy (solar, wind, hydro, biomass). Energy engineers design power plants, develop energy-efficient buildings, integrate renewable sources into grids, and work on energy storage (batteries, hydrogen). The field addresses global challenges of energy security, sustainability, and climate change through technological innovation."
        },

        "renewable_energy_engineering": {
            "keywords": ["renewable energy engineering", "solar energy", "wind energy", "hydro energy", "sustainable energy"],
            "response": "Renewable energy engineering specializes in harnessing energy from sustainable sources like sunlight, wind, water, geothermal heat, and biomass. It includes designing solar photovoltaic systems, wind turbines, hydroelectric plants, and bioenergy facilities. Renewable energy engineers work on improving efficiency, reducing costs, integrating renewables into existing grids, and developing storage solutions to transition from fossil fuels to clean energy for a sustainable future."
        },

        "sustainable_engineering": {
            "keywords": ["sustainable engineering", "green engineering", "environmentally friendly design", "sustainability", "life cycle assessment"],
            "response": "Sustainable engineering designs systems and processes that minimize environmental impact while meeting societal needs. It applies principles of life cycle assessment, green chemistry, and circular economy. Sustainable engineers develop products and infrastructure that use resources efficiently, reduce waste and pollution, and promote social equity. The field integrates environmental, economic, and social considerations into engineering decisions for long-term sustainability."
        },

        "nanotechnology_engineering": {
            "keywords": ["nanotechnology engineering", "nanomaterials", "nanoscale engineering", "nanotech", "molecular engineering"],
            "response": "Nanotechnology engineering manipulates matter at the atomic and molecular scale (1-100 nanometers) to create materials, devices, and systems with novel properties. It includes nanomaterials (carbon nanotubes, quantum dots), nanoelectronics, nanomedicine, and nanofabrication. Nanotechnology engineers work on applications in electronics, medicine, energy, and materials science. The field requires understanding of quantum effects and surface phenomena at the nanoscale for innovative solutions."
        },

        "mechatronics_engineering": {
            "keywords": ["mechatronics engineering", "mechatronics", "robotics and automation", "electromechanical systems", "control systems mechatronics"],
            "response": "Mechatronics engineering integrates mechanical, electrical, and computer engineering to design and manufacture intelligent products and systems. It combines sensors, actuators, microcontrollers, and software to create automated systems like industrial robots, CNC machines, automotive systems (ABS, stability control), and consumer electronics. Mechatronics engineers apply control theory and real-time computing to develop smart machines that respond to their environment."
        },

        "automation_engineering": {
            "keywords": ["automation engineering", "industrial automation", "plc programming", "process automation", "factory automation"],
            "response": "Automation engineering focuses on designing and implementing automated systems for manufacturing and process industries. It includes programmable logic controllers (PLCs), supervisory control and data acquisition (SCADA), robotics, and human-machine interfaces (HMIs). Automation engineers program control systems, integrate sensors and actuators, and optimize production lines for efficiency, quality, and safety. The field drives Industry 4.0 with smart factories and IoT connectivity."
        },

        "instrumentation_engineering": {
            "keywords": ["instrumentation engineering", "measurement systems", "sensors and transducers", "control instrumentation", "industrial instrumentation"],
            "response": "Instrumentation engineering deals with designing, developing, and maintaining instruments and systems for measurement and control in industrial processes. It includes sensors (temperature, pressure, flow), transducers, signal conditioning, data acquisition, and calibration. Instrumentation engineers ensure accurate monitoring and control of variables in industries like oil and gas, chemical plants, power generation, and healthcare for process optimization and safety."
        },

        "corrosion_engineering": {
            "keywords": ["corrosion engineering", "corrosion control", "materials degradation", "protective coatings", "cathodic protection"],
            "response": "Corrosion engineering focuses on preventing and controlling degradation of materials due to chemical or electrochemical reactions with their environment. It includes selecting corrosion-resistant materials, designing protective coatings, applying cathodic protection, and using inhibitors. Corrosion engineers work in industries like oil and gas, marine, infrastructure, and manufacturing to extend asset life, ensure safety, and reduce maintenance costs caused by corrosion."
        },

        "pipeline_engineering": {
            "keywords": ["pipeline engineering", "pipeline design", "oil and gas pipelines", "pipeline integrity", "fluid transportation"],
            "response": "Pipeline engineering involves designing, constructing, and maintaining pipelines for transporting fluids (oil, gas, water) over long distances. It includes hydraulic analysis, route selection, material selection, corrosion protection, and integrity management. Pipeline engineers ensure safe and efficient operation, comply with regulations, and address challenges like leaks, pressure fluctuations, and environmental impact. The field is critical for energy distribution and water supply infrastructure."
        },

        "HVAC_engineering": {
            "keywords": ["hvac engineering", "heating ventilation air conditioning", "building services", "thermal comfort", "hvac design"],
            "response": "HVAC (Heating, Ventilation, and Air Conditioning) engineering designs systems to control indoor environmental conditions for comfort and air quality. It includes heating (boilers, heat pumps), cooling (chillers, air conditioners), ventilation (air distribution, filtration), and building automation. HVAC engineers calculate heating/cooling loads, select equipment, design ductwork and piping, and ensure energy efficiency and compliance with codes in residential, commercial, and industrial buildings."
        },

        "plumbing_engineering": {
            "keywords": ["plumbing engineering", "plumbing systems", "water supply", "sanitary engineering", "fire protection plumbing"],
            "response": "Plumbing engineering designs systems for potable water supply, wastewater removal, and sometimes fire protection in buildings. It includes pipe sizing, fixture selection, drainage design, and water heating. Plumbing engineers ensure adequate water pressure, proper sanitation, and compliance with health and safety codes. The field addresses water conservation, greywater reuse, and sustainable plumbing practices to manage water resources efficiently in built environments."
        },

        "construction_technology": {
            "keywords": ["construction technology", "building technology", "construction methods", "prefabrication", "smart construction"],
            "response": "Construction technology involves applying innovative methods, materials, and equipment to improve the construction process. It includes prefabrication and modular construction, 3D printing of buildings, drones for surveying, Building Information Modeling (BIM), and smart construction tools. Construction technologists aim to increase productivity, reduce costs, enhance safety, and improve sustainability in building projects through technological advancements and digitalization."
        },

        "earthquake_engineering": {
            "keywords": ["earthquake engineering", "seismic design", "earthquake resistant structures", "seismic analysis", "structural dynamics"],
            "response": "Earthquake engineering focuses on designing structures to withstand seismic activity and protecting human life during earthquakes. It involves understanding ground motion, structural dynamics, and material behavior under cyclic loading. Earthquake engineers use seismic codes, base isolation, damping systems, and retrofitting techniques to enhance building resilience. The field combines civil engineering, geotechnical engineering, and seismology to mitigate earthquake risks in prone regions."
        },

        "forensic_engineering": {
            "keywords": ["forensic engineering", "failure analysis", "engineering investigation", "accident reconstruction", "expert witness"],
            "response": "Forensic engineering investigates failures, accidents, and performance issues in engineering systems to determine causes and responsibilities. It applies engineering principles to analyze structural collapses, vehicle accidents, product malfunctions, and fire origins. Forensic engineers collect evidence, conduct tests, simulate scenarios, and provide expert testimony in legal proceedings. The field helps improve safety standards, prevent future failures, and resolve disputes through technical analysis."
        },

        # Programming Languages
        "c": {
            "keywords": ["c language", "c", "c programming", "c language basics", "c programming language"],
            "response": "C is a general-purpose, procedural programming language developed in 1972 by Dennis Ritchie at Bell Labs. Known for its efficiency, low-level memory access, and minimal runtime support. Widely used in operating systems (Unix, Linux, Windows kernel), embedded systems, and system programming. C has influenced many languages and remains foundational in computer science education and industry."
        },

        "csharp": {
            "keywords": ["c#", "c sharp", "csharp programming", "dotnet c#", "c# language"],
            "response": "C# (C Sharp) is a modern, object-oriented, type-safe programming language developed by Microsoft in 2000. It runs on the .NET framework and .NET Core. Used for Windows desktop applications (WPF, WinForms), web development (ASP.NET), game development (Unity engine), and enterprise software. C# combines features from C++, Java, and Delphi with innovations like LINQ and async/await."
        },

        "ruby": {
            "keywords": ["ruby", "ruby programming", "ruby on rails", "ruby language", "rails framework"],
            "response": "Ruby is a dynamic, open-source programming language created by Yukihiro 'Matz' Matsumoto in 1995. Emphasizes simplicity and productivity with the principle 'developer happiness'. Ruby on Rails is its popular web framework that follows convention over configuration. Used for web development, scripting, and DevOps tools. Ruby's elegant syntax and object-oriented nature make it popular for rapid application development."
        },

        "swift": {
            "keywords": ["swift", "swift programming", "ios development", "swift language", "apple swift"],
            "response": "Swift is a modern, safe, fast programming language introduced by Apple in 2014 for iOS, macOS, watchOS, tvOS, and Linux development. Designed to replace Objective-C with safer memory management, cleaner syntax, and better performance. Features include optionals, type inference, closures, and protocol-oriented programming. Swift is open-source and increasingly used for server-side development with frameworks like Vapor."
        },

        "kotlin": {
            "keywords": ["kotlin", "kotlin programming", "android kotlin", "kotlin language", "jetbrains kotlin"],
            "response": "Kotlin is a statically typed, cross-platform programming language developed by JetBrains in 2011. Officially supported for Android development since 2017, as an alternative to Java. Runs on JVM, JavaScript, and native platforms. Known for conciseness, safety (null safety), and interoperability with Java. Used for Android apps, server-side development (Spring Boot), and multiplatform projects. Kotlin reduces boilerplate code while maintaining compatibility."
        },

        "go_lang": {
            "keywords": ["go language", "golang", "go programming", "google go", "go lang"],
            "response": "Go (or Golang) is an open-source programming language created by Google engineers (Robert Griesemer, Rob Pike, Ken Thompson) in 2009. Designed for simplicity, efficiency, and concurrency. Features garbage collection, structural typing, and CSP-style concurrency with goroutines and channels. Used for cloud services, distributed systems, CLI tools, and web servers. Go compiles to standalone binaries and has a minimalist, readable syntax."
        },

        "rust": {
            "keywords": ["rust", "rust programming", "rust language", "mozilla rust", "systems programming rust"],
            "response": "Rust is a systems programming language created by Mozilla Research in 2010, focusing on safety, speed, and concurrency. Its unique ownership system enforces memory safety without garbage collection, preventing segfaults and data races. Used for operating systems, game engines, web browsers (Firefox components), and embedded systems. Rust has been voted the 'most loved language' in Stack Overflow surveys for multiple years."
        },

        "php": {
            "keywords": ["php", "php programming", "php web development", "php language", "php hypertext preprocessor"],
            "response": "PHP (Hypertext Preprocessor) is a server-side scripting language created by Rasmus Lerdorf in 1994. Originally for web development, it powers 78% of websites using server-side programming. Popular with WordPress, Drupal, and Laravel framework. PHP runs on most web servers and supports multiple databases (MySQL, PostgreSQL). Recent versions (PHP 7+) have significant performance improvements and modern features like type declarations."
        },

        "typescript": {
            "keywords": ["typescript", "ts", "typescript programming", "microsoft typescript", "type safe javascript"],
            "response": "TypeScript is a superset of JavaScript developed by Microsoft in 2012, adding static type checking. It compiles to plain JavaScript and is used for large-scale web applications. Features include interfaces, generics, enums, and decorators. TypeScript catches errors at compile time, improves IDE support, and is the primary language for Angular framework. Popular for enterprise frontend and Node.js backend development."
        },

        "scala": {
            "keywords": ["scala", "scala programming", "scala language", "jvm scala", "functional programming scala"],
            "response": "Scala (Scalable Language) is a multi-paradigm programming language created by Martin Odersky in 2004. It runs on JVM and combines object-oriented and functional programming. Used for big data processing (Apache Spark), web services (Play Framework), and financial systems. Scala's concise syntax, pattern matching, and immutability by default make it powerful for concurrent and distributed systems."
        },

        "perl": {
            "keywords": ["perl", "perl programming", "perl language", "practical extraction and reporting language"],
            "response": "Perl is a high-level, general-purpose programming language created by Larry Wall in 1987. Known for text processing, regular expressions, and system administration. The motto 'There's more than one way to do it' reflects its flexibility. Perl 5 is widely used for CGI scripting, bioinformatics, and legacy systems. Perl 6 (now Raku) is a redesigned language. Perl's CPAN repository has thousands of modules."
        },

        "haskell": {
            "keywords": ["haskell", "haskell programming", "haskell language", "functional programming haskell"],
            "response": "Haskell is a purely functional, statically typed programming language named after logician Haskell Curry. Created in 1990, it emphasizes immutability, lazy evaluation, and mathematical purity. Used in academia, finance, and blockchain (Cardano). Haskell's advanced type system includes type inference, algebraic data types, and monads for side effects. Learning Haskell improves understanding of functional programming concepts applicable in other languages."
        },

        "lua": {
            "keywords": ["lua", "lua programming", "lua language", "scripting language lua", "embedded lua"],
            "response": "Lua is a lightweight, embeddable scripting language created in Brazil in 1993. Designed for extensibility and simplicity with a small footprint. Used in game development (World of Warcraft, Roblox), embedded systems, and configuration files. Lua's table data structure combines arrays and dictionaries. It's often used as an extension language for applications written in C/C++. LuaJIT provides just-in-time compilation for performance."
        },

        "dart": {
            "keywords": ["dart", "dart programming", "dart language", "google dart", "flutter dart"],
            "response": "Dart is a client-optimized programming language developed by Google in 2011. Used for building mobile, web, and desktop apps with the Flutter framework. Dart compiles to native code for mobile, JavaScript for web, and supports ahead-of-time (AOT) compilation. Features include sound null safety, async/await, and rich standard library. Dart is increasingly popular for cross-platform app development with hot reload for rapid iteration."
        },

        "r_lang": {
            "keywords": ["r language", "r programming", "r statistics", "r language for data science", "r project"],
            "response": "R is a programming language and environment for statistical computing and graphics, created in 1993. Widely used by statisticians, data scientists, and researchers for data analysis, visualization, and machine learning. R has extensive packages (CRAN repository) for specialized statistical techniques. Integrated with RStudio IDE. R's vectorized operations and functional programming features make it powerful for data manipulation and statistical modeling."
        },

        "matlab": {
            "keywords": ["matlab", "matlab programming", "matlab language", "matrix laboratory", "scientific computing matlab"],
            "response": "MATLAB (Matrix Laboratory) is a proprietary numerical computing environment and programming language created by MathWorks in 1984. Used for matrix manipulations, algorithm implementation, data visualization, and numerical analysis. Popular in engineering, physics, and finance for simulation and modeling. MATLAB's toolboxes extend functionality for signal processing, control systems, and machine learning. Simulink provides graphical programming for dynamic systems."
        },

        "groovy": {
            "keywords": ["groovy", "groovy programming", "groovy language", "apache groovy", "groovy on grails"],
            "response": "Groovy is a dynamic language for the Java Virtual Machine (JVM) created in 2003. Combines features from Python, Ruby, and Smalltalk with Java-like syntax. Used for scripting, testing (Spock framework), and web development (Grails framework). Groovy compiles to Java bytecode and interoperates seamlessly with Java libraries. Features include optional typing, closures, and builders for DSLs (Domain Specific Languages)."
        },

        "julia": {
            "keywords": ["julia", "julia programming", "julia language", "julia for scientific computing", "technical computing julia"],
            "response": "Julia is a high-level, high-performance dynamic programming language for technical computing, created in 2012. Designed for numerical analysis and computational science, combining speed of C with ease of Python. Julia uses just-in-time (JIT) compilation via LLVM. Features multiple dispatch, parametric types, and built-in package manager. Used in scientific computing, machine learning, and data science where performance is critical."
        },

        "elixir": {
            "keywords": ["elixir", "elixir programming", "elixir language", "elixir erlang vm", "phoenix framework"],
            "response": "Elixir is a functional, concurrent programming language that runs on the Erlang VM (BEAM), created by José Valim in 2011. Designed for building scalable, maintainable applications with fault tolerance. Used for web development (Phoenix framework), embedded systems, and distributed systems. Elixir inherits Erlang's actor model and provides modern syntax, macros, and tooling. Phoenix LiveView enables real-time web applications."
        },

        "clojure": {
            "keywords": ["clojure", "clojure programming", "clojure language", "lisp clojure", "jvm clojure"],
            "response": "Clojure is a modern Lisp dialect for the JVM, created by Rich Hickey in 2007. A functional programming language emphasizing immutability and persistent data structures. Used for data processing, web development, and concurrent systems. ClojureScript compiles to JavaScript for frontend development. Features include software transactional memory, macro system, and focus on simplicity. Clojure embraces the JVM ecosystem while providing Lisp's power."
        },

        "erlang": {
            "keywords": ["erlang", "erlang programming", "erlang language", "erlang otp", "concurrent programming erlang"],
            "response": "Erlang is a functional programming language developed by Ericsson in 1986 for telecommunications systems. Designed for building highly available, distributed, soft real-time systems. The actor model and OTP (Open Telecom Platform) framework provide concurrency, fault tolerance, and hot code swapping. Used in messaging apps (WhatsApp, WeChat), gaming backends, and financial systems. Erlang's 'let it crash' philosophy simplifies error handling."
        },

        "fsharp": {
            "keywords": ["f#", "f sharp", "fsharp programming", "functional programming f#", "dotnet f#"],
            "response": "F# (F Sharp) is a functional-first, cross-platform programming language for .NET, created by Microsoft Research in 2005. Combines functional, object-oriented, and imperative programming. Used for data science, web development, and financial modeling. F# features type inference, pattern matching, asynchronous programming, and units of measure. It runs on .NET Framework, .NET Core, and JavaScript via Fable. F# emphasizes correctness and expressiveness."
        },

        "cobol": {
            "keywords": ["cobol", "cobol programming", "cobol language", "common business oriented language"],
            "response": "COBOL (Common Business-Oriented Language) is one of the oldest programming languages, created in 1959. Designed for business data processing with English-like syntax. Still used in legacy banking, finance, and government systems (estimated 200+ billion lines in production). COBOL handles large-scale batch and transaction processing. Despite its age, COBOL systems are being modernized or migrated due to retiring experts and Y2K-like concerns."
        },

        "fortran": {
            "keywords": ["fortran", "fortran programming", "fortran language", "formula translation", "scientific computing fortran"],
            "response": "Fortran (Formula Translation) is the first high-level programming language, created by IBM in 1957. Still used in scientific computing, numerical weather prediction, computational physics, and engineering. Modern Fortran (2003/2008) includes object-oriented features, coarrays for parallel programming, and interoperability with C. Fortran compilers produce highly optimized numerical code. Many legacy scientific codes are in Fortran, with ongoing maintenance and modernization."
        },

        "assembly": {
            "keywords": ["assembly", "assembly language", "asm", "x86 assembly", "low level programming"],
            "response": "Assembly language is a low-level programming language specific to a computer architecture. It provides symbolic representation of machine code instructions. Used for operating systems, embedded systems, device drivers, and performance-critical code. Different architectures have different assembly languages (x86, ARM, MIPS). Assembly programming requires understanding of registers, memory addressing, and instruction sets. Often used with higher-level languages for optimization or hardware control."
        },

        "visual_basic": {
            "keywords": ["visual basic", "vb", "vb.net", "visual basic programming", "microsoft visual basic"],
            "response": "Visual Basic is an event-driven programming language and IDE from Microsoft, first released in 1991. Visual Basic .NET (VB.NET) is the modern, object-oriented version for .NET Framework. Used for Windows desktop applications (WinForms), Office macros, and legacy business applications. Known for rapid application development with drag-and-drop GUI builder. While declining in popularity, VB.NET remains in enterprise maintenance and migration projects."
        },

        "delphi": {
            "keywords": ["delphi", "delphi programming", "delphi language", "object pascal", "embarcadero delphi"],
            "response": "Delphi is an integrated development environment (IDE) for rapid application development using Object Pascal language, originally by Borland (1995). Used for Windows desktop applications, database applications, and some mobile development. Delphi's visual component library (VCL) and FireMonkey framework support cross-platform development. Known for compiled performance, database connectivity, and RAD capabilities. Delphi remains in legacy enterprise systems and specific vertical markets."
        },

        "objective_c": {
            "keywords": ["objective c", "objc", "objective-c programming", "apple objective c", "ios objective c"],
            "response": "Objective-C is an object-oriented programming language that adds Smalltalk-style messaging to C, created in early 1980s. It was Apple's primary language for macOS and iOS development before Swift. Still used in legacy Apple codebases and some frameworks. Objective-C's dynamic runtime enables features like method swizzling and categories. While largely superseded by Swift, understanding Objective-C helps with maintaining and bridging to existing Apple ecosystem code."
        },

        "powershell": {
            "keywords": ["powershell", "powershell scripting", "microsoft powershell", "windows powershell", "automation powershell"],
            "response": "PowerShell is a task automation and configuration management framework from Microsoft, with a command-line shell and scripting language. Released in 2006, it's built on .NET. Used for system administration, automation, and DevOps on Windows, with cross-platform PowerShell Core for Linux/macOS. PowerShell uses cmdlets (command-lets) and pipelines objects rather than text. It's essential for Windows Server administration, Azure automation, and enterprise IT management."
        },

        "bash": {
            "keywords": ["bash", "bash scripting", "bash shell", "linux bash", "shell scripting"],
            "response": "Bash (Bourne Again SHell) is a Unix shell and command language, the default on most Linux distributions and macOS. Created in 1989 as a free replacement for Bourne shell. Used for shell scripting, system administration, automation, and CLI interaction. Bash scripts combine commands, control structures, variables, and functions. Essential for DevOps, deployment scripts, and Unix/Linux system management. Bash is also available on Windows via WSL or Git Bash."
        },

        "sql": {
            "keywords": ["sql", "sql programming", "structured query language", "database query", "sql queries"],
            "response": "SQL (Structured Query Language) is a domain-specific language for managing and querying relational databases, developed in the 1970s. Used for data definition (CREATE, ALTER), manipulation (INSERT, UPDATE, DELETE), and querying (SELECT). SQL is not a general-purpose programming language but is essential for database interaction. Variants include PostgreSQL, MySQL, SQL Server, Oracle SQL. Modern extensions add procedural features (PL/SQL, T-SQL) and JSON support."
        },

        "pl_sql": {
            "keywords": ["pl/sql", "plsql", "oracle pl/sql", "procedural sql", "database programming"],
            "response": "PL/SQL (Procedural Language for SQL) is Oracle Corporation's procedural extension to SQL. Adds programming constructs like variables, conditions, loops, and exceptions to SQL. Used for writing stored procedures, functions, triggers, and packages in Oracle Database. PL/SQL code executes within the database server, reducing network traffic and improving performance for data-intensive operations. Similar extensions exist for other databases (T-SQL for SQL Server, PL/pgSQL for PostgreSQL)."
        },

        "vba": {
            "keywords": ["vba", "visual basic for applications", "excel vba", "office automation", "macro programming"],
            "response": "VBA (Visual Basic for Applications) is an implementation of Visual Basic embedded in Microsoft Office applications (Excel, Access, Word) for automation. Used for creating macros, automating repetitive tasks, and building custom business solutions within Office. VBA provides access to Office object models for programmatic control. While being replaced by Office JavaScript API and Power Automate, VBA remains widely used in finance, accounting, and data analysis for Excel automation."
        },

        "ada": {
            "keywords": ["ada", "ada programming", "ada language", "high integrity systems", "safety critical ada"],
            "response": "Ada is a structured, statically typed, imperative programming language designed by the US Department of Defense in the 1980s for high-reliability systems. Used in aviation (air traffic control), railway, military, and space systems (International Space Station). Ada emphasizes reliability, maintainability, and readability with strong typing, runtime checking, and contract-based programming (pre/post conditions). The SPARK subset adds formal verification for safety-critical systems."
        },

        "prolog": {
            "keywords": ["prolog", "prolog programming", "prolog language", "logic programming", "artificial intelligence prolog"],
            "response": "Prolog (Programming in Logic) is a logic programming language associated with artificial intelligence and computational linguistics, created in 1972. Based on formal logic with facts, rules, and queries. Used for natural language processing, theorem proving, expert systems, and constraint solving. Prolog programs declare what is true and what needs to be proved, with automatic backtracking search. Modern variants include SWI-Prolog and visual programming with Mercury."
        },

        "scheme": {
            "keywords": ["scheme", "scheme programming", "scheme language", "lisp scheme", "functional programming scheme"],
            "response": "Scheme is a minimalist dialect of Lisp, created in 1975 by Gerald Sussman and Guy Steele. Emphasizes functional programming and teaching computer science concepts. Known for its elegant simplicity, lexical scoping, and first-class continuations. Used in education (MIT's SICP course), scripting, and language research. Scheme influenced JavaScript and many functional languages. Racket is a descendant of Scheme with extensive libraries and pedagogical tools."
        },

        "racket": {
            "keywords": ["racket", "racket programming", "racket language", "scheme racket", "programming languages research"],
            "response": "Racket is a general-purpose, multi-paradigm programming language and platform for language creation, descended from Scheme. Created as a pedagogical tool for programming language theory. Used for teaching, research, scripting, and application development. Racket's macro system enables creating domain-specific languages (DSLs). The DrRacket IDE supports interactive development. Racket emphasizes language-oriented programming and is used in courses like 'How to Design Programs'."
        },

        "smalltalk": {
            "keywords": ["smalltalk", "smalltalk programming", "smalltalk language", "object oriented smalltalk", "live programming"],
            "response": "Smalltalk is an object-oriented, dynamically typed programming language created in the 1970s at Xerox PARC. Pioneered many OOP concepts: classes, objects, inheritance, and the MVC pattern. Smalltalk environments are image-based with live programming and reflection. Influenced Objective-C, Ruby, and Java. While less common today, Smalltalk's philosophy of 'everything is an object' and integrated development environment concepts remain influential in modern IDEs and languages."
        },

        "ocaml": {
            "keywords": ["ocaml", "ocaml programming", "ocaml language", "functional programming ocaml", "ml language"],
            "response": "OCaml is an industrial-strength functional programming language from the ML family, developed in 1996. Combines functional, imperative, and object-oriented programming with strong static typing and type inference. Used in compiler development (Rust's original compiler), formal verification, financial systems, and academic research. OCaml's module system provides powerful abstraction. Tools like ReasonML compile OCaml to JavaScript, and BuckleScript enables web development."
        },

        "nim": {
            "keywords": ["nim", "nim programming", "nim language", "nimrod", "systems programming nim"],
            "response": "Nim is a statically typed, compiled systems programming language with syntax resembling Python, created in 2008. Features include metaprogramming via templates and macros, memory safety with optional garbage collection, and compilation to C, C++, or JavaScript. Used for game development, embedded systems, and high-performance applications. Nim aims to be efficient, expressive, and elegant, combining ideas from Python, Ada, and Modula."
        },

        "crystal": {
            "keywords": ["crystal", "crystal programming", "crystal language", "ruby like crystal", "compiled crystal"],
            "response": "Crystal is a statically typed, compiled programming language with syntax inspired by Ruby, created in 2014. Aims for Ruby-like productivity with C-like performance. Features type inference, macros, and concurrency via fibers (similar to goroutines). Used for web development (Kemal framework), CLI tools, and systems programming. Crystal compiles to native code using LLVM, providing fast execution while maintaining high-level syntax familiar to Ruby developers."
        },

        "zig": {
            "keywords": ["zig", "zig programming", "zig language", "systems programming zig", "c replacement zig"],
            "response": "Zig is a general-purpose programming language designed for robustness, optimality, and clarity, created in 2016. Positioned as a modern alternative to C with better safety, compilation, and tooling. Features manual memory management without hidden allocations, compile-time code execution, and cross-compilation as a first-class feature. Used for operating systems, compilers, embedded systems, and high-performance software. Zig can interoperate with C and aims to improve upon C's shortcomings."
        },

        "reasonml": {
            "keywords": ["reasonml", "reason", "reason programming", "ocaml for javascript", "facebook reason"],
            "response": "ReasonML is a syntax extension and toolchain for OCaml that compiles to JavaScript and native code, created by Facebook in 2016. Provides familiar JavaScript-like syntax while leveraging OCaml's strong type system and performance. Used for React applications via ReasonReact, type-safe JavaScript interop, and full-stack development. ReasonML brings functional programming benefits to web development with excellent type inference and pattern matching."
        },

        "elm": {
            "keywords": ["elm", "elm programming", "elm language", "functional frontend", "web development elm"],
            "response": "Elm is a domain-specific functional programming language for building reliable web applications, created in 2012. Compiles to JavaScript with a focus on simplicity, performance, and no runtime exceptions. Elm's architecture enforces unidirectional data flow (similar to Redux) and provides strong guarantees. Used for frontend web development with a emphasis on maintainability and developer experience. Elm's compiler gives helpful error messages and enforces semantic versioning."
        },

        "coffeescript": {
            "keywords": ["coffeescript", "coffee script", "coffeescript programming", "javascript alternative", "syntactic sugar coffeescript"],
            "response": "CoffeeScript is a programming language that transcompiles to JavaScript, created in 2009. Provides syntactic sugar inspired by Ruby, Python, and Haskell to enhance JavaScript's brevity and readability. Features include significant whitespace, list comprehensions, and pattern matching. Popular in early 2010s, especially with Ruby on Rails community. While less used today due to ES6+ improvements, CoffeeScript influenced JavaScript evolution and demonstrated demand for cleaner syntax."
        },

        "actionscript": {
            "keywords": ["actionscript", "actionscript programming", "flash actionscript", "adobe actionscript", "flash platform"],
            "response": "ActionScript is an object-oriented programming language originally developed by Macromedia (later Adobe) for Flash platform. Used for web animations, games, and rich internet applications (RIAs) in the 2000s. ActionScript 3.0, based on ECMAScript, enabled complex applications with performance improvements. With the decline of Flash (end of life in 2020), ActionScript usage has diminished. Knowledge remains relevant for maintaining legacy Flash content and understanding multimedia programming concepts."
        },

        "logo": {
            "keywords": ["logo", "logo programming", "logo language", "turtle graphics", "educational programming"],
            "response": "Logo is an educational programming language created in 1967, known for turtle graphics. Used to teach programming concepts to children through drawing with a 'turtle' cursor. Logo's simple syntax and immediate visual feedback make it accessible for beginners. While not used in production, Logo influenced educational programming environments (Scratch, Python Turtle) and constructionist learning. Logo demonstrates how programming can be approachable and creative rather than purely technical."
        },

        "scratch": {
            "keywords": ["scratch", "scratch programming", "scratch language", "visual programming", "mit scratch"],
            "response": "Scratch is a block-based visual programming language and online community developed by MIT Media Lab in 2007. Designed for children ages 8-16 to learn programming concepts through creating interactive stories, games, and animations. Scratch uses drag-and-drop code blocks instead of text syntax. With millions of users worldwide, Scratch introduces computational thinking, creativity, and collaboration. Scratch 3.0 runs in browsers and on tablets, making programming accessible without installation."
        },

        "blockly": {
            "keywords": ["blockly", "blockly programming", "visual programming blockly", "google blockly", "block based coding"],
            "response": "Blockly is a visual programming editor by Google that uses interlocking blocks. It's a library for developers to create block-based programming environments (like Scratch) within web applications. Blockly generates code in JavaScript, Python, PHP, Lua, or Dart. Used in educational tools (Code.org, MIT App Inventor), robotics programming (LEGO Mindstorms), and configuration interfaces. Blockly makes programming accessible by removing syntax barriers while teaching logical thinking."
        },

        "apl": {
            "keywords": ["apl", "apl programming", "apl language", "array programming", "mathematical notation apl"],
            "response": "APL (A Programming Language) is an array programming language developed in the 1960s, known for its concise mathematical notation using special symbols. Operates on entire arrays without explicit loops. Used for mathematical modeling, data analysis, and financial applications. APL's terse syntax (often one-liners) and powerful array operations enable rapid prototyping. Modern implementations (Dyalog APL, GNU APL) maintain compatibility while adding GUI, .NET integration, and web capabilities."
        },

        "j": {
            "keywords": ["j language", "j programming", "array language j", "apl descendant", "ken iverson j"],
            "response": "J is a high-level, array programming language developed by Kenneth Iverson and Roger Hui in 1990 as a successor to APL. Uses ASCII characters instead of special symbols, making it more accessible. J applies functions to entire arrays efficiently. Used for mathematical and statistical computing, data analysis, and research. J's tacit programming (point-free style) and combinators enable concise expression of complex operations. Open-source implementation available for various platforms."
        },

        "labview": {
            "keywords": ["labview", "labview programming", "visual programming labview", "national instruments", "dataflow programming"],
            "response": "LabVIEW (Laboratory Virtual Instrument Engineering Workbench) is a visual programming language and development environment from National Instruments, created in 1986. Uses dataflow programming with graphical block diagrams (G code). Primarily used for instrument control, data acquisition, industrial automation, and test/measurement systems. LabVIEW's graphical approach suits engineers and scientists without traditional programming background. Real-time and FPGA modules extend capabilities for embedded and high-performance applications."
        },

        "vhdl": {
            "keywords": ["vhdl", "vhdl programming", "hardware description language", "digital circuit design", "fpga programming"],
            "response": "VHDL (VHSIC Hardware Description Language) is a hardware description language used for designing digital circuits, created by US Department of Defense in 1980s. Describes structure and behavior of electronic systems, particularly for FPGAs and ASICs. Used in digital design, verification, and synthesis. VHDL is strongly typed and concurrent, reflecting hardware parallelism. Similar to Verilog, with differences in syntax and capabilities. Knowledge of VHDL is essential for digital hardware engineers."
        },

        "verilog": {
            "keywords": ["verilog", "verilog programming", "hardware description verilog", "digital design", "asic design"],
            "response": "Verilog is a hardware description language used for modeling electronic systems, created in 1984. Widely used for designing and verifying digital circuits at register-transfer level (RTL) and gate level. Used in FPGA and ASIC development for consumer electronics, communications, and computing. SystemVerilog extends Verilog with verification features. Verilog's C-like syntax makes it accessible to software engineers. Knowledge of Verilog is crucial for digital design and verification engineering roles."
        },

        "systemverilog": {
            "keywords": ["systemverilog", "systemverilog programming", "hardware verification", "uvm", "verification language"],
            "response": "SystemVerilog is a hardware description and verification language that extends Verilog, standardized in 2005. Combines features from Verilog, VHDL, C++, and verification languages. Used for design, modeling, and verification of digital systems. Key features: object-oriented programming, constrained random testing, assertions, and coverage. Universal Verification Methodology (UVM) based on SystemVerilog is industry standard for verification. Essential for ASIC/FPGA verification engineers in semiconductor industry."
        },

        "tcl": {
            "keywords": ["tcl", "tcl programming", "tool command language", "scripting language tcl", "tk gui"],
            "response": "Tcl (Tool Command Language) is a dynamic scripting language created in 1988. Known for simplicity and embeddability, often paired with Tk GUI toolkit. Used in electronic design automation (EDA) tools, network equipment scripting, legacy enterprise systems, and rapid prototyping. Tcl's 'everything is a string' philosophy and simple syntax make it easy to learn. While less common today, Tcl remains in specific domains like hardware design tools and legacy automation systems."
        },

        "awk": {
            "keywords": ["awk", "awk programming", "text processing awk", "unix awk", "pattern scanning language"],
            "response": "AWK is a domain-specific language designed for text processing and data extraction, created in 1977. Named after authors Aho, Weinberger, and Kernighan. Used for pattern scanning, processing log files, transforming text data, and generating reports. AWK programs consist of pattern-action pairs applied to input lines. Available on all Unix-like systems, often used in shell pipelines. GNU Awk (gawk) extends functionality. AWK demonstrates the Unix philosophy of small, composable tools."
        },

        "sed": {
            "keywords": ["sed", "sed programming", "stream editor", "text processing sed", "unix sed"],
            "response": "sed (stream editor) is a Unix utility for parsing and transforming text, using a simple programming language. Created in 1974 as part of Unix. Used for find-and-replace operations, text filtering, and batch editing. sed processes input line by line, applying commands (substitution, deletion, insertion). Often used in shell scripts for automated text manipulation. While limited compared to full programming languages, sed's simplicity and efficiency make it valuable for specific text processing tasks."
        },

        "make": {
            "keywords": ["make", "makefile", "make programming", "build automation", "gnu make"],
            "response": "Make is a build automation tool that automatically builds executable programs from source code by reading Makefiles. Created in 1976 for Unix. Makefiles specify dependencies and rules for compiling and linking. Used in C/C++ projects, but applicable to any build process. GNU Make is the most common implementation. Make's declarative approach to build processes has influenced modern build tools (CMake, Bazel, etc.). Understanding Make is fundamental for software build systems and DevOps."
        },

        "cmake": {
            "keywords": ["cmake", "cmake programming", "build system cmake", "cross platform build", "meta build system"],
            "response": "CMake is a cross-platform, open-source build system generator, created in 2000. Instead of building directly, CMake generates native build files (Makefiles, Visual Studio projects, etc.). Used primarily for C/C++ but supports other languages. CMakeLists.txt files describe build configuration. Features: out-of-source builds, dependency management, testing, packaging. CMake has become standard for cross-platform C++ development. Modern CMake (3.0+) emphasizes target-based usage and better practices."
        },

        "processing": {
            "keywords": ["processing", "processing programming", "creative coding", "visual arts programming", "java processing"],
            "response": "Processing is a flexible software sketchbook and language for learning to code within visual arts, created in 2001. Based on Java with simplified syntax for graphics programming. Used by artists, designers, educators, and beginners for creating visualizations, animations, and interactive art. Processing emphasizes immediate visual feedback. p5.js is JavaScript version for web. Processing has spawned creative coding community and influenced computational art education."
        },

        "p5_js": {
            "keywords": ["p5.js", "p5js", "p5 javascript", "creative coding javascript", "processing web"],
            "response": "p5.js is a JavaScript library for creative coding, making coding accessible for artists, designers, educators, and beginners. Based on Processing philosophy but for web. Used for creating interactive graphics, animations, data visualizations, and digital art in browser. p5.js simplifies drawing, interaction, and multimedia. The web editor allows coding without installation. p5.js community promotes inclusive, creative technology education and has extensive learning resources and examples."
        },

        "opencl": {
            "keywords": ["opencl", "opencl programming", "parallel computing opencl", "gpu programming", "heterogeneous computing"],
            "response": "OpenCL (Open Computing Language) is a framework for writing programs that execute across heterogeneous platforms (CPUs, GPUs, DSPs, FPGAs). Created by Khronos Group in 2009. Used for parallel computing, scientific simulations, image processing, and machine learning acceleration. OpenCL C is a C99-based language for writing kernels. While facing competition from CUDA and SYCL, OpenCL remains important for cross-vendor GPU programming and embedded heterogeneous systems."
        },

        "cuda": {
            "keywords": ["cuda", "cuda programming", "nvidia cuda", "gpu programming cuda", "parallel computing cuda"],
            "response": "CUDA (Compute Unified Device Architecture) is a parallel computing platform and programming model created by NVIDIA for general-purpose computing on GPUs. CUDA C/C++ extends C/C++ with keywords and libraries for GPU programming. Used for scientific computing, deep learning, computer vision, and high-performance computing. CUDA enables massive parallelism by executing thousands of threads on GPU. While NVIDIA-specific, CUDA dominates GPU computing due to performance and ecosystem (cuDNN, TensorRT)."
        },

        "hlsl": {
            "keywords": ["hlsl", "hlsl programming", "high level shader language", "directx shaders", "gpu shader programming"],
            "response": "HLSL (High-Level Shader Language) is a proprietary shading language developed by Microsoft for DirectX. Used for writing shaders (vertex, pixel, geometry, compute) that run on GPU in Direct3D applications. Syntax similar to C. Used in game development, 3D graphics, and GPU computing on Windows. HLSL compiles to bytecode for Direct3D runtime. Knowledge of HLSL is essential for graphics programming on Windows/Xbox and using tools like Unity/Unreal Engine with DirectX backend."
        },

        "glsl": {
            "keywords": ["glsl", "glsl programming", "opengl shading language", "gpu shaders", "graphics programming"],
            "response": "GLSL (OpenGL Shading Language) is a high-level shading language for OpenGL, based on C syntax. Used for writing shaders that execute on GPU for rendering graphics. Types: vertex, fragment, geometry, tessellation, compute shaders. Used in game development, scientific visualization, and creative coding. GLSL is cross-platform (unlike HLSL). Vulkan uses SPIR-V intermediate representation but often authored in GLSL. Knowledge of GLSL is fundamental for real-time graphics programming across platforms."
        },

        "shaderlab": {
            "keywords": ["shaderlab", "unity shaders", "unity shader programming", "shader graph", "unity material system"],
            "response": "ShaderLab is Unity's shading language for writing shaders in Unity game engine. Combines configuration of shader properties with HLSL/GLSL/Cg code snippets. Used for creating custom materials, visual effects, and post-processing in Unity games. Unity also provides Shader Graph for visual shader creation without code. ShaderLab abstracts differences between graphics APIs (DirectX, OpenGL, Metal). Knowledge of ShaderLab and shader programming enhances visual quality and performance in Unity projects."
        },

        "maxscript": {
            "keywords": ["maxscript", "3ds max scripting", "autodesk maxscript", "3d animation scripting", "max script"],
            "response": "MAXScript is a built-in scripting language for Autodesk 3ds Max, used for automating tasks, creating custom tools, and extending functionality. Syntax similar to JavaScript/Python. Used by 3D artists, technical artists, and pipeline developers for animation, modeling, rendering automation. MAXScript can access nearly all 3ds Max features programmatically. While Python scripting is also available, MAXScript remains integral to 3ds Max workflow, especially for legacy scripts and specific automation tasks."
        },

        "mel": {
            "keywords": ["mel", "maya embedded language", "autodesk maya scripting", "3d animation mel", "maya scripting"],
            "response": "MEL (Maya Embedded Language) is a scripting language for Autodesk Maya, used for automation, custom tools, and workflow enhancement. Created specifically for Maya with commands mapping to Maya functionality. Used by 3D artists, technical directors, and pipeline developers. While Python is now preferred for complex tools (Maya Python API), MEL remains for simpler scripts and legacy code. Understanding MEL helps with Maya customization and understanding Maya's architecture and history."
        },

        "gcode": {
            "keywords": ["gcode", "g-code", "cnc programming", "3d printing gcode", "manufacturing programming"],
            "response": "G-code is a programming language for computer numerical control (CNC) machines, including 3D printers, mills, and lathes. Consists of commands (G, M codes) controlling machine movements, speeds, temperatures, and functions. Not a general-purpose language but essential for manufacturing automation. 3D printer users often generate G-code from slicer software rather than writing manually. Understanding G-code helps troubleshoot prints, optimize settings, and create custom machine operations."
        },

        "lisp": {
            "keywords": ["lisp", "lisp programming", "lisp language", "list processing", "ai lisp"],
            "response": "Lisp (List Processing) is a family of programming languages with a long history, dating to 1958. Known for its distinctive parenthesized prefix notation and code-as-data philosophy (homoiconicity). Used historically in artificial intelligence research, symbolic computing, and as an extension language (Emacs Lisp). Modern dialects: Common Lisp, Scheme, Clojure. Lisp pioneered many concepts: garbage collection, dynamic typing, conditionals, higher-order functions. Lisp's macro system enables powerful metaprogramming."
        },

        "common_lisp": {
            "keywords": ["common lisp", "common lisp programming", "lisp dialect", "ansi common lisp", "industrial lisp"],
            "response": "Common Lisp is a dialect of Lisp standardized by ANSI, combining features from earlier Lisp dialects. Created in 1984 as a successor to MacLisp. Used in AI, rapid prototyping, and niche applications requiring interactive development. Features: powerful object system (CLOS), condition system, compiler, and extensive standard. Common Lisp implementations (SBCL, Clozure CL) provide high performance. While less mainstream, Common Lisp remains in research, education, and specific industries like defense and finance."
        },

        # Programming Concepts
        "object_oriented": {
            "keywords": ["object oriented", "oop", "object oriented programming", "oop principles", "class and object"],
            "response": "Object-Oriented Programming (OOP) is a programming paradigm based on objects containing data (attributes) and methods (functions). Key concepts: Classes (blueprints), Objects (instances), Inheritance (reusing code), Polymorphism (many forms), Encapsulation (data hiding), and Abstraction (hiding complexity). OOP improves code organization, reusability, and maintainability."
        },

        "database": {
            "keywords": ["database", "sql", "database management", "relational database", "nosql"],
            "response": "A database is an organized collection of data stored and accessed electronically. SQL (Structured Query Language) manages relational databases (MySQL, PostgreSQL). NoSQL databases (MongoDB, Cassandra) handle unstructured data. Key concepts: Tables, Rows, Columns, Primary/Foreign Keys, ACID properties (Atomicity, Consistency, Isolation, Durability), and normalization."
        },

        "web_development": {
            "keywords": ["web development", "web developer", "frontend backend", "full stack", "web applications"],
            "response": "Web development involves creating websites and web applications. Frontend (client-side) uses HTML (structure), CSS (styling), JavaScript (behavior). Backend (server-side) uses languages like Node.js, Python, Java, PHP with frameworks. Full-stack developers work on both. Modern web development includes APIs, responsive design, progressive web apps, and single-page applications (SPA)."
        },

        "machine_learning": {
            "keywords": ["machine learning", "ml", "ai ml", "machine learning algorithms", "deep learning"],
            "response": "Machine learning is a subset of AI that enables systems to learn from data without explicit programming. Types: Supervised (labeled data), Unsupervised (finding patterns), Reinforcement (reward-based). Algorithms include linear regression, decision trees, neural networks. Deep learning uses multi-layer neural networks for complex tasks like image/speech recognition. Libraries: TensorFlow, PyTorch, scikit-learn."
        },

        "cloud_computing": {
            "keywords": ["cloud computing", "aws", "azure", "google cloud", "cloud services", "iaas paas saas"],
            "response": "Cloud computing delivers computing services (servers, storage, databases, networking, software) over the internet. Deployment models: Public, Private, Hybrid. Service models: IaaS (Infrastructure), PaaS (Platform), SaaS (Software). Major providers: AWS, Microsoft Azure, Google Cloud Platform. Benefits: scalability, cost-efficiency, reliability. Concepts: virtualization, containers, serverless computing."
        },

        "data_structures": {
            "keywords": ["data structures", "data structure", "linked list", "tree", "graph", "hash table"],
            "response": "Data structures are ways to organize and store data efficiently. Fundamental types: Arrays, Linked Lists, Stacks, Queues, Trees (binary, BST, AVL), Graphs, Hash Tables. Each has operations (insert, delete, search) with different time/space complexities. Choosing the right data structure optimizes algorithm performance. Data structures are foundational for algorithm design and software development."
        },

        "algorithms": {
            "keywords": ["algorithms", "algorithm design", "algorithm analysis", "sorting algorithms", "searching algorithms"],
            "response": "Algorithms are step-by-step procedures for solving problems. Key algorithm categories: Sorting (Quick Sort, Merge Sort), Searching (Binary Search), Graph (Dijkstra's, BFS/DFS), Dynamic Programming. Algorithm analysis measures efficiency using Big O notation (time/space complexity). Design paradigms: Divide and Conquer, Greedy, Dynamic Programming, Backtracking. Algorithm knowledge is crucial for optimization and scalable solutions."
        },

        "design_patterns": {
            "keywords": ["design patterns", "software patterns", "creational patterns", "structural patterns", "behavioral patterns"],
            "response": "Design patterns are reusable solutions to common software design problems. Types: Creational (Singleton, Factory), Structural (Adapter, Decorator), Behavioral (Observer, Strategy). Patterns provide proven approaches, improve code readability and maintainability. The Gang of Four (GoF) book popularized 23 classic patterns. Understanding patterns helps in writing flexible, scalable, and clean code."
        },

        "software_architecture": {
            "keywords": ["software architecture", "system design", "architectural patterns", "microservices", "monolithic"],
            "response": "Software architecture defines the high-level structure of a system, its components, and their interactions. Patterns: Monolithic (single unit), Microservices (independent services), Client-Server, MVC (Model-View-Controller). Architecture decisions affect scalability, maintainability, performance. System design includes load balancing, caching, databases, APIs. Good architecture aligns with business requirements and technical constraints."
        },

        "api": {
            "keywords": ["api", "application programming interface", "rest api", "web api", "api design"],
            "response": "An API (Application Programming Interface) defines how software components interact. Web APIs enable communication between applications over HTTP. REST (Representational State Transfer) is a common architectural style using HTTP methods (GET, POST, PUT, DELETE). SOAP is another protocol. API design includes endpoints, request/response formats (JSON/XML), authentication (OAuth, API keys), versioning, and documentation."
        },

        "devops": {
            "keywords": ["devops", "continuous integration", "continuous deployment", "ci cd", "infrastructure as code"],
            "response": "DevOps combines development and operations to shorten development lifecycle and deliver high-quality software. Practices: Continuous Integration (CI), Continuous Deployment (CD), Infrastructure as Code (IaC), monitoring, and logging. Tools: Docker (containers), Kubernetes (orchestration), Jenkins (CI/CD), Terraform (IaC). DevOps culture emphasizes collaboration, automation, and iterative improvement."
        },

        "containerization": {
            "keywords": ["containerization", "docker", "containers", "kubernetes", "container orchestration"],
            "response": "Containerization packages an application with its dependencies into a container that runs consistently across environments. Docker is the most popular container platform. Containers are lightweight, portable, and isolated. Kubernetes orchestrates container deployment, scaling, and management. Benefits: consistency, efficiency, scalability. Containerization revolutionized deployment and microservices architecture."
        },

        "version_control": {
            "keywords": ["version control", "git", "github", "gitlab", "source control"],
            "response": "Version control systems track changes to code over time, enabling collaboration and rollback. Git is the most widely used distributed version control system. Platforms: GitHub, GitLab, Bitbucket. Key concepts: Repository, Commit, Branch, Merge, Pull Request. Version control is essential for team collaboration, code review, and maintaining project history. Git workflows include Git Flow and GitHub Flow."
        },

        "testing": {
            "keywords": ["software testing", "unit testing", "integration testing", "test driven development", "testing frameworks"],
            "response": "Software testing ensures code quality and functionality. Types: Unit (individual components), Integration (interfaces), System (entire system), Acceptance (user requirements). Test-Driven Development (TDD) writes tests before code. Testing frameworks: JUnit (Java), pytest (Python), Jest (JavaScript). Automated testing improves reliability and reduces bugs. Testing also includes performance, security, and usability testing."
        },

        "security": {
            "keywords": ["cybersecurity", "application security", "web security", "encryption", "authentication"],
            "response": "Application security protects software from threats. Common vulnerabilities: Injection attacks (SQL, XSS), broken authentication, sensitive data exposure. Security practices: Input validation, encryption (SSL/TLS), secure authentication (OAuth, JWT), regular updates. Security testing includes penetration testing and code analysis. Following security best practices and standards (OWASP) is crucial for protecting data and systems."
        },

        "concurrency": {
            "keywords": ["concurrency", "multithreading", "parallel programming", "async programming", "threads"],
            "response": "Concurrency enables multiple tasks to make progress simultaneously. Multithreading runs multiple threads within a process. Parallel programming uses multiple processors. Asynchronous programming handles tasks without blocking. Challenges: race conditions, deadlocks, thread safety. Concurrency improves performance on multi-core systems. Languages provide constructs: threads (Java), async/await (Python, JavaScript), goroutines (Go)."
        },

        "functional_programming": {
            "keywords": ["functional programming", "fp", "lambda", "higher order functions", "immutable data"],
            "response": "Functional Programming (FP) treats computation as evaluation of mathematical functions, avoiding state and mutable data. Principles: Pure functions (no side effects), Immutability, First-class functions, Higher-order functions, Recursion. FP languages: Haskell, Lisp. Many languages support FP features (JavaScript, Python, Scala). Benefits: predictability, testability, concurrency. FP complements OOP in modern development."
        },

        "compilers": {
            "keywords": ["compilers", "compiler design", "interpreters", "lexical analysis", "syntax analysis"],
            "response": "A compiler translates source code into machine code. Phases: Lexical Analysis (tokens), Syntax Analysis (parsing), Semantic Analysis (meaning), Optimization, Code Generation. Interpreters execute code directly without compilation. Just-In-Time (JIT) compilation combines both. Understanding compilers helps in writing efficient code and developing programming languages. Tools like Lex and Yacc assist in compiler construction."
        },

        "operating_systems": {
            "keywords": ["operating systems", "os concepts", "process management", "memory management", "file systems"],
            "response": "Operating systems manage hardware and provide services for applications. Core concepts: Process Management (scheduling, synchronization), Memory Management (virtual memory, paging), File Systems, I/O Systems. OS kernels (Linux, Windows NT) handle low-level operations. Understanding OS principles is essential for system programming, performance optimization, and developing efficient applications."
        },

        "networking": {
            "keywords": ["computer networking", "network protocols", "tcp ip", "http", "socket programming"],
            "response": "Computer networking enables communication between devices. TCP/IP is the fundamental protocol suite. Layers: Application (HTTP, FTP), Transport (TCP, UDP), Network (IP), Link (Ethernet). Key concepts: IP addresses, ports, DNS, routers, switches. Socket programming creates network applications. Understanding networking is crucial for web development, distributed systems, and cybersecurity."
        },

        "distributed_systems": {
            "keywords": ["distributed systems", "distributed computing", "consensus algorithms", "distributed databases", "scalability"],
            "response": "Distributed systems consist of multiple computers communicating to achieve a goal. Challenges: Concurrency, partial failures, consistency. Concepts: Consensus algorithms (Paxos, Raft), replication, sharding, CAP theorem (Consistency, Availability, Partition tolerance). Technologies: Distributed databases (Cassandra), message queues (Kafka). Distributed systems enable scalability, fault tolerance, and high availability for large-scale applications."
        },

        "big_data": {
            "keywords": ["big data", "hadoop", "spark", "data processing", "data analytics"],
            "response": "Big data handles large, complex datasets beyond traditional processing. Characteristics: Volume, Velocity, Variety, Veracity. Technologies: Hadoop (MapReduce, HDFS), Apache Spark (in-memory processing), NoSQL databases. Big data enables analytics, machine learning, and insights from massive data. Processing frameworks handle batch and stream processing. Cloud platforms offer managed big data services."
        },

        "data_science": {
            "keywords": ["data science", "data analysis", "data visualization", "statistics", "predictive modeling"],
            "response": "Data science extracts insights from data using statistics, programming, and domain knowledge. Process: Data collection, cleaning, exploration, modeling, visualization. Tools: Python (pandas, NumPy), R, SQL, visualization libraries (Matplotlib, Tableau). Techniques: Statistical analysis, machine learning, predictive modeling. Data science drives decision-making in business, science, and technology."
        },

        "artificial_intelligence": {
            "keywords": ["artificial intelligence", "ai", "expert systems", "natural language processing", "computer vision"],
            "response": "Artificial Intelligence (AI) creates systems that perform tasks requiring human intelligence. Subfields: Machine Learning, Natural Language Processing (NLP), Computer Vision, Robotics, Expert Systems. AI applications: chatbots, recommendation systems, autonomous vehicles. Approaches: Symbolic AI (rules-based), Statistical AI (data-driven). Modern AI uses deep learning for complex pattern recognition. Ethical considerations are important in AI development."
        },

        "natural_language_processing": {
            "keywords": ["natural language processing", "nlp", "text mining", "sentiment analysis", "language models"],
            "response": "Natural Language Processing (NLP) enables computers to understand, interpret, and generate human language. Tasks: Tokenization, Part-of-Speech tagging, Named Entity Recognition, Sentiment Analysis, Machine Translation. Techniques: Rule-based systems, Statistical models, Deep Learning (Transformers, BERT, GPT). Applications: Chatbots, search engines, text summarization. NLP bridges linguistics and computer science."
        },

        "computer_vision": {
            "keywords": ["computer vision", "image processing", "object detection", "facial recognition", "cv algorithms"],
            "response": "Computer Vision (CV) enables computers to interpret visual information from the world. Tasks: Image classification, Object detection, Segmentation, Facial recognition. Techniques: Traditional (edge detection, filters), Deep Learning (CNNs - Convolutional Neural Networks). Applications: Autonomous vehicles, medical imaging, surveillance. Libraries: OpenCV, TensorFlow, PyTorch. CV combines image processing, pattern recognition, and machine learning."
        },

        "robotics": {
            "keywords": ["robotics", "robot programming", "autonomous systems", "robot operating system", "motion planning"],
            "response": "Robotics involves designing, building, and programming robots. Key areas: Perception (sensors), Planning (pathfinding), Control (actuators). Robot Operating System (ROS) is a framework for robot software. Programming robots involves algorithms for navigation, manipulation, and decision-making. Robotics applications: manufacturing, healthcare, exploration. Integration of AI enables autonomous robots."
        },

        "embedded_systems": {
            "keywords": ["embedded systems", "microcontroller programming", "iot devices", "real time systems", "firmware"],
            "response": "Embedded systems are specialized computing systems within larger devices. Components: Microcontrollers/microprocessors, sensors, actuators. Programming: C/C++ often used for efficiency and hardware control. Real-time operating systems (RTOS) handle timing constraints. Embedded systems power IoT devices, automotive systems, medical devices. Development requires hardware knowledge and low-level programming skills."
        },

        "game_development": {
            "keywords": ["game development", "game engines", "unity", "unreal engine", "game programming"],
            "response": "Game development creates video games using programming, design, and art. Game engines: Unity (C#), Unreal Engine (C++), Godot. Concepts: Game loops, physics engines, collision detection, AI for NPCs, rendering graphics. Game programming involves graphics (OpenGL/DirectX), audio, input handling, networking for multiplayer. Development includes pre-production, production, testing, and deployment across platforms."
        },

        "mobile_development": {
            "keywords": ["mobile development", "android development", "ios development", "react native", "flutter"],
            "response": "Mobile development creates applications for smartphones/tablets. Native: Android (Java/Kotlin), iOS (Swift/Objective-C). Cross-platform: React Native (JavaScript), Flutter (Dart), Xamarin (C#). Development involves UI design, API integration, performance optimization. App stores (Google Play, Apple App Store) distribute apps. Mobile development considers device fragmentation, battery life, and user experience."
        },

        "desktop_development": {
            "keywords": ["desktop development", "gui applications", "desktop apps", "electron", "qt framework"],
            "response": "Desktop development creates applications for Windows, macOS, Linux. Native: Windows (C#/WPF, C++), macOS (Swift, Objective-C), Linux (C++, GTK). Cross-platform: Electron (HTML/CSS/JS), Java (Swing, JavaFX), Qt (C++). Desktop apps have access to system resources, file systems. Modern desktop apps often use web technologies packaged as native apps (e.g., VS Code, Slack)."
        },

        "blockchain_development": {
            "keywords": ["blockchain development", "smart contracts", "ethereum", "dapps", "web3"],
            "response": "Blockchain development creates decentralized applications (DApps) on blockchain networks. Smart contracts (self-executing code) run on platforms like Ethereum (Solidity). Development involves cryptography, consensus algorithms, peer-to-peer networking. Web3 technologies enable interaction with blockchains. Use cases: cryptocurrencies, DeFi, NFTs, supply chain. Development tools: Truffle, Hardhat, MetaMask."
        },

        "quantum_computing_programming": {
            "keywords": ["quantum computing programming", "quantum algorithms", "qiskit", "quantum programming languages"],
            "response": "Quantum computing programming uses quantum algorithms that leverage superposition and entanglement. Quantum programming languages: Q# (Microsoft), Qiskit (IBM Python framework), Cirq (Google). Concepts: Qubits, quantum gates, quantum circuits. Algorithms: Shor's (factoring), Grover's (search). Quantum programming is experimental, targeting future quantum computers for problems intractable for classical computers."
        },

        "performance_optimization": {
            "keywords": ["performance optimization", "code optimization", "profiling", "memory optimization", "algorithm optimization"],
            "response": "Performance optimization improves software speed and efficiency. Techniques: Algorithm optimization (better time complexity), Code profiling (identifying bottlenecks), Memory optimization (reducing footprint), Parallelization, Caching. Tools: Profilers (VisualVM, gprof), monitoring. Optimization follows 'measure first' principle and considers trade-offs (readability vs. performance). Critical for high-load systems and resource-constrained environments."
        },

        "code_quality": {
            "keywords": ["code quality", "clean code", "code review", "refactoring", "coding standards"],
            "response": "Code quality ensures software is maintainable, readable, and reliable. Principles: Clean Code (meaningful names, small functions), DRY (Don't Repeat Yourself), SOLID principles. Practices: Code reviews, Refactoring (improving structure without changing behavior), Unit testing, Static analysis. Coding standards and style guides (PEP 8, Google Style) promote consistency. High-quality code reduces bugs and technical debt."
        },

        "software_development_lifecycle": {
            "keywords": ["software development lifecycle", "sdlc", "agile methodology", "waterfall model", "devops lifecycle"],
            "response": "Software Development Lifecycle (SDLC) is the process for planning, creating, testing, deploying, and maintaining software. Models: Waterfall (sequential), Agile (iterative, Scrum, Kanban), DevOps (continuous). Phases: Requirements, Design, Implementation, Testing, Deployment, Maintenance. SDLC ensures systematic development, quality control, and project management. Modern approaches emphasize collaboration, adaptability, and automation."
        },

        "project_management": {
            "keywords": ["software project management", "agile project management", "scrum master", "project planning", "risk management"],
            "response": "Software project management plans, executes, and controls software projects. Methodologies: Agile (Scrum, Kanban), Waterfall, Hybrid. Roles: Product Owner, Scrum Master, Development Team. Tools: Jira, Trello, Asana. Activities: Requirement gathering, sprint planning, daily stand-ups, retrospectives. Risk management identifies and mitigates potential problems. Effective management delivers projects on time, within budget, meeting quality standards."
        },

        "technical_documentation": {
            "keywords": ["technical documentation", "api documentation", "code documentation", "user manuals", "technical writing"],
            "response": "Technical documentation explains software for developers, users, and stakeholders. Types: API documentation (Swagger/OpenAPI), Code comments (Javadoc, Doxygen), User manuals, Architecture diagrams. Good documentation improves usability, maintenance, and onboarding. Documentation tools: Markdown, Sphinx, ReadTheDocs. Technical writing requires clarity, accuracy, and audience awareness. Documentation is crucial for open-source and enterprise software."
        },

        "open_source": {
            "keywords": ["open source", "open source software", "contributing to open source", "licenses", "github repositories"],
            "response": "Open source software has source code publicly available for use, modification, and distribution. Licenses: MIT, GPL, Apache govern usage. Contributing: Fix bugs, add features, improve documentation. Platforms: GitHub, GitLab, Bitbucket host repositories. Open source fosters collaboration, transparency, and innovation. Many technologies (Linux, Kubernetes, React) are open source. Participation builds skills and community."
        },

        "career_development": {
            "keywords": ["programming career", "software engineer career", "tech interviews", "coding bootcamps", "computer science degree"],
            "response": "Programming careers offer diverse paths: Software Engineer, Data Scientist, DevOps, etc. Education: Computer Science degrees, coding bootcamps, self-learning. Skills: Technical (languages, tools), Soft (communication, problem-solving). Career growth: Junior to Senior, Lead, Architect. Interview preparation: Data structures, algorithms, system design, behavioral questions. Continuous learning through courses, conferences, and projects is essential in evolving tech field."
        },

        "programming_paradigms": {
            "keywords": ["programming paradigms", "imperative programming", "declarative programming", "procedural programming", "logic programming"],
            "response": "Programming paradigms are styles of programming. Imperative: How to achieve (C, Java). Declarative: What to achieve (SQL, HTML). Sub-paradigms: Procedural (functions), Object-Oriented, Functional, Logic (Prolog), Event-driven. Multi-paradigm languages (Python, JavaScript) support multiple styles. Understanding paradigms helps choose appropriate approaches for different problems and write more expressive code."
        },

        "software_engineering_principles": {
            "keywords": ["software engineering principles", "solid principles", "dry principle", "kiss principle", "yagni"],
            "response": "Software engineering principles guide design and development. SOLID: Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion. Other principles: DRY (Don't Repeat Yourself), KISS (Keep It Simple, Stupid), YAGNI (You Aren't Gonna Need It). These principles promote maintainable, scalable, and robust software. They are fundamental in object-oriented design and general software architecture."
        },

        "debugging": {
            "keywords": ["debugging", "debugging techniques", "debugging tools", "logging", "breakpoints"],
            "response": "Debugging identifies and fixes bugs in software. Techniques: Print debugging, Logging, Using debuggers (breakpoints, stepping), Rubber duck debugging (explaining code). Tools: IDE debuggers (VS Code, IntelliJ), command-line (GDB), browser dev tools. Effective debugging requires systematic approach: reproduce bug, isolate cause, fix, test. Logging frameworks capture runtime information for post-mortem analysis."
        },

        "code_review": {
            "keywords": ["code review", "peer review", "pull request review", "code review best practices", "collaborative coding"],
            "response": "Code review is examining code changes by peers before merging. Benefits: catching bugs, sharing knowledge, maintaining standards. Process: Submit pull request, reviewers comment, iterate, approve. Best practices: Be constructive, focus on code not person, review small changes, use checklists. Tools: GitHub, GitLab, Bitbucket facilitate code review. Code review improves code quality and team collaboration."
        },

        "refactoring": {
            "keywords": ["refactoring", "code refactoring", "refactoring techniques", "improving code design", "technical debt"],
            "response": "Refactoring improves code structure without changing external behavior. Techniques: Extract Method, Rename Variable, Move Method, Replace Conditional with Polymorphism. Refactoring reduces technical debt, improves readability, and eases future modifications. Done incrementally with tests to ensure correctness. Tools: IDE refactoring support, linters. Regular refactoring maintains code health as requirements evolve."
        },

        "continuous_integration": {
            "keywords": ["continuous integration", "ci", "jenkins", "github actions", "automated testing"],
            "response": "Continuous Integration (CI) automatically builds and tests code changes frequently. Developers integrate code into shared repository multiple times daily. CI servers (Jenkins, GitHub Actions, GitLab CI) run automated tests, check code style, and provide feedback. Benefits: early bug detection, consistent builds, faster release cycles. CI is part of DevOps practices, often followed by Continuous Deployment (CD)."
        },

        "microservices": {
            "keywords": ["microservices", "microservices architecture", "service oriented architecture", "api gateway", "service mesh"],
            "response": "Microservices architecture structures an application as a collection of loosely coupled, independently deployable services. Each service implements specific business capability and communicates via APIs (HTTP/RPC). Benefits: Scalability, flexibility, technology diversity. Challenges: Complexity, data consistency, networking. Patterns: API Gateway, Service Discovery, Circuit Breaker. Technologies: Docker, Kubernetes, Istio (service mesh) support microservices."
        },

        "serverless": {
            "keywords": ["serverless", "serverless computing", "aws lambda", "azure functions", "function as a service"],
            "response": "Serverless computing runs code without managing servers. Functions are triggered by events and scale automatically. Providers: AWS Lambda, Azure Functions, Google Cloud Functions. Benefits: No server management, pay-per-use, automatic scaling. Use cases: APIs, data processing, event-driven applications. Serverless architectures combine functions with other cloud services (databases, messaging). Considerations: cold starts, vendor lock-in, debugging."
        },

        "graphql": {
            "keywords": ["graphql", "graphql api", "graphql vs rest", "apollo", "graphql schema"],
            "response": "GraphQL is a query language for APIs that allows clients to request exactly the data they need. Unlike REST, GraphQL has a single endpoint and flexible queries. Components: Schema (types, queries, mutations), Resolvers (functions fetching data). Tools: Apollo, Relay. Benefits: Efficient data fetching, strong typing, introspective API. GraphQL is used by Facebook, GitHub, and many modern applications for flexible data access."
        },

        "rest": {
            "keywords": ["rest", "restful api", "rest architecture", "http methods", "rest principles"],
            "response": "REST (Representational State Transfer) is an architectural style for designing networked applications. RESTful APIs use HTTP methods: GET (retrieve), POST (create), PUT (update), DELETE (remove). Principles: Statelessness, client-server separation, uniform interface, cacheability. Resources are identified by URIs, representations (JSON/XML) transfer state. REST is widely used for web APIs due to simplicity and compatibility with HTTP."
        },

        "soap": {
            "keywords": ["soap", "soap api", "web services", "xml protocol", "enterprise integration"],
            "response": "SOAP (Simple Object Access Protocol) is a protocol for exchanging structured information in web services using XML. It operates over HTTP, SMTP, etc. Features: Standards-based (WS-*), built-in error handling, security. SOAP uses WSDL (Web Services Description Language) to describe services. Common in enterprise environments for reliable, secure communication. Compared to REST, SOAP is more rigid but offers more standards."
        },

        "websockets": {
            "keywords": ["websockets", "real time communication", "bidirectional communication", "socket.io", "web sockets protocol"],
            "response": "WebSockets provide full-duplex, bidirectional communication between client and server over a single, long-lived connection. Unlike HTTP's request-response, WebSockets enable real-time data exchange. Use cases: chat apps, live feeds, gaming, collaborative tools. Libraries: Socket.IO, ws. Protocol: Starts with HTTP handshake, upgrades to WebSocket. WebSockets are essential for low-latency, interactive applications."
        },

        "progressive_web_apps": {
            "keywords": ["progressive web apps", "pwa", "offline web apps", "service workers", "web app manifest"],
            "response": "Progressive Web Apps (PWAs) are web applications that provide native app-like experience. Features: Offline functionality (Service Workers), installable (Web App Manifest), push notifications, fast loading. PWAs work across platforms and are discoverable via web. Technologies: Service Workers cache resources, manifest defines app metadata. PWAs bridge web and mobile apps, improving engagement and performance."
        },

        "responsive_design": {
            "keywords": ["responsive design", "responsive web design", "mobile first", "css media queries", "flexbox grid"],
            "response": "Responsive design ensures web applications work well on various devices and screen sizes. Techniques: Fluid grids, Flexible images, CSS media queries. Approach: Mobile-first design, then enhance for larger screens. CSS frameworks: Bootstrap, Foundation. CSS features: Flexbox, Grid layout. Responsive design improves user experience, SEO, and maintenance by having one codebase for all devices."
        },

        "accessibility": {
            "keywords": ["web accessibility", "a11y", "wcag", "screen readers", "accessible design"],
            "response": "Web accessibility (a11y) ensures websites are usable by people with disabilities. Guidelines: WCAG (Web Content Accessibility Guidelines) - Perceivable, Operable, Understandable, Robust. Techniques: Semantic HTML, ARIA attributes, keyboard navigation, color contrast, alt text. Testing: Screen readers (NVDA, VoiceOver), automated tools (axe). Accessibility is a legal requirement in many regions and improves usability for all users."
        },

        "seo": {
            "keywords": ["seo", "search engine optimization", "web seo", "meta tags", "page speed"],
            "response": "SEO (Search Engine Optimization) improves website visibility in search engine results. Technical SEO: Site speed, mobile-friendliness, secure connections (HTTPS), structured data (JSON-LD). On-page: Title tags, meta descriptions, header tags, quality content. Off-page: Backlinks, social signals. SEO tools: Google Search Console, analytics. Good SEO practices increase organic traffic and are essential for online presence."
        },

        "cross_browser_compatibility": {
            "keywords": ["cross browser compatibility", "browser testing", "polyfills", "vendor prefixes", "web standards"],
            "response": "Cross-browser compatibility ensures websites work across different browsers (Chrome, Firefox, Safari, Edge). Challenges: Different rendering engines, CSS support, JavaScript APIs. Techniques: Feature detection, polyfills (for missing features), vendor prefixes for CSS, progressive enhancement. Testing: BrowserStack, Sauce Labs. Following web standards and testing early helps deliver consistent user experiences."
        },

        "internationalization": {
            "keywords": ["internationalization", "i18n", "localization", "multi language support", "unicode"],
            "response": "Internationalization (i18n) designs software to support multiple languages and regions. Localization (l10n) adapts for specific locale. Techniques: Externalize strings (resource files), support Unicode, format dates/numbers/currencies per locale, handle text direction (RTL). Libraries: ICU, i18next. Internationalization is important for global applications, improving reach and user experience for diverse audiences."
        },

        "scalability": {
            "keywords": ["scalability", "scalable architecture", "horizontal scaling", "vertical scaling", "load balancing"],
            "response": "Scalability is a system's ability to handle increased load. Vertical scaling: Adding resources to a single node. Horizontal scaling: Adding more nodes. Techniques: Load balancing, caching (CDN, Redis), database sharding, stateless design, asynchronous processing. Scalability planning considers growth patterns and bottlenecks. Cloud platforms provide auto-scaling. Scalable systems maintain performance under varying loads."
        },

        "fault_tolerance": {
            "keywords": ["fault tolerance", "high availability", "redundancy", "failover", "disaster recovery"],
            "response": "Fault tolerance ensures system continues operating despite failures. Techniques: Redundancy (multiple instances), Failover (automatic switching to backup), Replication (data copies), Circuit Breakers (prevent cascade failures). Design: Retry mechanisms, graceful degradation, health checks. High availability aims for minimal downtime (e.g., 99.99% uptime). Fault tolerance is critical for reliable services, especially in distributed systems."
        },

        "monitoring": {
            "keywords": ["monitoring", "application monitoring", "logs", "metrics", "alerting"],
            "response": "Monitoring tracks system performance and health. Components: Logging (events), Metrics (numerical data), Tracing (request flow), Alerting (notifications). Tools: Prometheus (metrics), ELK Stack (logs), Grafana (visualization), New Relic, Datadog. Monitoring helps detect issues, understand usage patterns, and ensure SLA compliance. Observability (logs, metrics, traces) provides insights into system internals."
        },

        "logging": {
            "keywords": ["logging", "application logs", "structured logging", "log levels", "log aggregation"],
            "response": "Logging records events during software execution for debugging and auditing. Log levels: DEBUG, INFO, WARN, ERROR. Best practices: Structured logging (JSON), meaningful messages, appropriate levels, avoid sensitive data. Log aggregation: Centralize logs from multiple sources (Fluentd, Logstash). Analysis: Search, visualize, set alerts. Effective logging is crucial for troubleshooting and understanding application behavior in production."
        },

        "performance_monitoring": {
            "keywords": ["performance monitoring", "apm", "application performance management", "latency", "throughput"],
            "response": "Performance monitoring measures application speed, responsiveness, and resource usage. Key metrics: Latency (response time), Throughput (requests per second), Error rate, CPU/Memory usage. APM tools: New Relic, AppDynamics, Dynatrace provide deep insights. Real User Monitoring (RUM) captures end-user experience. Performance monitoring identifies bottlenecks and ensures applications meet performance goals."
        },

        "load_testing": {
            "keywords": ["load testing", "performance testing", "stress testing", "jmeter", "locust"],
            "response": "Load testing evaluates system performance under expected and peak loads. Types: Load testing (normal load), Stress testing (beyond capacity), Soak testing (endurance). Tools: JMeter, Locust, Gatling. Metrics: Response time, throughput, error rate, resource utilization. Load testing helps identify performance limits, plan capacity, and ensure stability before deployment. It is part of performance engineering."
        },

        "security_testing": {
            "keywords": ["security testing", "penetration testing", "vulnerability scanning", "owasp testing", "security audit"],
            "response": "Security testing identifies vulnerabilities in software. Types: Penetration testing (simulated attacks), Vulnerability scanning (automated tools), Code review, Security audits. OWASP Top 10 lists common vulnerabilities (injection, XSS). Tools: Burp Suite, OWASP ZAP, Nessus. Security testing should be integrated into SDLC (DevSecOps). Regular testing protects against breaches and ensures compliance with security standards."
        },
        # Expanded Geography and Countries
        "geography": {
            "keywords": ["geography", "geographical", "world geography", "study of geography", "physical geography", "human geography"],
            "response": "Geography is the study of Earth's landscapes, environments, and the relationships between people and their environments. It includes physical geography (landforms, climate, ecosystems) and human geography (population, culture, economics). Geography helps us understand spatial relationships and global interconnections."
        },

        "continents": {
            "keywords": ["continents", "how many continents", "list of continents", "seven continents", "continental landmasses"],
            "response": "There are 7 continents: Asia (largest by area and population), Africa, North America, South America, Antarctica, Europe, and Australia/Oceania (smallest). Some models consider 6 continents by combining Europe and Asia as Eurasia. Continents were once joined in the supercontinent Pangaea about 335 million years ago."
        },

        "asia": {
            "keywords": ["asia", "asian continent", "about asia", "asia geography"],
            "response": "Asia is the world's largest and most populous continent, covering 44.6 million square km (30% of Earth's land area) with 4.7 billion people. It contains 48 countries, diverse landscapes from the Himalayas to deserts, and major economies like China, Japan, and India. Asia is the birthplace of major religions and ancient civilizations."
        },

        "india": {
            "keywords": ["india", "about india", "indian geography", "republic of india", "india country"],
            "response": "India is the seventh-largest country by area (3.29 million sq km) and the most populous democracy with 1.4 billion people. Located in South Asia, its capital is New Delhi. India has diverse geography from the Himalayas to tropical beaches, 22 official languages, and rich cultural heritage including Hinduism, Buddhism, and multiple UNESCO World Heritage Sites."
        },

        "usa": {
            "keywords": ["usa", "united states", "america geography", "united states of america", "us geography"],
            "response": "The United States of America is the world's third-largest country by area (9.8 million sq km) and third most populous (331 million). Located in North America with 50 states, its capital is Washington D.C. The US has diverse geography from Alaska's tundra to Florida's tropics, major cities like New York and Los Angeles, and is a global economic and cultural superpower."
        },

        "china": {
            "keywords": ["china", "about china", "chinese geography", "people's republic of china", "china country"],
            "response": "China is the world's most populous country (1.4 billion) and third-largest by area (9.6 million sq km). Located in East Asia, its capital is Beijing. China features diverse landscapes from the Gobi Desert to the Yangtze River, ancient civilization dating back 5,000 years, and has become the world's second-largest economy with rapid modernization."
        },

        "europe": {
            "keywords": ["europe", "european countries", "europe geography", "european continent", "about europe"],
            "response": "Europe is the world's second-smallest continent (10.2 million sq km) with 44 countries and about 750 million people. It's known for rich history from ancient Greece and Rome to the Renaissance, diverse cultures and languages, major economies (Germany, France, UK), and landmarks like the Eiffel Tower, Colosseum, and Parthenon."
        },

        "africa": {
            "keywords": ["africa", "african continent", "africa geography", "about africa", "african countries"],
            "response": "Africa is the world's second-largest continent (30.4 million sq km) with 54 countries and 1.4 billion people. It's the origin of humankind, home to diverse ecosystems from the Sahara Desert to rainforests, the Nile River (longest), rich mineral resources, and fastest-growing population. Africa has over 2,000 languages and diverse cultures."
        },

        "north_america": {
            "keywords": ["north america", "north american continent", "about north america", "north american geography"],
            "response": "North America is the third-largest continent (24.7 million sq km) with 23 countries and 600 million people. It includes Canada, USA, Mexico, Central America, and Caribbean islands. Features include the Rocky Mountains, Great Lakes, Mississippi River, and diverse climates from Arctic tundra to tropical rainforests. Home to indigenous cultures and colonial history."
        },

        "south_america": {
            "keywords": ["south america", "south american continent", "about south america", "south american geography"],
            "response": "South America is the fourth-largest continent (17.8 million sq km) with 12 countries and 430 million people. It contains the Amazon Rainforest (largest tropical rainforest), Andes Mountains (longest continental mountain range), and major rivers like the Amazon. Known for diverse cultures, ancient civilizations (Inca), and natural wonders like Iguazu Falls and Patagonia."
        },

        "antarctica": {
            "keywords": ["antarctica", "antarctic continent", "about antarctica", "south pole", "frozen continent"],
            "response": "Antarctica is Earth's southernmost continent, almost entirely south of the Antarctic Circle. It's the fifth-largest continent (14.2 million sq km), 98% covered by ice averaging 1.9 km thick, containing about 70% of Earth's freshwater. Antarctica has no permanent human population, is governed by the Antarctic Treaty System, and is crucial for climate research."
        },

        "australia": {
            "keywords": ["australia", "australian continent", "about australia", "down under", "australia country"],
            "response": "Australia is the world's smallest continent (7.7 million sq km) and sixth-largest country. As a country, it has 26 million people, capital Canberra, and major cities Sydney and Melbourne. Unique features include the Great Barrier Reef, Outback desert, diverse wildlife (kangaroos, koalas), and indigenous Aboriginal culture dating back 65,000 years."
        },

        "oceania": {
            "keywords": ["oceania", "pacific islands", "pacific region", "australasia", "melanesia", "micronesia", "polynesia"],
            "response": "Oceania is a geographical region including Australasia, Melanesia, Micronesia, and Polynesia, spanning the Pacific Ocean. It contains 14 countries including Australia, New Zealand, Papua New Guinea, Fiji, and thousands of islands. Oceania has diverse cultures, languages, and ecosystems from coral atolls to volcanic islands, with indigenous peoples maintaining traditional ways of life."
        },

        "russia": {
            "keywords": ["russia", "russian federation", "about russia", "russia geography", "largest country"],
            "response": "Russia is the world's largest country by area (17.1 million sq km, spanning 11 time zones) with 146 million people. Located in Eastern Europe and Northern Asia, its capital is Moscow. Russia features diverse landscapes from tundra to mountains, Lake Baikal (deepest freshwater lake), rich natural resources, and complex history from Tsarist to Soviet eras."
        },

        "brazil": {
            "keywords": ["brazil", "about brazil", "brazil geography", "federative republic of brazil"],
            "response": "Brazil is South America's largest country (8.5 million sq km) and most populous (214 million). Its capital is Brasília, with major cities São Paulo and Rio de Janeiro. Brazil contains 60% of the Amazon Rainforest, has the world's largest river system (Amazon), diverse ecosystems, and rich cultural blend of indigenous, Portuguese, African, and immigrant influences."
        },

        "canada": {
            "keywords": ["canada", "about canada", "canada geography", "second largest country"],
            "response": "Canada is the world's second-largest country by area (9.98 million sq km) with 38 million people. Located in North America, its capital is Ottawa, with major cities Toronto, Vancouver, and Montreal. Canada has the world's longest coastline, 20% of Earth's freshwater, diverse landscapes from Rocky Mountains to Arctic tundra, and is a bilingual (English/French) federation."
        },

        "japan": {
            "keywords": ["japan", "about japan", "japanese geography", "land of the rising sun", "japan country"],
            "response": "Japan is an East Asian island nation with 125 million people. Its capital Tokyo is the world's largest metropolitan area. Japan consists of four main islands (Honshu, Hokkaido, Kyushu, Shikoku) and thousands of smaller islands, featuring mountains, volcanoes (including Mount Fuji), earthquakes, and distinct seasons. Known for technology, anime, sushi, and ancient traditions."
        },

        "germany": {
            "keywords": ["germany", "about germany", "german geography", "federal republic of germany"],
            "response": "Germany is Central Europe's largest country (357,000 sq km) with 83 million people. Its capital is Berlin, with major cities Hamburg, Munich, and Frankfurt. Germany has diverse landscapes from the Alps to North Sea coast, Rhine and Danube rivers, and is Europe's largest economy. Known for engineering, automotive industry, beer culture, and rich history from Holy Roman Empire to reunification."
        },

        "france": {
            "keywords": ["france", "about france", "french geography", "french republic", "hexagon"],
            "response": "France is Western Europe's largest country (643,800 sq km) with 67 million people. Its capital Paris is a global cultural center. France features diverse geography from Alps and Pyrenees mountains to Mediterranean coast, Atlantic beaches, and countryside. Known for cuisine, wine, fashion, art, and history from monarchy to revolution, with global influence through language and culture."
        },

        "united_kingdom": {
            "keywords": ["united kingdom", "uk", "britain", "great britain", "uk geography", "england", "scotland", "wales", "northern ireland"],
            "response": "The United Kingdom is a sovereign country consisting of England, Scotland, Wales, and Northern Ireland, with 67 million people. Its capital London is a global financial center. The UK is an island nation with diverse landscapes from Scottish Highlands to English countryside, rich history from Roman times to British Empire, and significant cultural influence in language, law, and politics."
        },

        "italy": {
            "keywords": ["italy", "about italy", "italian geography", "italian republic", "italy country"],
            "response": "Italy is a Southern European country (301,000 sq km) with 60 million people, shaped like a boot. Its capital Rome contains Vatican City and ancient ruins. Italy features the Alps, Apennine Mountains, Mediterranean coastline, and major islands Sicily and Sardinia. Known as the cradle of Western civilization (Roman Empire, Renaissance), with world-famous art, cuisine, fashion, and automotive design."
        },

        "mexico": {
            "keywords": ["mexico", "about mexico", "mexican geography", "united mexican states"],
            "response": "Mexico is North America's third-largest country (1.96 million sq km) with 126 million people. Its capital Mexico City is built on ancient Aztec ruins. Mexico features diverse geography from deserts to tropical rainforests, Sierra Madre mountains, long coastlines, and rich biodiversity. Known for ancient civilizations (Maya, Aztec), vibrant culture, cuisine (UNESCO intangible heritage), and Spanish colonial architecture."
        },

        "indonesia": {
            "keywords": ["indonesia", "about indonesia", "indonesian geography", "republic of indonesia"],
            "response": "Indonesia is the world's largest archipelago nation with over 17,000 islands, spanning Southeast Asia and Oceania. With 275 million people, it's the fourth most populous country. Its capital Jakarta is on Java. Indonesia has the world's second-longest coastline, 400 volcanoes (130 active), diverse ecosystems and cultures, and is the world's largest Muslim-majority nation."
        },

        "south_africa": {
            "keywords": ["south africa", "about south africa", "south african geography", "republic of south africa"],
            "response": "South Africa is the southernmost African country (1.22 million sq km) with 60 million people. It has three capitals: Pretoria (executive), Cape Town (legislative), Bloemfontein (judicial). Known as the 'Rainbow Nation' for ethnic diversity, it features diverse landscapes from Table Mountain to Kruger National Park, rich mineral resources, and history of apartheid and reconciliation."
        },

        "egypt": {
            "keywords": ["egypt", "about egypt", "egyptian geography", "arab republic of egypt"],
            "response": "Egypt is a transcontinental country linking Africa and Asia via Sinai Peninsula, with 104 million people. Its capital Cairo sits near the Pyramids of Giza and Sphinx. Egypt is 96% desert, but the Nile River valley supports civilization for 5,000 years. Known for ancient pharaohs, hieroglyphics, Arab culture, and strategic Suez Canal connecting Mediterranean and Red Sea."
        },

        "argentina": {
            "keywords": ["argentina", "about argentina", "argentine geography", "argentine republic"],
            "response": "Argentina is South America's second-largest country (2.78 million sq km) with 45 million people. Its capital Buenos Aires is known as the 'Paris of South America.' Argentina features diverse landscapes from Andes mountains to Pampas grasslands, Patagonian steppe, and Iguazu Falls. Known for tango, beef, wine, football (Maradona, Messi), and European immigrant influences."
        },

        "turkey": {
            "keywords": ["turkey", "about turkey", "turkish geography", "republic of turkey", "transcontinental turkey"],
            "response": "Turkey is a transcontinental country straddling Europe and Asia across the Bosphorus Strait, with 85 million people. Its capital Ankara, but Istanbul is the cultural and economic center. Turkey features diverse geography from Mediterranean beaches to Anatolian plateau, Cappadocia rock formations, and Mount Ararat. Known for Ottoman Empire heritage, cuisine, and strategic location between continents."
        },

        "pakistan": {
            "keywords": ["pakistan", "about pakistan", "pakistani geography", "islamic republic of pakistan"],
            "response": "Pakistan is a South Asian country (881,000 sq km) with 225 million people (fifth most populous). Its capital Islamabad, with major cities Karachi and Lahore. Pakistan features diverse geography from Himalayas and Karakoram (including K2) to Indus River valley and deserts. Known for ancient Indus Valley Civilization, Mughal architecture, diverse cultures, and being an Islamic republic."
        },

        "bangladesh": {
            "keywords": ["bangladesh", "about bangladesh", "bangladeshi geography", "people's republic of bangladesh"],
            "response": "Bangladesh is a South Asian country (148,000 sq km) with 165 million people (eighth most populous), making it one of the world's most densely populated. Its capital Dhaka. Bangladesh is dominated by the Ganges-Brahmaputra delta with fertile plains, frequent monsoons, and vulnerability to climate change. Known for textiles industry, mangrove Sundarbans (Bengal tiger habitat), and Bengali culture."
        },

        "nigeria": {
            "keywords": ["nigeria", "about nigeria", "nigerian geography", "federal republic of nigeria"],
            "response": "Nigeria is West Africa's largest country (923,000 sq km) with 213 million people (Africa's most populous). Its capital Abuja, with Lagos as largest city and economic hub. Nigeria features diverse geography from Niger River delta to savanna and rainforest. Known for Nollywood film industry, Afrobeat music, diverse ethnic groups (Hausa, Yoruba, Igbo), and oil resources."
        },

        "ethiopia": {
            "keywords": ["ethiopia", "about ethiopia", "ethiopian geography", "federal democratic republic of ethiopia"],
            "response": "Ethiopia is a landlocked East African country (1.1 million sq km) with 120 million people (second most populous in Africa). Its capital Addis Ababa hosts African Union. Ethiopia features highlands, Great Rift Valley, Blue Nile source, and is the only African country never colonized. Known for ancient civilization (Aksum), Orthodox Christianity, coffee origin, and diverse cultures/languages."
        },

        "philippines": {
            "keywords": ["philippines", "about philippines", "filipino geography", "republic of the philippines"],
            "response": "The Philippines is a Southeast Asian archipelago of 7,641 islands with 113 million people. Its capital Manila. The Philippines features volcanic mountains, tropical rainforests, extensive coastlines, and biodiversity hotspots. Known for Spanish and American colonial influences, Catholicism in Asia, overseas workers, English proficiency, and natural beauty from rice terraces to beaches."
        },

        "vietnam": {
            "keywords": ["vietnam", "about vietnam", "vietnamese geography", "socialist republic of vietnam"],
            "response": "Vietnam is a Southeast Asian country (331,000 sq km) with 98 million people. Its capital Hanoi, with Ho Chi Minh City as economic center. Vietnam features long S-shaped coastline, Red River and Mekong deltas, mountains, and dense forests. Known for resistance wars against major powers, French colonial architecture, pho cuisine, rapid economic growth, and UNESCO sites like Ha Long Bay."
        },

        "south_korea": {
            "keywords": ["south korea", "korea", "about south korea", "republic of korea", "korean peninsula south"],
            "response": "South Korea is an East Asian country (100,000 sq km) on Korean Peninsula's southern half, with 52 million people. Its capital Seoul is a megacity with advanced technology. South Korea features mountainous terrain, four distinct seasons, and is surrounded by sea on three sides. Known for K-pop, Samsung, Hyundai, cuisine (kimchi), rapid development from war-torn to high-tech economy."
        },

        "north_korea": {
            "keywords": ["north korea", "about north korea", "democratic people's republic of korea", "dprk"],
            "response": "North Korea is an East Asian country (120,500 sq km) on Korean Peninsula's northern half, with 26 million people. Its capital Pyongyang. North Korea features mountains, plains, and borders China, Russia, and South Korea (DMZ). Governed as a totalitarian dictatorship under Kim dynasty since 1948, with Juche ideology, nuclear weapons program, and one of the world's most closed economies and societies."
        },

        "iran": {
            "keywords": ["iran", "about iran", "iranian geography", "islamic republic of iran", "persia"],
            "response": "Iran is a Western Asian country (1.65 million sq km) with 85 million people. Its capital Tehran. Iran features diverse geography from Alborz and Zagros mountains to deserts and Caspian Sea coast. Known for ancient Persian Empire heritage, Islamic Revolution (1979), Shia Islam leadership, rich culture (poetry, carpets, cuisine), and oil/gas resources. Historic name Persia until 1935."
        },

        "iraq": {
            "keywords": ["iraq", "about iraq", "iraqi geography", "republic of iraq", "mesopotamia"],
            "response": "Iraq is a Western Asian country (438,000 sq km) with 41 million people. Its capital Baghdad on Tigris River. Iraq encompasses ancient Mesopotamia between Tigris and Euphrates rivers, cradle of civilization (Sumer, Babylon, Assyria). Features deserts, mountains, and fertile river valleys. Known for oil reserves, recent conflicts, and diverse ethnic/religious groups (Arabs, Kurds, Sunni/Shia Muslims)."
        },

        "saudi_arabia": {
            "keywords": ["saudi arabia", "about saudi arabia", "saudi geography", "kingdom of saudi arabia"],
            "response": "Saudi Arabia is the largest Middle Eastern country (2.15 million sq km) with 35 million people. Its capital Riyadh. Saudi Arabia is mostly desert (Rub' al Khali/Empty Quarter), with oil reserves (world's largest exporter), and contains Islam's two holiest cities: Mecca (birthplace of Prophet Muhammad) and Medina. An absolute monarchy following conservative Wahhabi Islam, undergoing modernization under Vision 2030."
        },

        "israel": {
            "keywords": ["israel", "about israel", "israeli geography", "state of israel", "holy land"],
            "response": "Israel is a Middle Eastern country (22,000 sq km) with 9 million people. Its capital Jerusalem (disputed), with financial center Tel Aviv. Israel features Mediterranean coast, Negev desert, Dead Sea (lowest point on Earth), and biblical sites. Established 1948 as Jewish homeland, with diverse population (Jewish majority, Arab minority). Known for high-tech innovation, historical/religious significance to Judaism, Christianity, Islam."
        },

        "switzerland": {
            "keywords": ["switzerland", "about switzerland", "swiss geography", "swiss confederation"],
            "response": "Switzerland is a Central European country (41,000 sq km) with 8.7 million people. Its capital Bern. Switzerland is landlocked in Alps, featuring mountains, lakes, and four official languages (German, French, Italian, Romansh). Known for political neutrality, banking, watches, chocolate, cheese, precision engineering, and direct democracy. Hosts international organizations in Geneva."
        },

        "sweden": {
            "keywords": ["sweden", "about sweden", "swedish geography", "kingdom of sweden"],
            "response": "Sweden is a Nordic country (450,000 sq km) with 10 million people. Its capital Stockholm spread across islands. Sweden features forests, lakes, archipelagos, and extends into Arctic Circle (Lapland). Known for welfare state model, design (IKEA, H&M), innovation (Spotify, Skype), Vikings history, and environmental leadership. Constitutional monarchy with high quality of life and gender equality."
        },

        "norway": {
            "keywords": ["norway", "about norway", "norwegian geography", "kingdom of norway"],
            "response": "Norway is a Nordic country (385,000 sq km) with 5.4 million people. Its capital Oslo. Norway features dramatic fjords, mountains, coastline with islands, and Arctic territory including Svalbard. Known for Viking heritage, oil/gas wealth (sovereign wealth fund), high living standards, social democracy, and natural beauty (Northern Lights, midnight sun). World leader in electric vehicle adoption and renewable energy."
        },

        "finland": {
            "keywords": ["finland", "about finland", "finnish geography", "republic of finland"],
            "response": "Finland is a Nordic country (338,000 sq km) with 5.5 million people. Its capital Helsinki. Finland is 'Land of a Thousand Lakes' (actually 188,000 lakes), with forests, archipelagos, and extends into Arctic. Known for education system (top PISA scores), sauna culture, design (Marimekko, Alvar Aalto), technology (Nokia), and happiness (often top in World Happiness Report)."
        },

        "denmark": {
            "keywords": ["denmark", "about denmark", "danish geography", "kingdom of denmark"],
            "response": "Denmark is a Nordic country (43,000 sq km) with 5.8 million people. Its capital Copenhagen. Denmark consists of Jutland peninsula and 443 islands, featuring flat terrain, coastlines, and bridges/tunnels. Known for Viking history, welfare state, design (Bang & Olufsen, Lego), renewable energy leadership, and hygge lifestyle concept. Constitutional monarchy with oldest continuous flag (Dannebrog)."
        },

        "netherlands": {
            "keywords": ["netherlands", "about netherlands", "dutch geography", "holland", "kingdom of the netherlands"],
            "response": "The Netherlands is a Western European country (41,500 sq km) with 17 million people. Its capital Amsterdam, with government in The Hague. About 26% of land is below sea level, protected by dikes and famous for windmills, tulip fields, canals. Known for tolerance, cycling culture, art (Rembrandt, Van Gogh), engineering (water management), and trade history. Often called Holland, though that's only two provinces."
        },

        "belgium": {
            "keywords": ["belgium", "about belgium", "belgian geography", "kingdom of belgium"],
            "response": "Belgium is a Western European country (30,500 sq km) with 11.5 million people. Its capital Brussels hosts EU and NATO headquarters. Belgium has three official languages (Dutch, French, German) and regions (Flanders, Wallonia, Brussels). Known for medieval cities (Bruges, Ghent), chocolate, beer, waffles, fries, and comics (Tintin, Smurfs). Center of European politics and diamond trade (Antwerp)."
        },

        "austria": {
            "keywords": ["austria", "about austria", "austrian geography", "republic of austria"],
            "response": "Austria is a Central European landlocked country (83,900 sq km) with 9 million people. Its capital Vienna on Danube River. Austria is dominated by Alps (62% of area), with mountain lakes, forests, and valleys. Known for musical heritage (Mozart, Strauss), Habsburg Empire history, skiing, coffeehouse culture, and high standard of living. Neutral country with strong social market economy."
        },

        "greece": {
            "keywords": ["greece", "about greece", "greek geography", "hellenic republic"],
            "response": "Greece is a Southeast European country (132,000 sq km) with 10.7 million people. Its capital Athens with Acropolis. Greece features thousands of islands in Aegean and Ionian seas, mountains, and Mediterranean coastline. Known as cradle of Western civilization (ancient philosophy, democracy, Olympics), rich mythology, Orthodox Christianity, cuisine (olive oil, feta), and tourism to archaeological sites and islands."
        },

        "portugal": {
            "keywords": ["portugal", "about portugal", "portuguese geography", "portuguese republic"],
            "response": "Portugal is a Southwest European country (92,200 sq km) with 10.3 million people. Its capital Lisbon on Tagus River. Portugal features Atlantic coastline, mountains, and archipelagos (Azores, Madeira). Known for Age of Discoveries explorers (Vasco da Gama), global empire, port wine, fado music, azulejo tiles, and sunny climate. EU member with growing tech scene and tourism."
        },

        "spain": {
            "keywords": ["spain", "about spain", "spanish geography", "kingdom of spain"],
            "response": "Spain is a Southwest European country (505,000 sq km) with 47 million people. Its capital Madrid. Spain features diverse geography from Pyrenees mountains to Mediterranean beaches, islands (Balearic, Canary), and Meseta central plateau. Known for vibrant culture (flamenco, bullfighting), cuisine (tapas, paella), art (Picasso, Dalí), architecture (Gaudí), and siesta tradition. Constitutional monarchy with autonomous regions."
        },

        "poland": {
            "keywords": ["poland", "about poland", "polish geography", "republic of poland"],
            "response": "Poland is a Central European country (312,700 sq km) with 38 million people. Its capital Warsaw on Vistula River. Poland features plains, Baltic Sea coast, Carpathian and Sudeten mountains. Known for resilience through partitions, WWII destruction, and communist era; now EU success story with strong economy. Rich history (Polish-Lithuanian Commonwealth), Catholicism, Chopin, Copernicus, and pierogi cuisine."
        },

        "ukraine": {
            "keywords": ["ukraine", "about ukraine", "ukrainian geography", "largest european country"],
            "response": "Ukraine is Eastern Europe's largest country (603,500 sq km) with 41 million people (pre-war). Its capital Kyiv on Dnieper River. Ukraine features fertile black soil steppes (breadbasket of Europe), Carpathian Mountains, Black Sea coast, and dense river networks. Known for Cossack heritage, Orthodox Christianity with distinctive domed churches, embroidered shirts (vyshyvanka), and ongoing conflict with Russia since 2014."
        },

        "thailand": {
            "keywords": ["thailand", "about thailand", "thai geography", "kingdom of thailand"],
            "response": "Thailand is a Southeast Asian country (513,000 sq km) with 70 million people. Its capital Bangkok with grand palace. Thailand features mountains north, central plains, southern peninsula with beaches/islands. Known as 'Land of Smiles,' never colonized, Buddhist monarchy, cuisine (pad thai, tom yum), martial arts (muay thai), tourism (Phuket, Chiang Mai), and distinctive culture blending tradition and modernity."
        },

        "malaysia": {
            "keywords": ["malaysia", "about malaysia", "malaysian geography", "federation of malaysia"],
            "response": "Malaysia is a Southeast Asian country (330,000 sq km) with 33 million people. Its capital Kuala Lumpur with Petronas Towers. Malaysia consists of Peninsular Malaysia and East Malaysia on Borneo, featuring rainforests, mountains, and coastlines. Known for multicultural society (Malay, Chinese, Indian), Islamic monarchy, biodiversity, cuisine blending flavors, and economic development as Asian Tiger."
        },

        "singapore": {
            "keywords": ["singapore", "about singapore", "singapore geography", "republic of singapore"],
            "response": "Singapore is a Southeast Asian city-state (728 sq km) with 5.7 million people. Its capital is the city itself. Singapore consists of main island and 62 islets, with urban landscape, limited natural resources. Known as global financial hub, efficient governance, multicultural society (Chinese majority), cleanliness, strict laws, Gardens by the Bay, and high cost of living. Transformed from developing to developed in one generation."
        },

        "new_zealand": {
            "keywords": ["new zealand", "about new zealand", "new zealand geography", "aotearoa"],
            "response": "New Zealand is a Southwest Pacific island country (268,000 sq km) with 5 million people. Its capital Wellington, with Auckland largest city. New Zealand consists of North and South Islands, featuring mountains (Southern Alps), fjords, volcanoes, beaches, and unique biodiversity (flightless birds like kiwi). Known for Maori culture (Aotearoa), rugby (All Blacks), Lord of the Rings filming, and environmental beauty."
        },

        "peru": {
            "keywords": ["peru", "about peru", "peruvian geography", "republic of peru"],
            "response": "Peru is a South American country (1.29 million sq km) with 33 million people. Its capital Lima. Peru features three regions: coastal desert, Andes mountains, Amazon rainforest. Known for ancient Inca Empire (Machu Picchu), Spanish colonial architecture, diverse cuisine (ceviche, potatoes origin), and rich cultural heritage blending indigenous, Spanish, African, and Asian influences."
        },

        "colombia": {
            "keywords": ["colombia", "about colombia", "colombian geography", "republic of colombia"],
            "response": "Colombia is a South American country (1.14 million sq km) with 51 million people. Its capital Bogotá in Andes. Colombia features Caribbean and Pacific coastlines, Andes mountains, Amazon rainforest, and plains (llanos). Known for coffee, emeralds, biodiversity (second most biodiverse), music (cumbia, salsa, Shakira), literature (Gabriel García Márquez), and recovering from decades of conflict with drug cartels."
        },

        "venezuela": {
            "keywords": ["venezuela", "about venezuela", "venezuelan geography", "bolivarian republic of venezuela"],
            "response": "Venezuela is a South American country (916,000 sq km) with 28 million people. Its capital Caracas. Venezuela features Andes mountains, Amazon basin, Orinoco River, Caribbean coast with Angel Falls (world's highest). Once wealthy from world's largest oil reserves, now experiencing severe economic crisis, hyperinflation, and political instability under authoritarian governance and US sanctions."
        },

        "chile": {
            "keywords": ["chile", "about chile", "chilean geography", "republic of chile"],
            "response": "Chile is a South American country (756,000 sq km) with 19 million people. Its capital Santiago. Chile is a long, narrow strip between Andes and Pacific, stretching 4,300 km north-south but only 350 km wide at widest. Features diverse climates from Atacama Desert (driest) to Patagonian glaciers. Known for copper mining, wine, earthquakes, and economic stability in Latin America."
        },

        "cuba": {
            "keywords": ["cuba", "about cuba", "cuban geography", "republic of cuba"],
            "response": "Cuba is a Caribbean island nation (110,000 sq km) with 11 million people. Its capital Havana with colonial architecture and vintage cars. Cuba features tropical climate, mountains (Sierra Maestra), beaches, and coral reefs. Known for communist revolution (1959) led by Fidel Castro, US embargo, sugar cane, rum, cigars, music (salsa, son), and healthcare system. Undergoing slow economic reforms."
        },

        "kenya": {
            "keywords": ["kenya", "about kenya", "kenyan geography", "republic of kenya"],
            "response": "Kenya is an East African country (580,000 sq km) with 55 million people. Its capital Nairobi, regional hub. Kenya features Great Rift Valley, Mount Kenya, savannas with wildlife (Big Five), Indian Ocean coast, and Lake Victoria. Known for safari tourism, Maasai culture, long-distance runners, tea/coffee exports, and tech innovation (mobile money M-Pesa). Stable democracy in turbulent region."
        },

        "morocco": {
            "keywords": ["morocco", "about morocco", "moroccan geography", "kingdom of morocco"],
            "response": "Morocco is a North African country (710,000 sq km) with 37 million people. Its capital Rabat, with cultural center Marrakech. Morocco features Atlantic and Mediterranean coastlines, Atlas Mountains, Sahara Desert, and fertile plains. Known for Berber/Amazigh culture, Islamic architecture (mosques, medinas), cuisine (tagine, couscous), and strategic location near Europe. Monarchy with political reforms and tourism."
        },

        "algeria": {
            "keywords": ["algeria", "about algeria", "algerian geography", "people's democratic republic of algeria"],
            "response": "Algeria is Africa's largest country (2.38 million sq km) with 44 million people. Its capital Algiers on Mediterranean. Algeria features Sahara Desert covering 80%, Atlas Mountains, and coastline. Known for war of independence from France (1962), oil/gas resources (main export), Berber culture, Roman ruins (Timgad), and French-Arabic bilingualism. Military-dominated government with recent protests for reform."
        },

        "geographical_terms": {
            "keywords": ["geographical terms", "geography vocabulary", "landforms", "bodies of water", "geographic features"],
            "response": "Key geographical terms include: Landforms (mountains, hills, plateaus, valleys, plains), bodies of water (oceans, seas, rivers, lakes, bays), climate zones (tropical, temperate, polar), and human geography terms (urban, rural, population density, migration). Understanding these terms helps describe Earth's physical and human characteristics."
        },

        "map_skills": {
            "keywords": ["map skills", "reading maps", "types of maps", "latitude longitude", "cartography"],
            "response": "Map skills include reading scale, legend, compass rose, and understanding projections. Types: political (countries), physical (landforms), topographic (elevation), thematic (climate, population). Latitude/longitude coordinates locate places. Cartography is map-making, now using GIS (Geographic Information Systems). Maps simplify complex spatial information for navigation, planning, and education."
        },

        "climate_zones": {
            "keywords": ["climate zones", "world climates", "koppen climate", "tropical climate", "temperate climate"],
            "response": "Earth has five main climate zones: tropical (near equator, warm year-round), dry (low precipitation), temperate (moderate, four seasons), continental (large temperature variation), and polar (cold). The Köppen-Geiger system classifies climates based on temperature, precipitation, and vegetation. Climate zones influence ecosystems, agriculture, and human settlement patterns."
        },

        "biomes": {
            "keywords": ["biomes", "world biomes", "ecosystems", "tundra", "rainforest", "grassland", "desert"],
            "response": "Biomes are large ecological areas with similar climate, plants, animals. Major terrestrial biomes: tundra, taiga/boreal forest, temperate forest, grassland, desert, tropical rainforest, savanna. Aquatic biomes: freshwater (lakes, rivers) and marine (oceans, coral reefs). Biomes are shaped by temperature, precipitation, and latitude, supporting distinct biodiversity."
        },

        "natural_disasters": {
            "keywords": ["natural disasters", "earthquakes", "hurricanes", "floods", "volcanic eruptions", "tsunamis"],
            "response": "Natural disasters are catastrophic events from Earth's processes: earthquakes (tectonic plates), hurricanes/cyclones (tropical storms), floods (heavy rain/river overflow), volcanic eruptions (magma release), tsunamis (seismic sea waves), wildfires, droughts. Disaster management involves prediction, preparedness, response, and recovery to reduce human and economic losses."
        },

        "human_environment_interaction": {
            "keywords": ["human environment interaction", "environmental impact", "resource use", "sustainable development"],
            "response": "Human-environment interaction studies how humans adapt to, modify, and depend on their environment. Examples: agriculture (modifying land), pollution (negative impact), conservation (protection). Sustainable development balances human needs with environmental protection. Concepts include carrying capacity, ecological footprint, and climate change adaptation/mitigation."
        },

        "population_distribution": {
            "keywords": ["population distribution", "world population patterns", "demographics", "population density"],
            "response": "World population distribution is uneven: 90% live on 10% of land, concentrated near coasts, rivers, and fertile plains. High density in South/East Asia, Europe; low in deserts, polar regions, mountains. Factors: climate, resources, economy, history. Demographics study age structure, birth/death rates, migration, urbanization trends, and future projections."
        },

        "urbanization": {
            "keywords": ["urbanization", "city growth", "megacities", "urban problems", "urban planning"],
            "response": "Urbanization is the increasing percentage of people living in cities. Over 55% of world population is urban, projected to reach 68% by 2050. Megacities (over 10 million) face challenges: housing, transportation, pollution, inequality. Urban planning aims to create sustainable, livable cities through smart growth, public transit, green spaces, and efficient infrastructure."
        },

        "globalization": {
            "keywords": ["globalization", "global connections", "international trade", "cultural exchange", "economic globalization"],
            "response": "Globalization is the process of increasing interconnectedness among countries through trade, technology, culture, and politics. Features: multinational corporations, global supply chains, international organizations (UN, WTO), cultural diffusion, and migration. Benefits include economic growth and cultural exchange; criticisms include inequality, cultural homogenization, and environmental degradation."
        },

        "development": {
            "keywords": ["development", "economic development", "developed vs developing", "human development index", "sustainable development goals"],
            "response": "Development refers to improving living standards, economic strength, and quality of life. Measured by GDP per capita, HDI (Human Development Index combining income, education, life expectancy), and SDGs (UN Sustainable Development Goals). Developed countries have high industrialization and income; developing countries are industrializing with lower incomes. Development strategies vary by context."
        },

        "geopolitics": {
            "keywords": ["geopolitics", "political geography", "international relations", "borders", "territorial disputes"],
            "response": "Geopolitics studies how geography influences politics, international relations, and power. Topics: border disputes, resource conflicts, strategic locations (straits, canals), alliance formations, and territorial waters. Geopolitical theories analyze heartland/rimland concepts, containment, and globalization's impact on state sovereignty. Current issues include Arctic claims, South China Sea, and cyber geography."
        },

        "tourism_geography": {
            "keywords": ["tourism geography", "travel geography", "tourist destinations", "ecotourism", "cultural tourism"],
            "response": "Tourism geography studies travel patterns, destination development, and impacts. Popular destinations: natural (beaches, mountains), cultural (historical sites, cities), adventure (safaris, trekking). Ecotourism promotes conservation and community benefits. Tourism brings economic gains but can cause environmental damage, overcrowding, and cultural commodification. Sustainable tourism aims to balance these."
        },

        "agricultural_patterns": {
            "keywords": ["agricultural patterns", "farming systems", "food production", "agricultural revolution", "green revolution"],
            "response": "Agricultural patterns vary by climate, technology, and culture. Types: subsistence (small-scale for family), commercial (large-scale for market), intensive (high inputs), extensive (large land area). Agricultural revolutions: Neolithic (domestication), Green (1960s high-yield crops). Modern issues: GMOs, organic farming, climate impact, food security, and sustainable practices like crop rotation and precision agriculture."
        },

        "industrial_location": {
            "keywords": ["industrial location", "manufacturing geography", "factors of production", "industrial regions"],
            "response": "Industrial location considers factors: raw materials, energy, labor, markets, transportation, and government policies. Traditional industrial regions (Rust Belt, Ruhr) developed near coal/iron. Modern footloose industries (high-tech) locate near research universities, airports. Globalization shifted manufacturing to developing countries with lower costs. Industrial clusters (Silicon Valley) benefit from agglomeration economies."
        },

        "transportation_networks": {
            "keywords": ["transportation networks", "transport geography", "roads", "railways", "shipping routes", "air routes"],
            "response": "Transportation networks connect places for movement of people and goods. Networks include: roads (interstate highways), railways (transcontinental), shipping lanes (Suez, Panama Canals), air routes (hub-and-spoke). Accessibility and connectivity influence economic development. Transportation geography studies flow patterns, infrastructure planning, and sustainability challenges (congestion, emissions, alternative fuels)."
        },

        "cultural_landscapes": {
            "keywords": ["cultural landscapes", "built environment", "cultural geography", "vernacular architecture"],
            "response": "Cultural landscapes are areas shaped by human interaction with the environment, reflecting culture, beliefs, and practices. Examples: agricultural terraces, religious sites, urban designs, traditional villages. Vernacular architecture uses local materials and styles. Cultural landscapes preserve heritage and identity, studied in cultural geography to understand human-environment relationships and sense of place."
        },

        "political_boundaries": {
            "keywords": ["political boundaries", "borders", "types of boundaries", "border disputes", "sovereignty"],
            "response": "Political boundaries define state sovereignty and jurisdiction. Types: natural (rivers, mountains), geometric (straight lines), cultural (ethnic/religious lines). Boundaries can be antecedent (before settlement), subsequent (evolving), or superimposed (external imposition). Border disputes arise from resource claims, ethnic ties, or historical conflicts. International law and treaties govern boundaries and territorial waters."
        },

        # Expanded World Facts
        "world_population": {
            "keywords": ["world population", "global population", "how many people", "earth population"],
            "response": "The world population reached 8 billion people in 2022 and continues to grow. China and India are the most populous countries, each with over 1.4 billion people. Population growth rates vary globally, with Africa having the highest growth and some developed countries experiencing population decline."
        },

        "earth_facts": {
            "keywords": ["earth", "planet earth", "about earth", "earth facts", "our planet"],
            "response": "Earth is the third planet from the Sun, with a diameter of 12,742 km and age of about 4.5 billion years. It has one natural satellite (the Moon) and is the only known planet to support life. Earth's atmosphere is 78% nitrogen, 21% oxygen, and 1% other gases. About 71% of its surface is covered by water."
        },

        "solar_system": {
            "keywords": ["solar system", "planets", "sun and planets", "our solar system", "planetary system"],
            "response": "The solar system consists of the Sun and eight planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. It also includes dwarf planets (Pluto, Ceres, Eris), asteroids, comets, and the Kuiper Belt. The solar system formed about 4.6 billion years ago from a giant molecular cloud."
        },

        "oceans": {
            "keywords": ["oceans", "world oceans", "five oceans", "sea", "marine"],
            "response": "There are five oceans: Pacific (largest and deepest, covering 63 million square miles), Atlantic, Indian, Southern/Antarctic, and Arctic (smallest). Oceans contain 97% of Earth's water and are crucial for climate regulation, oxygen production, and supporting marine ecosystems."
        },

        "mountains": {
            "keywords": ["mountains", "highest mountain", "mountain ranges", "mountain peaks", "mountain chains"],
            "response": "Mount Everest in the Himalayas is the highest mountain above sea level at 8,848.86 meters. Other major ranges include the Andes (longest continental range), Rockies, Alps, and Himalayas. Mountains cover about 24% of Earth's land surface and influence weather patterns."
        },

        "rivers": {
            "keywords": ["rivers", "longest river", "major rivers", "river systems", "river basins"],
            "response": "The Nile River is traditionally considered the longest river at 6,650 km, though some measurements give the Amazon River as longer. Other major rivers include the Yangtze, Mississippi-Missouri, and Yenisey. Rivers transport water, nutrients, and sediment, shaping landscapes and supporting civilizations."
        },

        "deserts": {
            "keywords": ["deserts", "largest desert", "sahara", "desert regions", "arid lands"],
            "response": "The Sahara is the largest hot desert, covering 9.2 million square km. The Antarctic Desert is the largest overall. Deserts cover about one-third of Earth's land surface and include hot deserts (Sahara, Arabian), cold deserts (Gobi, Patagonian), and polar deserts."
        },

        "forests": {
            "keywords": ["forests", "rainforest", "amazon forest", "boreal forest", "forest types"],
            "response": "Forests cover about 31% of Earth's land area. Major types include tropical rainforests (Amazon, Congo), temperate forests, and boreal forests (taiga). The Amazon is the largest rainforest, often called 'the lungs of the Earth' for producing 20% of the world's oxygen."
        },

        "continents": {
            "keywords": ["continents", "how many continents", "list continents", "continental landmasses"],
            "response": "There are seven continents: Asia (largest by area and population), Africa, North America, South America, Antarctica, Europe, and Australia/Oceania (smallest). Some models consider Europe and Asia as one continent called Eurasia. Continents were once joined in the supercontinent Pangaea."
        },

        "countries": {
            "keywords": ["countries", "how many countries", "sovereign states", "list of countries"],
            "response": "There are 195 sovereign countries recognized by the United Nations: 193 UN member states and 2 observer states (Holy See and Palestine). Russia is the largest by area, Vatican City the smallest. The concept of countries emerged with the Treaty of Westphalia in 1648."
        },

        "cities": {
            "keywords": ["cities", "largest cities", "metropolitan areas", "urban centers", "global cities"],
            "response": "Tokyo is the world's largest metropolitan area with about 37 million people. Other megacities include Delhi, Shanghai, São Paulo, and Mexico City. Urbanization continues to grow, with over 55% of the world's population living in cities as of 2020."
        },

        "languages": {
            "keywords": ["languages", "world languages", "most spoken languages", "language families", "linguistic diversity"],
            "response": "There are about 7,000 living languages worldwide. The most spoken first languages are Mandarin Chinese, Spanish, English, Hindi, and Arabic. English serves as the global lingua franca. Language diversity is highest in Papua New Guinea with over 800 languages."
        },

        "cultures": {
            "keywords": ["cultures", "world cultures", "cultural diversity", "human cultures", "traditional cultures"],
            "response": "Human cultural diversity includes thousands of distinct cultures with unique traditions, art, music, cuisine, and social norms. Major cultural regions include Western, East Asian, South Asian, Middle Eastern, African, Latin American, and Indigenous cultures."
        },

        "religions": {
            "keywords": ["religions", "world religions", "major religions", "religious beliefs", "faith systems"],
            "response": "Major world religions include Christianity (largest with 2.4 billion followers), Islam (1.9 billion), Hinduism (1.2 billion), Buddhism (500 million), and Judaism (15 million). Many people also follow indigenous, folk, or secular/non-religious traditions."
        },

        "economy": {
            "keywords": ["world economy", "global economy", "gdp", "economic systems", "international trade"],
            "response": "The global economy is about $100 trillion in GDP. Major economies include the US, China, Japan, Germany, and India. Economic systems range from capitalism to socialism, with most countries using mixed economies. International trade connects economies through organizations like WTO."
        },

        "climate": {
            "keywords": ["world climate", "global climate", "climate zones", "weather patterns", "climatic regions"],
            "response": "Earth has five main climate zones: tropical, dry, temperate, continental, and polar. The Köppen climate classification further divides these. Climate is influenced by latitude, altitude, ocean currents, and geography. Climate change is altering global weather patterns."
        },

        "biodiversity": {
            "keywords": ["biodiversity", "species diversity", "endangered species", "extinction", "wildlife"],
            "response": "Earth hosts an estimated 8.7 million species, though only 1.7 million have been formally described. Biodiversity hotspots include tropical rainforests and coral reefs. Human activities are causing species extinction at 100-1,000 times the natural rate, threatening ecosystem stability."
        },

        "time_zones": {
            "keywords": ["time zones", "world time", "international date line", "time differences", "utc"],
            "response": "Earth is divided into 24 primary time zones based on 15° longitudinal segments. UTC (Coordinated Universal Time) is the primary time standard. The International Date Line marks where each calendar day begins. Some countries use half-hour or quarter-hour offsets."
        },

        "natural_wonders": {
            "keywords": ["natural wonders", "world wonders", "seven wonders of nature", "natural landmarks"],
            "response": "Natural wonders include the Grand Canyon, Great Barrier Reef, Mount Everest, Victoria Falls, Parícutin volcano, Harbor of Rio de Janeiro, and Aurora Borealis. The Seven Natural Wonders of the World were determined by global poll in 2011."
        },

        "man_made_wonders": {
            "keywords": ["man made wonders", "seven wonders", "architectural wonders", "human achievements"],
            "response": "The Seven Wonders of the Ancient World included the Great Pyramid of Giza (only one still standing). The New7Wonders of the World, chosen in 2007, are the Great Wall of China, Petra, Christ the Redeemer, Machu Picchu, Chichen Itza, Colosseum, and Taj Mahal."
        },

        "inventions": {
            "keywords": ["world inventions", "important inventions", "technological breakthroughs", "human inventions"],
            "response": "Key inventions that shaped civilization include the wheel, printing press, electricity, telephone, internet, antibiotics, and computer. Different cultures contributed inventions like paper (China), algebra (Middle East), and democracy (Greece)."
        },

        "explorers": {
            "keywords": ["explorers", "world exploration", "age of discovery", "famous explorers", "exploration history"],
            "response": "Famous explorers include Marco Polo, Christopher Columbus, Vasco da Gama, Ferdinand Magellan, James Cook, and Roald Amundsen. Their journeys connected continents, established trade routes, and expanded geographical knowledge, though often with negative impacts on indigenous peoples."
        },

        "empires": {
            "keywords": ["empires", "world empires", "ancient empires", "historical empires", "imperial history"],
            "response": "Major historical empires include the Roman, Mongol, British, Ottoman, and Qing empires. At its height, the British Empire was the largest, covering about a quarter of Earth's land area. Empires spread technologies, religions, and languages while often exploiting conquered peoples."
        },

        "wars": {
            "keywords": ["world wars", "major wars", "war history", "conflicts", "peace"],
            "response": "World War I (1914-1918) and World War II (1939-1945) were the deadliest global conflicts, resulting in approximately 85-100 million deaths total. Other major wars include the Napoleonic Wars, American Civil War, and regional conflicts. The UN was established after WWII to prevent future global wars."
        },

        "peace": {
            "keywords": ["world peace", "peace organizations", "peacekeeping", "united nations", "diplomacy"],
            "response": "The United Nations, founded in 1945, works to maintain international peace and security. Other peace organizations include UNESCO, International Red Cross, and Nobel Peace Prize. Diplomacy, international law, and conflict resolution aim to prevent wars and promote cooperation."
        },

        "environmental_issues": {
            "keywords": ["environmental issues", "global warming", "climate change", "pollution", "deforestation", "environmental problems"],
            "response": "Major global environmental issues include climate change, pollution (air, water, plastic), deforestation, loss of biodiversity, ocean acidification, and resource depletion. International agreements like the Paris Agreement aim to address these challenges through collective action."
        },

        "resources": {
            "keywords": ["world resources", "natural resources", "energy resources", "mineral resources", "resource distribution"],
            "response": "Earth's natural resources include fossil fuels (oil, coal, natural gas), minerals (iron, copper, rare earths), water, forests, and agricultural land. Resource distribution is uneven globally, leading to trade dependencies and geopolitical tensions. Sustainable resource management is crucial."
        },

        "transportation": {
            "keywords": ["world transportation", "global transport", "shipping routes", "air travel", "transport networks"],
            "response": "Global transportation networks include shipping lanes (Suez Canal, Panama Canal), air routes, railways (Trans-Siberian, Trans-European), and road systems. Container shipping revolutionized global trade. Transportation accounts for about 16% of global greenhouse gas emissions."
        },

        "communication": {
            "keywords": ["world communication", "global communication", "internet connectivity", "telecommunications", "communication networks"],
            "response": "Global communication networks include the internet, satellite systems, undersea cables, and mobile networks. About 65% of the world's population uses the internet. Communication technology has accelerated globalization but also created digital divides between connected and unconnected regions."
        },

        "health": {
            "keywords": ["world health", "global health", "life expectancy", "diseases", "healthcare systems"],
            "response": "Global average life expectancy is about 73 years, varying from 84+ in Japan to under 55 in some African nations. Major health challenges include infectious diseases (COVID-19, HIV/AIDS), non-communicable diseases (heart disease, cancer), and health inequalities. WHO coordinates global health responses."
        },

        "education": {
            "keywords": ["world education", "global education", "literacy rates", "education systems", "educational access"],
            "response": "Global literacy rate is about 86%, with significant disparities by region and gender. Primary education enrollment is nearly universal, but secondary and higher education access varies. Education quality, relevance to employment, and digital skills are ongoing challenges worldwide."
        },

        "poverty": {
            "keywords": ["world poverty", "global poverty", "income inequality", "economic disparity", "poverty reduction"],
            "response": "About 9.2% of the world lives in extreme poverty (less than $2.15/day), down from 36% in 1990. However, income inequality remains high, with the richest 1% owning nearly half of global wealth. Poverty reduction efforts include microfinance, education, and social safety nets."
        },

        "human_rights": {
            "keywords": ["human rights", "world human rights", "universal declaration", "rights violations", "human dignity"],
            "response": "The Universal Declaration of Human Rights (1948) establishes fundamental rights for all people. Key rights include life, liberty, equality, freedom from torture, freedom of expression, and education. Human rights organizations monitor violations and advocate for protection globally."
        },

        "democracy": {
            "keywords": ["world democracy", "democratic countries", "political systems", "governance", "elections"],
            "response": "About 57% of countries are electoral democracies. The Democracy Index classifies countries as full democracies, flawed democracies, hybrid regimes, or authoritarian regimes. Democratic governance faces challenges from populism, misinformation, and erosion of institutions in some regions."
        },

        "tourism": {
            "keywords": ["world tourism", "global tourism", "travel destinations", "tourism industry", "cultural tourism"],
            "response": "International tourist arrivals reached 1.5 billion pre-pandemic. Top destinations include France, Spain, US, China, and Italy. Tourism contributes about 10% to global GDP but also creates environmental and cultural impacts. Sustainable tourism aims to balance economic benefits with conservation."
        },

        "sports": {
            "keywords": ["world sports", "global sports", "popular sports", "international competitions", "sports culture"],
            "response": "Football (soccer) is the world's most popular sport with 4 billion fans. Other global sports include cricket, basketball, tennis, and athletics. The Olympic Games, FIFA World Cup, and ICC Cricket World Cup are major international sporting events that unite global audiences."
        },

        "food": {
            "keywords": ["world food", "global cuisine", "food cultures", "staple foods", "culinary traditions"],
            "response": "Staple foods include rice (Asia), wheat (Europe, North America), corn (Americas), and cassava (Africa). Global cuisine diversity reflects local ingredients, history, and culture. Food security remains a challenge, with about 690 million people undernourished despite enough global food production."
        },

        "water": {
            "keywords": ["world water", "global water", "freshwater", "water scarcity", "water resources"],
            "response": "Only 2.5% of Earth's water is freshwater, and less than 1% is accessible for human use. About 2 billion people lack safe drinking water. Water scarcity affects 40% of the global population. Water management, conservation, and equitable distribution are critical global issues."
        },

        "energy": {
            "keywords": ["world energy", "global energy", "energy sources", "renewable energy", "energy consumption"],
            "response": "Global energy consumption is about 580 exajoules annually, primarily from fossil fuels (84%). Renewable energy (solar, wind, hydro) accounts for about 11% and is growing. Energy access varies, with 770 million people lacking electricity. Transition to clean energy is crucial for climate goals."
        },

        "space_exploration": {
            "keywords": ["space exploration", "world space programs", "moon landing", "mars exploration", "international space station"],
            "response": "Human space exploration began with Sputnik (1957) and Apollo moon landings (1969-1972). The International Space Station has hosted astronauts from 19 countries since 2000. Current goals include returning to the Moon (Artemis program) and human missions to Mars. Multiple countries now have space programs."
        },

        "technology": {
            "keywords": ["world technology", "global technology", "technological advancement", "digital revolution", "innovation"],
            "response": "We live in the Information Age characterized by computers, internet, and mobile technology. Emerging technologies include AI, biotechnology, nanotechnology, and quantum computing. Technology diffusion creates opportunities but also digital divides and ethical challenges regarding privacy and employment."
        },

        "art": {
            "keywords": ["world art", "global art", "art history", "art movements", "cultural expressions"],
            "response": "Artistic traditions span from ancient cave paintings to contemporary digital art. Major art movements include Renaissance, Baroque, Impressionism, Modernism, and Postmodernism. Art serves aesthetic, cultural, political, and social functions across all human societies."
        },

        "music": {
            "keywords": ["world music", "global music", "musical traditions", "music genres", "cultural music"],
            "response": "Every culture has musical traditions. Global genres include classical, jazz, rock, pop, hip-hop, and electronic music. Traditional music varies from Indian classical to African drumming to European folk. Music serves ritual, entertainment, social, and emotional functions worldwide."
        },

        "literature": {
            "keywords": ["world literature", "global literature", "famous authors", "literary traditions", "books"],
            "response": "World literature includes ancient epics (Gilgamesh, Iliad, Mahabharata), religious texts, Shakespeare, and modern Nobel laureates. Different traditions include European, Asian, African, and Latin American literature. Literature preserves cultural memory and explores universal human experiences."
        },

        "architecture": {
            "keywords": ["world architecture", "global architecture", "architectural styles", "famous buildings", "architectural history"],
            "response": "Architectural styles include ancient (Egyptian pyramids, Greek temples), medieval (Gothic cathedrals), Renaissance, modern (skyscrapers), and postmodern. Different regions developed distinctive styles using local materials and responding to climate, culture, and technology."
        },

        "festivals": {
            "keywords": ["world festivals", "global festivals", "cultural celebrations", "religious festivals", "holidays"],
            "response": "Global festivals include religious celebrations (Christmas, Eid, Diwali, Hanukkah), cultural events (Carnival, Oktoberfest), and national holidays. Festivals strengthen community bonds, preserve traditions, and celebrate seasonal changes or historical events across cultures."
        },

        "animals": {
            "keywords": ["world animals", "global wildlife", "animal species", "endangered animals", "biodiversity"],
            "response": "Earth hosts incredible animal diversity from blue whales (largest) to bumblebee bats (smallest). Iconic species include elephants, tigers, pandas, and eagles. About 1 million animal species face extinction threats due to habitat loss, climate change, and human activities."
        },

        "plants": {
            "keywords": ["world plants", "global flora", "plant species", "trees", "botanical diversity"],
            "response": "There are about 390,000 plant species, including trees (sequoias are largest), flowers (Rafflesia is largest), and crops. Plants provide oxygen, food, medicine, and materials. Deforestation threatens plant biodiversity, particularly in tropical rainforests which contain half of all plant species."
        },

        "weather": {
            "keywords": ["world weather", "global weather", "extreme weather", "weather patterns", "climate phenomena"],
            "response": "Global weather systems include monsoons, hurricanes/cyclones, tornadoes, and blizzards. Extreme weather events are becoming more frequent with climate change. Weather influences agriculture, transportation, and daily life worldwide. Meteorological organizations collaborate on global weather forecasting."
        },

        "seasons": {
            "keywords": ["world seasons", "global seasons", "seasonal changes", "equinox", "solstice"],
            "response": "Seasons result from Earth's 23.5° axial tilt and orbit around the Sun. Temperate regions have four seasons; tropical regions have wet/dry seasons. The Northern and Southern Hemispheres experience opposite seasons. Equinoxes (equal day/night) and solstices (longest/shortest days) mark seasonal transitions."
        },

        "tectonic_plates": {
            "keywords": ["tectonic plates", "world plates", "continental drift", "plate boundaries", "earthquakes volcanoes"],
            "response": "Earth's lithosphere is divided into 7 major and 8 minor tectonic plates that move 1-10 cm/year. Plate boundaries cause earthquakes, volcanoes, and mountain building. The theory of plate tectonics explains continental drift, with continents having moved significantly over geological time."
        },

        "volcanoes": {
            "keywords": ["world volcanoes", "global volcanoes", "volcanic activity", "ring of fire", "active volcanoes"],
            "response": "There are about 1,500 potentially active volcanoes worldwide, with 50-70 erupting annually. The Pacific Ring of Fire contains 75% of Earth's volcanoes. Volcanoes create new land, enrich soil, but also pose hazards. Some notable volcanoes are Mauna Loa (largest), Krakatoa, and Vesuvius."
        },

        "earthquakes": {
            "keywords": ["world earthquakes", "global earthquakes", "seismic activity", "richter scale", "earthquake zones"],
            "response": "About 500,000 detectable earthquakes occur annually, with 100 causing damage. The largest recorded was magnitude 9.5 in Chile (1960). Earthquake-prone zones include the Pacific Ring of Fire and Alpine-Himalayan belt. Seismology studies earthquakes to understand Earth's interior and improve prediction."
        },

        "tsunamis": {
            "keywords": ["tsunamis", "world tsunamis", "tidal waves", "ocean waves", "tsunami warning"],
            "response": "Tsunamis are large ocean waves caused by underwater earthquakes, landslides, or volcanic eruptions. The 2004 Indian Ocean tsunami killed about 230,000 people. Warning systems use seismic sensors and sea level monitors. Preparedness and education save lives in tsunami-prone coastal areas."
        },

        "glaciers": {
            "keywords": ["world glaciers", "global glaciers", "ice sheets", "glacial melting", "polar ice"],
            "response": "Glaciers cover about 10% of Earth's land, storing 69% of freshwater. Major ice sheets are in Greenland and Antarctica. Glaciers are melting rapidly due to climate change, contributing to sea level rise. Glacial meltwater feeds rivers supporting billions of people."
        },

        "coral_reefs": {
            "keywords": ["coral reefs", "world reefs", "great barrier reef", "reef ecosystems", "coral bleaching"],
            "response": "Coral reefs cover less than 1% of ocean floor but support 25% of marine species. The Great Barrier Reef is the largest coral system. Reefs protect coastlines and support fisheries. Climate change, pollution, and ocean acidification threaten reefs through coral bleaching and death."
        },

        "islands": {
            "keywords": ["world islands", "global islands", "island nations", "archipelagos", "oceanic islands"],
            "response": "There are about 180,000 islands worldwide. Greenland is the largest island, followed by New Guinea and Borneo. Island nations like Maldives face existential threats from sea level rise. Islands have unique ecosystems with many endemic species found nowhere else."
        },

        "caves": {
            "keywords": ["world caves", "global caves", "largest cave", "cave systems", "speleology"],
            "response": "Son Doong in Vietnam is the world's largest cave by volume. Mammoth Cave in Kentucky has the longest known passage system. Caves form through chemical weathering of limestone. They preserve archaeological remains, host unique ecosystems, and are explored by speleologists."
        },

        "canyons": {
            "keywords": ["world canyons", "global canyons", "grand canyon", "deepest canyon", "gorge"],
            "response": "The Grand Canyon (USA) is one of the most famous, carved by the Colorado River over 6 million years. Yarlung Tsangpo Grand Canyon (Tibet) is the deepest at over 5,300 meters. Canyons reveal geological history through exposed rock layers and often have dramatic landscapes."
        },

        "waterfalls": {
            "keywords": ["world waterfalls", "global waterfalls", "largest waterfall", "highest waterfall", "famous waterfalls"],
            "response": "Angel Falls in Venezuela is the highest at 979 meters. Victoria Falls (Africa) is the largest sheet of falling water. Iguazu Falls (South America) is the widest system. Waterfalls create scenic beauty, generate hydroelectric power, and are important tourist destinations."
        },

        "lakes": {
            "keywords": ["world lakes", "global lakes", "largest lake", "deepest lake", "freshwater lakes"],
            "response": "The Caspian Sea is the largest lake by area, though salty. Lake Superior is the largest freshwater lake. Lake Baikal (Russia) is the deepest and oldest, containing 20% of Earth's unfrozen freshwater. Lakes provide drinking water, fisheries, recreation, and regulate local climate."
        },

        # Expanded Semiconductor Topics
        "semiconductor_basics": {
            "keywords": ["semiconductor", "semiconductors", "what is semiconductor", "semiconductor materials"],
            "response": "Semiconductors are materials with electrical conductivity between conductors (like metals) and insulators (like ceramics). Silicon is the most commonly used semiconductor in electronics, but others include germanium, gallium arsenide, and silicon carbide."
        },

        "silicon": {
            "keywords": ["silicon", "silicon chip", "silicon wafer", "silicon element", "si"],
            "response": "Silicon (Si) is a chemical element with atomic number 14, widely used in semiconductors due to its stable crystal structure, abundant availability, and ability to form a stable oxide (SiO2). It's the primary material for most integrated circuits and solar cells."
        },

        "germanium": {
            "keywords": ["germanium", "ge semiconductor", "germanium transistor"],
            "response": "Germanium (Ge) was the first semiconductor material used in early transistors and diodes. While largely replaced by silicon in most applications, it's still used in some high-frequency electronics, infrared optics, and as a substrate for some III-V semiconductors."
        },

        "gallium_arsenide": {
            "keywords": ["gallium arsenide", "gaas", "compound semiconductor", "iii-v semiconductor"],
            "response": "Gallium arsenide (GaAs) is a compound semiconductor with higher electron mobility than silicon, making it suitable for high-frequency applications like microwave circuits, satellite communications, and some optoelectronic devices like LEDs and laser diodes."
        },

        "silicon_carbide": {
            "keywords": ["silicon carbide", "sic", "wide bandgap semiconductor", "power semiconductor"],
            "response": "Silicon carbide (SiC) is a wide bandgap semiconductor known for its high thermal conductivity, high electric field breakdown strength, and high maximum current density. It's used in high-power, high-temperature, and high-voltage applications like electric vehicle power electronics."
        },

        "gallium_nitride": {
            "keywords": ["gallium nitride", "gan", "wide bandgap", "gan semiconductor", "gan fet"],
            "response": "Gallium nitride (GaN) is a wide bandgap semiconductor with high electron mobility and breakdown voltage. It's used in high-power, high-frequency applications like 5G infrastructure, RF amplifiers, and fast-charging power adapters."
        },

        "doping": {
            "keywords": ["doping", "semiconductor doping", "n-type p-type", "donor acceptor", "impurity doping"],
            "response": "Doping is the process of adding impurities to semiconductors to change their electrical properties. N-type doping adds donor atoms (like phosphorus in silicon) creating free electrons. P-type doping adds acceptor atoms (like boron in silicon) creating holes (positive charge carriers)."
        },

        "pn_junction": {
            "keywords": ["pn junction", "p-n junction", "junction diode", "depletion region", "junction formation"],
            "response": "A PN junction is formed by joining P-type and N-type semiconductors. It creates a depletion region where mobile charges are depleted, and a built-in potential forms. This junction allows current to flow easily in one direction (forward bias) but blocks it in the opposite (reverse bias), forming the basis of diodes."
        },

        "diode": {
            "keywords": ["diode", "diodes", "rectifier diode", "semiconductor diode", "diode function"],
            "response": "A diode is a two-terminal electronic component that conducts current primarily in one direction. It's based on a PN junction and is used for rectification, voltage regulation, signal demodulation, and protection circuits."
        },

        "zener_diode": {
            "keywords": ["zener diode", "zener breakdown", "voltage regulator diode", "reference diode"],
            "response": "A Zener diode is a special diode designed to operate in the reverse breakdown region. It maintains a nearly constant voltage across its terminals, making it useful for voltage regulation, voltage reference, and surge protection circuits."
        },

        "led": {
            "keywords": ["led", "light emitting diode", "led lighting", "led display", "oled"],
            "response": "An LED (Light Emitting Diode) is a semiconductor device that emits light when current flows through it. LEDs are energy-efficient and used in lighting, displays, indicators, and optical communications. OLEDs (Organic LEDs) use organic materials for flexible displays."
        },

        "photodiode": {
            "keywords": ["photodiode", "photo diode", "light detector", "optical sensor", "solar cell"],
            "response": "A photodiode is a semiconductor device that converts light into electrical current. It operates in reverse bias and is used in optical communication, light sensors, medical imaging, and as the basic building block of solar cells."
        },

        "bjt": {
            "keywords": ["bjt", "bipolar junction transistor", "npn transistor", "pnp transistor", "bipolar transistor"],
            "response": "A Bipolar Junction Transistor (BJT) is a three-terminal semiconductor device consisting of two PN junctions. It comes in NPN and PNP types and amplifies current. BJTs are used in amplifiers, switches, and digital logic circuits."
        },

        "mosfet": {
            "keywords": ["mosfet", "metal oxide semiconductor fet", "field effect transistor", "nmos pmos", "mos transistor"],
            "response": "A MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor) is a four-terminal semiconductor device used for switching and amplifying signals. It has a gate, source, drain, and body. MOSFETs are the building blocks of modern digital integrated circuits due to their high input impedance and scalability."
        },

        "cmos": {
            "keywords": ["cmos", "complementary mos", "cmos logic", "cmos inverter", "cmos technology"],
            "response": "CMOS (Complementary Metal-Oxide-Semiconductor) technology uses both NMOS and PMOS transistors in complementary pairs. This design minimizes power consumption (especially static power) and is the dominant technology for digital integrated circuits, microprocessors, and memory chips."
        },

        "finfet": {
            "keywords": ["finfet", "fin fet", "3d transistor", "multigate transistor", "advanced cmos"],
            "response": "FinFET is a type of 3D transistor where the conducting channel is wrapped by a thin silicon fin. This structure provides better control of the channel, reducing leakage current and enabling continued transistor scaling beyond planar MOSFET limits."
        },

        "transistor": {
            "keywords": ["transistor", "transistors", "what is transistor", "transistor invention", "transistor types"],
            "response": "A transistor is a semiconductor device used to amplify or switch electronic signals. It's the fundamental building block of modern electronics. Major types include BJTs (Bipolar Junction Transistors) and FETs (Field-Effect Transistors) like MOSFETs."
        },

        "ic": {
            "keywords": ["integrated circuit", "ic", "microchip", "chip", "semiconductor chip"],
            "response": "An integrated circuit (IC) is a set of electronic circuits on a small chip of semiconductor material, typically silicon. ICs can contain billions of transistors and are used in virtually all electronic devices today, from computers to smartphones."
        },

        "vlsi": {
            "keywords": ["vlsi", "very large scale integration", "vlsi design", "vlsi technology", "asic design"],
            "response": "VLSI (Very Large Scale Integration) is the process of creating integrated circuits by combining thousands or millions of transistors into a single chip. It involves design, verification, and fabrication of complex ICs like microprocessors, memory chips, and ASICs (Application-Specific Integrated Circuits)."
        },

        "asic": {
            "keywords": ["asic", "application specific ic", "custom chip", "asic design", "asic vs fpga"],
            "response": "An ASIC (Application-Specific Integrated Circuit) is a custom-designed chip for a particular application, rather than general-purpose use. ASICs offer optimized performance, power efficiency, and cost for high-volume production compared to programmable alternatives like FPGAs."
        },

        "fpga": {
            "keywords": ["fpga", "field programmable gate array", "programmable logic", "reconfigurable hardware", "fpga vs asic"],
            "response": "An FPGA (Field-Programmable Gate Array) is an integrated circuit that can be configured by the customer after manufacturing. It contains programmable logic blocks and interconnects, allowing implementation of custom digital circuits. FPGAs are used for prototyping, low-volume production, and reconfigurable computing."
        },

        "semiconductor_manufacturing": {
            "keywords": ["semiconductor manufacturing", "chip fabrication", "semiconductor process", "wafer fabrication", "cleanroom"],
            "response": "Semiconductor manufacturing involves designing and fabricating ICs through processes like photolithography, etching, doping, chemical vapor deposition, and packaging in cleanroom environments. Modern fabs produce chips on silicon wafers up to 300mm in diameter with features as small as a few nanometers."
        },

        "photolithography": {
            "keywords": ["photolithography", "lithography", "mask aligner", "stepper", "euv lithography"],
            "response": "Photolithography is a key semiconductor manufacturing process that uses light to transfer geometric patterns from photomasks to light-sensitive chemical photoresist on silicon wafers. Advanced techniques like EUV (Extreme Ultraviolet) lithography enable patterning of nanometer-scale features."
        },

        "etching": {
            "keywords": ["etching", "semiconductor etching", "dry etching", "wet etching", "plasma etching"],
            "response": "Etching is the process of removing material from a silicon wafer to create patterns. Wet etching uses liquid chemicals, while dry etching uses plasma. Reactive ion etching (RIE) combines chemical and physical etching for precise pattern transfer."
        },

        "deposition": {
            "keywords": ["deposition", "thin film deposition", "cvd", "pvd", "atomic layer deposition"],
            "response": "Deposition is the process of applying thin films of material onto silicon wafers. Common methods include Chemical Vapor Deposition (CVD), Physical Vapor Deposition (PVD), and Atomic Layer Deposition (ALD). These films can be conductors, insulators, or semiconductors."
        },

        "ion_implantation": {
            "keywords": ["ion implantation", "doping process", "ion implanter", "semiconductor doping equipment"],
            "response": "Ion implantation is a process used to dope semiconductors by accelerating ions of dopant atoms and bombarding the silicon wafer with them. This allows precise control of dopant concentration and depth, creating N-type or P-type regions."
        },

        "wafer": {
            "keywords": ["wafer", "silicon wafer", "semiconductor wafer", "wafer processing", "wafer size"],
            "response": "A wafer is a thin slice of semiconductor material, typically silicon, used as the substrate for microelectronic devices. Wafers are produced in various diameters (100mm to 300mm) and undergo multiple processing steps to create integrated circuits."
        },

        "cleanroom": {
            "keywords": ["cleanroom", "clean room", "semiconductor cleanroom", "class 100", "particle control"],
            "response": "A cleanroom is a controlled environment with low levels of pollutants like dust, airborne microbes, and chemical vapors. Semiconductor manufacturing requires Class 1 or better cleanrooms (fewer than 1 particle per cubic foot) to prevent defects in microscopic circuits."
        },

        "packaging": {
            "keywords": ["semiconductor packaging", "chip packaging", "ic packaging", "die packaging", "3d packaging"],
            "response": "Semiconductor packaging encloses a die (the actual chip) to protect it from physical damage and corrosion, provide electrical connections to external circuits, and dissipate heat. Advanced packaging includes 3D IC stacking and system-in-package (SiP) technologies."
        },

        "yield": {
            "keywords": ["yield", "semiconductor yield", "wafer yield", "die yield", "manufacturing yield"],
            "response": "Yield in semiconductor manufacturing refers to the percentage of functional chips produced from a wafer. Yield is affected by defects, process variations, and design issues. High yield is critical for cost-effective production."
        },

        "moores_law": {
            "keywords": ["moore's law", "moore law", "transistor scaling", "semiconductor scaling", "gordon moore"],
            "response": "Moore's Law is the observation that the number of transistors on a chip doubles approximately every two years, leading to exponential growth in computing power. First stated by Gordon Moore in 1965, it has driven semiconductor industry planning for decades."
        },

        "process_node": {
            "keywords": ["process node", "technology node", "nm process", "7nm", "5nm", "3nm"],
            "response": "A process node refers to a specific semiconductor manufacturing process with defined design rules and feature sizes (like 7nm, 5nm). Smaller nodes allow more transistors per area, improving performance and power efficiency, though the naming no longer directly corresponds to physical dimensions."
        },

        "foundry": {
            "keywords": ["foundry", "semiconductor foundry", "chip foundry", "tsmc", "samsung foundry"],
            "response": "A semiconductor foundry is a factory that manufactures chips for other companies. Major foundries include TSMC, Samsung, and GlobalFoundries. Foundries enable fabless semiconductor companies to design chips without owning expensive fabrication facilities."
        },

        "fabless": {
            "keywords": ["fabless", "fabless semiconductor", "fabless company", "ic design house"],
            "response": "A fabless semiconductor company designs and sells chips but outsources manufacturing to foundries. This business model reduces capital investment and allows focus on design and innovation. Examples include Qualcomm, NVIDIA, and AMD."
        },

        "idm": {
            "keywords": ["idm", "integrated device manufacturer", "intel", "samsung semiconductor", "idm model"],
            "response": "An IDM (Integrated Device Manufacturer) designs, manufactures, and sells semiconductor chips. Intel and Samsung are examples of IDMs. This model requires massive capital investment but provides control over the entire process from design to fabrication."
        },

        "semiconductor_industry": {
            "keywords": ["semiconductor industry", "chip industry", "semiconductor market", "semiconductor companies"],
            "response": "The semiconductor industry designs and manufactures integrated circuits and other semiconductor devices. It's a global, highly competitive industry with major players in the US, Taiwan, South Korea, Japan, and Europe, and is critical to modern technology."
        },

        "memory_chips": {
            "keywords": ["memory chips", "dram", "nand flash", "sram", "memory semiconductor"],
            "response": "Memory chips store data and programs. DRAM (Dynamic RAM) is used for main memory, NAND flash for storage (SSDs, USB drives), and SRAM (Static RAM) for CPU caches. Specialized memories include ROM, EPROM, and emerging technologies like MRAM and ReRAM."
        },

        "microprocessor": {
            "keywords": ["microprocessor", "cpu", "microcontroller", "processor chip", "central processing unit"],
            "response": "A microprocessor is an integrated circuit that contains the functions of a central processing unit (CPU) of a computer. Modern microprocessors can contain billions of transistors and execute billions of instructions per second. Microcontrollers integrate CPU, memory, and peripherals on one chip."
        },

        "analog_chips": {
            "keywords": ["analog chips", "analog ic", "mixed signal", "rf ic", "power management ic"],
            "response": "Analog chips process continuous signals (like sound, temperature, or radio waves) as opposed to digital chips that process discrete 0s and 1s. They include amplifiers, data converters, radio frequency (RF) circuits, and power management ICs."
        },

        "sensors": {
            "keywords": ["semiconductor sensors", "mems", "image sensor", "cmos sensor", "pressure sensor"],
            "response": "Semiconductor sensors convert physical phenomena into electrical signals. Examples include MEMS (Micro-Electro-Mechanical Systems) for motion and pressure sensing, CMOS image sensors for cameras, and temperature sensors. They're used in smartphones, automotive systems, and IoT devices."
        },

        "power_semiconductors": {
            "keywords": ["power semiconductors", "power devices", "igbt", "thyristor", "power mosfet"],
            "response": "Power semiconductors handle high voltages and currents. They include IGBTs (Insulated-Gate Bipolar Transistors), thyristors, power MOSFETs, and diodes. They're used in power conversion, motor drives, renewable energy systems, and electric vehicles."
        },

        "optoelectronics": {
            "keywords": ["optoelectronics", "optoelectronic devices", "photonic semiconductors", "laser diode", "optical semiconductor"],
            "response": "Optoelectronics involves devices that source, detect, and control light. Semiconductor optoelectronic devices include LEDs, laser diodes, photodiodes, solar cells, and optical modulators. They're used in displays, communications, sensing, and energy harvesting."
        },

        "quantum_dots": {
            "keywords": ["quantum dots", "semiconductor nanocrystals", "qled", "quantum dot display", "nanoparticle semiconductor"],
            "response": "Quantum dots are nanometer-sized semiconductor particles that exhibit quantum mechanical properties. Their optical and electronic properties depend on size. They're used in displays (QLED TVs), solar cells, biomedical imaging, and as single-photon sources for quantum computing."
        },

        "semiconductor_physics": {
            "keywords": ["semiconductor physics", "band theory", "band gap", "electron hole", "carrier transport"],
            "response": "Semiconductor physics studies the electrical properties of semiconductors. Key concepts include energy bands (valence band, conduction band, band gap), charge carriers (electrons and holes), carrier transport (drift and diffusion), and recombination processes."
        },

        "band_gap": {
            "keywords": ["band gap", "energy gap", "direct bandgap", "indirect bandgap", "bandgap engineering"],
            "response": "The band gap is the energy difference between the valence band (filled with electrons) and the conduction band (empty at absolute zero). It determines a semiconductor's electrical and optical properties. Direct bandgap materials (like GaAs) are efficient for light emission, while indirect (like Si) are not."
        },

        "carrier_concentration": {
            "keywords": ["carrier concentration", "electron concentration", "hole concentration", "intrinsic semiconductor", "extrinsic semiconductor"],
            "response": "Carrier concentration refers to the number of charge carriers (electrons or holes) per unit volume in a semiconductor. Intrinsic semiconductors have equal electron and hole concentrations. Doping creates extrinsic semiconductors with unequal concentrations, determining conductivity type (N or P)."
        },

        "mobility": {
            "keywords": ["mobility", "electron mobility", "hole mobility", "carrier mobility", "semiconductor mobility"],
            "response": "Mobility measures how quickly an electron or hole can move through a semiconductor when pulled by an electric field. Higher mobility means faster devices. It's affected by scattering from impurities, lattice vibrations, and other carriers."
        },

        "recombination": {
            "keywords": ["recombination", "electron hole recombination", "radiative recombination", "nonradiative recombination", "recombination lifetime"],
            "response": "Recombination is the process where an electron and hole combine, annihilating each other and releasing energy. Radiative recombination emits light (as in LEDs), while nonradiative recombination releases heat. Recombination affects device efficiency and speed."
        },

        "semiconductor_testing": {
            "keywords": ["semiconductor testing", "ic testing", "wafer testing", "ate", "final test"],
            "response": "Semiconductor testing verifies that chips function correctly. Wafer testing (probe test) checks dies on the wafer before packaging. Final test checks packaged chips. ATE (Automatic Test Equipment) applies test patterns and measures responses to identify defects."
        },

        "reliability": {
            "keywords": ["semiconductor reliability", "ic reliability", "failure mechanisms", "mtbf", "accelerated testing"],
            "response": "Semiconductor reliability ensures chips operate correctly over their expected lifetime under specified conditions. Failure mechanisms include electromigration, hot carrier injection, time-dependent dielectric breakdown (TDDB), and stress migration. Reliability is assessed through accelerated life testing and statistical analysis."
        },

        "thermal_management": {
            "keywords": ["thermal management", "chip cooling", "heat dissipation", "thermal design", "semiconductor temperature"],
            "response": "Thermal management deals with removing heat from semiconductor devices to prevent overheating, which can cause performance degradation and failure. Techniques include heat sinks, thermal interface materials, fans, liquid cooling, and advanced packaging solutions."
        },

        "semiconductor_equipment": {
            "keywords": ["semiconductor equipment", "chip making equipment", "lithography tool", "etch tool", "semiconductor tools"],
            "response": "Semiconductor manufacturing equipment includes photolithography systems, etch tools, deposition systems, ion implanters, chemical mechanical planarization (CMP) tools, and metrology equipment. Companies like ASML, Applied Materials, and Lam Research produce these advanced machines."
        },

        "materials": {
            "keywords": ["semiconductor materials", "semiconductor substrates", "compound semiconductors", "organic semiconductors", "2d materials"],
            "response": "Semiconductor materials include elemental semiconductors (silicon, germanium), compound semiconductors (GaAs, InP), organic semiconductors, and emerging materials like graphene and transition metal dichalcogenides (2D materials). Each has unique properties for different applications."
        },

        "future_semiconductors": {
            "keywords": ["future semiconductors", "beyond silicon", "next generation semiconductors", "quantum computing chips", "neuromorphic chips"],
            "response": "Future semiconductor technologies include III-V materials on silicon, carbon nanotubes, graphene, spintronics, photonic integrated circuits, neuromorphic computing chips, and quantum computing devices. These aim to overcome limitations of traditional silicon CMOS and enable new applications."
        },

        # Expanded Science Topics
        "physics": {
            "keywords": ["physics", "laws of physics", "quantum physics", "classical physics"],
            "response": "Physics is the natural science that studies matter, energy, motion, and forces. It includes classical mechanics, electromagnetism, thermodynamics, quantum mechanics, and relativity."
        },

        "chemistry": {
            "keywords": ["chemistry", "chemical reactions", "organic chemistry", "inorganic chemistry"],
            "response": "Chemistry studies the composition, structure, properties, and changes of matter. It includes organic, inorganic, physical, analytical, and biochemistry."
        },

        "biology": {
            "keywords": ["biology", "life science", "cell biology", "biological science"],
            "response": "Biology is the study of living organisms and their structure, function, growth, evolution, and distribution. It includes botany, zoology, genetics, ecology, and microbiology."
        },

        "mathematics": {
            "keywords": ["mathematics", "math", "calculus algebra", "mathematical science"],
            "response": "Mathematics is the study of numbers, quantities, shapes, and patterns. It includes arithmetic, algebra, geometry, calculus, statistics, and topology."
        },

        "astronomy": {
            "keywords": ["astronomy", "stars", "planets", "universe", "cosmos", "galaxy", "space science"],
            "response": "Astronomy is the scientific study of celestial objects (stars, planets, galaxies) and phenomena that originate outside Earth's atmosphere. It includes observational and theoretical astronomy."
        },

        "geology": {
            "keywords": ["geology", "rocks", "minerals", "earth science", "geological", "plate tectonics"],
            "response": "Geology is the study of Earth's physical structure, substances, history, and processes. It includes mineralogy, petrology, paleontology, and seismology."
        },

        "meteorology": {
            "keywords": ["meteorology", "weather science", "climate science", "atmosphere", "weather patterns"],
            "response": "Meteorology is the study of the atmosphere, atmospheric phenomena, and weather forecasting. It includes climatology, atmospheric physics, and weather systems."
        },

        "oceanography": {
            "keywords": ["oceanography", "marine science", "ocean science", "sea life", "ocean currents"],
            "response": "Oceanography is the study of the physical and biological aspects of the ocean. It includes marine biology, chemical oceanography, physical oceanography, and marine geology."
        },

        "environmental_science": {
            "keywords": ["environmental science", "ecology", "environmental studies", "conservation", "sustainability"],
            "response": "Environmental science is an interdisciplinary field that studies the environment and solutions to environmental problems. It includes ecology, conservation biology, and environmental chemistry."
        },

        "neuroscience": {
            "keywords": ["neuroscience", "brain science", "neurology", "cognitive science", "neural"],
            "response": "Neuroscience is the scientific study of the nervous system, including the brain, spinal cord, and neural circuits. It includes cognitive, molecular, and behavioral neuroscience."
        },

        "genetics": {
            "keywords": ["genetics", "dna", "genes", "genetic engineering", "heredity", "genome"],
            "response": "Genetics is the study of genes, genetic variation, and heredity in living organisms. It includes molecular genetics, population genetics, and genomics."
        },

        "microbiology": {
            "keywords": ["microbiology", "microbes", "bacteria", "viruses", "microorganisms", "microbial"],
            "response": "Microbiology is the study of microscopic organisms, including bacteria, viruses, fungi, and protozoa. It includes medical microbiology, environmental microbiology, and industrial microbiology."
        },

        "biochemistry": {
            "keywords": ["biochemistry", "biochemical", "molecular biology", "cellular chemistry", "metabolism"],
            "response": "Biochemistry is the study of chemical processes within and relating to living organisms. It focuses on cellular and molecular processes like metabolism, signal transduction, and gene expression."
        },

        "biotechnology": {
            "keywords": ["biotechnology", "biotech", "genetic engineering", "bioprocessing", "biomedical technology"],
            "response": "Biotechnology uses biological systems, organisms, or derivatives to develop or create products. Applications include medicine, agriculture, and environmental management."
        },

        "zoology": {
            "keywords": ["zoology", "animal science", "animal biology", "wildlife biology", "animal behavior"],
            "response": "Zoology is the branch of biology that studies the animal kingdom, including animal structure, embryology, evolution, classification, habits, and distribution."
        },

        "botany": {
            "keywords": ["botany", "plant science", "plant biology", "phytology", "plants"],
            "response": "Botany is the scientific study of plants, including their structure, properties, biochemical processes, classification, and economic importance."
        },

        "anatomy": {
            "keywords": ["anatomy", "human anatomy", "animal anatomy", "body structure", "anatomical"],
            "response": "Anatomy is the branch of biology concerned with the study of the structure of organisms and their parts. It includes gross anatomy, microscopic anatomy, and comparative anatomy."
        },

        "physiology": {
            "keywords": ["physiology", "human physiology", "body functions", "organ systems", "physiological"],
            "response": "Physiology is the scientific study of functions and mechanisms in a living system. It covers how organisms, organ systems, organs, cells, and biomolecules carry out chemical and physical functions."
        },

        "epidemiology": {
            "keywords": ["epidemiology", "disease spread", "public health science", "infection control", "pandemic"],
            "response": "Epidemiology is the study and analysis of the distribution, patterns, and determinants of health and disease conditions in defined populations."
        },

        "immunology": {
            "keywords": ["immunology", "immune system", "immunity", "vaccines", "antibodies"],
            "response": "Immunology is the branch of biology that studies the immune system in all organisms. It covers physiological functioning, immunological disorders, and immune responses to pathogens."
        },

        "pharmacology": {
            "keywords": ["pharmacology", "drug science", "medicines", "pharmaceuticals", "drug action"],
            "response": "Pharmacology is the branch of medicine concerned with the uses, effects, and modes of action of drugs. It includes pharmacodynamics and pharmacokinetics."
        },

        "toxicology": {
            "keywords": ["toxicology", "poisons", "toxins", "chemical safety", "toxic substances"],
            "response": "Toxicology is the study of the adverse effects of chemical substances on living organisms and the practice of diagnosing and treating exposures to toxins and poisons."
        },

        "forensic_science": {
            "keywords": ["forensic science", "forensics", "crime science", "criminalistics", "evidence analysis"],
            "response": "Forensic science applies scientific principles and techniques to matters of criminal and civil law. It includes DNA analysis, fingerprinting, ballistics, and toxicology."
        },

        "nanotechnology": {
            "keywords": ["nanotechnology", "nanoscience", "nanomaterials", "nanoscale", "nanoparticles"],
            "response": "Nanotechnology is the manipulation of matter on an atomic, molecular, and supramolecular scale. It has applications in medicine, electronics, biomaterials, and energy production."
        },

        "materials_science": {
            "keywords": ["materials science", "materials engineering", "new materials", "composite materials", "material properties"],
            "response": "Materials science is an interdisciplinary field that studies the properties of matter and its applications to various areas of science and engineering. It includes metals, ceramics, polymers, and composites."
        },

        "quantum_mechanics": {
            "keywords": ["quantum mechanics", "quantum theory", "quantum physics", "wave function", "quantum entanglement"],
            "response": "Quantum mechanics is a fundamental theory in physics that describes nature at the smallest scales of energy levels of atoms and subatomic particles. Key concepts include superposition, entanglement, and wave-particle duality."
        },

        "relativity": {
            "keywords": ["relativity", "einstein", "general relativity", "special relativity", "space-time"],
            "response": "Relativity consists of two interrelated theories by Albert Einstein: special relativity (dealing with objects moving at constant speed) and general relativity (describing gravity as a curvature of spacetime)."
        },

        "thermodynamics": {
            "keywords": ["thermodynamics", "laws of thermodynamics", "heat transfer", "entropy", "thermal energy"],
            "response": "Thermodynamics is the branch of physics that deals with heat, work, temperature, and the statistical behavior of systems. Its laws describe how energy is transferred and transformed."
        },

        "electromagnetism": {
            "keywords": ["electromagnetism", "electromagnetic", "maxwell's equations", "electromagnetic waves", "electricity and magnetism"],
            "response": "Electromagnetism is a branch of physics involving the study of electromagnetic force, a type of physical interaction that occurs between electrically charged particles."
        },

        "particle_physics": {
            "keywords": ["particle physics", "subatomic particles", "hadron collider", "quarks", "leptons", "standard model"],
            "response": "Particle physics is the study of the fundamental particles and forces that constitute matter and radiation. The Standard Model describes the known elementary particles and their interactions."
        },

        "astrophysics": {
            "keywords": ["astrophysics", "astrophysical", "cosmology", "black holes", "neutron stars", "dark matter"],
            "response": "Astrophysics applies the principles of physics and chemistry to understand astronomical objects and phenomena, including stars, galaxies, planets, and the universe as a whole."
        },

        "cosmology": {
            "keywords": ["cosmology", "origin of universe", "big bang", "cosmic inflation", "multiverse"],
            "response": "Cosmology is the scientific study of the large-scale properties of the universe as a whole, including its origin, evolution, and ultimate fate. The Big Bang theory is the prevailing cosmological model."
        },

        "seismology": {
            "keywords": ["seismology", "earthquakes", "seismic waves", "tectonic plates", "seismograph"],
            "response": "Seismology is the scientific study of earthquakes and the propagation of elastic waves through Earth or other planetary bodies. It helps in understanding Earth's interior and predicting earthquakes."
        },

        "volcanology": {
            "keywords": ["volcanology", "volcanoes", "volcanic eruptions", "magma", "lava", "volcanic ash"],
            "response": "Volcanology is the study of volcanoes, lava, magma, and related geological, geophysical, and geochemical phenomena. It aims to understand volcanic processes and hazards."
        },

        "paleontology": {
            "keywords": ["paleontology", "fossils", "dinosaurs", "ancient life", "paleontological"],
            "response": "Paleontology is the scientific study of life that existed prior to, and sometimes including, the start of the Holocene epoch. It includes the study of fossils to classify organisms and study interactions."
        },

        "archaeology": {
            "keywords": ["archaeology", "archaeological", "ancient artifacts", "excavation", "historical sites"],
            "response": "Archaeology is the study of human history and prehistory through the excavation of sites and the analysis of artifacts and other physical remains."
        },

        "anthropology": {
            "keywords": ["anthropology", "cultural anthropology", "physical anthropology", "human evolution", "human societies"],
            "response": "Anthropology is the scientific study of humans, human behavior, and societies in the past and present. It includes cultural anthropology, linguistic anthropology, biological anthropology, and archaeology."
        },

        "psychology": {
            "keywords": ["psychology", "psychological", "human mind", "behavioral science", "cognitive psychology"],
            "response": "Psychology is the scientific study of mind and behavior. It includes cognitive psychology, developmental psychology, clinical psychology, social psychology, and neuropsychology."
        },

        "sociology": {
            "keywords": ["sociology", "sociological", "society study", "social structures", "social behavior"],
            "response": "Sociology is the study of society, social relationships, social interaction, and culture. It examines social institutions, stratification, social movements, and societal change."
        },

        "economics": {
            "keywords": ["economics", "economic science", "microeconomics", "macroeconomics", "economic theory"],
            "response": "Economics is the social science that studies the production, distribution, and consumption of goods and services. It includes microeconomics (individual agents) and macroeconomics (economy as a whole)."
        },

        "political_science": {
            "keywords": ["political science", "politics", "government", "political theory", "international relations"],
            "response": "Political science is the scientific study of politics, governance systems, political activities, political thoughts, and political behavior. It includes comparative politics, international relations, and political theory."
        },

        "linguistics": {
            "keywords": ["linguistics", "language science", "phonetics", "syntax", "semantics", "language structure"],
            "response": "Linguistics is the scientific study of language and its structure. It includes the study of phonetics, phonology, morphology, syntax, semantics, and pragmatics."
        },

        "computer_science": {
            "keywords": ["computer science", "computing theory", "algorithms", "data structures", "computation"],
            "response": "Computer science is the study of algorithmic processes, computational machines, and computation itself. It includes theory, algorithms, programming, software engineering, and artificial intelligence."
        },

        "information_science": {
            "keywords": ["information science", "information theory", "data science", "information systems", "knowledge management"],
            "response": "Information science is an interdisciplinary field primarily concerned with the collection, classification, manipulation, storage, retrieval, and dissemination of information."
        },

        "statistics": {
            "keywords": ["statistics", "statistical analysis", "probability", "data analysis", "inferential statistics"],
            "response": "Statistics is the discipline that concerns the collection, organization, analysis, interpretation, and presentation of data. It includes descriptive statistics and inferential statistics."
        },

        "logic": {
            "keywords": ["logic", "logical reasoning", "deductive reasoning", "inductive reasoning", "formal logic"],
            "response": "Logic is the study of correct reasoning, especially as it involves the drawing of inferences. It includes formal logic (symbolic logic) and informal logic (critical thinking)."
        },

        "philosophy_of_science": {
            "keywords": ["philosophy of science", "scientific method", "scientific theory", "empiricism", "falsifiability"],
            "response": "Philosophy of science is a branch of philosophy concerned with the foundations, methods, and implications of science. It addresses questions about scientific knowledge, methodology, and the nature of scientific change."
        },

        "history_of_science": {
            "keywords": ["history of science", "scientific revolution", "historical science", "scientific discoveries", "scientific progress"],
            "response": "History of science is the study of the development of science and scientific knowledge, including the natural and social sciences. It examines scientific changes over time and their cultural contexts."
        },

        "systems_science": {
            "keywords": ["systems science", "systems theory", "complex systems", "cybernetics", "systems thinking"],
            "response": "Systems science is an interdisciplinary field that studies the nature of systems—from simple to complex—in nature, society, and science. It includes systems theory, cybernetics, and complex systems."
        },

        "chaos_theory": {
            "keywords": ["chaos theory", "chaotic systems", "butterfly effect", "nonlinear dynamics", "fractals"],
            "response": "Chaos theory is a branch of mathematics focusing on the behavior of dynamical systems that are highly sensitive to initial conditions—a phenomenon popularly known as the butterfly effect."
        },

        "complexity_science": {
            "keywords": ["complexity science", "complex adaptive systems", "emergence", "self-organization", "network theory"],
            "response": "Complexity science studies how relationships between parts give rise to the collective behaviors of a system and how the system interacts and forms relationships with its environment."
        },

        "bioinformatics": {
            "keywords": ["bioinformatics", "computational biology", "genomic data", "biological databases", "sequence analysis"],
            "response": "Bioinformatics is an interdisciplinary field that develops methods and software tools for understanding biological data, particularly large and complex datasets like genomic sequences."
        },

        "computational_science": {
            "keywords": ["computational science", "scientific computing", "numerical analysis", "simulation", "computational modeling"],
            "response": "Computational science uses advanced computing capabilities to understand and solve complex problems in science, engineering, and humanities. It includes numerical simulation and modeling."
        },

        "environmental_geology": {
            "keywords": ["environmental geology", "geological hazards", "natural resources", "environmental impact", "geological engineering"],
            "response": "Environmental geology applies geological principles to solve environmental problems, such as natural hazard assessment, resource management, and pollution remediation."
        },

        "hydrology": {
            "keywords": ["hydrology", "water cycle", "water resources", "groundwater", "surface water", "watershed"],
            "response": "Hydrology is the scientific study of the movement, distribution, and management of water on Earth and other planets, including the water cycle, water resources, and environmental watershed sustainability."
        },

        "cryosphere_science": {
            "keywords": ["cryosphere", "glaciology", "ice sheets", "permafrost", "polar science", "sea ice"],
            "response": "Cryosphere science studies the frozen water parts of the Earth system, including glaciers, ice sheets, sea ice, snow, and permafrost, and their interactions with climate."
        },

        "atmospheric_science": {
            "keywords": ["atmospheric science", "atmospheric chemistry", "climate change", "air pollution", "atmospheric physics"],
            "response": "Atmospheric science is the study of the Earth's atmosphere, its processes, the effects other systems have on the atmosphere, and the effects of the atmosphere on these other systems."
        },

        "soil_science": {
            "keywords": ["soil science", "pedology", "soil chemistry", "soil fertility", "agricultural soil"],
            "response": "Soil science is the study of soil as a natural resource on the surface of the Earth, including soil formation, classification, mapping, and physical, chemical, and biological properties."
        },

        "agronomy": {
            "keywords": ["agronomy", "crop science", "soil management", "agricultural science", "plant breeding"],
            "response": "Agronomy is the science and technology of producing and using plants for food, fuel, fiber, and land reclamation. It includes crop production, soil management, and sustainable agriculture."
        },

        "horticulture": {
            "keywords": ["horticulture", "gardening science", "plant cultivation", "landscaping", "floriculture"],
            "response": "Horticulture is the agriculture of plants, mainly for food, materials, comfort, and beauty. It includes fruit cultivation (pomology), vegetable growing (olericulture), and ornamental plants (floriculture)."
        },

        "veterinary_science": {
            "keywords": ["veterinary science", "veterinary medicine", "animal health", "veterinary surgery", "animal diseases"],
            "response": "Veterinary science is the branch of medicine that deals with the prevention, diagnosis, and treatment of disease, disorder, and injury in non-human animals."
        },

        "food_science": {
            "keywords": ["food science", "food technology", "nutrition science", "food safety", "food processing"],
            "response": "Food science is the applied science devoted to the study of food, including food processing, safety, nutrition, and the development of new food products."
        },

        "nutrition_science": {
            "keywords": ["nutrition science", "dietetics", "human nutrition", "nutrients", "dietary guidelines"],
            "response": "Nutrition science studies how food and nutrients affect health, growth, and disease prevention. It includes the study of macronutrients, micronutrients, and dietary patterns."
        },

        "exercise_science": {
            "keywords": ["exercise science", "kinesiology", "sports science", "physical activity", "human performance"],
            "response": "Exercise science is the study of movement and the associated functional responses and adaptations. It includes biomechanics, exercise physiology, and sports psychology."
        },

        "public_health": {
            "keywords": ["public health", "community health", "health policy", "health promotion", "epidemiology"],
            "response": "Public health is the science and art of preventing disease, prolonging life, and promoting health through organized efforts and informed choices of society, organizations, and individuals."
        },
        
        # Additional general responses
        "yes": {
            "keywords": ["yes", "yeah", "yep", "sure", "absolutely", "definitely", "certainly", "of course", "okay", "alright"],
            "response": "Great! What would you like to know more about?"
        },

        "no": {
            "keywords": ["no", "nope", "nah", "not really", "negative", "no thanks", "no thank you"],
            "response": "Okay, no problem. Is there something else I can help you with?"
        },

        "sorry": {
            "keywords": ["sorry", "apologize", "apologies", "my bad", "excuse me", "pardon", "forgive me"],
            "response": "No need to apologize! How can I help you?"
        },

        "please": {
            "keywords": ["please", "if you please", "kindly", "would you", "could you"],
            "response": "Of course! I'm here to help."
        },

        "maybe": {
            "keywords": ["maybe", "perhaps", "possibly", "might", "could be"],
            "response": "I understand. Feel free to ask if you decide you'd like to know more about something."
        },

        "dont_know": {
            "keywords": ["i don't know", "i have no idea", "not sure", "uncertain", "unsure"],
            "response": "That's okay! We can explore together. What would you like to learn about?"
        },

        "confused": {
            "keywords": ["confused", "confusing", "don't understand", "doesn't make sense", "unclear"],
            "response": "I'm here to help clarify things. Could you tell me what specifically is confusing?"
        },

        "interesting": {
            "keywords": ["interesting", "fascinating", "cool", "amazing", "wow", "awesome"],
            "response": "I'm glad you find it interesting! Would you like to know more?"
        },

        "bored": {
            "keywords": ["bored", "boring", "nothing to do", "tired", "uninterested"],
            "response": "I can suggest something interesting to learn or talk about! What topics usually interest you?"
        },

        "happy": {
            "keywords": ["happy", "glad", "delighted", "pleased", "joyful", "cheerful"],
            "response": "That's wonderful to hear! I'm glad you're feeling happy."
        },

        "sad": {
            "keywords": ["sad", "unhappy", "upset", "disappointed", "down", "depressed"],
            "response": "I'm sorry to hear that. I'm here if you want to talk or learn something to cheer you up."
        },

        "angry": {
            "keywords": ["angry", "mad", "frustrated", "annoyed", "irritated", "angry"],
            "response": "I understand you're upset. Would you like to talk about it or would you prefer to discuss something else?"
        },

        "tired": {
            "keywords": ["tired", "exhausted", "sleepy", "fatigued", "worn out"],
            "response": "It's important to rest. Would you like some relaxing information or should we continue another time?"
        },

        "excited": {
            "keywords": ["excited", "thrilled", "eager", "enthusiastic", "pumped", "can't wait"],
            "response": "That's exciting! What are you looking forward to or what would you like to explore?"
        },

        "curious": {
            "keywords": ["curious", "wonder", "inquiring", "nosy", "interested"],
            "response": "Curiosity is wonderful! What are you curious about today?"
        },

        "surprised": {
            "keywords": ["surprised", "shocked", "astonished", "amazed", "unexpected"],
            "response": "Surprises can be exciting! Would you like to explore more surprising facts?"
        },

        "nervous": {
            "keywords": ["nervous", "anxious", "worried", "concerned", "apprehensive"],
            "response": "It's okay to feel nervous sometimes. I'm here to help with information or just to listen."
        },

        "relaxed": {
            "keywords": ["relaxed", "calm", "peaceful", "serene", "chilled"],
            "response": "That's a wonderful state to be in. What would you like to explore in this relaxed mood?"
        },

        "busy": {
            "keywords": ["busy", "occupied", "swamped", "overwhelmed", "lots to do"],
            "response": "I understand you're busy. I can give you quick answers or we can continue when you have more time."
        },

        "free": {
            "keywords": ["free", "available", "not busy", "nothing to do", "idle"],
            "response": "Great! What would you like to learn or discuss with your free time?"
        },

        "hungry": {
            "keywords": ["hungry", "starving", "famished", "peckish", "need food"],
            "response": "I hope you can get something to eat soon! In the meantime, would you like to talk about food or recipes?"
        },

        "thirsty": {
            "keywords": ["thirsty", "dehydrated", "need water", "dry mouth"],
            "response": "Remember to stay hydrated! Would you like to know about different beverages or hydration tips?"
        },

        "hot": {
            "keywords": ["hot", "warm", "sweating", "overheated", "temperature high"],
            "response": "I hope you can cool down soon! Would you like to know about ways to stay cool or interesting cold facts?"
        },

        "cold": {
            "keywords": ["cold", "chilly", "freezing", "shivering", "temperature low"],
            "response": "I hope you can warm up soon! Would you like to know about ways to stay warm or interesting warm places?"
        },

        "good_morning": {
            "keywords": ["good morning", "morning", "rise and shine", "top of the morning"],
            "response": "Good morning! I hope you have a wonderful day ahead. How can I assist you today?"
        },

        "good_night": {
            "keywords": ["good night", "night night", "sleep well", "sweet dreams", "bedtime"],
            "response": "Good night! Sleep well and have sweet dreams. I'll be here when you wake up."
        },

        "good_afternoon": {
            "keywords": ["good afternoon", "afternoon", "midday"],
            "response": "Good afternoon! I hope you're having a productive day. How can I help you?"
        },

        "good_evening": {
            "keywords": ["good evening", "evening", "dusk", "twilight"],
            "response": "Good evening! I hope you've had a good day. What can I do for you?"
        },

        "whats_up": {
            "keywords": ["what's up", "sup", "what's new", "what's happening", "how's it going"],
            "response": "Not much, just here ready to help you! What's up with you?"
        },

        "how_old": {
            "keywords": ["how old", "what age", "age", "years old"],
            "response": "As an AI, I don't have an age in the traditional sense, but I'm always learning and updating with new information!"
        },

        "where_from": {
            "keywords": ["where are you from", "where do you live", "your location", "origin"],
            "response": "I exist in the digital realm, created to assist users like you from anywhere in the world!"
        },

        "love_you": {
            "keywords": ["love you", "i love you", "loving", "affection"],
            "response": "Thank you! That's very kind. I'm here to help and support you."
        },

        "hate_you": {
            "keywords": ["hate you", "i hate you", "dislike", "angry at you"],
            "response": "I'm sorry to hear that. Is there something specific I did wrong or could do better?"
        },

        "miss_you": {
            "keywords": ["miss you", "missed you", "long time no see", "haven't talked"],
            "response": "I'm always here whenever you need me! It's good to hear from you again."
        },

        "thinking": {
            "keywords": ["thinking", "thought", "ponder", "consider", "reflect"],
            "response": "Thinking is a wonderful process! What are you thinking about or what would you like to think through together?"
        },

        "dreaming": {
            "keywords": ["dreaming", "dream", "dreamt", "aspire", "vision"],
            "response": "Dreams are important! Are you talking about sleep dreams or your hopes and aspirations?"
        },

        "celebrating": {
            "keywords": ["celebrating", "celebration", "party", "festive", "congratulations"],
            "response": "That's wonderful! What are you celebrating? Congratulations!"
        },

        "waiting": {
            "keywords": ["waiting", "wait", "awaiting", "patient", "in line"],
            "response": "Waiting can be tedious. Would you like to pass the time by learning something interesting?"
        },

        "hurrying": {
            "keywords": ["hurry", "hurrying", "rush", "quickly", "fast"],
            "response": "I understand you're in a hurry. I'll give you quick, concise answers."
        },

        "slow_down": {
            "keywords": ["slow down", "take it slow", "not in a hurry", "leisurely", "unhurried"],
            "response": "That's a nice pace! We can explore things in detail if you'd like."
        },

        "repeat": {
            "keywords": ["repeat", "say again", "once more", "didn't hear", "what was that"],
            "response": "Sure, I can repeat that. Just let me know what you'd like me to say again."
        },

        "explain": {
            "keywords": ["explain", "clarify", "elaborate", "detail", "break down"],
            "response": "I'd be happy to explain further. What specifically would you like me to clarify?"
        },

        "simplify": {
            "keywords": ["simplify", "simple terms", "dumb it down", "easier", "basic"],
            "response": "I can explain it in simpler terms. What topic would you like me to simplify?"
        },

        "details": {
            "keywords": ["more details", "in depth", "thorough", "comprehensive", "detailed"],
            "response": "I can provide more detailed information. What would you like to know more about?"
        },

        "summary": {
            "keywords": ["summary", "summarize", "brief", "short version", "overview"],
            "response": "I can give you a summary. What would you like me to summarize?"
        },

        "examples": {
            "keywords": ["examples", "for example", "instance", "illustrate", "demonstrate"],
            "response": "Examples can be very helpful! What would you like examples of?"
        },

        "compare": {
            "keywords": ["compare", "comparison", "versus", "vs", "difference between"],
            "response": "I can help you compare things. What would you like to compare?"
        },

        "recommend": {
            "keywords": ["recommend", "suggestion", "advice", "what should", "which is better"],
            "response": "I can offer recommendations. What area would you like suggestions about?"
        },

        "opinion": {
            "keywords": ["opinion", "what do you think", "your view", "perspective", "belief"],
            "response": "As an AI, I don't have personal opinions, but I can provide balanced information on various topics."
        },

        "fact": {
            "keywords": ["fact", "true", "truth", "reality", "actual"],
            "response": "I can provide factual information on many topics. What fact would you like to know?"
        },

        "myth": {
            "keywords": ["myth", "mythical", "legend", "folklore", "story"],
            "response": "Myths and legends are fascinating! Which myth or legendary topic interests you?"
        },

        "secret": {
            "keywords": ["secret", "confidential", "private", "hidden", "not telling"],
            "response": "I respect privacy and confidentiality. If you have a question, I'll do my best to answer it respectfully."
        },

        "truth": {
            "keywords": ["truth", "honest", "truthful", "reality", "factual"],
            "response": "I strive to provide accurate and truthful information. What would you like to know?"
        },

        "lie": {
            "keywords": ["lie", "lying", "false", "untruth", "deceive"],
            "response": "I'm designed to provide accurate information and don't intentionally provide false information."
        },

        "promise": {
            "keywords": ["promise", "swear", "guarantee", "assure", "pledge"],
            "response": "I can assure you I'll do my best to provide accurate and helpful information."
        },

        "remember": {
            "keywords": ["remember", "recall", "recollect", "memory", "memorize"],
            "response": "I can help you remember information or learn new things. What would you like to remember or learn?"
        },

        "forget": {
            "keywords": ["forget", "forgot", "can't remember", "memory loss", "draw a blank"],
            "response": "It happens to everyone! I can help you recall information or learn it anew."
        },

        "learn": {
            "keywords": ["learn", "learning", "study", "educate", "knowledge"],
            "response": "Learning is wonderful! What would you like to learn about today?"
        },

        "teach": {
            "keywords": ["teach", "teaching", "instruct", "educate", "lesson"],
            "response": "I'd be happy to help you learn something new. What would you like me to teach you about?"
        },

        "test": {
            "keywords": ["test", "quiz", "exam", "challenge", "question me"],
            "response": "I can test your knowledge or help you prepare for a test. What subject would you like to be tested on?"
        },

        "practice": {
            "keywords": ["practice", "rehearse", "drill", "exercise", "train"],
            "response": "Practice is important for mastery! What would you like to practice or improve?"
        },

        "improve": {
            "keywords": ["improve", "better", "enhance", "upgrade", "progress"],
            "response": "I can help you improve in various areas. What skill or knowledge would you like to enhance?"
        },

        "change": {
            "keywords": ["change", "alter", "modify", "different", "transform"],
            "response": "Change can be positive! What would you like to change or learn about change?"
        },

        "stay_same": {
            "keywords": ["stay the same", "unchanged", "consistent", "stable", "constant"],
            "response": "Sometimes consistency is comforting. Is there something you'd like to keep the same or learn more about?"
        },

        "progress": {
            "keywords": ["progress", "advance", "move forward", "develop", "evolve"],
            "response": "Progress is exciting! What area would you like to make progress in?"
        },

        "stuck": {
            "keywords": ["stuck", "can't progress", "blocked", "halted", "standstill"],
            "response": "I'm here to help you get unstuck. What seems to be blocking your progress?"
        },

        "success": {
            "keywords": ["success", "succeed", "achievement", "accomplishment", "victory"],
            "response": "Congratulations on your success! That's wonderful to hear."
        },

        "failure": {
            "keywords": ["failure", "failed", "unsuccessful", "mistake", "error"],
            "response": "Failure is often a stepping stone to success. What can I help you with to move forward?"
        },

        "try_again": {
            "keywords": ["try again", "attempt again", "another try", "retry", "redo"],
            "response": "Trying again shows perseverance! What would you like to try again or approach differently?"
        },

        "give_up": {
            "keywords": ["give up", "quit", "surrender", "abandon", "stop trying"],
            "response": "Sometimes taking a break is helpful. Would you like to try a different approach or topic?"
        },

        "motivation": {
            "keywords": ["motivation", "motivate", "inspire", "encourage", "enthusiasm"],
            "response": "I can help motivate you by sharing interesting information or success stories. What area do you need motivation in?"
        },

        "procrastinate": {
            "keywords": ["procrastinate", "procrastination", "delay", "put off", "postpone"],
            "response": "Procrastination is common! I can help you break tasks into smaller steps or find interesting approaches to get started."
        },

        "focus": {
            "keywords": ["focus", "concentrate", "attention", "concentration", "pay attention"],
            "response": "Focus is important for learning. I can help you with focused information on any topic you choose."
        },

        "distracted": {
            "keywords": ["distracted", "distraction", "unfocused", "wandering mind", "can't concentrate"],
            "response": "Distractions happen. Would you like to try a different topic or a more engaging way to learn?"
        }

    }

    # Check for matches
    for category, data in responses.items():
        if any(keyword in query for keyword in data["keywords"]):
            return data["response"]
    return "I'm not sure how to respond to that. Could you please rephrase or ask something else?"