# File Spider — File Scraper Tool

![File Spider](https://raw.githubusercontent.com/Legit1101/File-Spider/main/IMG_6149.PNG)


## Description

File Spider is a tool designed to scan a website and extract files of various types (like PDF, TXT, PNG, DOC, ZIP, CSV, etc.).
It performs a recursive scan up to a specified depth, retrieving links to files along with their count by file format.
It’s a helpful tool for bug bounty hunters, penetration testers, or anyone who wants to gather files from a website.

## Features

* Crawls a website up to a specified depth.
* Detects files by their extensions.
* Prints a count of files by their format.
* Saves results to CSV if needed.
* Allows multithreading (with multiple workers) for faster scanning.
* Measures execution time for the scan.

## File Types Supported:

- pdf, txt, png, jpg, jpeg, gif, svg
- zip, tar, gz
- xls, xlsx, doc, docx, ppt, pptx
- json, xml, csv, msg, rtf, dat, apk, exe
- wav, mp3, webm, mov, mp4, ogg
- css, js, cpp, c, php, go, rb, jar, iso, vtt, srt

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/YOUR_USERNAME/File-Spider.git
   ```
2. Change directory:

   ```
   cd File-Spider
   ```
3. Install prerequisites:

   ```
   pip install -r requirements.txt
   ```

## Requirements (requirements.txt)

```
beautifulsoup4
requests
```

## Usage

```
python filespider.py -u <URL> -d <DEPTH> -o <FILE> -w <WORKERS>
```

**Arguments:**

* `-u, --url`: Target website (required).
* `-d, --depth`: Crawling depth (integer). (Default: 2)
* `-o, --output`: CSV output file (optional).
* `-w, --workers`: Number of threads for faster scanning (Default: 5)

**Example:**

python filespider.py -u https://example.com -d 2 -o files.csv -w 10

## Contact

Instagram: [@th3cyberside](https://instagram.com/th3cyberside)
LinkedIn: [Krishna Patwa](https://www.linkedin.com/in/krishna-patwa/)

