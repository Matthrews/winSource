import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '1500548410@qq.com'  # 填写发信人的邮箱账号
my_pass = 'kelifohlqplfjheh'  # 发件人邮箱授权码
my_user = '1010351486@qq.com'  # 收件人邮箱账号
# my_user = '1500548410@qq.com'


def sendmail(html):
    try:
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱授权码

        msg = MIMEText(html, 'html', 'utf-8')  # 填写邮件内容
        msg['From'] = formataddr(["admin", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["user", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "用户咨询"  # 邮件的主题，也可以说是标题

        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print("邮件发送成功")
    except Exception:
        print("邮件发送失败")


if __name__ == "__main__":
    content = "测试内容"
    sendmail(content)
