#! python3
"""
Project:    Sandbox
Filename:   gui_scrape
Created by: PJC
Created on: December 14, 2016
"""

from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import base64
import json
import logging
import os
import re
import requests


# Setup logging.  Display INFO messages and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)

config = {}


def fetch_url():

    url_to_fetch = url.get()
    config['images'] = []
    images.set(())   # initialized as an empty tuple

    try:

        page = requests.get(url_to_fetch)

    except requests.RequestException as rex:

        set_status_box(str(rex))

    else:

        soup = BeautifulSoup(page.content, 'html.parser')
        page_images = fetch_images(soup, url_to_fetch)

        if page_images:

            images.set(tuple(img['name'] for img in page_images))
            set_status_box('Images found: {}'.format(len(page_images)))

        else:

            set_status_box('No images found')

        config['images'] = page_images


def fetch_images(soup, base_url):

    page_images = []
    for image in soup.findAll('img'):

        source = image.get('src')
        image_url = ('{base_url}/{src}'.format(base_url=base_url, src=source))
        name = image_url.split('/')[-1]

        if re.search('.*\.png|\.jpg|\.gif$', name):

            page_images.append(dict(name=name, url=image_url))

    return page_images


def save():

    if not config.get('images'):

        alert('No images to save')

        return

    if save_method.get() == 'img':

        directory_name = filedialog.askdirectory(mustexist=True)
        save_images(directory_name)

    else:

        filename = filedialog.asksaveasfilename(initialfile='images.json', filetypes=[('JSON', '.json')])
        save_json(filename)


def save_images(directory_name):

    if directory_name and config.get('images'):

        for image in config['images']:

            image_data = requests.get(image['url']).content
            filename = os.path.join(directory_name, image['name'])

            with open(filename, 'wb') as image_file:

                image_file.write(image_data)

        alert('Done')


def save_json(filename):
    if filename and config.get('images'):
        data = {}
        for img in config['images']:
            img_data = requests.get(img['url']).content
            b64_img_data = base64.b64encode(img_data)
            str_img_data = b64_img_data.decode('utf-8')
            data[img['name']] = str_img_data

        with open(filename, 'w') as ijson:
            ijson.write(json.dumps(data))
        alert('Done')


def set_status_box(message):
    status_message.set(message)


def alert(message):
    messagebox.showinfo(message=message)


if __name__ == '__main__':

    # Set up and name main window
    root = Tk()
    root.title('Scrape Images')

    # Set up the main frame and configure placement and size
    mainframe = ttk.Frame(root, padding='5 5 5 5')
    mainframe.grid(row=0, column=0, sticky=(E, W, N, S))

    # Set up the URL frame and configure placement and size
    url_frame = ttk.LabelFrame(mainframe, text='URL', padding='5 5 5 5')
    url_frame.grid(row=0, column=0, sticky=(E, W))
    url_frame.columnconfigure(0, weight=1)
    url_frame.rowconfigure(0, weight=1)

    # Set up the URL frame elements
    url = StringVar()
    url.set('http://groucho.dev.techstreet.com')
    url_entry = ttk.Entry(url_frame, width=40, textvariable=url)
    url_entry.grid(row=0, column=0, sticky=(E, W, S, N), padx=5)
    fetch_btn = ttk.Button(url_frame, text='Fetch info', command=fetch_url)
    fetch_btn.grid(row=0, column=1, sticky=W, padx=5)

    # Set up the image frame and configure placement and size
    image_frame = ttk.LabelFrame(mainframe, text='Content', padding='9 0 0 0')
    image_frame.grid(row=1, column=0, sticky=(N, S, E, W))

    # Set up the image frame elements
    images = StringVar()
    image_listbox = Listbox(image_frame, listvariable=images, height=6, width=25)
    image_listbox.grid(row=0, column=0, sticky=(E, W), pady=5)
    scrollbar = ttk.Scrollbar(image_frame, orient=VERTICAL, command=image_listbox.yview)
    scrollbar.grid(row=0, column=1, sticky=(S, N), pady=6)
    image_listbox.configure(yscrollcommand=scrollbar.set)

    # Set up the radio frame and configure placement and size
    radio_frame = ttk.Frame(image_frame)
    radio_frame.grid(row=0, column=2, sticky=(N, S, W, E))

    # Set up the radio frame elements
    choice_lbl = ttk.Label(radio_frame, text="Choose how to save images")
    choice_lbl.grid(row=0, column=0, padx=5, pady=5)
    save_method = StringVar()
    save_method.set('img')
    image_only_radio = ttk.Radiobutton(radio_frame, text='As Images', variable=save_method, value='img')
    image_only_radio.grid(row=1, column=0, padx=5, pady=2, sticky=W)
    image_only_radio.configure(state='normal')
    json_radio = ttk.Radiobutton(radio_frame, text='As JSON', variable=save_method, value='json')
    json_radio.grid(row=2, column=0, padx=5, pady=2, sticky=W)

    # Add the Scape button to the main frame
    scrape_btn = ttk.Button(mainframe, text='Scrape!', command=save)
    scrape_btn.grid(row=2, column=0, sticky=E, pady=5)

    # Set up the status frame and configure placement and size
    status_frame = ttk.Frame(root, relief='sunken', padding='2 2 2 2')
    status_frame.grid(row=1, column=0, sticky=(E, W, S))
    status_message = StringVar()
    status_message.set('Type a URL to start scraping...')
    status = ttk.Label(status_frame, textvariable=status_message, anchor=W)
    status.grid(row=0, column=0, sticky=(E, W))

    # Run the application
    root.mainloop()
