import requests
from bs4 import BeautifulSoup
import argparse
import csv
from urllib.parse import urljoin, urlparse
from collections import Counter
import concurrent.futures

FILE_EXTENSIONS = {
    'pdf', 'txt', 'png', 'jpg', 'jpeg', 'gif', 'svg',
    'zip', 'tar', 'gz', 'xls', 'xlsx', 'doc', 'docx',
    'ppt', 'pptx', 'json', 'xml', 'csv', 'msg', 'rtf',
    'dat', 'apk', 'exe', 'wav', 'mp3', 'webm', 'mov',
    'mp4', 'ogg', 'css', 'js', 'cpp', 'c', 'php',
    'go', 'rb', 'jar', 'iso', 'vtt', 'srt'
}

def extract_file_links(url, domain, maxdepth=2, depth=0, visited=None, files=None, workers=5):
    if visited is None:
        visited = set()
    if files is None:
        files = set()

    if depth > maxdepth or url in visited:
        return files

    visited.add(url)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return files

    soup = BeautifulSoup(response.text, "html.parser")

    links = set()
    for a in soup.find_all("a", href=True):
        link = urljoin(url, a['href'])

        parsed = urlparse(link)
        if parsed.netloc == domain or parsed.netloc == '':

            if link.split('.')[-1].lower() in FILE_EXTENSIONS:
                files.add(link)
            elif depth < maxdepth:
                links.add(link)

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(extract_file_links, link, domain, maxdepth, depth+1, visited, files, workers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            future.result()

    return files


def main():
    parser = argparse.ArgumentParser(
        description='Website File Spider',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Example:\n  python filespider.py -u http://example.com -o files.csv -d 2 -w 10'
    )
    parser.add_argument('-u', '--url', help='Target website (required)', required=True)
    parser.add_argument('-o', '--output', help='CSV output file')
    parser.add_argument('-d', '--depth',
                        help='Crawling depth (integer).\n'
                             'depth 0 = starting URL\n'
                             'depth 1 = starting URL + links from it\n'
                             'depth 2 = starting URL + links from those links, and so on.',
                        default=2, type=int)
    parser.add_argument('-w', '--workers',
                        help='Thread pool workers (integer).\n'
                             '(from 1 to 10) Higher = faster, but more load on server.',
                        default=5, type=int)

    args = parser.parse_args()

    parsed = urlparse(args.url)
    domain = parsed.netloc

    files = extract_file_links(args.url, domain=domain, maxdepth=args.depth, workers=args.workers)
    print(f"Files found on {args.url}:")

    for f in files:
        print(f)

    # Count by extension
    counter = Counter([f.split('.')[-1].lower() for f in files])

    print("\nFiles found by extension:")
    for ext, count in counter.items():
        print(f"{ext}: {count}")

    print(f"\nTotal files found: {len(files)}")

    if args.output:
        with open(args.output, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Files'])

            for f in files:
                writer.writerow([f])

        print(f"Files successfully saved to CSV {args.output}")

    print("\nTool by LEGIT")
    print("Instagram: @th3cyberside")
    print("LinkedIn: https://www.linkedin.com/in/krishna-patwa/")


if __name__ == "__main__":
    main()
