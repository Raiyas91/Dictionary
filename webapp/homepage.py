import justpy as jp


class Home:
    path = '/'

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view='hHh lpr fFf')
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=layout, show_if_above=True, v_mode="left", bordered=True)
        scroller = jp.QScrollArea(a=drawer, classes='fit')
        qlist = jp.QList(a=scroller)
        a_classes = 'p-2 m-2 text-xl text-blue-500 hover:text-blue-700'
        jp.A(a=qlist, text="Home", href='/', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href='/dictionary', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href='/about',classes=a_classes)
        jp.Br(a=qlist)

        jp.QBtn(a=toolbar, dense=True, flat= True, round=True, icon='menu', click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text ="Instant Dictionary")

        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        div1 = jp.Div(a=div, text='This is the Home Page!', classes='text-4xl m-2')
        div2 = jp.Div(a=div, text="""
        Hey! This is my Instant Dictionary Web Page. I have provided thousands of English definitions.Language is constantly evolving, and I wish to shine a light on how language is being used. Hope you find it useful!
        """, classes='text-lg')
        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True