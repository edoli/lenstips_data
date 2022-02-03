import os

def build():
    lens_names = [name for name in os.listdir('data') if os.path.isdir(os.path.join('data', name))]

    inner_html = ''
    for lens_name in lens_names:
        lens_imgs = os.listdir(os.path.join('data', lens_name))
        row_html = f'<tr><td><div class="name">{lens_name}</div></td><td>'
        row_html += ''.join([f'<img src="{lens_name}/{lens_img}" />' for lens_img in lens_imgs])
        row_html += '</td></tr>'

        inner_html += row_html


    html = f'''
<!doctype html>

<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>A Basic HTML5 Template</title>
    <meta name="description" content="Lens data">
    <meta name="author" content="edoli">

    <meta property="og:title" content="Lens data">
    <meta property="og:type" content="website">
    <meta property="og:description" content="Lens data">
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <table border="1">
	<th>이름</th>
	<th>이미지들</th>
    {inner_html}
    </table>    
</body>
</html>
    '''

    f = open('data/index.html', 'w', encoding='utf8')
    f.write(html)
    f.close()

def main():
    build()


if __name__ == '__main__':
    build()