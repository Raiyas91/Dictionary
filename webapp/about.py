import justpy as jp


class About:
    path = ('/about')

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        div1 = jp.Div(a=div, text='This is the About Page!', classes='text-4xl m-2')
        div2 = jp.Div(a=div, text="""
        Hey! This is my Instant Dictionary Web Page. I have provided thousands of English definitions.Language is constantly evolving, and I wish to shine a light on how language is being used. Hope you find it useful!
        """, classes='text-lg')
        return wp


