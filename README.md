# AI-Powered Resume Job Matcher

An intelligent tool that analyzes resumes and matches them with relevant job descriptions using Natural Language Processing (NLP).

## Features

- Resume parsing from .docx files
- Skill extraction and analysis
- Job matching using TF-IDF and Cosine Similarity
- Skill gap analysis
- Interactive web interface using Streamlit

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-resume-job-matcher
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Upload your resume in .docx format

4. View the results:
   - Detected skills from your resume
   - Top matching jobs with match percentages
   - Detailed job descriptions
   - Potential skill gaps

## Project Structure

```
.
├── app.py              # Streamlit web application
├── resume_parser.py    # Resume parsing and text extraction
├── job_matcher.py      # NLP matching logic
├── requirements.txt    # Project dependencies
├── data/
│   └── sample_jobs.py  # Sample job descriptions
└── README.md          # Project documentation
```

## Technical Details

- **Resume Parsing**: Uses `docx2txt` for extracting text from .docx files
- **Text Processing**: Implements TF-IDF vectorization and Cosine Similarity for matching
- **Frontend**: Built with Streamlit for a clean, responsive interface
- **NLP Pipeline**: 
  1. Text extraction and cleaning
  2. TF-IDF vectorization
  3. Cosine similarity calculation
  4. Skill gap analysis

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 