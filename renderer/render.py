from config import config
from notion.client import NotionClient
import time
import threading
import yaml

start_time = time.time()

client = NotionClient(token_v2=config["token_v2"])

pages = []
def render_yaml(page:object):
    page = client.get_block(page.id)
    if not page.children: return
    page_setting = yaml.load(page.children[0].title)
    print(page_setting)

def get_all_pages(page_url_or_id:str):
    # 페이지의 모든 하위 페이지의 링크를 가져옴
    page = client.get_block(page_url_or_id)

    for child in page.children:
        if child.type == 'page':
            print(f"[{child.type}] {child.title} ({child.id})")
            pages.append(child.id)
            render_yaml(child)
            get_all_pages(child.id)

        elif child.type == 'collection_view':
            for row in child.collection.get_rows():
                print(f"[{row.type}] [{child.title}] {row.title} ({row.id})")
                pages.append(child.id)
                render_yaml(child)
                get_all_pages(row.id)

        else:
            get_all_pages(child.id)
    return pages

a = get_all_pages(config['root_page_url'])


print(f"작업 소요 시간 : {time.time() - start_time}s")
