import pandas as pd
from sklearn.model_selection import train_test_split
import random

def generate_email_subjects(num_subjects, categories, keywords):
    subjects = []
    labels = []

    for _ in range(num_subjects):
        category = random.choice(categories)
        keyword = random.choice(keywords[category])

        if random.random() < 0.5:
            keyword = random.choice(keywords[category])

        noise_options = ["", "special offer ", "limited time ", "exclusive ", "flash sale ", "save now ", "hot deal ", "last chance "]
        noise = random.choice(noise_options)

        punctuation_options = ["", "!", "?", "!!", "?!"]
        punctuation = random.choice(punctuation_options)

        action_words = ["", 'update', 'announcement', 'news', 'opportunity', 'alert', 'reminder', 'discount', 'new arrival', 'sale']
        action_word = random.choice(action_words)

        subject = f"{noise}{keyword} {action_word}{punctuation}".capitalize()

        structure_choices = [f"{keyword} {action_word}{punctuation}",
                             f"{action_word.capitalize()}! {keyword} {punctuation}",
                             f"{action_word.capitalize()} {keyword.capitalize()} {punctuation}",
                             f"{noise}{keyword} {action_word.capitalize()} {punctuation}",
                             f"{noise}{keyword.capitalize()}! {action_word.capitalize()} {punctuation}"]

        if random.random() < 0.2:
            subject = f"{keyword.capitalize()} {action_word}{punctuation}"

        subject = random.choice(structure_choices)

        if random.random() < 0.25:
            subject = f"Attention: {subject}"

        if random.random() < 0.15:
            subject = f"URGENT: {subject}"

        if random.random() < 0.1:
            subject = f"IMPORTANT: {subject}"

        if random.random() < 0.2:
            emoji_options = ["", "🔥", "💥", "🌟", "🚀", "🎉", "🔔", "❗", "✨", "💰", "📢"]
            emoji = random.choice(emoji_options)
            subject = f"{subject} {emoji}"

        subjects.append(subject)
        labels.append(category)

    return subjects, labels

categories = ["Technology", "Health", "Finance", "Travel", "Food",
              "Fashion", "Sports", "Education", "Entertainment", "Science",
              "Art", "Business", "Music", "Fitness", "Home",
              "Gaming", "Environment", "Books", "Pets", "Movies",
              "Automotive", "Social Media", "Career", "Shopping", "Weather",
              "Nature", "DIY and Crafts", "Travel Planning", "Mindfulness", "Space and Astronomy", 
              "Fashion Sustainability", "Cybersecurity", "Culinary Arts", "Virtual Reality", "Mind-Body Connection",
              "Artificial Intelligence", "Parenting", "Language and Linguistics", "Digital Marketing", "History and Archaeology",
              "Robotics", "Pop Science", "Alternative Energy", "Extreme Adventures", "Unexplained Phenomena",
              "Countries and Cultures", "Astrology and Horoscopes", "Futurism", "Outer Space", "Dreams and Dream Interpretation",
              "Aviation", "Personal Relationships", "Personal Interests", "Personal Finance", "Personal Development",
              "Volcanic & Seismic Activity", "Marriage & Love Life", "Food & Cooking"]

keywords = {
    "Technology": ["Innovation", "Gadgets", "Smartphones", "Artificial Intelligence", "Programming",
                   "Data Science", "Cloud Computing", "Cybersecurity", "Augmented Reality", "Virtual Reality",
                   "Blockchain", "Machine Learning", "Internet of Things", "Robotics", "Tech Startups",
                   "Mobile Apps", "Web Development", "Computer Vision", "Big Data", "Quantum Computing",
                   "IT Infrastructure", "Software Engineering", "Network Security", "Open Source",
                   "Digital Transformation"],

    "Health": ["Wellness", "Fitness", "Nutrition", "Medical", "Mental Health",
               "Dietary Supplements", "Healthy Recipes", "Well-being", "Weight Loss", "Exercise",
               "Alternative Medicine", "Healthcare Trends", "Medical Research", "Preventive Care", "Holistic Health",
               "Physical Therapy", "Healthy Lifestyle", "Mindfulness", "Yoga", "Counseling",
               "Vitamins", "Healthy Aging", "Self-care", "Health Technology", "Medical Innovations"],

    "Finance": ["Investment", "Budgeting", "Stock Market", "Financial Planning", "Cryptocurrency",
                "Personal Finance", "Retirement Planning", "Wealth Management", "Economic Trends", "Real Estate",
                "Credit Management", "Savings Tips", "Financial Education", "Insurance", "Tax Planning",
                "Fintech", "Global Markets", "Entrepreneurial Finance", "Financial Literacy", "Asset Allocation",
                "Market Analysis", "Blockchain in Finance", "Peer-to-peer Lending", "Credit Cards", "Robo-Advisors"],

    "Travel": ["Destinations", "Vacation Deals", "Adventure", "Travel Tips", "Hotels",
               "Cruises", "Budget Travel", "Solo Travel", "Family Vacations", "Luxury Travel",
               "Cultural Experiences", "Beach Resorts", "Mountain Retreats", "City Breaks", "Historical Sites",
               "Travel Gadgets", "Airfare Discounts", "Travel Safety", "Food Tourism", "Travel Apps",
               "Ecotourism", "Road Trips", "Backpacking", "Travel Insurance", "Digital Nomad Lifestyle"],

    "Food": ["Recipes", "Cuisine", "Cooking Tips", "Food Trends", "Restaurant Reviews",
             "Healthy Eating", "Vegetarian & Vegan", "International Flavors", "Desserts", "Beverages",
             "Gourmet Cooking", "Quick Meals", "Food Photography", "Kitchen Gadgets", "Meal Prep",
             "Farm-to-Table", "Local Ingredients", "Street Food", "BBQ & Grilling", "Cookbook Recommendations",
             "Food Festivals", "Wine & Spirits", "Coffee Culture", "Dining Etiquette", "Food History"],

    "Fashion": ["Style Tips", "Trends", "Fashion Shows", "Shopping Deals", "Accessories",
                "Designer Spotlights", "Street Fashion", "Sustainable Fashion", "Vintage Finds", "Seasonal Fashion",
                "Beauty Tips", "Makeup Trends", "Hairstyle Ideas", "Fashion Influencers", "Fashion Photography",
                "Celebrity Fashion", "DIY Fashion", "Luxury Brands", "Fashion Events", "Fashion History",
                "Online Shopping", "Thrift Store Finds", "Fashion for All Body Types", "Fashion and Technology",
                "Workplace Fashion"],

    "Sports": ["Games", "Scores", "Athlete Interviews", "Training Tips", "Sports Events",
               "Team Sports", "Extreme Sports", "Fitness Challenges", "Sports Gear", "Fan Experience",
               "Olympic Games", "Athletics", "Sports Medicine", "Outdoor Adventures", "Sports Psychology",
               "E-sports", "Youth Sports", "Sports Nutrition", "Sports Betting", "Behind the Scenes",
               "Athlete Profiles", "Sports Science", "Motorsports", "Sports Business", "Inspirational Sports Stories"],

    "Education": ["Learning Resources", "Study Tips", "Online Courses", "Education Technology", "Student Life",
                  "STEM Education", "Language Learning", "Study Abroad", "Career Development", "Educational Apps",
                  "E-learning Platforms", "Teaching Strategies", "College Life", "Literacy Programs",
                  "Learning Disabilities",
                  "Educational Events", "Teacher Spotlights", "Parental Involvement", "MOOCs", "Educational Podcasts",
                  "Edutainment", "Virtual Classrooms", "Education Policy", "Educational Psychology", "Art Education"],

    "Entertainment": ["Celebrity News", "Movie Reviews", "TV Shows", "Concerts", "Events",
                      "Award Shows", "Red Carpet Fashion", "Celebrity Interviews", "Film Festivals",
                      "Entertainment Industry",
                      "Behind the Scenes", "Film Criticism", "Documentaries", "Musical Performances", "Cultural Events",
                      "Upcoming Releases", "Pop Culture", "Fan Theories", "Reality TV", "Streaming Services",
                      "Gaming Culture", "Comedy Shows", "Theater Productions", "Entertainment Technology", "Fan Clubs"],

    "Science": ["Discoveries", "Research", "Space Exploration", "Innovation", "Environmental Science",
                "Biotechnology", "Scientific Breakthroughs", "Astronomy", "Physics", "Chemistry",
                "Biology", "Geology", "Climate Science", "Medical Research", "Scientific Ethics",
                "Robotics", "Oceanography", "Neuroscience", "Genetics", "Paleontology",
                "Scientific Experiments", "Science Communication", "Science History", "Women in Science",
                "Data Science"],

    "Art": ["Gallery Exhibitions", "Artists Spotlight", "Art Critiques", "Art Auctions", "Creative Inspiration",
            "Contemporary Art", "Classical Art", "Street Art", "Digital Art", "Sculpture",
            "Art Installations", "Art and Technology", "Art Restoration", "Art Movements", "Art History",
            "Art Collecting", "Public Art", "Performance Art", "Mixed Media", "Cultural Heritage",
            "Art Education", "Art Therapy", "Art Fairs", "Art and Society", "Artistic Expression"],

    "Business": ["Entrepreneurship", "Startups", "Business Trends", "Leadership", "Corporate News",
                 "Business Strategy", "Innovation in Business", "Marketing Strategies", "Finance in Business",
                 "Social Responsibility",
                 "Small Business Tips", "Global Business", "E-commerce", "Supply Chain Management",
                 "Customer Experience",
                 "Business Technology", "Entrepreneurial Mindset", "Workplace Culture", "Business Ethics",
                 "Success Stories",
                 "Business Networking", "Corporate Social Media", "Investor Relations", "Business Analysis",
                 "Future of Work"],

    "Music": ["New Releases", "Concerts", "Music Festivals", "Artist Interviews", "Music Genres",
              "Music Reviews", "Album Recommendations", "Music History", "Local Music Scene", "Classical Music",
              "Indie Music", "Music Production", "Songwriting", "Music Education", "Musical Instruments",
              "Live Performances", "Music Technology", "Music and Culture", "Music and Mental Health", "Music Business",
              "Music Discoveries", "Soundtracks", "Favorite Playlists", "Music Festivals", "International Music"],

    "Fitness": ["Workouts", "Training Programs", "Nutrition Tips", "Fitness Challenges", "Healthy Living",
                "Yoga", "Cardio Workouts", "Strength Training", "Mental Fitness", "Outdoor Fitness",
                "Fitness Gear", "Athlete Spotlights", "Fitness Trends", "Group Fitness", "Crossfit",
                "Mind-body Exercises", "Recovery Techniques", "Fitness Technology", "Wellness Retreats",
                "Holistic Fitness",
                "Healthy Recipes", "Fitness Competitions", "Fitness for Beginners", "Senior Fitness", "Fitness Apps"],

    "Home": ["Interior Design", "Home Improvement", "Organizing Tips", "DIY Projects", "Decor Ideas",
             "Home Maintenance", "Smart Home Technology", "Gardening", "Sustainable Living", "Pet-friendly Homes",
             "Home Office Ideas", "House Tours", "Home Decor Trends", "Home Renovations", "Furniture Design",
             "Kitchen Design", "Bathroom Ideas", "Bedroom Makeovers", "Outdoor Living", "Home Energy Efficiency",
             "Home Security", "Real Estate Tips", "Apartment Living", "Home Buying Guide", "Home Entertainment"],

    "Gaming": ["Video Game News", "Game Reviews", "Gaming Events", "Tips and Cheats", "Gaming Hardware",
               "Esports", "Gaming Communities", "Game Development", "Virtual Reality Games", "Mobile Gaming",
               "PC Gaming", "Console Gaming", "Gaming Industry", "Game Design", "Gaming Culture",
               "Streaming Games", "Retro Gaming", "Indie Games", "Gaming Technology", "Gaming Tournaments",
               "Game Collecting", "Gaming Conventions", "Online Multiplayer Games", "Gaming Accessories",
               "Gaming Merchandise"],

    "Environment": ["Climate Change", "Conservation", "Green Living", "Environmental Activism",
                    "Eco-friendly Practices",
                    "Sustainable Development", "Renewable Energy", "Waste Reduction", "Biodiversity",
                    "Wildlife Conservation",
                    "Ocean Conservation", "Air Quality", "Environmental Education", "Zero Waste Lifestyle",
                    "Carbon Footprint",
                    "Eco-friendly Technology", "Green Architecture", "Permaculture", "Environmental Justice",
                    "Sustainable Fashion",
                    "Environmental Policies", "Eco-tourism", "Water Conservation", "Green Products",
                    "Circular Economy"],

    "Books": ["Book Recommendations", "Author Interviews", "Book Reviews", "Literary Events", "Reading Lists",
              "Classic Literature", "Contemporary Fiction", "Mystery and Thrillers", "Science Fiction", "Fantasy",
              "Non-fiction", "Biographies", "Book Club Discussions", "Children's Books", "Young Adult Fiction",
              "Science Fiction", "Fantasy", "Biography/Memoir", "Young Adult", "Historical Fiction", "Poetry", "Book Adaptations", "Book Festivals", "Writing Tips", "Bookstores",
    "Publishing Industry", "Literary Awards", "Book Trends", "Reading Habits", "Book News"],

    "Pets": ["Pet Care Tips", "Pet Adoption", "Animal Welfare", "Pet Health", "Cute Pet Stories",
             "Pet Training", "Pet Products", "Pet Grooming", "Pet Behavior", "Pet Insurance",
             "Exotic Pets", "Pet-friendly Travel", "Wildlife", "Animal Companionship", "Pet Photography",
             "Famous Pets", "Adorable Videos", "Pet-Friendly Events", "Pet Charity", "Pet Fashion",
             "Aquariums", "Zoos", "Bird Watching", "Reptiles", "Small Pets"],

    "Movies": ["Film Reviews", "Movie Trailers", "Actor Interviews", "Film Festivals", "Cinematic Trends",
               "Classic Films", "Blockbusters", "Indie Films", "Documentaries", "Animated Movies",
               "Cinematography", "Film Genres", "Movie Soundtracks", "Film Criticism", "Behind the Scenes",
               "Upcoming Releases", "Movie Theaters", "Streaming Platforms", "Film History", "Oscar Contenders",
               "Cult Classics", "Directors' Spotlight", "Film Industry News", "Movie Merchandise", "Movie Awards"],

    "Automotive": ["Car Reviews", "Auto Shows", "Driving Tips", "Automotive Technology", "Motorcycles",
                   "Electric Vehicles", "Concept Cars", "Luxury Cars", "Classic Cars", "Auto Racing",
                   "SUVs", "Trucks", "Car Maintenance", "Road Safety", "Car Accessories",
                   "Hybrid Cars", "Fuel Efficiency", "Automotive Design", "Innovations in Vehicles", "Car Rentals",
                   "Vintage Cars", "Driverless Cars", "Traffic Updates", "Motor Shows", "Automotive Events"],

    "Social Media": ["Social Trends", "Platform Updates", "Influencer News", "Social Media Marketing", "Digital Culture",
                     "Content Creation", "Social Media Strategy", "Online Communities", "Social Impact", "Social Media and Business",
                     "Viral Content", "Digital Influencers", "User-generated Content", "Social Media Analytics", "Online Presence",
                     "Digital Marketing", "Tech and Social Media", "Privacy on Social Media", "Social Media for Small Businesses", "Social Media Campaigns",
                     "Social Media Psychology", "Social Media and Mental Health", "Emerging Platforms", "Social Media Trends", "Social Media Policies"],

    "Career": ["Job Opportunities", "Career Advice", "Professional Development", "Networking Tips", "Workplace Trends",
               "Remote Work", "Freelancing", "Job Interviews", "Resume Building", "Entrepreneurship",
               "Leadership", "Work-Life Balance", "Corporate Culture", "Career Transitions", "Success Stories",
               "Skill Development", "Job Search Strategies", "Career Fairs", "Salary Negotiation", "Workplace Productivity",
               "Diversity in the Workplace", "Employee Well-being", "Job Satisfaction", "Women in the Workplace", "Job Security"],

    "Shopping": ["Sales and Discounts", "Shopping Guides", "Fashion Deals", "Consumer Reviews", "Online Shopping",
                 "Retail Trends", "E-commerce", "Luxury Shopping", "Thrift Shopping", "Shopping for a Cause",
                 "Personal Styling", "Seasonal Sales", "Product Recommendations", "Gift Ideas", "Shopping Apps",
                 "Consumer Electronics", "Home Goods", "Beauty Products", "Gourmet Food", "Fashion Accessories",
                 "Shopping Hauls", "Sustainable Shopping", "Shopping on a Budget", "Shopping Destinations", "Shopping Events"],

    "Weather": ["Local Forecasts", "Seasonal Updates", "Weather Events", "Travel Advisories", "Climate Reports",
                "Natural Disasters", "Meteorology", "Climate Change", "Weather Phenomena", "Extreme Weather",
                "Weather Technology", "Weather Preparedness", "Weather and Health", "Global Weather Patterns", "Weather Photography",
                "Historical Weather Events", "Weather Apps", "Climate Action", "Weather and Agriculture", "Weather News",
                "Space Weather", "Weather Forecasting", "Weather and Tourism", "Weather Research", "Weather Monitoring"],
    
    "Nature": ["Biodiversity Conservation", "Wildlife Photography", "Nature Reserves", "Ecological Restoration", "Botany",
               "Natural Habitats", "Bird Watching", "Climate-friendly Gardening", "Eco-friendly Tourism", "Nature Walks",
               "Environmental Stewardship", "Conservation Organizations", "National Parks", "Nature Documentaries", "Ocean Exploration",
               "Biomes of the World", "Invasive Species Management", "Nature-inspired Art", "Nature Education", "Ecotourism",
               "Nature Poetry", "Ethical Wildlife Tourism", "Meteorological Phenomena", "Natural Resources", "Green Spaces"],

    "DIY and Crafts": ["DIY Home Decor", "Crafting Tutorials", "Upcycling Projects", "DIY Fashion", "Handmade Gifts",
                      "Crafting Materials", "DIY Beauty Products", "DIY Garden Projects", "Paper Crafts", "Knitting",
                      "DIY Tech Projects", "Jewelry Making", "DIY Pet Accessories", "Sewing Projects", "Woodworking",
                      "DIY Party Decorations", "DIY Photography Hacks", "Quilting", "Embroidery", "Candle Making",
                      "Pottery", "Scrapbooking", "DIY Kids Crafts", "Origami", "DIY Eco-friendly Solutions"],

    "Travel Planning": ["Travel Itineraries", "Budget Travel Tips", "Adventure Travel Planning", "Cultural Immersion", "Solo Travel Adventures",
                       "Family-Friendly Destinations", "Luxury Travel Experiences", "Travel Apps and Gadgets", "Travel Safety Tips", "Food Tourism",
                       "Digital Nomad Lifestyle", "Packing Hacks", "Travel Insurance Tips", "Hidden Gems", "Eco-friendly Travel", "Road Trip Essentials",
                       "Local Experiences", "Photography Expeditions", "Traveling with Pets", "Traveling on a Shoestring", "Group Travel Ideas",
                       "Cruise Vacations", "Winter Wonderland Travel", "Historical Journeys", "Voluntourism", "Traveling for Festivals"],

    "Mindfulness": ["Mindful Meditation", "Mindful Eating", "Mindful Parenting", "Mindful Workspaces", "Mindful Walking",
                    "Mindful Technology Use", "Mindful Relationships", "Mindful Breathing Exercises", "Mindful Journaling", "Mindfulness Retreats",
                    "Mindful Art Practices", "Mindfulness for Stress Reduction", "Mindful Communication", "Mindful Traveling", "Mindfulness in Education",
                    "Mindful Leadership", "Mindful Aging", "Mindful Sleep Practices", "Mindful Exercise", "Mindful Gardening",
                    "Mindfulness Apps", "Mindful Self-Compassion", "Mindfulness and Creativity", "Mindfulness in the Workplace", "Mindfulness for Anxiety"],

    "Space and Astronomy": ["Space Exploration", "Astronomy News", "Exoplanets", "Stargazing Tips", "Black Holes",
                           "Space Telescopes", "Astrophotography", "Cosmology", "Astronaut Biographies", "Space Missions",
                           "Mars Exploration", "Satellites", "Constellations", "Alien Life Search", "Space Agencies",
                           "Meteor Showers", "Space Colonization", "Asteroid Mining", "Galaxies", "Space Tourism",
                           "Lunar Exploration", "Astrobiology", "Space Weather", "Telescopes and Observatories", "Space Science for Kids"],

    "Fashion Sustainability": ["Ethical Fashion Brands", "Slow Fashion Movement", "Sustainable Textiles", "Eco-Friendly Fashion", "Circular Fashion",
                               "Fair Trade Fashion", "Upcycled Fashion", "Zero-Waste Fashion", "Vegan Fashion", "Sustainable Beauty Products",
                               "Environmental Impact of Fashion", "Sustainable Fashion Events", "Greenwashing in Fashion", "Sustainable Fashion Innovations", "Eco-Friendly Fabrics",
                               "Sustainable Jewelry", "Second-Hand Fashion", "Ethical Manufacturing Practices", "Sustainable Fashion Bloggers", "Sustainable Fashion for Kids",
                               "Sustainable Fashion Education", "Sustainable Fashion and Technology", "Carbon Neutral Fashion", "Biodegradable Fashion", "Sustainable Fashion Certification"],

    "Cybersecurity": ["Network Security", "Cyber Threat Intelligence", "Endpoint Security", "Incident Response", "Security Audits",
                      "Data Encryption", "Cloud Security", "Mobile Security", "Cybersecurity Best Practices", "Identity and Access Management",
                      "Penetration Testing", "Phishing Prevention", "Malware Analysis", "Security Compliance", "Cybersecurity Frameworks",
                      "Biometric Security", "Social Engineering", "Security Awareness Training", "Threat Hunting", "Zero Trust Security",
                      "Blockchain Security", "IoT Security Challenges", "Cryptocurrency Security", "Security Automation", "Cybersecurity Conferences"],

    "Culinary Arts": ["Culinary Techniques", "Gastronomy", "Culinary Schools", "International Cuisine", "Food Pairing",
                      "Culinary History", "Fine Dining Experiences", "Chef Profiles", "Farm-to-Table Movement", "Artisanal Foods",
                      "Culinary Tours", "Street Food Adventures", "Experimental Cooking", "Food and Wine Pairing", "Dessert Innovations",
                      "Food Photography Tips", "Gourmet Food Festivals", "Cooking Competitions", "Food Styling", "Culinary Science",
                      "Cheese and Wine Tasting", "Sustainable Agriculture in Culinary", "Food Preservation Techniques", "Fermentation", "Edible Flowers"],

    "Virtual Reality": ["VR Gaming", "Immersive Experiences", "VR Art", "Virtual Tours", "VR in Education",
                       "Healthcare Applications of VR", "VR Film-making", "VR Simulations", "Social VR", "VR Development",
                       "VR Hardware", "VR and Mental Health", "VR for Training", "360-degree Videos", "VR Therapy",
                       "VR Journalism", "VR in Real Estate", "VR for Architecture", "VR for Travel Exploration", "VR Accessibility",
                       "Augmented Reality vs Virtual Reality", "VR and Cognitive Enhancement", "VR and Social Interaction", "VR and Historical Recreation", "VR Fitness"],

    "Mind-Body Connection": ["Holistic Healing", "Mind-Body Exercises", "Energy Healing", "Chakra Balancing", "Acupuncture",
                             "Ayurvedic Medicine", "Tai Chi", "Qi Gong", "Reiki", "Meditation Practices",
                             "Mindful Movement", "Breathwork", "Yoga Philosophy", "Herbal Medicine", "Traditional Chinese Medicine",
                             "Sound Healing", "Holistic Nutrition", "Color Therapy", "Aromatherapy", "Holistic Psychotherapy",
                             "Mindfulness-Based Stress Reduction", "Mind-Body Medicine Research", "Spiritual Wellness", "Shamanic Healing", "Holistic Health Retreats"],
    
    "Artificial Intelligence": ["AI Ethics", "Explainable AI", "AI in Healthcare", "AI in Education", "Natural Language Processing",
                               "Computer Vision", "AI and Creativity", "Ethical AI Practices", "AI for Social Good", "AI Bias",
                               "AI in Business", "Automated Decision Making", "AI Governance", "AI in Robotics", "AI-driven Art",
                               "AI and Human Augmentation", "Quantum AI", "Neuromorphic Computing", "AI Research Advances", "AI and Privacy",
                               "AI and Cybersecurity", "AI for Accessibility", "AI Startups", "AI and Climate Change", "AI in Agriculture"],

    "Parenting": ["Positive Discipline", "Parenting Styles", "Child Development Milestones", "Parenting Hacks", "Balancing Work and Family",
                  "Effective Communication with Kids", "Teen Parenting Challenges", "Parenting Books", "Co-Parenting Strategies", "Single Parenting",
                  "Parenting Support Communities", "Parenting for Special Needs", "Mindful Parenting", "Parenting and Technology", "Parenting and Education",
                  "Family Bonding Activities", "Parenting and Mental Health", "Parenting Tips for Newborns", "Parenting Through Adolescence", "Parenting and Gender Roles",
                  "Parenting and Nutrition", "Parenting and Sleep", "Parenting and Creativity", "Parenting and Multiculturalism", "Parenting and Sports"],

    "Language and Linguistics": ["Language Learning Apps", "Multilingualism", "Language Preservation", "Linguistic Diversity", "Language Evolution",
                                "Applied Linguistics", "Language Teaching Methods", "Translation and Interpretation", "Computational Linguistics", "Sociolinguistics",
                                "Language Acquisition", "Bilingualism", "Sign Language", "Dialects and Accents", "Language and Culture", "Language and Identity",
                                "Neurolinguistics", "Linguistic Anthropology", "Language Revitalization", "Language Disorders", "Historical Linguistics", "Language and Technology",
                                "Language and Literature", "Language Standardization", "Language Policies", "Language in the Workplace", "Language and Cognitive Science"],

    "Digital Marketing": ["Content Marketing", "Social Media Advertising", "Search Engine Optimization (SEO)", "Email Marketing", "Influencer Marketing",
                         "Video Marketing", "Digital Marketing Analytics", "E-commerce Marketing", "Online Branding", "Marketing Automation",
                         "Data-driven Marketing", "Digital Marketing Trends", "Customer Relationship Management (CRM)", "Personalization in Marketing", "Mobile Marketing",
                         "Affiliate Marketing", "User-Generated Content", "Voice Search Optimization", "Interactive Content", "Chatbots in Marketing",
                         "Cross-channel Marketing", "Augmented Reality in Marketing", "Virtual Events in Marketing", "Marketing Funnels", "Retention Marketing",
                         "Behavioral Targeting", "Storytelling in Marketing", "Ethics in Digital Marketing", "Measuring ROI in Digital Marketing"],

    "History and Archaeology": ["Archaeological Discoveries", "Historical Figures", "Ancient Civilizations", "Historical Artifacts", "World History",
                               "Historical Architecture", "Military History", "Historical Events", "Historical Mysteries", "Archaeological Excavations",
                               "Cultural Heritage Preservation", "Paleontology", "History of Science", "Medieval History", "Renaissance History",
                               "Colonial History", "Industrial Revolution", "Modern History", "Women in History", "History of Exploration",
                               "Archaeological Techniques", "Historical Documentaries", "Revolutionary Movements", "Archaeogenetics", "Public History",
                               "Digital Archaeology", "Historical Preservation", "Archaeological Ethics", "History Education"],

    "Robotics": ["Robotics in Industry", "Humanoid Robots", "Medical Robotics", "Autonomous Vehicles", "Social Robots",
                 "Robotics and Artificial Intelligence", "Soft Robotics", "Swarm Robotics", "Robotic Process Automation", "Robotics in Education",
                 "Bio-inspired Robotics", "Robotics Ethics", "Robotic Surgery", "Exoskeletons", "Robotics for Space Exploration", "Military Robotics",
                 "Agricultural Robotics", "Underwater Robotics", "Drone Technology", "Human-Robot Interaction", "Robotics Research Advances",
                 "Robotics Competitions", "Robotic Prosthetics", "Robotics in Manufacturing", "Robotics for Disaster Response", "Robotics and Accessibility",
                 "Robotic Assisted Rehabilitation", "Robotic Toys and Gadgets", "Robotics in Sports"],

    "Pop Science": ["Science Explainers", "Fun Scientific Facts", "Science for Kids", "Scientific Debunking", "Pseudoscience Awareness",
                    "Scientific Curiosities", "Science and Everyday Life", "Citizen Science Projects", "Scientific Phenomena", "Unsolved Mysteries in Science",
                    "Science Communication", "Science Humor", "Science Podcasts", "Science and Philosophy", "Science Behind Movie Scenes",
                    "Scientific Innovations", "Science and Art Collaboration", "Science and Music", "Science Poetry", "Science and Creativity",
                    "Science Fiction and Reality", "Science Museums", "Science Cafés", "Scientific Mysteries", "Science and Spirituality",
                    "Science and Cultural Impact", "Science Journalism", "Science and Global Issues", "Scientific Outreach Programs"],

    "Alternative Energy": ["Renewable Energy Sources", "Solar Power", "Wind Energy", "Hydropower", "Geothermal Energy",
                          "Biomass Energy", "Tidal Energy", "Alternative Energy Storage", "Green Building", "Energy Efficiency",
                          "Sustainable Transportation", "Smart Grids", "Microgrids", "Energy Harvesting", "Energy Conservation",
                          "Hydrogen Energy", "Nuclear Fusion", "Wave Energy", "Solar Innovations", "Renewable Energy Policies",
                          "Sustainable Energy Financing", "Energy Transition", "Renewable Energy for Rural Areas", "Energy Independence", "Energy and Climate Change",
                          "Carbon Neutral Initiatives", "Renewable Energy Education", "Community Renewable Energy Projects", "Alternative Energy Research"],
    
    "Extreme Adventures": ["Extreme Sports", "Skydiving", "Base Jumping", "Rock Climbing", "Whitewater Rafting",
                          "Bungee Jumping", "Snowboarding", "Ice Climbing", "Cave Diving", "Paragliding",
                          "Free Solo Climbing", "Shark Cage Diving", "Volcano Boarding", "Sandboarding", "Wingsuit Flying",
                          "Big Wave Surfing", "Ice Cross Downhill", "Motocross Racing", "Parkour", "Ziplining",
                          "Heli-Skiing", "Bull Riding", "Cliff Diving", "Windsurfing", "Ski BASE Jumping",
                          "Sailing in Stormy Seas", "Highlining", "Ice Cross Racing", "Acrobatic Paragliding", "Extreme Ironing"],

    "Unexplained Phenomena": ["UFO Sightings", "Cryptids", "Paranormal Investigations", "Haunted Places", "Ghosts and Spirits",
                              "Extraterrestrial Life Theories", "Bermuda Triangle Mysteries", "Crop Circles", "Spontaneous Human Combustion", "Time Slips",
                              "Near-Death Experiences", "Out-of-Body Experiences", "Doppelgangers", "Psychic Phenomena", "Telepathy",
                              "Alien Abductions", "Poltergeists", "Shadow People", "Mothman Sightings", "Chupacabra Sightings",
                              "Mystery Spontaneous Fires", "Black-Eyed Children", "Mystery Lights", "Disappearance of Flight MH370", "The Voynich Manuscript",
                              "The Wow! Signal", "The Dyatlov Pass Incident", "The Mary Celeste Mystery", "The Lost Colony of Roanoke", "The Taos Hum"],

    "Countries and Cultures": ["Cultural Festivals", "Traditional Customs", "World Cuisine", "Cultural Heritage Sites", "Cultural Diplomacy",
                               "Famous Landmarks", "UNESCO World Heritage Sites", "Cultural Etiquette", "Cultural Exchange Programs", "Cultural Diversity",
                               "Indigenous Cultures", "Folklore and Mythology", "Cultural Conservation", "Global Traditions", "Famous Explorers",
                               "Cultural Celebrations", "Intercultural Communication", "Living Abroad Experiences", "Cultural Appropriation", "Cultural Revivals",
                               "Heritage Tourism", "Cultural Anthropology", "Cultural Preservation Laws", "Cultural Impact on Business", "Global Nomad Lifestyle",
                               "Languages of the World", "Cultural Tourism Trends", "Cultural Identity", "Cultural Heritage and Technology", "Cultural Impact on Fashion"],

    "Astrology and Horoscopes": ["Zodiac Signs", "Natal Charts", "Astrological Compatibility", "Horoscope Readings", "Astrological Houses",
                                 "Retrograde Planets", "Astrology and Personal Growth", "Astrology and Relationships", "Astrological Transits", "Astrology and Career",
                                 "Astrology and Health", "Chinese Zodiac", "Vedic Astrology", "Astrological Elements", "Astrology and Decision Making", "Astrology and Psychology",
                                 "Astrology and Spirituality", "Astrology and the Moon", "Astrology and Numerology", "Astrology and Tarot", "Astrology and Gemstones",
                                 "Astrology and Plants", "Astrology in Popular Culture", "Astrology and Wellness", "Astrology and Fashion", "Astrology Apps", "Astrology and Parenting",
                                 "Astrology and Sports", "Astrological Predictions"],

    "Futurism": ["Future Technology", "Emerging Trends", "Futuristic Design", "Space Colonization", "Transhumanism",
                 "Post-Humanism", "Future of Work", "Futuristic Fashion", "Future of Transportation", "Futuristic Architecture",
                 "Artificial Intelligence in the Future", "Future Healthcare", "Climate Change Solutions", "Future Energy Sources", "Future of Education",
                 "Virtual Reality in the Future", "Future of Entertainment", "Space Tourism in the Future", "Future Urban Planning", "Future Food Trends",
                 "Nanotechnology in the Future", "Future of Communication", "Future Space Exploration", "Future of Finance", "Futuristic Travel", "Future Sports",
                 "Future Wildlife Conservation", "Future Social Structures", "Future of Personal Development", "Future Global Challenges", "Futurist Predictions"],

    "Outer Space": ["NASA Missions", "Astronomy News", "Space Exploration Technologies", "Black Holes", "Exoplanets",
                    "Mars Rovers", "International Space Station", "Hubble Space Telescope", "Space Colonization", "Cosmic Phenomena",
                    "Asteroid Impact Prevention", "Search for Extraterrestrial Intelligence (SETI)", "Jupiter's Moons", "Saturn's Rings", "Neutron Stars",
                    "Dark Matter", "Interstellar Travel", "Space Probes", "The Milky Way Galaxy", "The Oort Cloud",
                    "Star Clusters", "Gamma-Ray Bursts", "The Kuiper Belt", "The Solar Wind", "Extragalactic Astronomy", "The Big Bang Theory",
                    "Astrobiology", "Cosmic Rays", "Astrophysics Research", "Celestial Navigation"],

    "Dreams and Dream Interpretation": ["Lucid Dreaming", "Common Dream Symbols", "Nightmares", "Recurring Dreams", "Prophetic Dreams",
                                       "Sleep Paralysis", "Dreams and Emotions", "Dream Journaling", "Dreams and Creativity", "Dreams and Memory",
                                       "Cultural Perspectives on Dreams", "Dreams and Spiritual Connection", "Dreams and Psychology", "Dreams and Healing", "Dreams and Reality",
                                       "Sleep Disorders", "Dream Incubation", "Precognitive Dreams", "Dreams and Personal Growth", "Dreams and Relationships",
                                       "Dreams and Past Lives", "Dreams and Symbolism", "Dreams and Problem Solving", "Dreams in Literature", "Dreams in Art",
                                       "Dreams in Film", "Dreams and Neuroscience", "Dream Interpretation Techniques", "Dreams and Parallel Realities", "Dreams and Virtual Reality"],

    "Aviation": ["Commercial Aviation", "Private Aviation", "Aviation Technology", "Aircraft Design", "Airline Industry",
                 "Airport Operations", "Aviation Safety", "Pilot Training", "Air Traffic Control", "Aviation Regulations",
                 "Future of Aviation", "Airplane Maintenance", "Airports of the World", "Aviation History", "Airline Alliances",
                 "Space Travel", "Supersonic Travel", "Aviation and the Environment", "Airplane Innovations", "Aviation Events",
                 "Airplane Spotting", "Aviation Museums", "Aviation Photography", "Flying Adventures", "Aviation Careers",
                 "Aerial Surveying", "Unmanned Aerial Vehicles (UAVs)", "Human-powered Flight", "Aviation News", "Aviation Challenges"],
    
    "Personal Interests": ["Hobbies Exploration", "Artistic Pursuits", "Creative Writing", "Photography Adventures", "Culinary Arts at Home",
                          "Book Club Experiences", "DIY Crafting", "Gardening Adventures", "Exploring Local Culture", "Adventure Sports",
                          "Music Exploration", "Film Appreciation", "Tech and Gadgets Enthusiasm", "Outdoor Adventures", "Cultural Festivals Participation",
                          "Philanthropy and Volunteering", "Personal Finance Mastery", "Fitness Challenges", "Learning New Instruments", "Language Learning Journeys",
                          "Mindful Travel Experiences", "Exploring Meditation Techniques", "Cooking and Baking Experiments", "Art and Craft Workshops", "Board Game Nights",
                          "Astrology and Birth Chart Analysis", "Comic Book Collecting", "Sustainable Living Practices", "Historical Reenactment", "Bird Watching Expeditions"],
    
    "Personal Relationships": ["Effective Communication", "Building Trust", "Healthy Boundaries", "Conflict Resolution", "Quality Time Together",
                              "Emotional Intimacy", "Love Languages", "Dating Tips", "Long-Distance Relationships", "Maintaining Friendships",
                              "Family Dynamics", "Parenting Partnerships", "Navigating Breakups", "Relationship Red Flags", "Relationship Goals",
                              "Couples Counseling", "Solo Travel Experiences", "Building a Support System", "Forgiveness Practices", "Celebrating Milestones",
                              "Interpersonal Skills", "Dealing with Toxic Relationships", "Social Connection Strategies", "Cultivating Empathy", "Relationship and Personal Growth",
                              "Balancing Independence and Togetherness", "Relationships in the Digital Age", "Quality Family Time", "Relationships and Mental Health"],
    
    "Personal Development": ["Goal Setting", "Time Management", "Productivity Hacks", "Self-Reflection", "Mindset Shifts",
                            "Learning New Skills", "Personal Growth Books", "Positive Habits", "Motivational Quotes", "Overcoming Challenges",
                            "Life Coaching", "Self-Discovery", "Building Resilience", "Stress Management", "Emotional Intelligence",
                            "Setting Boundaries", "Gratitude Practices", "Healthy Relationships", "Effective Communication", "Assertiveness",
                            "Career Planning", "Financial Literacy", "Building Confidence", "Decision-Making Strategies", "Finding Purpose",
                            "Coping with Change", "Mindfulness Practices", "Continuous Learning", "Adaptability", "Well-being Techniques"],
    
    "Personal Finance": ["Budgeting Tips", "Saving Strategies", "Investment Planning", "Retirement Savings", "Financial Independence",
                        "Debt Management", "Credit Score Improvement", "Emergency Funds", "Frugal Living", "Side Hustles",
                        "Real Estate Investment", "Stock Market Basics", "Passive Income Ideas", "Financial Literacy Resources", "Tax Planning",
                        "Estate Planning", "Money Mindset", "Financial Goal Setting", "Managing Expenses", "Student Loan Tips",
                        "Credit Card Management", "Entrepreneurial Finances", "Financial Wellness", "Insurance Planning", "Wealth Building",
                        "Money and Relationships", "Negotiating Salaries", "Financial Education for Kids", "Philanthropy", "Digital Wallets"],
    
    "Food & Cooking": ["Recipes", "Culinary Tips", "Cooking Techniques", "Dining Experiences", "Gourmet Cuisine",
                       "Baking", "International Foods", "Food Pairing", "Home Cooking", "Foodie Adventures",
                       "Food Blogs", "Cookware", "Chef's Specials", "Healthy Eating", "Dessert Creations",
                       "Farm-to-Table", "Cooking Challenges", "Culinary Trends", "Food Photography", "Spices",
                       "Cooking Shows", "Wine Pairing", "Culinary Festivals", "Local Ingredients", "Fusion Cuisine"],

    "Marriage & Love Life": ["Relationship Advice", "Date Night Ideas", "Love Languages", "Marriage Tips", "Romantic Getaways",
                            "Communication in Relationships", "Family Planning", "Couple's Fitness", "Parenting Together",
                            "Intimacy Tips", "Marriage Enrichment", "Romantic Surprises", "Celebrating Milestones",
                            "Navigating Challenges", "Quality Time", "Building Trust", "Love and Respect", "Spousal Support",
                            "Lifestyle Compatibility", "Managing Finances as a Couple", "Adventures Together", "Well-being",
                            "Wedding Anniversaries", "Couple's Hobbies", "Emotional Connection", "Healthy Arguments"],

    "Volcanic & Seismic Activity": ["Earthquake Preparedness", "Volcano Monitoring", "Geological Surveys", "Tectonic Plates",
                                    "Seismic Events", "Natural Disaster Response", "Volcanic Eruptions", "Earth's Crust",
                                    "Seismology", "Volcanic Hazards", "Fault Lines", "Emergency Evacuation Plans", "Disaster Relief",
                                    "Geothermal Energy", "Plate Boundaries", "Volcanic Ash", "Tsunami Warnings", "Geological Phenomena",
                                    "Earthquake-Resistant Construction", "Volcanic Research", "Richter Scale", "Emergency Kits",
                                    "Tsunami Preparedness", "Volcanic Monitoring Technology", "Seismic Retrofitting", "Tectonic Activity"],
}

num_subjects = 100000

subjects, labels = generate_email_subjects(num_subjects, categories, keywords)

df = pd.DataFrame({"Subject": subjects, "Category": labels})

train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

train_df.to_csv("email_subjects_train.tsv", sep='\t', index=False)

test_df.to_csv("email_subjects_test.tsv", sep='\t', index=False)