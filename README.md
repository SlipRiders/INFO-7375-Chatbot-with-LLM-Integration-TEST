# ACM Algorithm Template Query System
Name:Xiaoyang chen INFO7375 Assignment
This repository contains a Streamlit-based web application that allows users to query for algorithm templates. The application uses OpenAI's GPT-3.5-turbo model to validate algorithm names and provide code templates in Java.

## Features

- Validate if an algorithm name is recognized.
- Provide Java code templates for valid algorithms.
- Maintain a chat history of user queries and responses.
- Clear chat history with a single button click.

## Setup Instructions

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or later
- An OpenAI API key

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/SlipRiders/INFO-7375-Chatbot-with-LLM-Integration-TEST.git
cd algorithm-template-query-system
```
2. **Create and activate a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
​	3.**Install the required dependencies:**

```bash
pip install -r requirements.txt
```

### Configuration

1. **Set up OpenAI API key:**

   Create a `.env` file in the root directory of the project and add your OpenAI API key:

### Running the Application

1. **Start the Streamlit application**
2. **Open your web browser and navigate to**

```
streamlit run app.py
http://localhost:8501
```

### Usage

- **Input your algorithm query:** Type the name of the algorithm you are interested in the text input box.
- **Query:** Click the 'Query' button to validate the algorithm name and get the code template if valid.
- **View chat history:** The application will display a history of your queries and responses.
- **Clear cache:** Click the 'Clear Cache' button to reset the chat history.

### Example

1. **Input:** "Binary Search"
2. **Query:** Click 'Query'
3. **Output:** The application will display the Java code template for Binary Search.

### Troubleshooting

- **Invalid Algorithm Name:** If the algorithm name is not recognized, the application will prompt you to input a valid algorithm name.
- **API Key Issues:** Ensure your OpenAI API key is correctly set in the `.env` file or as an environment variable.

### Contributing

Contributions are welcome! Please create an issue or submit a pull request for any features, bug fixes, or enhancements.

### License

This project is licensed under the MIT License. See the LICENSE file for details.
