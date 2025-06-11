# AI-Powered Resume Job Matcher

An intelligent system that matches resumes with job descriptions using machine learning techniques.

## Features

- Resume parsing and analysis
- Job description processing
- Skill matching and scoring
- Experience level assessment
- Education qualification matching
- Interactive web interface

## Data Requirements

The project requires two types of data:

1. **Resumes**: 
   - Format: JSON or structured text
   - Required fields: name, email, skills, experience, education
   - Sample data provided in `data/sample_resumes.py`

2. **Job Descriptions**:
   - Format: JSON or structured text
   - Required fields: title, company, requirements, description
   - Sample data provided in `data/sample_jobs.py`

### Sample Data

The repository includes sample data files to demonstrate the expected format:
- `data/sample_resumes.py`: Contains example resume structures
- `data/sample_jobs.py`: Contains example job descriptions

For production use, you'll need to:
1. Replace the sample data with your actual dataset
2. Ensure your data follows the same structure as the samples
3. Place your data files in the `data/` directory

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MASTER-UTKARSH/AI-Powered-Resume-Job-Match.git
cd AI-Powered-Resume-Job-Match
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the provided local URL (usually http://localhost:8501)

3. Upload resumes and job descriptions through the web interface

## Project Structure

```
AI-Powered-Resume-Job-Match/
├── app.py                 # Streamlit web application
├── resume_parser.py       # Resume parsing and processing
├── job_matcher.py         # Job matching algorithm
├── requirements.txt       # Project dependencies
├── data/                  # Data directory
│   ├── sample_resumes.py  # Sample resume data
│   └── sample_jobs.py     # Sample job data
└── README.md             # Project documentation
```

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 