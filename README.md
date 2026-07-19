# 📰 News Aggregator CLI

A lightweight **Command-Line News Aggregator** built with Python that fetches the latest news articles from **NewsAPI** based on a keyword. The application removes duplicate articles, saves the results as a JSON file, and optionally exports them to a CSV file.

---

## ✨ Features

- 🔎 Search news articles by keyword
- 🌐 Fetch real-time news using the NewsAPI
- 🚫 Remove duplicate articles
- 💾 Save news articles in JSON format
- 📊 Export news to CSV
- ⚡ Simple command-line interface
- 📦 Uses command-line arguments for flexibility

---

## 📋 Requirements

- 🐍 Python 3.x

### Required Python Libraries

Install the required packages:

```bash
pip install requests pandas
```

---

## 🔑 NewsAPI Key

This project uses the **NewsAPI** to fetch news articles.

1. Create a free account at **https://newsapi.org/**
2. Generate your API key.
3. Replace the existing key with your own:

```python
API_KEY = "YOUR_API_KEY"
```

---

## 🚀 How to Run

1. Make sure **Python 3** is installed.
2. Install the required libraries.
3. Add your NewsAPI key.
4. Open a terminal in the project directory.
5. Run the program.

### Search using the default keyword (`technology`)

```bash
python news_aggregator.py
```

### Search using a custom keyword

```bash
python news_aggregator.py --keyword artificial intelligence
```

### Export results to CSV

```bash
python news_aggregator.py --keyword sports --export csv
```

> **Note:** If your system uses `python3`, replace `python` with `python3`.

---

## 💻 Example Output

```text
Done! Total articles: 25
```

The program automatically creates:

- 📄 `news.json`
- 📊 `news.csv` (when `--export csv` is used)

---

## 📁 Project Structure

```text
News-Aggregator-CLI/
│
├── news_aggregator.py
├── news.json
├── news.csv
└── README.md
```

---

## ⚙️ Command-Line Arguments

| Argument | Description |
|----------|-------------|
| `--keyword` | 🔎 Search news using a specific keyword |
| `--export csv` | 📊 Export fetched news to a CSV file |

### Examples

```bash
python news_aggregator.py --keyword technology
```

```bash
python news_aggregator.py --keyword business --export csv
```

```bash
python news_aggregator.py --keyword science
```

---

## 📂 Output Files

### 📄 JSON Output

Stores complete article information.

```text
news.json
```

### 📊 CSV Output

Contains:

- 📰 Title
- 🏢 Source
- 📅 Published Date

```text
news.csv
```

---

## ⚙️ Functions

| Function | Purpose |
|----------|---------|
| `fetch_news()` | 🌐 Fetches news articles from NewsAPI |
| `remove_duplicates()` | 🚫 Removes duplicate articles based on title |
| `save_json()` | 💾 Saves articles as a JSON file |
| `export_csv()` | 📊 Exports selected article information to CSV |
| `main()` | 🎯 Handles command-line arguments and program execution |

---

## 🛡️ Error Handling

The application handles:

- ⚠️ No news articles found
- 🚫 Duplicate news removal
- 📋 API response parsing
- ❌ Invalid command-line arguments

---

## 🛠️ Technologies Used

- 🐍 Python
- 🌐 Requests
- 📊 Pandas
- 📄 JSON
- ⚙️ Argparse
- 📰 NewsAPI

---

## 🚀 Future Improvements

- 🌍 Filter news by country
- 🗂️ Filter by category
- 📰 Display article descriptions in the terminal
- 🔗 Open articles directly in the browser
- 📅 Filter by publication date
- 📈 Export to Excel or PDF
- 🖥️ Interactive terminal interface
- 🌐 GUI/Web version using Flask

---

## 👨‍💻 Author

**Muhammad Hanzla**

---

⭐ If you found this project useful, consider giving it a **star** on GitHub!
