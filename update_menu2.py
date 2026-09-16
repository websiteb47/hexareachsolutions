import os

html_files = ["index.html", "about.html", "contact.html", "plans.html", "portfolio.html", "services.html"]
base_dir = "c:/Users/user/Desktop/Hexa-ReachSolution-website/"

target_8_spaces = """        <li>
            <a class="menu-item" href="about.html">ABOUT US</a>
            <ul>
                <li><a href="about.html">About Company</a></li>
                <li><a href="about.html#team">Our Team</a></li>
            </ul>
        </li>

        <li>
            <a class="menu-item" href="services.html">SERVICES</a>
            <ul>
                <li><a href="services.html#social-media"><i class="ri-megaphone-line"></i> Social Media Marketing</a></li>
                <li><a href="services.html#branding"><i class="ri-award-line"></i> Brand Promotions</a></li>
                <li><a href="services.html#graphic-design"><i class="ri-palette-line"></i> Graphic Designing</a></li>
                <li><a href="services.html#ads"><i class="ri-line-chart-line"></i> Sponsored Ads</a></li>
                <li><a href="services.html#business-profile"><i class="ri-building-line"></i> Business Pages</a></li>
                <li><a href="services.html#podcast"><i class="ri-mic-line"></i> Podcast Marketing</a></li>
                <li><a href="services.html#digital-podcast"><i class="ri-radio-line"></i> Digital Podcast</a></li>
                <li><a href="services.html#whatsapp"><i class="ri-whatsapp-line"></i> WhatsApp API</a></li>
                <li><a href="services.html#SEO"><i class="ri-search-eye-line"></i> SEO</a></li>
                <li><a href="services.html#web"><i class="ri-code-box-line"></i> Web Design & Hosting</a></li>
                <li><a href="services.html#video-editing"><i class="ri-movie-line"></i> Video Editing</a></li>
                <li><a href="services.html#content-marketing"><i class="ri-article-line"></i> Content Marketing</a></li>
            </ul>
        </li>"""

replacement_8_spaces = """        <li>
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

target_40_spaces = """                                        <li>
                                            <a class="menu-item" href="about.html">ABOUT US</a>
                                            <ul>
                                                <li><a href="about.html">About Company</a></li>
                                                <li><a href="about.html#team">Our Team</a></li>
                                            </ul>
                                        </li>

                                        <li>
                                            <a class="menu-item" href="services.html">SERVICES</a>
                                            <ul>
                                                <li><a href="services.html#social-media"><i class="ri-megaphone-line"></i> Social Media Marketing</a></li>
                                                <li><a href="services.html#branding"><i class="ri-award-line"></i> Brand Promotions</a></li>
                                                <li><a href="services.html#graphic-design"><i class="ri-palette-line"></i> Graphic Designing</a></li>
                                                <li><a href="services.html#ads"><i class="ri-line-chart-line"></i> Sponsored Ads</a></li>
                                                <li><a href="services.html#business-profile"><i class="ri-building-line"></i> Business Pages</a></li>
                                                <li><a href="services.html#podcast"><i class="ri-mic-line"></i> Podcast Marketing</a></li>
                                                <li><a href="services.html#digital-podcast"><i class="ri-radio-line"></i> Digital Podcast</a></li>
                                                <li><a href="services.html#whatsapp"><i class="ri-whatsapp-line"></i> WhatsApp API</a></li>
                                                <li><a href="services.html#SEO"><i class="ri-search-eye-line"></i> SEO</a></li>
                                                <li><a href="services.html#web"><i class="ri-code-box-line"></i> Web Design & Hosting</a></li>
                                                <li><a href="services.html#video-editing"><i class="ri-movie-line"></i> Video Editing</a></li>
                                                <li><a href="services.html#content-marketing"><i class="ri-article-line"></i> Content Marketing</a></li>
                                            </ul>
                                        </li>"""

replacement_40_spaces = """                                        <li>
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

for file in html_files:
    file_path = os.path.join(base_dir, file)
    with open(file_path, "r", encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace(target_8_spaces, replacement_8_spaces)
    new_content = new_content.replace(target_40_spaces, replacement_40_spaces)
    
    if new_content != content:
        with open(file_path, "w", encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"No match found in {file}")
