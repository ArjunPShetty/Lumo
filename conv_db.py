def get_conversational_response(query):
    """Return conversational responses based on query."""
    query = query.lower().strip()

    # Define response categories
    responses = {
        # Greetings
        "greetings": {
            "keywords": ["hi", "hello", "hey", "good morning", "good afternoon", "good evening", "greetings"],
            "response": "Hello! How can I help you today?"
        },

        # Farewells
        "farewells": {
            "keywords": ["bye", "goodbye", "see you", "exit", "quit", "farewell"],
            "response": "Goodbye! Have a nice day!"
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

        # Entertainment
        "joke": {
            "keywords": ["joke", "funny", "laugh"],
            "response": "Why don't scientists trust atoms? Because they make up everything!"
        },

        "another_joke": {
            "keywords": ["another joke", "more jokes"],
            "response": "Why did the computer go to the doctor? Because it had a virus!"
        },

        # General conversation
        "weather": {
            "keywords": ["weather", "rain", "sunny", "temperature"],
            "response": "I'm sorry, I don't have access to current weather data. You might want to check a weather app or website for the latest information."
        },

        "time": {
            "keywords": ["time", "clock", "what time"],
            "response": "I'm afraid I don't have access to the current time. Please check your device's clock."
        },

        "help": {
            "keywords": ["help", "assist", "support"],
            "response": "I'm here to help! You can ask me about Alvas College, programming questions, electronics and communication topics, or just have a general conversation."
        },

        "about_user": {
            "keywords": ["about me", "who am i", "my name"],
            "response": "I'd love to know more about you! What's your name or what would you like to talk about?"
        },

        "hobbies": {
            "keywords": ["hobby", "hobbies", "interests", "like to do"],
            "response": "I enjoy helping people learn and providing information! What are your hobbies?"
        },

        "food": {
            "keywords": ["food", "eat", "hungry", "restaurant", "cuisine"],
            "response": "Food is wonderful! What's your favorite cuisine or dish?"
        },

        "sports": {
            "keywords": ["sports", "game", "football", "cricket", "basketball"],
            "response": "Sports are exciting! Which sports do you enjoy watching or playing?"
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

        # Programming Questions
        "programming": {
            "keywords": ["programming", "coding", "code"],
            "response": "Programming is the process of creating instructions for computers to follow. What specific programming language or concept would you like to know about?"
        },

        "python": {
            "keywords": ["python", "python programming"],
            "response": "Python is a high-level, interpreted programming language known for its simplicity and readability. It's great for beginners and used in web development, data science, AI, and more."
        },

        "java": {
            "keywords": ["java", "java programming"],
            "response": "Java is an object-oriented programming language known for its 'write once, run anywhere' capability. It's widely used for enterprise applications, Android development, and web applications."
        },

        "cpp": {
            "keywords": ["c++", "cpp", "c plus plus"],
            "response": "C++ is a powerful, high-performance programming language that extends C with object-oriented features. It's commonly used for system programming, game development, and performance-critical applications."
        },

        "javascript": {
            "keywords": ["javascript", "js", "node.js"],
            "response": "JavaScript is a versatile programming language primarily used for web development. It runs in browsers and can also be used server-side with Node.js."
        },

        "algorithms": {
            "keywords": ["algorithm", "algorithms", "data structure"],
            "response": "Algorithms are step-by-step procedures for solving problems. Common types include sorting algorithms (bubble sort, quick sort), searching algorithms (binary search), and graph algorithms."
        },

        "variables": {
            "keywords": ["variable", "variables", "data types"],
            "response": "Variables are containers for storing data values. In programming, they have names and can hold different types of data like numbers, strings, or objects."
        },

        "loops": {
            "keywords": ["loop", "loops", "for loop", "while loop"],
            "response": "Loops are programming constructs that repeat a block of code. Common types are 'for' loops (when you know how many times to repeat) and 'while' loops (when you repeat until a condition is met)."
        },

        "functions": {
            "keywords": ["function", "functions", "methods"],
            "response": "Functions are reusable blocks of code that perform specific tasks. They help organize code, avoid repetition, and make programs more modular."
        },

        # Electronics and Communication Questions
        "electronics": {
            "keywords": ["electronics", "electronic", "circuit"],
            "response": "Electronics is the branch of physics and engineering that deals with the flow of electrons in circuits and devices. What specific topic would you like to know about?"
        },

        "communication": {
            "keywords": ["communication", "telecommunication", "signal"],
            "response": "Communication engineering deals with the transmission of information through various mediums. This includes wired and wireless communication systems."
        },

        "transistor": {
            "keywords": ["transistor", "transistors"],
            "response": "A transistor is a semiconductor device used to amplify or switch electronic signals. There are BJTs (Bipolar Junction Transistors) and MOSFETs (Metal-Oxide-Semiconductor Field-Effect Transistors)."
        },

        "resistor": {
            "keywords": ["resistor", "resistance"],
            "response": "A resistor is a passive electrical component that opposes the flow of current. It's measured in ohms (Ω) and used to control voltage and current in circuits."
        },

        "capacitor": {
            "keywords": ["capacitor", "capacitance"],
            "response": "A capacitor is an electronic component that stores electrical energy in an electric field. It's measured in farads (F) and used in filtering, timing, and energy storage applications."
        },

        "inductor": {
            "keywords": ["inductor", "inductance"],
            "response": "An inductor is a passive electrical component that stores energy in a magnetic field when current flows through it. It's measured in henries (H) and used in filters and transformers."
        },

        "diode": {
            "keywords": ["diode", "diodes"],
            "response": "A diode is a semiconductor device that allows current to flow in one direction only. Common types include rectifier diodes, Zener diodes, and LEDs (Light Emitting Diodes)."
        },

        "microcontroller": {
            "keywords": ["microcontroller", "arduino", "raspberry pi"],
            "response": "A microcontroller is a small computer on a single integrated circuit containing a processor core, memory, and programmable input/output peripherals. Arduino and Raspberry Pi are popular microcontroller platforms."
        },

        "antenna": {
            "keywords": ["antenna", "antennas"],
            "response": "An antenna is a device that converts electrical signals into electromagnetic waves for transmission, or vice versa for reception. Different types include dipole, Yagi, and parabolic antennas."
        },

        "modulation": {
            "keywords": ["modulation", "am", "fm", "pm"],
            "response": "Modulation is the process of varying a carrier signal to encode information. Common types include Amplitude Modulation (AM), Frequency Modulation (FM), and Phase Modulation (PM)."
        },

        "fiber_optics": {
            "keywords": ["fiber optics", "optical fiber", "fiber optic"],
            "response": "Fiber optics uses light to transmit data through thin glass or plastic fibers. It's used for high-speed internet, telecommunications, and medical imaging due to its high bandwidth and low signal loss."
        },

        "satellite": {
            "keywords": ["satellite", "satellite communication"],
            "response": "Satellite communication uses artificial satellites to transmit signals over long distances. It's used for television broadcasting, internet services, GPS, and weather monitoring."
        },

        # NEW: Additional Engineering Topics
        "civil_engineering": {
            "keywords": ["civil engineering", "civil engineer", "construction engineering"],
            "response": "Civil engineering involves designing, constructing, and maintaining infrastructure like buildings, roads, bridges, and water supply systems."
        },

        "mechanical_engineering": {
            "keywords": ["mechanical engineering", "mechanical engineer", "thermodynamics"],
            "response": "Mechanical engineering deals with the design, analysis, manufacturing, and maintenance of mechanical systems, including engines, machines, and thermal systems."
        },

        "electrical_engineering": {
            "keywords": ["electrical engineering", "electrical engineer", "power systems"],
            "response": "Electrical engineering focuses on electricity, electronics, and electromagnetism, including power generation, transmission, and electrical machines."
        },

        "aerospace_engineering": {
            "keywords": ["aerospace engineering", "aerospace", "aircraft design"],
            "response": "Aerospace engineering involves the design and development of aircraft and spacecraft, including aerodynamics, propulsion systems, and materials science."
        },

        "chemical_engineering": {
            "keywords": ["chemical engineering", "chemical engineer", "process engineering"],
            "response": "Chemical engineering applies chemistry, physics, and mathematics to process raw materials into valuable products, including chemicals, fuels, and pharmaceuticals."
        },

        "biomedical_engineering": {
            "keywords": ["biomedical engineering", "biomedical", "medical devices"],
            "response": "Biomedical engineering combines engineering principles with medical sciences to design and create equipment, devices, and software used in healthcare."
        },

        # Programming Languages
        "c": {
            "keywords": ["c language", "c", "c programming", "c language basics"],
            "response": "C is a general-purpose programming language known for its efficiency and low-level access to memory. It's widely used in system programming and embedded systems."
        },

        "csharp": {
            "keywords": ["c#", "c sharp", "csharp programming"],
            "response": "C# (C Sharp) is a modern, object-oriented programming language developed by Microsoft, commonly used for Windows applications, game development with Unity, and web services."
        },

        "ruby": {
            "keywords": ["ruby", "ruby programming", "ruby on rails"],
            "response": "Ruby is a dynamic, open-source programming language focused on simplicity and productivity. It's often used with the Ruby on Rails framework for web development."
        },

        "swift": {
            "keywords": ["swift", "swift programming", "ios development"],
            "response": "Swift is a powerful and intuitive programming language developed by Apple for iOS, macOS, watchOS, and tvOS app development."
        },

        "kotlin": {
            "keywords": ["kotlin", "kotlin programming", "android kotlin"],
            "response": "Kotlin is a statically typed programming language that runs on the Java Virtual Machine. It's officially supported for Android development and known for its conciseness and safety."
        },

        "go_lang": {
            "keywords": ["go language", "golang", "go programming"],
            "response": "Go (or Golang) is an open-source programming language developed by Google, known for its simplicity, efficiency, and built-in support for concurrent programming."
        },

        "rust": {
            "keywords": ["rust", "rust programming", "rust language"],
            "response": "Rust is a systems programming language focused on safety, speed, and concurrency. It prevents segfaults and guarantees thread safety without a garbage collector."
        },

        "php": {
            "keywords": ["php", "php programming", "php web development"],
            "response": "PHP is a popular server-side scripting language designed for web development, often used with databases like MySQL to create dynamic websites."
        },

        # Advanced Programming Concepts
        "object_oriented": {
            "keywords": ["object oriented", "oop", "object oriented programming"],
            "response": "Object-Oriented Programming (OOP) is a programming paradigm based on objects containing data and methods. Key concepts include classes, objects, inheritance, polymorphism, and encapsulation."
        },

        "database": {
            "keywords": ["database", "sql", "database management"],
            "response": "A database is an organized collection of data stored and accessed electronically. SQL (Structured Query Language) is commonly used to manage relational databases."
        },

        "web_development": {
            "keywords": ["web development", "web developer", "frontend backend"],
            "response": "Web development involves creating websites and web applications. It includes frontend (client-side, like HTML/CSS/JavaScript) and backend (server-side, like Node.js, Python, PHP) development."
        },

        "machine_learning": {
            "keywords": ["machine learning", "ml", "ai ml"],
            "response": "Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience without explicit programming, using algorithms and statistical models."
        },

        "cloud_computing": {
            "keywords": ["cloud computing", "aws", "azure", "google cloud"],
            "response": "Cloud computing delivers computing services over the internet, including storage, processing, and databases. Popular providers are AWS, Microsoft Azure, and Google Cloud Platform."
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