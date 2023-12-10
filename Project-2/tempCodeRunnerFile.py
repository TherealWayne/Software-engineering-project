#SOFTWARE ENGINEERING PROJECT
#Authors: 1. Wayne Bell 2. Clemente De Rosa 3. Waeil Mikhaeli 
#Date: 12/11/2023
#Version: 1.0
#Description: This is the main file of the project. This project assumes that the user has already created a database called risk_factors.db and a table called risk_factors in the database. 
# The user can enter the company name (Walmart or Kroger) and the risk factors for the company will be stored in the database. 
# The user can then get the risk factors for the company from the database and the risk factors will be displayed in a dataframe.
# The data is gathered from an AI API but due to time constraints and this being the first version, it is assumed that the data is already available in the form of a dictionary.



# Importing the libraries
import numpy as np
import sqlite3
import pandas as pd



# Importing the dataset
def store_risk_factors(company_name, risk_factors):
    conn = sqlite3.connect('risk_factors.db')
    c = conn.cursor()
    c.execute("INSERT INTO risk_factors (company_name, risk_factor) VALUES (?, ?)", (company_name, risk_factors))
    conn.commit()
    conn.close()

# Risk factors for Walmart
walmart_risk_factors = {
    "Pandemic-related risks": "The COVID_19 pandemic has had a significant impact on Walmart’s business operations, financial performance, and supply chain. The company is exposed to various risks such as supply chain disruptions, reduced consumer demand, and increased costs due to safety measures.",
    "Competition risks": "Walmart operates in a highly competitive retail industry and faces intense competition from various players such as Kroger, Amazon, Target and Costco. The company is exposed to risks such as pricing pressures, loss of market share, and reduced profitability.",
    "Regulatory risks": "Walmart is subject to various laws and regulations in the countries where it operates. The company is exposed to risks such as changes in laws and regulations, compliance failures, and legal disputes.",
    "Supply chain risks": "Walmart’s business operations are dependent on its supply chain, which is exposed to various risks such as natural disasters, geopolitical risks, and labor disputes.",
    "Cybersecurity risks": "Walmart’s business operations are dependent on its information technology systems, which are exposed to various risks such as cyber attacks, data breaches, and system failures.",
    "Environmental risks": "Walmart’s business operations are exposed to various environmental risks such as climate change, natural disasters, and resource scarcity.",
    "Reputational risks": "Walmart’s reputation is critical to its business operations and financial performance. The company is exposed to risks such as negative publicity, product recalls, and ethical issues.",
    "Legal risks": "Walmart is exposed to various legal risks such as lawsuits, regulatory investigations, and compliance failures.",
    "Labor risks": "Walmart’s business operations are dependent on its workforce, which is exposed to various risks such as labor disputes, unionization, and employee turnover.",
    "Financial risks": "Walmart’s business operations are exposed to various financial risks such as foreign currency exchange rate fluctuations, interest rate fluctuations, and credit risks."
}

# Risk factors for Kroger
kroger_risk_factors = {
    "Pandemic-related risks": "The COVID-19 pandemic has had a significant impact on Kroger’s business operations, financial performance, and supply chain. The company is exposed to various risks such as supply chain disruptions, reduced consumer demand, and increased costs due to safety measures.",
    "Competition risks": "Kroger operates in a highly competitive retail industry and faces intense competition from various players such as Walmart, Amazon, Target and Costco. The company is exposed to risks such as pricing pressures, loss of market share, and reduced profitability.",
    "Regulatory risks": "Kroger is subject to various laws and regulations in the countries where it operates. The company is exposed to risks such as changes in laws and regulations, compliance failures, and legal disputes.",
    "Supply chain risks": "Kroger’s business operations are dependent on its supply chain, which is exposed to various risks such as natural disasters, geopolitical risks, and labor disputes.",
    "Cybersecurity risks": "Kroger’s business operations are dependent on its information technology systems, which are exposed to various risks such as cyber attacks, data breaches, and system failures.",
    "Environmental risks": "Kroger’s business operations are exposed to various environmental risks such as climate change, natural disasters, and resource scarcity.",
    "Reputational risks": "Kroger’s reputation is critical to its business operations and financial performance. The company is exposed to risks such as negative publicity, product recalls, and ethical issues.",
    "Legal risks": "Kroger is exposed to various legal risks such as lawsuits, regulatory investigations, and compliance failures.",
    "Labor risks": "Kroger’s business operations are dependent on its workforce, which is exposed to various risks such as labor disputes, unionization, and employee turnover.",
    "Financial risks": "Kroger’s business operations are exposed to various financial risks such as foreign currency exchange rate fluctuations, interest rate fluctuations, and credit risks."
}


# Storing the risk factors in the database
company_name = input("Enter the company name (walmart or kroger) Don't use any caps: ")
while company_name.lower() not in ["walmart", "kroger"]:
    print("Invalid company name. Please enter either walmart or kroger.")
    company_name = input("Enter the company name (walmart or kroger): ")
for key, value in eval(f"{company_name.lower()}_risk_factors").items():
    store_risk_factors(company_name, value)

# Getting the risk factors from the database
conn = sqlite3.connect('risk_factors.db')
c = conn.cursor()
c.execute("SELECT risk_factor FROM risk_factors WHERE company_name = ?", (company_name,))
rows = c.fetchall()
conn.close()

# Creating a dataframe
df = pd.DataFrame(rows, columns=['Risk Factors'])







