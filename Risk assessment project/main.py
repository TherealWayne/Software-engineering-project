#Import the neccessary libraries

import requests
import json 

# Retrieve the 10-K reports from EDGAR
# WALMART 
# Define the API endpoint
url = 'https://data.sec.gov/submissions/CIK0000104169.json'

# Send the API request
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Extract the URL of the 10K report
report_url = data['filings'][0]['url']

# Retrieve the 10K report
report = requests.get(report_url)

# Extract the risk factors from the 10-K reports
from bs4 import BeautifulSoup 

# Parse the report to extract the risk factors
soup = BeautifulSoup(report.content, 'html.parser')
risk_factors = soup.find('a', {'name': 'item1a'}).find_next('p').get_text()

# Use NLP techniques to identify the risk factors 
from collections import Counter
import re 

# Analyze the risk factors and identify the top 10 major risk factors
risk_factors = re.sub(r'[^\w\s]','',risk_factors) # Remove punctuation
risk_factors = risk_factors.lower() # Convert to lowercase
risk_factors_list = risk_factors.split() # Split into words
risk_factors_count = Counter(risk_factors_list) # Count the frequency of each word
top_risk_factors = risk_factors_count.most_common(10) # Get the top 10 most frequent words
print(top_risk_factors) # Print the top 10 most frequent words 

# Retrieve the 10K report of the similar company from Edgar.com using their API
# Kroger
# Define the API endpoint of the competitor company
competitor_url = 'https://data.sec.gov/submissions/CIK0000056873.json' 

# Send the API request
competitor_response = requests.get(competitor_url) 

# Parse the JSON response
competitor_data = competitor_response.json()

# Extract the URL of the 10K report
competitor_report_url = competitor_data['filings'][0]['url']

# Retrieve the 10K report
competitor_report = requests.get(competitor_report_url)

# Extract the risk factors from the 10-K reports
# Parse the report to extract the risk factors
competitor_soup = BeautifulSoup(competitor_report.content, 'html.parser')
competitor_risk_factors = competitor_soup.find('a', {'name': 'item1a'}).find_next('p').get_text()

# Use NLP techniques to identify the risk factors
# Analyze the risk factors and identify the top 10 major risk factors
competitor_risk_factors = re.sub(r'[^\w\s]','',competitor_risk_factors) # Remove punctuation
competitor_risk_factors = competitor_risk_factors.lower() # Convert to lowercase
competitor_risk_factors_list = competitor_risk_factors.split() # Split into words
competitor_risk_factors_count = Counter(competitor_risk_factors_list) # Count the frequency of each word
competitor_top_risk_factors = competitor_risk_factors_count.most_common(10) # Get the top 10 most frequent words
print(competitor_top_risk_factors) # Print the top 10 most frequent words


# Identify the similarities and differences between the risk factors of the two companies
common_risk_factors = set(risk_factors_list).intersection(set(competitor_risk_factors_list))
unique_risk_factors_a = set(risk_factors_list).difference(set(competitor_risk_factors_list))
unique_risk_factors_b = set(competitor_risk_factors_list).difference(set(risk_factors_list))

# Generate a summary report of the top 10 major risk factors for both companies
print('Top 10 Major Risk Factors for Walmart:')
for factor in top_risk_factors:
    print(factor[0], factor[1])

print('\nTop 10 Major Risk Factors for Kroger:')
for factor in competitor_top_risk_factors:
    print(factor[0], factor[1])

print('\nCommon Risk Factors:')
for factor in common_risk_factors:
    print(factor)

print('\nUnique Risk Factors for Walmart:')
for factor in unique_risk_factors_a:
    print(factor)

print('\nUnique Risk Factors for Kroger:')
for factor in unique_risk_factors_b:
    print(factor)

# Use cosine similarity to compare the risk factors
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define the documents to be compared
documents = [risk_factors, competitor_risk_factors]

# Create the document vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Compare the document vectors
cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])


