def search_and_download(search_term: str, driver_path: str, target_path='./images', number_images=10):
    target_folder = os.path.join(target_path, '_'.join(search_term.lower().split(' '))) # make the folder name inside images with the search string

    if not os.path.exists(target_folder):
        os.makedirs(target_folder) # make directory using the target path if it doesn't exist already

    with webdriver.Chrome(executable_path=driver_path) as wd:
        res = fetch_image_urls(search_term, number_images, wd=wd, sleep_between_interactions=0.5)

    counter = 0
    for elem in res:
        persist_image(target_folder, elem, counter)
        counter += 1
import os,time, requests
from selenium import webdriver

DRIVER_PATH = './chromedriver'
search_term = 'apple'
# num of images you can pass it from here  by default it's 10 if you are not passing
# number_images = 10
search_and_download(search_term=search_term, driver_path=DRIVER_PATH) # method to download images