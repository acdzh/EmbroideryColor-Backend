from app.blueprints.user import user
import random
import os


def send_code(code):
    os.system("powershell sendmsg {}".format(code))


@user.route('/verify/getcode', methods=['GET', 'POST'])
def get_verify_code():
    code = random.randint(1000, 9999)
    send_code(code)
    return 'dd'
