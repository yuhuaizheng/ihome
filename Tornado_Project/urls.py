# !/usr/bin/python
# -*- encoding: utf-8 -*-
# @author:spider1998
import os
from handlers import VerifyCode,Passport,Profile,House,Orders
from handlers.BaseHandler import StaticFileHandler


handlers = [
    (r"/api/imagecode", VerifyCode.ImageCodeHandler),#图片验证码
    (r"/api/smscode",VerifyCode.SMSCodeHandler),#手机验证码
    (r"/api/register", Passport.RegisterHandler),#注册
    (r"/api/login", Passport.LoginHandler),#登录
    (r"/api/logout", Passport.LogoutHandler),#退出
    (r"/api/check_login", Passport.CheckLoginHandler),# 判断用户是否登录
    (r"/api/profile/avatar", Profile.AvatarHandler), # 用户上传头像
    (r"/api/profile", Profile.ProfileHandler), # 个人主页获取个人信息
    (r"/api/profile/name", Profile.NameHandler), # 个人主页修改用户名
    (r"/api/profile/auth", Profile.AuthHandler), # 实名认证
    (r"/api/house/area", House.AreaInfoHandler), # 城区信息
    (r'^/api/house/info$', House.HouseInfoHandler), # 上传房屋的基本信息
    (r'^/api/house/image$', House.HouseImageHandler), # 上传房屋图片
    (r'^/api/house/my$', House.MyHousesHandler), # 查询用户发布的房源
    (r'^/api/house/list$', House.HouseListHandler), # 房屋过滤列表数据
    (r'^/api/house/list2$', House.HouseListRedisHandler), # 房屋过滤列表数据
    (r'^/api/order$', Orders.OrderHandler), # 下单
    (r'^/api/order/my$', Orders.MyOrdersHandler), # 我的订单，作为房客和房东同时适用
    (r'^/api/order/accept$', Orders.AcceptOrderHandler), # 接单
    (r'^/api/order/reject$', Orders.RejectOrderHandler), # 拒单
    (r'^/api/order/comment$', Orders.OrderCommentHandler),#评论
    (r'^/api/house/index$', House.IndexHandler), # 首页
    (r"/(.*)",StaticFileHandler,dict(path=os.path.join(os.path.dirname(__file__),"html"),
                                     default_filename="index.html")),
]