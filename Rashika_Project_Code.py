# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:09:38 2024

@author: RASHIKA GANGWAR
"""

# Import necessary libraries
import PyPDF2
import nltk
import random
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# Download NLTK resources 
nltk.download('punkt')
nltk.download('stopwords')

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            for page_num in range(len(pdf_reader.pages)):
                text += pdf_reader.pages[page_num].extractText()
    except FileNotFoundError:
        print(f"Error: File not found - {pdf_path}")
    except Exception as e:
        print(f"Error: {e}")
    return text

# Function to preprocess text
def preprocess_text(text):
    sentences = sent_tokenize(text)
    tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]
    stop_words = set(stopwords.words('english'))
    filtered_sentences = [
        [word.lower() for word in sentence if word.isalnum() and word.lower() not in stop_words]
        for sentence in tokenized_sentences
    ]
    return filtered_sentences

# Function to identify chapters (placeholder implementation)
def identify_chapters(text):
    # Implement chapter identification logic based on headings or other patterns
    return ["Chapter 1", "Chapter 2", "Chapter 3"]

# Function to identify key concepts within a chapter
def identify_key_concepts(chapter_text):
    # Implement key concept identification logic (TF-IDF, NER, etc.)
    return ["List", "Function", "Class", "Exception", "Module"]

# Function to generate a multiple-choice question
def generate_multiple_choice_question(concept):
    question_text = f"What is {concept} used for in Python?"
    correct_answer = f"{concept} allows..."
    incorrect_answers = ["To create a list", "For loops in Python", "To define a class", "Handling exceptions"]
    options = [correct_answer] + random.sample(incorrect_answers, 3)
    random.shuffle(options)
    return question_text, options

# Function to generate a true/false question
def generate_true_false_question(concept):
    statement = f"{concept} is a fundamental concept in Python programming."
    is_true = random.choice([True, False])
    return statement, is_true

# Function to generate a fill-in-the-blank question
def generate_fill_in_the_blank_question(concept):
    sentence = f"In Python, a {concept} is used to represent a collection of elements."
    blank_position = sentence.find(concept)
    question_text = sentence[:blank_position] + "_____" + sentence[blank_position + len(concept):]
    return question_text, concept

# Function to parse book content and identify chapters
def parse_book_content(book_text):
    # Implement logic to split the text into chapters
    return identify_chapters(book_text)

# Function to generate diverse questions for each chapter
def generate_diverse_questions(chapters, num_questions_per_chapter=5):
    questions = []
    used_concepts = set()

    for chapter in chapters:
        # Placeholder implementation for getting the chapter text
        chapter_text = get_chapter_text(book_text, chapter)
        key_concepts = identify_key_concepts(chapter_text)

        for concept in key_concepts:
            if concept not in used_concepts:
                # Mark the concept as used
                used_concepts.add(concept)

                # Generate multiple-choice question
                mcq_question, mcq_options = generate_multiple_choice_question(concept)
                questions.append((mcq_question, mcq_options))

                # Generate true/false question
                tf_question, is_true = generate_true_false_question(concept)
                questions.append((tf_question, is_true))

                # Generate fill-in-the-blank question
                fib_question, fib_answer = generate_fill_in_the_blank_question(concept)
                questions.append((fib_question, fib_answer))

    # Shuffle the questions for diversity
    random.shuffle(questions)

    # Select a subset of questions based on the modified num_questions_per_chapter
    selected_questions = questions[:num_questions_per_chapter * len(chapters)]

    return selected_questions

# Function to get the text of a specific chapter (placeholder implementation)
def get_chapter_text(book_text, chapter):
    # Implement logic to extract text for a specific chapter
    # You may need to use chapter headings, page numbers, or other markers
    # to identify the beginning and end of each chapter.
    return book_text  # Placeholder, replace with actual implementation

# Example usage
book_text = "OneDrive\\Desktop\Learning_Python.pdf"

# Generate fewer questions (e.g., 2 questions per chapter)
generated_questions = generate_diverse_questions(parse_book_content(book_text), num_questions_per_chapter=5)

# Print generated questions
for i, (question, answer) in enumerate(generated_questions, 1):
    print(f"Question {i}: {question}")
    print(f"Answer {i}: {answer}\n")
