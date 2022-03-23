import sanic
from sanic.response import text

app = sanic.Sanic('hello')


@app.get('/index')
async def index(self):
    return text("haha")


app.run(host='0.0.0.0', port=8000, auto_reload=True)
