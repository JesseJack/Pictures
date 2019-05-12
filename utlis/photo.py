# -*- coding:utf-8 -*-
import glob

from PIL import Image


def get_imgs():
    return glob.glob('static/upload/*.jpg')


def save_upload(upload_img):
    """
    将上传的图片写入到指定路径
    :param upload_img:
    :return:
    """
    save_to = 'static/upload/{}'.format(upload_img['filename'])
    with open(save_to, 'wb') as fh:
        fh.write(upload_img['body'])
    return save_to


def make_thumb(save_to, thumb_name):
    """
    把指定路径的图片生成缩略图
    :param save_to:
    :param thump_name:
    :return:
    """
    im = Image.open(save_to)
    im.thumbnail((200,200))
    im.save('static/upload/thumb/{}'.format(thumb_name))