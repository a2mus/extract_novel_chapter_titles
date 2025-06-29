# Novel Chapter Extractor

## Description
The Novel Chapter Extractor is a Python application designed to extract chapter content from online novels, providing a convenient way to save them for offline reading or analysis. It features a graphical user interface (GUI) for ease of use.

## Features
*   **Graphical User Interface (GUI):** User-friendly interface for easy interaction.
*   **Chapter Extraction:** Automatically extracts chapter content from specified novel URLs.
*   **Saves to Markdown:** Extracted content can be saved in Markdown format for portability and readability.
*   **Dynamic Content Handling:** Capable of handling dynamically loaded content on web pages.

## Requirements
*   Python 3.x
*   A modern web browser (e.g., Google Chrome, Mozilla Firefox)

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your_username/extract_novel_chapter_titles.git
    cd extract_novel_chapter_titles
    ```
    (Replace `your_username` with the actual GitHub username if this project is hosted on GitHub.)

2.  **Install dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Download and set up the appropriate WebDriver:**
    The application uses Selenium, which requires a WebDriver for your browser.
    *   **ChromeDriver:** For Google Chrome. Download from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads). Make sure the WebDriver version matches your Chrome browser version.
    *   **GeckoDriver:** For Mozilla Firefox. Download from [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases).
    Place the downloaded WebDriver executable in your system's PATH or in the project directory.

## Usage

1.  **Run the application:**
    ```bash
    python main.py
    ```
2.  **Using the GUI:**
    *   Enter the URL of the novel you wish to extract.
    *   Select output options (e.g., save format, destination).
    *   Click the "Extract" or "Start" button to begin the process.

## Troubleshooting

*   **WebDriver Mismatch:** If you encounter issues, ensure that the version of your WebDriver (e.g., ChromeDriver) precisely matches the version of your installed web browser. Update either the browser or the WebDriver as necessary.
*   **Browser Not Found:** Make sure your chosen web browser is installed and accessible from your system's PATH.
*   **Dependency Issues:** If the application fails to start or throws import errors, ensure all dependencies listed in `requirements.txt` are correctly installed.