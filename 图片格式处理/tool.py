import re

def replace_images(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'!\[(.*?)\]\((.*?)\)'
    matches = re.findall(pattern, content)

    replaced_content = content
    image_counter = 1
    for match in matches:
        old_syntax = match[0]
        image_path = match[1]
        new_syntax = '{%% asset_img %d.png %%}' % image_counter
        replaced_content = replaced_content.replace('![%s](%s)' % (old_syntax, image_path), new_syntax, 1)
        image_counter += 1

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(replaced_content)

# Example usage:
replace_images('input.md', 'output.md')