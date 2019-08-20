import pytest,allure

class Test_ABC:

    # 添加测试步骤
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step(title="第一个测试")
    def test_001(self):
        # 添加测试描述
        allure.attach('描述的具体内容是...',"测试用例1的描述")
        assert 0

    # 添加用例所在位置，已知的链接，可点击链接跳转到用例管理工具中(例：禅道)查看用例
    @allure.testcase("测试所在位置的url链接/test_001")
    # 添加用例的bug，已知的链接，可点击链接跳转到用例管理工具中(例：禅道)的bug所在位置
    @allure.issue("bug所在的url链接")
    # 添加用例的优先级
    @allure.severity(allure.severity_level.TRIVIAL)

    @allure.step(title="第二个测试")
    def test_002(self):
        # 添加测试描述
        allure.attach('描述的具体内容', "用例2描述")
        assert 1