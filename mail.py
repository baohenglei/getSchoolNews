#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
class Mail(object):
    def mailing(self,subject,body):
        try:
            # 设置邮件服务地址及默认端口号，这里选择的是outlook邮箱
            smtp_server = "smtp.office365.com:587"
            # 设置发送来源的邮箱地址
            mail_account = "linrobot@outlook.com"
            mail_passwd = "$.robotlin"
            sender_email = "linrobot@outlook.com"
            receiver_email = ["944140927@qq.com"]
            #,"hl00lf@stu.xjtu.edu.cn"

            # subject代表邮件主题信息
            #subject = 'subject\n\n'
            #body = 'bodystr'
            content = 'content\r\n'
            # 普通文本邮件
            msg = MIMEText(body, 'plain', 'utf-8')
            msg['Subject'] = subject
            msg['From'] = mail_account
            msg['To'] = receiver_email[0]
            msg["Accept-Language"] = "zh-CN"
            msg["Accept-Charset"] = "ISO-8859-1,utf-8"



            server = smtplib.SMTP()
            # 服务器连接
            server.connect(smtp_server)
            # 返回服务器特性
            server.ehlo()
            # 进行TLS安全传输
            server.starttls()
            # 账号密码登录
            server.login(mail_account, mail_passwd)
            # 邮件正文发送
            #body = "Dear Student, \n Please send your report\n Thank you for your attention"

            server.sendmail(sender_email, receiver_email, msg.as_string())
            # 关闭服务器连接
            server.close()
            return True
        except Exception as e:
            print(e)
            return False