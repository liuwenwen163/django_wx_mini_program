# encoding: utf-8

import os
import smtplib
import django

from backend import settings
from email.mime.text import MIMEText

__author__ = "bbw"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

def send_mail():
    msg = MIMEText("邮件通道测试", "plaiin", "utf-8")
    msg['FROM'] = "Mail Test"  # 发送方
    msg['Subject'] = "【Mail Test】"  # 邮件主题
    receivers = ['bowen513s@163.com']
    server = smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.set_debuglevel(1)
    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    server.sendmail(settings.EMAIL_FROM, receivers, msg.as_string())
    server.close()


if __name__ == "__main__":
    send_mail()


