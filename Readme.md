
# Python Automation and Chatbot Projects

This repository contains several simple yet practical Python projects demonstrating automation tasks and chatbot implementations with both command-line and GUI interfaces.  
**Note:** Each project file may contain multiple versions of the same task (e.g., CLI and GUI), with one active and others commented out.

---

## Projects Included

### 1. Hangman Game  
A classic word guessing game implemented in the command line.  
**Features:**  
- Random word selection  
- User input validation  
- Display of guessed letters and remaining attempts  

**Requirements:** None (standard Python)

**Note:** Different versions (if any) are contained in the same file with inactive ones commented out.

---

### 2. Stock Portfolio Tracker  
Track your stock investments with a simple CLI app and a GUI version with live prices via Alpha Vantage API.  
**Features:**  
- Input stocks and quantities  
- Calculate total portfolio value  
- Save portfolio to CSV  
- GUI version fetches live stock prices (requires API key)

**Requirements:**  
- For CLI: None (standard Python)  
- For GUI: `requests`, `pandas`, `tkinter` (usually pre-installed with Python)  
- Alpha Vantage API key for live prices: [Get your free API key here](https://www.alphavantage.co/support/#api-key)

Install dependencies via:  
```bash
pip install requests pandas
````

**Note:** Both CLI and GUI code versions exist in the same file; only one is active at a time.

---

### 3. Task Automation Tool (File Handling + Web Scraping)

A GUI tool to automate common tasks:

* Move all `.jpg` files from one folder to another
* Extract email addresses from a text file and save them
* Scrape and save the `<title>` of a webpage

**Features:**

* User-friendly Tkinter GUI
* File/folder selection dialogs
* Error handling for missing files or network errors

**Requirements:**

* `requests`
* `tkinter` (usually included in Python standard library)

Install dependencies via:

```bash
pip install requests
```

**Note:** Multiple task versions or implementations may be present in the same file with only one active.

---

### 4. Chatbot Applications

Three progressively sophisticated chatbots in one Python file to interact with users:

* **Basic chatbot:** simple rule-based replies (CLI or GUI)
* **Flexible keyword chatbot:** keyword matching for more natural replies (Tkinter GUI)
* **NLP-enhanced chatbot:** uses NLTK for tokenization and intent recognition (Tkinter GUI)

**Features:**

* Text-based interaction window
* Intent detection for greetings, farewells, and help
* Auto-close on goodbye messages

**Requirements:**

* For NLP chatbot: `nltk` and download the `punkt` tokenizer
* `tkinter` (usually included with Python)

Install dependencies via:

```bash
pip install nltk
python -c "import nltk; nltk.download('punkt')"
```

**Note:** All chatbot versions coexist in the same file; only one is uncommented to run at a time.

---

## How to Run

Each project has a main Python file. Run the active version inside it directly, for example:

* Hangman CLI:

```bash
python hangman.py
```

* Stock Portfolio Tracker (CLI or GUI, depending on active code):

```bash
python stock_tracker.py
```

* Task Automation Tool (GUI):

```bash
python task_automation.py
```

* Chatbot Application (basic, flexible, or NLP-enhanced based on uncommented section):

```bash
python chatbot.py
```

---

## requirements.txt example

```
requests
pandas
nltk
```

*Note:* `tkinter` is usually bundled with Python and does not need to be installed separately.

---

## License

This repository is provided as-is for learning and experimentation. Feel free to adapt and enhance!

---
## Developed by *Rafay Adeel*

