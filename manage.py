# 启动程序
from app import create_app

"""
development:    开发环境
production:     生产环境
testing:        测试环境
default:        默认环境

"""

app = create_app('development')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'])
