#! python3
"""
Project:    Sandbox
Filename:   scrape
Created by: PJC
Created on: December 14, 2016
"""

from bs4 import BeautifulSoup
import argparse
import base64
import json
import logging
import os
import requests


# Setup logging.  Display INFO messages and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)


def scrape(url, save_format, image_type):
    try:

        page = requests.get(url)

    except requests.RequestException as rex:

        logger.info(str(rex))

    else:

        web_page = BeautifulSoup(page.content, 'html.parser')
        images = fetch_images(web_page, url)
        images = filter_images(images, image_type)
        save(images, save_format)


def fetch_images(web_page, base_url):
    images = []
    for image in web_page.findAll('img'):

        image_source = image.get('src')
        image_url = ('{base_url}/{src}'.format(base_url=base_url, src=image_source))
        name = image_url.split('/')[-1]
        images.append(dict(name=name, url=image_url))

    return images


def filter_images(images, image_type):
    if image_type == 'all':

        return images

    ext_map = {'png': ['.png'], 'jpg': ['.jpg', '.jpeg'], 'gif': ['.gif']}
    return [img for img in images if matches_extension(img['name'], ext_map[image_type])]


def matches_extension(filename, extension_list):

    name, extension = os.path.splitext(filename.lower())
    return extension in extension_list


def save(images, save_format):
    if images:

        if save_format == 'img':

            save_images(images)

        else:

            save_json(images)

        logger.info('Done')

    else:

        logger.info('No images to save.')


def save_images(images):
    for image in images:

        image_data = requests.get(image['url']).content
        with open(image['name'], 'wb') as image_file:

            image_file.write(image_data)


def save_json(images):
    data = {}
    for image in images:

        image_data = requests.get(image['url']).content
        b64_image_data = base64.b64encode(image_data)
        str_image_data = b64_image_data.decode('utf-8')
        data[image['name']] = str_image_data

    with open('images.json', 'w') as json_file:

        json_file.write(json.dumps(data))


def main():

    parser = argparse.ArgumentParser(
        description='Scrape a webpage.')

    parser.add_argument(
        '-t',
        '--type',
        choices=['all', 'png', 'jpg', 'gif'],
        default='all',
        help='The image type to scrape.')

    parser.add_argument(
        '-f',
        '--format',
        choices=['img', 'json'],
        default='img',
        help='The format images are saved to.')

    parser.add_argument(
        'url',
        help='The URL to scrape for images.')

    args = parser.parse_args()
    scrape(args.url, args.format, args.type)


if __name__ == '__main__':
    main()
