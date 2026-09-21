import os

css_code = """
/* ==================================================
   MOBILE SUB-TABS STYLING (Requested Design)
================================================== */
@media (max-width: 991px) {
    /* Remove background and shadow for mobile sub-menus */
    #mainmenu ul ul {
        background: transparent !important;
        box-shadow: none !important;
        padding-left: 20px !important;
        padding-top: 5px !important;
        padding-bottom: 5px !important;
        width: auto !important;
    }

    /* Reset child links */
    #mainmenu li li a {
        display: block !important;
        padding: 6px 15px !important;
        font-size: 15px !important;
        color: #4b5e73 !important;
    }

    #mainmenu li li a:hover {
        background: transparent !important;
        color: #2c3e50 !important;
    }

    /* Hide the icons and sub-titles in mobile view */
    #mainmenu li li a i.nav-icon {
        display: none !important;
    }
    #mainmenu li li a .d-menu-sub {
        display: none !important;
    }

    /* Add the right arrow before the menu title */
    #mainmenu li li a .d-menu-title::before {
        content: "\\2192\\00a0 ";
        color: #66798c;
        font-weight: 400;
    }
    
    #mainmenu li li a .d-menu-title {
        display: inline-block;
        font-size: 14px !important;
        font-weight: 500 !important;
        color: #5d6c7b !important;
    }
}
"""

with open("c:/Users/user/Desktop/Hexa-ReachSolution-website/css/style.css", "a", encoding="utf-8") as f:
    f.write(css_code)

print("Mobile menu CSS appended.")
