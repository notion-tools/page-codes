from config import config
from notion.client import NotionClient
import time, threading, yaml, datetime, importlib, os, yaml
from render_moudle import *

client = NotionClient(token_v2=config["token_v2"])

moudle = []
for i in os.listdir('render_moudle'):
    if not i.startswith("__"):
        moudle.append(i.replace(".py", ""))

def render_page(page):
    """ 페이지의 설정을 가져와 적용하는 함수
    인자 : 노션 페이지 객체
    """

    print(f"[{threading.currentThread().getName()}] [{page.type}] {page.title} ({page.id})")
    if not page.children: return
    page.children[0].caption = f"Rendering..."

    # 페이지 설정 가져오기
    page_setting = yaml.load(page.children[0].title, Loader=yaml.BaseLoader)

    # 코드 init(초기화)
    for i in page.children:
        if i.type == "code" and (i.title.startswith("<!-- Created By NTBot") or i.caption.startswith("[Created By NTBot]")):
            i.remove()
    
    # 속성별 코드
    if "page_category" in page_setting.keys():
        exec(f"page_category.main(page, page_setting['page_category'])", None, locals())

    for i in page_setting.keys():
        if i in moudle and i != "page_category":
            exec(f"{i}.main(page, page_setting[i])", None, locals())

    # 마무리 
    page.children[0].caption = f"Last Render : {datetime.datetime.now()}"

    return 

def get_all_pages(page_url_or_id:str):
    # 페이지의 모든 하위 페이지의 링크를 가져옴
    # 주의 : 최상위 페이지의 정보는 가져오지 않음
    page = client.get_block(page_url_or_id)

    if page.type == "page":
        t = threading.Thread(target=render_page, args=(page,))
        t.start()
    
    for child in page.children:
        if child.type == 'collection_view': # 데이터베이스 하위 페이지 가져오기
            for row in child.collection.get_rows():
                get_all_pages(row.id)
        else:
            get_all_pages(child.id)

if __name__ == "__main__":
    get_all_pages(config['root_page_url'])

