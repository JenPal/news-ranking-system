# News Ranking System

This project is a news-ranking system designed to surface the most relevant, timely, and trustworthy LinkedIn posts based on trending topics. The system uses a combination of AI-powered classifiers, keyword and fuzzy matching, and engagement metrics to rank posts while ensuring transparency, safety, and user feedback.

## Features
- **Trending Topic Detection**: Detects and builds a dynamic list of trending topics from both external and internal sources.
- **Post Scanning**: Scans Social posts for mentions of these topics using keyword and fuzzy matching.
- **Heuristic Filtering**: Filters out posts that are non-news or non-timely.
- **LLM-Powered Classification**: Uses an LLM to judge the newsworthiness, relevance, originality, and safety of posts.
- **Ranking**: Combines AI signals with author credibility and engagement metrics to rank posts.
- **Editorial Review**: Provides a manual review for edge cases like viral potential or borderline safety.
- **Transparency & Feedback**: Posts are labeled, tagged for relevant audiences, and allow for user feedback for constant improvement.

## Installation

### Clone the repository:
   ```bash
   git clone https://github.com/JenPal/news-ranking-system.git
   ```

### Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### Usage
To run the project, execute the following script:

```bash
python src/main.py
```
This will initialize the news ranking process and output the most relevant posts based on your specified criteria.

### Guardrails
This system incorporates strong guardrails to ensure fairness and safety, including:

- Multi-layer filtering
- Moderation APIs
- Editorial controls
- Transparency
- Regular bias and quality audits

### License
This project is licensed under the MIT License - see the LICENSE file for details.



Ask ChatGPT

