import argparse
import aiohttp
import asyncio
from collections import Counter
import re


async def fetch_url(sessia, url):
    async with sessia.get(url) as step:
        text = await step.text()
        return re.findall(r'\b\w+\b', text.lower())


async def fetch_all_urls(all_urls, concurrent):
    async with aiohttp.ClientSession() as sessia:
        sem = asyncio.Semaphore(concurrent)
        tasks = []
        async with sem:
            for url in all_urls:
                tasks.append(fetch_url(sessia, url))
        return await asyncio.gather(*tasks)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', type=int)
    parser.add_argument('urls_file', type=argparse.FileType('r'))
    args = parser.parse_args()
    all_urls = []
    for url in args.urls_file.readlines():
        all_urls.append(url)

    loop = asyncio.get_event_loop()
    fetch = fetch_all_urls(all_urls, args.c)
    steps = loop.run_until_complete(fetch)

    all_words = []
    for step in steps:
        all_words.extend(step)

    top_words = Counter(all_words).most_common(3)
    print("Top 3 words in urls:")
    for word, count in top_words:
        print(f"'{word}': {count}")


if __name__ == '__main__':
    main()
