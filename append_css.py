import os
with open("c:/Users/user/Desktop/Hexa-ReachSolution-website/css/style.css", "a", encoding="utf-8") as f:
    f.write("""\n
/* Dropdown Menu Subtitles Styling (Requested Design) */
#mainmenu ul ul {
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    padding: 15px 0 !important;
    width: 250px;
}

#mainmenu ul ul li {
    padding: 0 !important;
    margin: 0 !important;
    border-bottom: none !important;
}

#mainmenu li li a {
    display: block;
    padding: 12px 25px !important;
    white-space: normal;
    line-height: 1.4;
    transition: all 0.3s ease;
    border: none !important;
}

#mainmenu li li a:hover {
    background: #f8f9fa;
}

.d-menu-title {
    display: block;
    font-size: 15px;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 4px;
}

.d-menu-sub {
    display: block;
    font-size: 12px;
    color: #7f8c8d;
    font-weight: 400;
    line-height: 1.3;
}
""")
print("Appended CSS successfully.")
