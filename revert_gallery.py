html_path = r'c:\Users\Jesse\OneDrive\Desktop\Nikki Studio\dist\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = r'<div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-7 w-full gap-0">'
end_marker = r'</section>'
end_idx = content.find(end_marker, content.find(start_marker))

if end_idx != -1:
    new_grid_html = """<div class="grid grid-cols-2 md:grid-cols-3 gap-6 md:gap-8 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
                        <div class="rounded-2xl border border-black hover:-translate-y-2 hover:shadow-xl hover:border-primary hover:shadow-primary/20 transition-all duration-300 overflow-hidden">
                            <img src="img/nikki-studio-01.jpeg" alt="Nail Art" class="w-full h-48 sm:h-64 md:h-72 object-cover">
                        </div>
                        <div class="rounded-2xl border border-black hover:-translate-y-2 hover:shadow-xl hover:border-primary hover:shadow-primary/20 transition-all duration-300 overflow-hidden">
                            <img src="img/nikki-studio-02.jpeg" alt="Nail Art" class="w-full h-48 sm:h-64 md:h-72 object-cover">
                        </div>
                        <div class="rounded-2xl border border-black hover:-translate-y-2 hover:shadow-xl hover:border-primary hover:shadow-primary/20 transition-all duration-300 overflow-hidden">
                            <img src="img/nikki-studio-03.jpeg" alt="Nail Art" class="w-full h-48 sm:h-64 md:h-72 object-cover">
                        </div>
                        <div class="rounded-2xl border border-black hover:-translate-y-2 hover:shadow-xl hover:border-primary hover:shadow-primary/20 transition-all duration-300 overflow-hidden">
                            <img src="img/nikki-studio-04.jpeg" alt="Nail Art" class="w-full h-48 sm:h-64 md:h-72 object-cover">
                        </div>
                        <div class="rounded-2xl border border-black hover:-translate-y-2 hover:shadow-xl hover:border-primary hover:shadow-primary/20 transition-all duration-300 overflow-hidden">
                            <img src="img/nikki-studio-05.jpeg" alt="Nail Art" class="w-full h-48 sm:h-64 md:h-72 object-cover">
                        </div>
                        <div class="rounded-2xl border border-black hover:-translate-y-2 hover:shadow-xl hover:border-primary hover:shadow-primary/20 transition-all duration-300 overflow-hidden">
                            <img src="img/nikki-studio-06.jpeg" alt="Nail Art" class="w-full h-48 sm:h-64 md:h-72 object-cover">
                        </div>
                        <div class="rounded-2xl border border-black hover:-translate-y-2 hover:shadow-xl hover:border-primary hover:shadow-primary/20 transition-all duration-300 overflow-hidden">
                            <img src="img/nikki-studio-07.jpeg" alt="Nail Art" class="w-full h-48 sm:h-64 md:h-72 object-cover">
                        </div>
                        <div class="rounded-2xl border border-black hover:-translate-y-2 hover:shadow-xl hover:border-primary hover:shadow-primary/20 transition-all duration-300 overflow-hidden">
                            <img src="img/nikki-studio-08.jpeg" alt="Nail Art" class="w-full h-48 sm:h-64 md:h-72 object-cover">
                        </div>
                        <div class="rounded-2xl border border-black hover:-translate-y-2 hover:shadow-xl hover:border-primary hover:shadow-primary/20 transition-all duration-300 overflow-hidden">
                            <img src="img/nikki-studio-09.jpeg" alt="Nail Art" class="w-full h-48 sm:h-64 md:h-72 object-cover">
                        </div>
                        <div class="rounded-2xl border border-black hover:-translate-y-2 hover:shadow-xl hover:border-primary hover:shadow-primary/20 transition-all duration-300 overflow-hidden">
                            <img src="img/nikki-studio-10.jpeg" alt="Nail Art" class="w-full h-48 sm:h-64 md:h-72 object-cover">
                        </div>
                        <div class="rounded-2xl border border-black hover:-translate-y-2 hover:shadow-xl hover:border-primary hover:shadow-primary/20 transition-all duration-300 overflow-hidden">
                            <div class="w-full h-48 sm:h-64 md:h-72 overflow-hidden">
                                <img src="img/nikki-studio-11.jpeg" alt="Nail Art" class="w-full h-full object-cover object-[50%_0%] scale-[1.2]">
                            </div>
                        </div>
                        <div class="rounded-2xl border border-black hover:-translate-y-2 hover:shadow-xl hover:border-primary hover:shadow-primary/20 transition-all duration-300 overflow-hidden">
                            <img src="img/Nikki-studio-nails-artist-swindon.png" alt="Nail Art" class="w-full h-48 sm:h-64 md:h-72 object-cover object-top">
                        </div>
                    </div>
                """
    
    before_grid = content[:content.find(start_marker)]
    after_grid = content[end_idx:]
    new_content = before_grid + new_grid_html + after_grid
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
