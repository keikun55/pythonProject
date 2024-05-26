from icrawler.builtin import BingImageCrawler
import streamlit as st
from PIL import Image
from icrawler.builtin import BingImageCrawler
import os, shutil
import glob

def crawling(keyword):
    folder_base = os.path.dirname(os.path.abspath(__file__))
    if os.path.exists(folder_base + "/image_crawling"):
        shutil.rmtree(folder_base + "/image_crawling")
    crawler = BingImageCrawler(storage={'root_dir': folder_base + '/image_crawling'})
    crawler.crawl(keyword=keyword, max_num=10)



def make_image_search():
    keyword = st.text_input("descript about image")
    if st.button("search"):
        crawling(keyword)
        files = glob.glob(os.path.dirname(os.path.abspath(__file__)) + "/image_crawling/*.jpg")
        print (files)
        for i, file in enumerate(files):
            img = Image.open(file)
            st.image(img, caption=f"画像{i + 1}")
if __name__ == "__main__":
    make_image_search()