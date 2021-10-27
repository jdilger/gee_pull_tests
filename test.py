# test.py

from contributions.render_html import create_graph
test = create_graph([r"repo_count.txt"])
print(type(test))

with open('test.html','w') as f:
    f.writelines(test)
