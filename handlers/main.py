import tornado.web

from utlis.photo import get_imgs, save_upload, make_thumb


class IndexHandler(tornado.web.RequestHandler):
    """
    首页，所关注的用户图片流
    """
    def get(self):
        imgs = get_imgs()
        self.render('index.html', imgs=imgs)


class ExploreHandler(tornado.web.RequestHandler):
    """
    发现或最近上传的图片页面
    """
    def get(self):
        imgs = get_imgs()
        self.render('explore.html', imgs=imgs)


class PostHandler(tornado.web.RequestHandler):
    """
    单个图片详情页面
    """
    def get(self, post_id):
        self.render('post.html', post_id=post_id)


class UploadHandler(tornado.web.RequestHandler):
    """
    处理图片上传
    """
    def get(self, *args, **kwargs):
        self.render('upload.html')

    def post(self, *args, **kwargs):
        img_list = self.request.files.get('picture', [])

        #此处用到open函数/pillow模块thumbnail缩略图，代码重构写成函数封装到utlis

        # for upload_img in img_list:
        # # upload_img = img_list[0]
        # # {"filename": ..., "content_type": ..., "body": ...}.files
        #     with open('static/upload/{}'.format(upload_img['filename']), 'wb') as fh:
        #         fh.write(upload_img['body'])
        #
        #     from PIL import Image
        #     im = Image.open('static/upload/{}'.format(upload_img['filename']))
        #     im.thumbnail((200,200))
        #     im.save('static/upload/thumb/thumb_{}'.format(upload_img['filename']))
        # # self.write(upload_img['filename'] + ' ' + upload_img['content_type'])
        # self.write('upload done')
        for upload_img in img_list:
            save_to = save_upload(upload_img)
            make_thumb(save_to, 'thumb_{}'.format(upload_img['filename']))
        self.write('upload done')
