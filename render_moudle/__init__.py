import os
moudle = []
for i in os.listdir('render_moudle'):
    if not i.startswith("__"):
        moudle.append(i.replace(".py", ""))
__all__ = moudle