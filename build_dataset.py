from FileIO import read_html, write_string_to_file
from requests.exceptions import MissingSchema

sample_urls = [
    "https://en.wikipedia.org/wiki/Computer_science",
    "https://en.wikipedia.org/wiki/Information_retrieval",
    "https://en.wikipedia.org/wiki/Natural-language_processing",
    "https://en.wikipedia.org/wiki/Dog",
    "sfa"
]

if __name__ == "__main__":
    for url in sample_urls:
        filename = "dataset/%s.txt" % url.split("/")[-1]
        try:
            text = read_html(url)
            filename = "dataset/%s.txt" % url.split("/")[-1]
            write_string_to_file(text, filename)
        except MissingSchema as e:
            print(e)
        except Exception as e:
            print(e)

