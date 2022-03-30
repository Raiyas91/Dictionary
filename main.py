import justpy as jp

from webapp.about import About
from webapp.homepage import Home

jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)

jp.justpy(port=8001)
