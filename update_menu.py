import os
import re

new_menu_template = """<li>
    <a class="menu-item" href="about.html">ABOUT US</a>
    <ul>
        <li><a href="about.html"><span class="d-menu-title">About Company</span><span class="d-menu-sub">Discover our story</span></a></li>
        <li><a href="about.html#team"><span class="d-menu-title">Our Team</span><span class="d-menu-sub">Meet our experts</span></a></li>
    </ul>
</li>
<li>
    <a class="menu-item" href="services.html">SERVICES</a>
    <ul>
        <li><a href="services.html#SEO"><span class="d-menu-title">SEO</span><span class="d-menu-sub">Local SEO & GMB Optimization</span></a></li>
        <li><a href="services.html#content-marketing"><span class="d-menu-title">Content Marketing</span><span class="d-menu-sub">Creative Copy & Campaigns</span></a></li>
        <li><a href="services.html#ads"><span class="d-menu-title">Paid Media</span><span class="d-menu-sub">Google & Meta Ads Strategy</span></a></li>
        <li><a href="services.html#social-media"><span class="d-menu-title">Social Media</span><span class="d-menu-sub">Handling & Engagement</span></a></li>
        <li><a href="services.html#web"><span class="d-menu-title">Web Design</span><span class="d-menu-sub">Responsive & E-commerce</span></a></li>
        <li><a href="services.html#graphic-design"><span class="d-menu-title">Graphic Design</span><span class="d-menu-sub">Logos & Branding</span></a></li>
    </ul>
</li>"""

def align_text(template, indent):
    lines = template.split('\n')
    indented_lines = []
    base_spaces = 0
    for idx, line in enumerate(lines):
        if idx == 0:
            indented_lines.append(indent + line)
        else:
            indented_lines.append(indent + line)
    return '\n'.join(indented_lines)

html_files = ["index.html", "about.html", "contact.html", "plans.html", "portfolio.html", "services.html"]
base_dir = "c:/Users/user/Desktop/Hexa-ReachSolution-website/"

pattern = re.compile(r'([ \t]*)<li>\s*<a class="menu-item" href="about\.html">ABOUT US</a>.*?<a class="menu-item" href="services\.html">SERVICES</a>[^<]*<ul>.*?</ul>\s*</li>', re.DOTALL)

for file in html_files:
    file_path = os.path.join(base_dir, file)
    with open(file_path, "r", encoding='utf-8') as f:
        content = f.read()

    def replacer(match):
        indent = match.group(1)
        return align_text(new_menu_template, indent).replace("<li>\n" + indent, "<li>\n")

    new_content, count = pattern.subn(replacer, content)
    
    if count > 0:
        with open(file_path, "w", encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"No match found in {file}")

