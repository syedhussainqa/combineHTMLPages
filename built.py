print('Building a site - Execution begins')
top_html = open('templates/top.html').read()
middle1_html = open('content/index.html').read()
middle2_html = open('content/project.html').read()
middle3_html = open('content/blog.html').read()
bottom_html = open('templates/bottom.html').read()
print('Building a site - Execution ends')


combine_html = top_html + middle1_html + middle3_html + bottom_html
open('output_file.html', 'w+').write(combine_html)
