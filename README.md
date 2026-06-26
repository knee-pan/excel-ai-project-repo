# Excel AI Project

### AI-Powered Analysis for Existing Excel Files

![OpenAI](https://img.shields.io/badge/existing_excel_file-open_ai-pink)
![GitHub Repo](https://img.shields.io/badge/github-repo-blue?logo=github)

This project analyzes customer demand records stored in an Excel file and generates KPI reports using Artificial Intelligence.

The application reads an existing Excel file, categorizes requests, generates solution recommendations, and creates a new worksheet containing summarized metrics and insights.

---

## Features

For each record in the Excel file, AI can analyze:

* Category
* Responsible Team
* Solution Recommendation

The application automatically creates a new worksheet containing:

* Total Demand Count
* Category Distribution
* Team-Based Distribution
* Average Resolution Time
* Top 3 Most Active Employees
* Top Problems (Pareto Analysis)

---

## Excel Input Structure

| Customer | Request     | Status | Assignee | Category | Team    | Resolution     |
| -------- | ----------- | ------ | -------- | -------- | ------- | -------------- |
| ABC Ltd. | Login Issue | Closed | Ahmet    | Access   | Support | Password Reset |

---

## KPI Dashboard Example

| KPI                     | Value    |
| ----------------------- | -------- |
| Total Requests          | 120      |
| Open Requests           | 35       |
| Average Resolution Time | 3.2 Days |

---

## Top Users Example

| Assignee | Request Count |
| -------- | ------------- |
| Ahmet    | 32            |
| Zeynep   | 27            |
| Mehmet   | 21            |

---

## Project Structure

```text
excel-ai-project/
│
├── data/
│   └── talepler.xlsx
│
├── output/
│   └── talepler_ai.xlsx
│
├── services/
│   ├── ai_engine.py
│   └── kpi_engine.py
│
├── main.py
├── config.py
├── .env
└── requirements.txt
```

---

## Installation

Install the required packages:

```bash
pip install openai
pip install python-dotenv
```

Or install all dependencies using:

```bash
pip install -r requirements.txt
```

Verify installed packages:

```bash
pip show openai
pip show python-dotenv
```

---

## Environment Variables

Create a `.env` file in the project root directory and add your OpenAI API key:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

Example Python code:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print(api_key)
```

---

## Troubleshooting

If your API key is not being loaded:

1. Verify that the `.env` file is located in the project root directory.
2. Ensure the variable name is exactly:

```env
OPENAI_API_KEY=
```

3. Call `load_dotenv()` before accessing environment variables.
4. Check OpenAI error messages and response codes for additional details.
5. If you do not know excel sheet name:

***excel_file = pd.ExcelFile(file_path)***

***print(excel_file.sheet_names)***

6. If you encounter this error (<b>PermissionError: [Errno 13] Permission denied </b>) after running the project, <br>the Excel file is still open or is being used by someone else. Close Excel completely.


---

## Output

The application generates a new Excel file containing:

* KPI Dashboard
* Category Analysis
* Team Performance Metrics
* Top 3 Most Active Employees
* Pareto Analysis
* AI-Based Solution Recommendations

---

## Future Improvements

* Interactive Dashboard
* Automated Email Reports
* Power BI Integration
* Trend Analysis
* Excel Charts & Visualizations
* Multi-language AI Support

---

## License

This project is licensed under the MIT License.

[MIT LICENSE](https://choosealicense.com/licenses/mit/)
