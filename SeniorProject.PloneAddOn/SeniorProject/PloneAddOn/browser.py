from zope.publisher.browser import BrowserView

class HelloView(BrowserView):

    def __call__(self):
        return """
        <html>
        <head>
          <title>Hello World</title>
        </head>
        <body>
          Hello World
        </body>
        </html>
        """
