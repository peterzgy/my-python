#!/usr/bin/env  python
#coding=utf-8
#author:zouguoyin
#describe:项目一键构建
import jenkins
def  jenkins_get_server():
    print("start to get")
    jenkins_server_url = "http://jenkins.test.ebsfw.com/jenkins" 
    user_id = "admin"
    api_token = "Jenkins@ebs#123"
    server=jenkins.Jenkins(jenkins_server_url,username=user_id,password=api_token)
    return server

"""
#执行构建任务
"""
def jenkins_exe_job(projectname):
    print("执行%s构建任务开始"%(projectname))
    server=jenkins_get_server()
    #server.build_job("项目名字")
    ret=server.build_job(projectname)
    print("执行%s构建任务结束，%s"%(projectname,ret))
    print("*"*100)

"""
#获取job的信息
"""
def jenkins_get_jobs():
    server=jenkins_get_server()
    for j in server.get_all_jobs():
        print(j["name"]+" 构建状态: "+j["color"])
"""
#执行部署
"""
def beta7_deploy():
    list1=['ebs-server', 'bh-joiningTrader-web', 'bihu-admin-manager', 'bihu-web', 'bihu-wechat-web','auth-center', 'ebs-consumer', 'ebs-cooperate', 'ebs-gateway', 'ebs-openapi', 'ebs-pay-center', 'ebs-producer', 'ebs-task-consumer', 'fail-rebuild', 'mq-center', 'msg-center', 'tpd-center', 'user-center']
    for i in range(len(list1)):
        jenkins_exe_job(list1[i])
if __name__=="__main__":
    beta7_deploy()
    jenkins_get_jobs()

    

