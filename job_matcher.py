import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class JobMatcher:
    def __init__(self):
        """Initialize the JobMatcher with TF-IDF vectorizer."""
        self.vectorizer = TfidfVectorizer(
            stop_words='english',
            ngram_range=(1, 2),
            max_features=5000
        )
        self.job_descriptions = []
        self.job_titles = []
        self.tfidf_matrix = None
        
    def add_job_descriptions(self, job_data):
        """
        Add job descriptions to the matcher.
        
        Args:
            job_data: List of dictionaries containing 'title' and 'description'
        """
        self.job_titles = [job['title'] for job in job_data]
        self.job_descriptions = [job['description'] for job in job_data]
        
        # Create TF-IDF matrix for job descriptions
        self.tfidf_matrix = self.vectorizer.fit_transform(self.job_descriptions)
        
    def find_matches(self, resume_text, top_n=5):
        """
        Find the best matching jobs for a given resume.
        
        Args:
            resume_text: Text content of the resume
            top_n: Number of top matches to return
            
        Returns:
            list: List of dictionaries containing job title and match percentage
        """
        if self.tfidf_matrix is None:
            raise ValueError("No job descriptions have been added to the matcher")
            
        # Transform resume text to TF-IDF vector
        resume_vector = self.vectorizer.transform([resume_text])
        
        # Calculate cosine similarity
        similarities = cosine_similarity(resume_vector, self.tfidf_matrix).flatten()
        
        # Get top N matches
        top_indices = similarities.argsort()[-top_n:][::-1]
        
        # Create results
        matches = []
        for idx in top_indices:
            match = {
                'title': self.job_titles[idx],
                'match_percentage': round(similarities[idx] * 100, 2)
            }
            matches.append(match)
            
        return matches
    
    def get_skill_gaps(self, resume_text, job_description):
        """
        Analyze potential skill gaps between resume and job description.
        
        Args:
            resume_text: Text content of the resume
            job_description: Text content of the job description
            
        Returns:
            list: List of potential missing skills
        """
        # Extract skills from both texts
        resume_skills = set(resume_text.lower().split())
        job_skills = set(job_description.lower().split())
        
        # Find skills in job description that are not in resume
        missing_skills = job_skills - resume_skills
        
        return list(missing_skills) 