import streamlit as st
import tempfile
import os
from resume_parser import extract_text_from_docx, extract_skills
from job_matcher import JobMatcher
from data.sample_jobs import SAMPLE_JOBS

# Set page config
st.set_page_config(
    page_title="AI Resume Job Matcher",
    page_icon="💼",
    layout="wide"
)

# Initialize session state
if 'job_matcher' not in st.session_state:
    st.session_state.job_matcher = JobMatcher()
    st.session_state.job_matcher.add_job_descriptions(SAMPLE_JOBS)

def main():
    st.title("💼 AI Resume Job Matcher")
    st.write("Upload your resume and find the best matching jobs!")

    # File uploader
    uploaded_file = st.file_uploader("Upload your resume (DOCX format)", type=['docx'])

    if uploaded_file is not None:
        # Save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name

        try:
            # Extract text from resume
            resume_text = extract_text_from_docx(tmp_file_path)
            
            # Extract skills
            skills = extract_skills(resume_text)
            
            # Display extracted skills
            st.subheader("📋 Detected Skills")
            st.write(", ".join(skills))
            
            # Find job matches
            matches = st.session_state.job_matcher.find_matches(resume_text)
            
            # Display matches
            st.subheader("🎯 Top Job Matches")
            
            for i, match in enumerate(matches, 1):
                with st.expander(f"{i}. {match['title']} - {match['match_percentage']}% Match"):
                    st.write("**Job Description:**")
                    # Find the matching job description
                    job_desc = next(job['description'] for job in SAMPLE_JOBS if job['title'] == match['title'])
                    st.write(job_desc)
                    
                    # Show skill gaps
                    st.write("**Potential Skill Gaps:**")
                    skill_gaps = st.session_state.job_matcher.get_skill_gaps(resume_text, job_desc)
                    if skill_gaps:
                        st.write(", ".join(skill_gaps[:5]))  # Show top 5 skill gaps
                    else:
                        st.write("No significant skill gaps detected!")

        except Exception as e:
            st.error(f"Error processing resume: {str(e)}")
        finally:
            # Clean up temporary file
            os.unlink(tmp_file_path)

if __name__ == "__main__":
    main() 