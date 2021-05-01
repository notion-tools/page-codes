from notion.client import NotionClient
from notion import block
import datetime

def get_code(arg):
    code = """<!-- 뒤로가기 버튼 -->

<style>
	#back {
    position: fixed;
    left: 50px;
    top: 100px;
    font-size: 32px;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 40px;
    box-sizing: border-box;
    transition: background-color 200ms;
    color: #000;
    text-decoration: none;
}

#back:hover {
        background-color: #f0f0f0;
    }
</style>

<a id="back" href="javascript:history.back()"><svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="#000000" viewBox="0 0 256 256"><rect width="256" height="256" fill="none"></rect><line x1="216" y1="128" x2="40" y2="128" fill="none" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="24"></line><polyline points="112 56 40 128 112 200" fill="none" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="24"></polyline></svg></a>"""

    return f"<!-- Created By NTBot (page_width) - {datetime.datetime.now()} -->\n" + code

def main(page, arg):
    if arg:
        new_block = page.children.add_new(block.CodeBlock, title=get_code(arg), language="html")
        new_block.move_to(page.children[1], "after")
        new_block.caption = f"oopy"

if __name__ == "__main__":
    print(main_html("main"))