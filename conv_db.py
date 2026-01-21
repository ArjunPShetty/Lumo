# conv_db.py
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

        # NEW: More Programming Languages
        "c_language": {
            "keywords": ["c language", "c programming", "c language basics"],
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

        # NEW: Advanced Programming Concepts
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

        # NEW: Geography and Countries
        "geography": {
            "keywords": ["geography", "geographical", "world geography"],
            "response": "Geography is the study of Earth's landscapes, environments, and the relationships between people and their environments. It includes physical and human geography."
        },

        "continents": {
            "keywords": ["continents", "how many continents", "list of continents"],
            "response": "There are 7 continents: Asia, Africa, North America, South America, Antarctica, Europe, and Australia (or Oceania)."
        },

        "india": {
            "keywords": ["india", "about india", "indian geography"],
            "response": "India is the seventh-largest country by area and the second-most populous country. It's located in South Asia with New Delhi as its capital, and has diverse cultures, languages, and landscapes."
        },

        "usa": {
            "keywords": ["usa", "united states", "america geography"],
            "response": "The United States of America (USA) is a country in North America with 50 states. Its capital is Washington D.C., and it's known for its diverse geography, economy, and cultural influence."
        },

        "china": {
            "keywords": ["china", "about china", "chinese geography"],
            "response": "China is the world's most populous country, located in East Asia. Its capital is Beijing, and it's known for the Great Wall, diverse landscapes, and rapid economic growth."
        },

        "europe": {
            "keywords": ["europe", "european countries", "europe geography"],
            "response": "Europe is a continent located entirely in the Northern Hemisphere, with 44 countries. It's known for its rich history, diverse cultures, and landmarks like the Eiffel Tower and Colosseum."
        },

        "africa": {
            "keywords": ["africa", "african continent", "africa geography"],
            "response": "Africa is the second-largest continent by area and population. It's known for its biodiversity, the Sahara Desert, the Nile River, and diverse cultures across 54 countries."
        },

        # NEW: World Facts
        "world_population": {
            "keywords": ["world population", "global population", "how many people"],
            "response": "The world population is over 8 billion people as of 2023, with Asia being the most populous continent."
        },

        "earth_facts": {
            "keywords": ["earth", "planet earth", "about earth"],
            "response": "Earth is the third planet from the Sun and the only known celestial body to support life. It has an atmosphere composed mainly of nitrogen and oxygen, and about 71% of its surface is covered by water."
        },

        "solar_system": {
            "keywords": ["solar system", "planets", "sun and planets"],
            "response": "The solar system consists of the Sun and eight planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. It also includes dwarf planets like Pluto, asteroids, and comets."
        },

        "oceans": {
            "keywords": ["oceans", "world oceans", "five oceans"],
            "response": "There are five oceans: Pacific Ocean (largest), Atlantic Ocean, Indian Ocean, Southern Ocean, and Arctic Ocean (smallest)."
        },

        "mountains": {
            "keywords": ["mountains", "highest mountain", "mountain ranges"],
            "response": "Mount Everest in the Himalayas is the highest mountain above sea level at 8,848 meters. Other major ranges include the Andes, Rockies, and Alps."
        },

        # NEW: Semiconductors (Detailed)
        "semiconductor_basics": {
            "keywords": ["semiconductor", "semiconductors", "what is semiconductor"],
            "response": "Semiconductors are materials with electrical conductivity between conductors (like metals) and insulators (like ceramics). Silicon is the most commonly used semiconductor in electronics."
        },

        "silicon": {
            "keywords": ["silicon", "silicon chip", "silicon wafer"],
            "response": "Silicon is a chemical element widely used in semiconductors due to its stable crystal structure and ability to be doped with impurities to modify its electrical properties."
        },

        "doping": {
            "keywords": ["doping", "semiconductor doping", "n-type p-type"],
            "response": "Doping is the process of adding impurities to semiconductors to change their electrical properties. N-type doping adds electrons, while P-type doping creates holes (positive charge carriers)."
        },

        "pn_junction": {
            "keywords": ["pn junction", "p-n junction", "junction diode"],
            "response": "A PN junction is formed by joining P-type and N-type semiconductors. It allows current to flow in one direction, forming the basis of diodes and other semiconductor devices."
        },

        "ic": {
            "keywords": ["integrated circuit", "ic", "microchip"],
            "response": "An integrated circuit (IC) is a set of electronic circuits on a small chip of semiconductor material, typically silicon. ICs are used in virtually all electronic devices today."
        },

        "vlsi": {
            "keywords": ["vlsi", "very large scale integration", "vlsi design"],
            "response": "VLSI (Very Large Scale Integration) is the process of creating integrated circuits by combining thousands or millions of transistors into a single chip."
        },

        "semiconductor_manufacturing": {
            "keywords": ["semiconductor manufacturing", "chip fabrication", "semiconductor process"],
            "response": "Semiconductor manufacturing involves designing and fabricating ICs through processes like photolithography, etching, doping, and packaging in cleanroom environments."
        },

        # NEW: Science Topics
        "physics": {
            "keywords": ["physics", "laws of physics", "quantum physics"],
            "response": "Physics is the natural science that studies matter, energy, motion, and forces. It includes classical mechanics, electromagnetism, thermodynamics, and quantum mechanics."
        },

        "chemistry": {
            "keywords": ["chemistry", "chemical reactions", "organic chemistry"],
            "response": "Chemistry studies the composition, structure, properties, and changes of matter. It includes organic, inorganic, physical, and analytical chemistry."
        },

        "biology": {
            "keywords": ["biology", "life science", "cell biology"],
            "response": "Biology is the study of living organisms and their structure, function, growth, evolution, and distribution. It includes botany, zoology, genetics, and ecology."
        },

        "mathematics": {
            "keywords": ["mathematics", "math", "calculus algebra"],
            "response": "Mathematics is the study of numbers, quantities, shapes, and patterns. It includes arithmetic, algebra, geometry, calculus, and statistics."
        },

        # NEW: Current Technologies
        "ai": {
            "keywords": ["artificial intelligence", "ai", "what is ai"],
            "response": "Artificial Intelligence (AI) refers to machines or software that mimic human intelligence, including learning, reasoning, and problem-solving. Applications include chatbots, image recognition, and autonomous vehicles."
        },

        "blockchain": {
            "keywords": ["blockchain", "bitcoin", "cryptocurrency"],
            "response": "Blockchain is a decentralized digital ledger that records transactions across many computers. It's the technology behind cryptocurrencies like Bitcoin and has applications in finance, supply chain, and more."
        },

        "iot": {
            "keywords": ["iot", "internet of things", "smart devices"],
            "response": "The Internet of Things (IoT) refers to interconnected devices that communicate over the internet, such as smart home devices, wearables, and industrial sensors."
        },

        "5g": {
            "keywords": ["5g", "5g technology", "fifth generation"],
            "response": "5G is the fifth generation of cellular network technology, offering faster speeds, lower latency, and greater capacity than 4G, enabling advancements in IoT, autonomous vehicles, and telemedicine."
        },

        "quantum_computing": {
            "keywords": ["quantum computing", "quantum computer", "qubit"],
            "response": "Quantum computing uses quantum-mechanical phenomena like superposition and entanglement to perform computations. It has potential to solve problems that are intractable for classical computers."
        },

        # Additional general responses
        "yes": {
            "keywords": ["yes", "yeah", "yep", "sure"],
            "response": "Great! What would you like to know more about?"
        },

        "no": {
            "keywords": ["no", "nope", "nah"],
            "response": "Okay, no problem. Is there something else I can help you with?"
        },

        "sorry": {
            "keywords": ["sorry", "apologize"],
            "response": "No need to apologize! How can I help you?"
        },

        "please": {
            "keywords": ["please"],
            "response": "Of course! I'm here to help."
        }
    }

    # Check for matches
    for category, data in responses.items():
        if any(keyword in query for keyword in data["keywords"]):
            return data["response"]
    return "I'm not sure how to respond to that. Could you please rephrase or ask something else?"