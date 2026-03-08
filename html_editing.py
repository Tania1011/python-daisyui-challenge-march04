# Last time modified: 03/05/26
# Author: Tania1011
# Class 07 - Assignment 1
# Purpose: Generate a Flower Garden Shop website using DaisyUI + Tailwind CSS frameworks.
# This script reads a base HTML file, modifies it to include the necessary CSS links, 
# and adds content such as a navigation bar, banner, flower cards, and a footer.


def generate_website():
    #  Read base HTML
    with open("base.html", "r") as website:
        html_base = website.read()

    #  Page title
    page_title = "Bloom Garden Flower Shop"
    html_modified = html_base.replace("<title>Document", f"<title>{page_title}")

    #  DaisyUI + Tailwind
    daisy_ui = """
<!-- Daisy UI -->
<link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
<link href="https://cdn.jsdelivr.net/npm/daisyui@5/themes.css" rel="stylesheet" type="text/css" />
"""
    html_modified = html_modified.replace("</head>", daisy_ui + "\n</head>")

    #  Theme
    theme = "garden"
    html_modified = html_modified.replace('<html lang="en">', f'<html lang="en" data-theme="{theme}">')

    #  Navbar
    nav_bar = """
<div class="navbar bg-base-100 shadow-sm">
  <a class="btn btn-ghost text-xl">Bloom Garden Flower Shop</a>
</div>
"""

    #  Hero/banner
    flower_banner = """
<div class="hero min-h-[400px]" style="background-image: url(images/OIP.jpg);">
  <div class="hero-overlay bg-opacity-50"></div>
  <div class="hero-content text-center text-neutral-content">
    <div class="max-w-md">
      <h1 class="mb-5 text-5xl font-bold">Bloom Garden</h1>
      <p class="mb-5">Discover beautiful flowers from around the world.</p>
      <button class="btn btn-primary">Explore Flowers</button>
    </div>
  </div>
</div>
"""

    #  Flower Shop Section
    flower_shop = """
<div class="container mx-auto px-4 mt-10">
<h2 class="text-3xl font-bold text-center mb-8">Flower Shop</h2>

<div class="grid grid-cols-1 md:grid-cols-3 gap-6">

<div class="card bg-base-100 shadow-xl">
  <figure><img src="images/rose.jpg" /></figure>
  <div class="card-body">
    <h2 class="card-title">Rose</h2>
    <p>Classic flower symbolizing love and beauty.</p>
    <div class="card-actions justify-end">
      <button class="btn btn-primary">View</button>
    </div>
  </div>
</div>

<div class="card bg-base-100 shadow-xl">
  <figure><img src="images/flowers.jpg" /></figure>
  <div class="card-body">
    <h2 class="card-title">Sunflower</h2>
    <p>Bright yellow flower that follows the sun.</p>
    <div class="card-actions justify-end">
      <button class="btn btn-secondary">View</button>
    </div>
  </div>
</div>

<div class="card bg-base-100 shadow-xl">
  <figure><img src="images/tulips.jpg" /></figure>
  <div class="card-body">
    <h2 class="card-title">Tulips</h2>
    <p>Beautiful spring flower from Europe.</p>
    <div class="card-actions justify-end">
      <button class="btn btn-accent">View</button>
    </div>
  </div>
</div>

</div>
</div>
"""

    #  Horizontal Footer
    footer = """
<footer class="footer p-10 bg-base-200 text-base-content rounded-t-lg mt-10 flex justify-around">
  <div>
    <span class="footer-title">Bloom Garden</span>
    <a class="link link-hover">Home</a>
    <a class="link link-hover">Shop</a>
    <a class="link link-hover">Gallery</a>
    <a class="link link-hover">Contact</a>
  </div>
  <div>
    <span class="footer-title">Social</span>
    <a class="link link-hover">Instagram</a>
    <a class="link link-hover">Facebook</a>
    <a class="link link-hover">Pinterest</a>
    <a class="link link-hover">YouTube</a>
  </div>
  <div>
    <span class="footer-title">Contact</span>
    <a class="link link-hover">Email: info@bloomgarden.com</a>
    <a class="link link-hover">Phone: +1 234 567 890</a>
  </div>
</footer>
"""

    #  Inject navbar, hero/banner, flower shop, and footer into body
    html_modified = html_modified.replace('<body>', '<body>\n' + nav_bar + flower_banner)
    html_modified = html_modified.replace('</body>', flower_shop + footer + "\n</body>")

    #  Write final HTML
    with open("index.html", "w") as file:
        file.write(html_modified)

    print("index.html generated successfully! Open the file in a web browser to view the Bloom Garden Flower Shop website.")

#  Run the generator
generate_website()
