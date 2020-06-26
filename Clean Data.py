import numpy as np
import re
import pandas as pd

# Read in data (Insert full file path if FileNotFound)
file_path = 'job_postings_excel.xlsx'
full_data = pd.read_excel(file_path)


# Change all NULL, empy entries to string NA
clean_NaN =  full_data.fillna('missing')
print(clean_NaN.shape)

# Remove punction marks and weird symbols
punct = re.compile(r'[^\w\s]+')

clean_NaN['company_profile'] = [punct.sub('', x) for x in clean_NaN['company_profile'].tolist()]
clean_NaN['description'] = [punct.sub('', x) for x in clean_NaN['description'].tolist()]
clean_NaN['requirements'] = [punct.sub('', x) for x in clean_NaN['requirements'].tolist()]
clean_NaN['benefits'] = [punct.sub('', x) for x in clean_NaN['benefits'].tolist()]


# Lower Case 
#df.poem = df.poem.apply(lambda x: x.lower())
clean_NaN['title'] = clean_NaN['title'].apply(lambda x: x.lower())
clean_NaN['location'] = clean_NaN['location'].apply(lambda x: x.lower())
clean_NaN['department'] = clean_NaN['department'].apply(lambda x: x.lower())
clean_NaN['company_profile'] = clean_NaN['company_profile'].apply(lambda x: x.lower())
clean_NaN['description'] = clean_NaN['description'].apply(lambda x: x.lower())
clean_NaN['requirements'] = clean_NaN['requirements'].apply(lambda x: x.lower()) 
clean_NaN['benefits'] = clean_NaN['benefits'].apply(lambda x: x.lower()) 
clean_NaN['employment_type'] = clean_NaN['employment_type'].apply(lambda x: x.lower()) 
clean_NaN['required_experience'] = clean_NaN['required_experience'].apply(lambda x: x.lower()) 
clean_NaN['required_education'] = clean_NaN['required_education'].apply(lambda x: x.lower()) 
clean_NaN['industry'] = clean_NaN['industry'].apply(lambda x: x.lower()) 
clean_NaN['function'] = clean_NaN['function'].apply(lambda x: x.lower()) 

# Ensure that salary range is a string value
clean_NaN['salary_range'] = clean_NaN['salary_range'].astype(np.unicode)

# Remove weird symbols from columns
#company_profile = clean_NaN['company_profile'].to_numpy()
#description = clean_NaN['description'] .to_numpy()

# Create a new Excel with cleaner data
clean_NaN.to_excel('/home/thabo/Documents/Bsc CompSci/Fourth Year/Semester 1/COMS3007 ML/Assignment/ML-Assignment/Job_Postings(clean).xlsx', sheet_name='Job_Postings')


