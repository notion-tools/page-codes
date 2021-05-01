from notion.client import NotionClient
from notion import block
import datetime

def main_html(category):
    with open("global/main.html", "r", encoding="utf-8") as f:
        code = f.read()
        if category == "main":
            code = code.replace("[1]", "top-nav-btn-selected")
        elif category == "page":
            code = code.replace("[2]", "top-nav-btn-selected")
        elif category == "template":
            code = code.replace("[3]", "top-nav-btn-selected")
        elif category == "embed":
            code = code.replace("[4]", "top-nav-btn-selected")
        code = code.replace("[1]", "")
        code = code.replace("[2]", "")
        code = code.replace("[3]", "")
        code = code.replace("[4]", "")


        return code

def main(page, arg):
    new_block = page.children.add_new(block.CodeBlock, title=main_html(arg), language="html")
    new_block.move_to(page.children[0], "after")
    new_block.caption = f"[Created By NTBot] {datetime.datetime.now()}"

if __name__ == "__main__":
    print(main_html("main"))