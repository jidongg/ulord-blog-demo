# coding=utf-8
# @File  : config.py
# @Author: PuJi
# @Date  : 2018/4/12 0012

import os


class BaseConfig(object):

    def __init__(self):
        self.ipfs_host = '127.0.0.1'
        self.ipfs_port = 5001
        self.ulord_url = "http://10.175.0.98:5000/v1"
        # self.ulord_url = "http://192.168.14.67:5000/v1"
        # self.ulord_url = "http://127.0.0.1:5000/v1"
        self.ulord_head = {
            # "appkey": "37fd0c5e3eeb11e8a12af48e3889c8ab"
            # "appkey": "2b111d70452f11e89c2774e6e2f53324"
            "appkey": "ab1944f849e811e8b894fa163e37b4c3"
        }
        self.ulord_publish = "/transactions/publish/"
        self.ulord_publish_data = {
            "author": "justin",
            "title": "第一篇技术博客",
            "tag": ["blockchain", "IPFS"],
            "ipfs_hash": "QmVcVaHhMeWNNetSLTZArmqaHMpu5ycqntx7mFZaci63VF",
            "price": 0.1,
            "content_type": ".txt",
            "pay_password": "123",
            "description": "这是使用IPFS和区块链生成的第一篇博客的描述信息"
        }
        self.ulord_regist = "/transactions/createwallet/"
        self.ulord_transaction = "/transactions/consume/"
        self.ulord_paytouser = "/transactions/paytouser/"
        self.ulord_queryblog = "/content/list/"
        self.ulord_querybalance = "/transactions/balance/"
        self.ulord_checkbought = "/transactions/check/"
        self.ulord_userpublished = "/content/publish/list/"
        self.ulord_userbought = "/content/consume/list/"
        self.ulord_in = "/transactions/account/in/"
        self.ulord_out = "/transactions/account/out/"
        self.ulord_billings = "/transactions/publish/account/"
        self.ulord_publish_num = "/transactions/publish/count/"
        self.ulord_view = "/content/view/"
        self.ulord_billings_detail = "/transactions/account/inout/"
        # {
        #     'username':用户名,
        #     'claim_id':博客ID
        # }
        # return :
        # {
        #     "errcode":0/other,
        #     "reason":"success/资源不存在"
        # }

        # TODO ulord other URL
        # self.password = "123"
        # self.username = "shuxudong"
        # self.password = "123"
        # self.username = "cln"
        self.password = "123"
        self.username = "cln"

        # activity
        self.activity = True
        self.amount = 10

        # encryption
        self.utilspath = os.path.join(os.getcwd(), 'utils')
        self.pubkeypath = os.path.join(self.utilspath, 'public.pem')
        self.privkeypath = os.path.join(self.utilspath, 'private.pem')


baseconfig = BaseConfig()


class DevConfig(object):
    Debug = True
    SECRET_KEY = "ulord platform is good"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite.db'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    JSON_AS_ASCII = False # support chinese


