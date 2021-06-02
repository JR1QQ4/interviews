#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest

# fixture 其实就是自定义前置和后置操作
# conftest.py配置里可以实现数据共享，不需要import就能自动找到一些配置
# scope="module" 可以实现多个.py跨文件共享前置，每一个.py文件调用一次
# scope="session" 以实现多个.py跨文件使用一个session来完成多个用例
# fixture(scope="function", params=None. autouse=False, ids=None, name=None):
# 可以使用此装饰器（带或不带参数）来定义fixture功能，fixture功能的名称可以在以后使用
# 引用它会在运行测试之前调用它：test模块或类可以使用pytest.mark.usefixture(fixturename)标记
# 测试功能可以直接使用fixture名称作为输入参数，在这种情况下，夹具实例从fixture返回功能将被注入
# scope：有四个级别参数，function默认，class，module，session
# params：一个可选的参数列表，它将导致多个参数调用fixture功能和所有测试使用它
# autouse：如果为True，则为所有测试激活fixture func可以看到它，如果为False（默认）则需要手动激活
# ids：每个字符串id的列表，每个字符串对应于params，如果没有指定自动生成
# name：fixture的名称，如果fixture在定义它的同一模块使用，夹具的功能名称将被请求夹具的功能arg遮蔽
# @pytest.fixture()
# def login():
#     print("登录成功")
# def test_s1(login):
#     print("用例1：登录之后其他动作111")
# def test_s2():
#     print("用例2，不需要登录，操作222")
# def test_s3(login):
#     print("用例3：登录之后其他动作333")


# 02 03 12 13
# @pytest.mark.parametrize("x", [0, 1])
# @pytest.mark.parametrize("y", [2, 3])
# def test_foo(x, y):
#     print("测试数据组合：x->%s, y->%s" % (x, y))

# 等价于 @pytest.mark.skip(reason="no way of currently testing this")
# def test_function():
#     if not True:
#         pytest.skip("unsupported configuration")

# @pytest.mark.webtest
# def test_send_http():
#     print("test_send_http")
# @pytest.mark.ws
# def test_send_webservice():
#     print("test_send_webservice")

# @pytest.fixture(scope="function")
# @pytest.fixture(scope="module")
# def demo_fix():
#     print("\n测试用例的前置准备操作")
#     yield
#     print("测试用例的后置操作")
# def test_1(demo_fix):
#     print("\n开始执行测试用例11111")
# def test_2():
#     print("\n开始执行测试用例22222")
# def test_3(demo_fix):
#     print("\n开始执行测试用例33333")

# allure
# pip install pytest==4.5.0 --index-url  https://pypi.douban.com/simple
# pip install allure-pytest==2.8.6 --index-url  https://pypi.douban.com/simple
# allure是一个命令行工具，需要去github上下载最新版 https://github.com/allure-framework/allure2/releases
# import allure
# @pytest.fixture(scope="session")
# def login():
#     print("用例先登录")
# @allure.step("步骤1：点xxx")
# def step_1():
#     print("step 111")
# @allure.step("步骤2：点yyy")
# def step_2():
#     print("step 222")
# @allure.feature("编辑页面")
# class TestEditPage:
#     """编辑页面 Edit"""
#     @allure.story("这是第一xxx的用例")
#     def test_1(self, login):
#         """用例描述：先登录，再去执行xxx"""
#         step_1()
#         step_2()
#         print("xxx")
#     @allure.story("打开a页面")
#     def test_2(self, login):
#         """用例描述：先登录，再去执行yyy"""
#         print("yyy")
# >pytest --alluredir=./report/allure_raw
# >allure serve report/allure_raw
# >allure generate directory-with-results/ -o directory-with-report

# @pytest.fixture
# def init():
#     print("---------init start------------")
#     yield True, 100
#     print("---------init end------------")
# @pytest.fixture
# def init2():
#     print("---------init2 start------------")
#     yield "{'a': '123', 'b': '234'}"
#     print("---------init2 end------------")
# @pytest.fixture(scope="class")
# def init_cls():
#     print("---------class start------------")
#     yield ['q', 123]
#     print("---------class end------------")
# @pytest.mark.usefixtures("init_cls")
# class TestFixture:
#     @pytest.mark.usefixtures("init")
#     def test_one(self, init):
#         print("test one")
#         print(init)
#     @pytest.mark.usefixtures("init2")
#     def test_two(self, init_cls):
#         print("test two")
#         print(init_cls)
#     @pytest.mark.usefixtures("init")
#     @pytest.mark.usefixtures("init2")
#     def test_three(self):
#         print("test three")
#         print(init2)

if __name__ == '__main__':
    pytest.main(["-s", "pytest_test.py"])
    # pytest.main(["-s", "pytest_test.py", "-m=webtest"])
    # pytest.main(["-s", "pytest_test.py", "-m", "not webtest"])

