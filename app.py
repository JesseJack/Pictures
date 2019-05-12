import tornado.options
from tornado.options import define, options

from handlers.main import IndexHandler, ExploreHandler, PostHandler

define('port', default='8000', help='Listening port', type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers=[
            (r"/", IndexHandler),
            (r"/explore", ExploreHandler),
            (r"/post/(?P<post_id>[0-9]+)", PostHandler),
        ]
        settings = dict(
            debug=True,
            template_path='templates',
            static_path='static',
        )
        super().__init__(handlers, **settings)

application = Application()

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(options.port)
    print("Server start on port {}".format(str(options.port)))
    tornado.ioloop.IOLoop.current().start()


# 项目的业务逻辑：
#     运行基本程序：
#         app.py
#         handlers配置
#         templates和static目录配置
#     业务逻辑：
#         发现或最近上传的图片页面/explore  ExploreHandler
#         所关注的用户图片流 / IndexHandler
#         单个图片详情页面 / post/id  PostHandler

