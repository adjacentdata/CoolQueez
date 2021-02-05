#https://opentdb.com/api.php?amount=10&type=multiple

import requests


req = requests.get("https://opentdb.com/api.php",params={"amount": 10, "type": "multiple"})
req.raise_for_status()
data = req.json()
print(data)
all_questions = data

# all_questions = {
#     "response_code": 0,
#     "results": [
#         {"category": "Geography",
#          "type": "multiple",
#          "difficulty": "easy",
#          "question": "Which city is the capital of the United States of America?",
#          "correct_answer": "Washington D.C",
#          "incorrect_answers": ["Seattle", "Albany", "Los Angeles"]},
#         {"category": "Science: Computers", "type": "multiple", "difficulty": "hard",
#          "question": "What was the name of the security vulnerability found in Bash in 2014?",
#          "correct_answer": "Shellshock",
#          "incorrect_answers": ["Heartbleed", "Bashbug", "Stagefright"]},
#         {"category": "Entertainment: Comics", "type": "multiple", "difficulty": "easy",
#          "question": "Who is the creator of the comic series &quot;The Walking Dead&quot;?",
#          "correct_answer": "Robert Kirkman",
#          "incorrect_answers": ["Stan Lee", "Malcolm Wheeler-Nicholson", "Robert Crumb"]},
#         {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
#          "question": "There are 6 legendary cards in &quot;Clash Royale&quot;.",
#          "correct_answer": "False", "incorrect_answers": ["True"]},
#         {"category": "Entertainment: Japanese Anime & Manga", "type": "multiple",
#          "difficulty": "easy",
#          "question": "What is the name of the stuffed lion in Bleach?",
#          "correct_answer": "Kon", "incorrect_answers": ["Jo", "Urdiu", "Chad"]},
#         {"category": "General Knowledge", "type": "multiple", "difficulty": "hard",
#          "question": "The Swedish word &quot;Grunka&quot; means what in English?",
#          "correct_answer": "Thing", "incorrect_answers": ["People", "Place", "Pineapple"]},
#         {"category": "Entertainment: Music", "type": "multiple", "difficulty": "easy",
#          "question": "What was Rage Against the Machine&#039;s debut album?",
#          "correct_answer": "Rage Against the Machine",
#          "incorrect_answers": ["Evil Empire", "Bombtrack", "The Battle Of Los Angeles"]},
#         {"category": "Entertainment: Japanese Anime & Manga", "type": "multiple",
#          "difficulty": "medium",
#          "question": "In the &quot;Toaru Majutsu no Index&quot; anime, Touma Kamijou is a level 0 esper that has the ability to do what?",
#          "correct_answer": "Dispell any esper or magical powers",
#          "incorrect_answers": ["Teleport", "Make telepathic communications",
#                                "Create electricity from his own body"]},
#         {"category": "Geography", "type": "multiple", "difficulty": "medium",
#          "question": "Which country has the abbreviation &quot;CH&quot;?",
#          "correct_answer": "Switzerland",
#          "incorrect_answers": ["China", "Canada", "No Country"]},
#         {"category": "Entertainment: Video Games", "type": "multiple",
#          "difficulty": "medium",
#          "question": "What former MOBA, created by Waystone Games and published by EA, was shut down in 2014?",
#          "correct_answer": "Dawngate",
#          "incorrect_answers": ["Strife", "League of Legends", "Heroes of Newerth"]}]}
