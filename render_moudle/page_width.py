from notion.client import NotionClient
from notion import block
import datetime

def get_code(arg):
    code = ""

    if arg == "normal":
        code = """<!-- 사이트 width -->
<style>
/* 전체 */
:root .width {
	width: 1280px !important;
}
:root .padding{
	padding-left: 0 !important;
  padding-right: 0 !important;
}
</style>
"""

    return f"<!-- Created By NTBot (page_width) - {datetime.datetime.now()} -->\n" + code

def main(page, arg):
    new_block = page.children.add_new(block.CodeBlock, title=get_code(arg), language="html")
    new_block.move_to(page.children[1], "after")
    new_block.caption = f"oopy"

if __name__ == "__main__":
    print(main_html("main"))