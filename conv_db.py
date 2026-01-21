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

    # Default response if no match found
    return "I'm not sure I understand that. Could you please rephrase your question or ask about Alvas College, programming, electronics, or something else?"