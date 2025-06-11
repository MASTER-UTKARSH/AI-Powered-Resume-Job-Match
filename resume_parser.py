import docx2txt
import re

def clean_text(text):
    """Clean the extracted text by removing extra whitespace and special characters."""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters but keep basic punctuation
    text = re.sub(r'[^\w\s.,;:!?-]', '', text)
    return text.strip()

def extract_text_from_docx(file_path):
    """
    Extract text from a .docx file and clean it.
    
    Args:
        file_path: Path to the .docx file
        
    Returns:
        str: Cleaned text content from the resume
    """
    try:
        # Extract text from docx
        text = docx2txt.process(file_path)
        # Clean the extracted text
        cleaned_text = clean_text(text)
        return cleaned_text
    except Exception as e:
        raise Exception(f"Error processing resume: {str(e)}")

def extract_skills(text):
    """
    Extract potential skills from the resume text.
    This is a basic implementation that can be enhanced with more sophisticated NLP.
    
    Args:
        text: Cleaned resume text
        
    Returns:
        list: List of potential skills
    """
    # Common technical skills to look for
    common_skills = [
        'python', 'java', 'javascript', 'c++', 'c#', 'ruby', 'php',
        'html', 'css', 'sql', 'nosql', 'mongodb', 'postgresql',
        'aws', 'azure', 'gcp', 'docker', 'kubernetes',
        'machine learning', 'deep learning', 'ai', 'data science',
        'tensorflow', 'pytorch', 'scikit-learn', 'pandas', 'numpy'
    ]
    
    # Convert text to lowercase for matching
    text_lower = text.lower()
    
    # Find matching skills
    found_skills = []
    for skill in common_skills:
        if skill in text_lower:
            found_skills.append(skill)
            
    return found_skills 