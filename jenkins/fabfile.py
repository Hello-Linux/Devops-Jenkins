#!/usr/bin/env python
# encoding:utf8
# version:1.0.0
# date:2017-08-09
from fabric.api import *
import sys
import os

env.user = 'hsadmin'
env.port = 22
env.roledefs = {
    'tomcat_web2': ['1.2.3.4','3.4.5.6.7'],
    'tomcat_web1': ['12.34.5.6','1.2.4.6.7'],
    'tomcat_pre_web': ['123.45.6.7'],
    'tomcat_mgmt': ['123.4.5.6'],
    'tomcat_gateway': ['2.3.4.2'],
    'tomcat_lend1': ['1.56.7.8.2'],
    'tomcat_lend2': ['5.6.7.247'],
    'tomcat_core_match': ['1.2.3.27'],
    'tomcat_escrow_retry': ['123.34.5.27'],
    'tomcat_message_center': ['1.2.3.27'],
    'tomcat_message_sms': ['1.2.3.27'],
    'tomcat_schedule': ['123.34.5.205'],
    'tomcat_core_repay': ['123.34.5.205'],
    'tomcat_report': ['123.34.5.205'],
    'tomcat_mail': ['123.34.5.205'],
    'tomcat_core_dubbo1': ['123.34.5.205'],
    'tomcat_core_dubbo2': ['123.34.5.205'],
    'tomcat_rule_engine': ['123.34.5.205', '123.34.5.205'],
    'tomcat_message-audio': ['123.34.5.205'],
    'tomcat_core-check': ['123.34.5.205'],
    'tomcat_oa1': ['123.34.5.205'],
    'tomcat_oa2': ['123.34.5.205'],
    'tomcat_cfca': ['123.34.5.205'],
    'tomcat_crm1': ['123.34.5.205'],
    'tomcat_crm2': ['123.34.5.205'],
    'tomcat_crm_dubbo': ['123.34.5.205', '123.34.5.205'],
    'tomcat_stat': ['123.34.5.205'],
    'tomcat_datashare': ['123.34.5.205'],
    'tomcat_event_dubbo1': ['123.34.5.205'],
    'tomcat_event_dubbo2': ['123.34.5.205'],
    'nginx': ['123.34.5.205']
}
env.key_filename = '/jenkins_python_aliyun/id_rsa'
'''Tips

if you want to can some information about this file
please edit the file for some tickes!
'''
########################Variable's target for all job#############################
item1 = os.listdir("/var/lib/jenkins/workspace/product_core-match/core-match/target")
newlist1 = []
for name1 in item1:
    if name1.endswith(".jar"):
        newlist1.append(name1)
target_match = str(newlist1[0]).split('.jar',1)[0]

item2 = os.listdir("/var/lib/jenkins/workspace/product_core-repay/core-repay/target")
newlist2 = []
for name2 in item2:
    if name2.endswith(".jar"):
        newlist2.append(name2)
target_repay = str(newlist2[0]).split('.jar',1)[0]

item3 = os.listdir("/var/lib/jenkins/workspace/product_escrow-retry/escrow-retry/target")
newlist3 = []
for name3 in item3:
    if name3.endswith(".jar"):
        newlist3.append(name3)
target_retry = str(newlist3[0]).split('.jar',1)[0]

item4 = os.listdir("/var/lib/jenkins/workspace/product_core-dubbo/core-dubbo/target")
newlist4 = []
for name4 in item4:
    if name4.endswith(".jar"):
        newlist4.append(name4)
target_coredubbo = str(newlist4[0]).split('.jar',1)[0]

item5 = os.listdir("/var/lib/jenkins/workspace/product_rule_engine/ruleengine-service/target")
newlist5 = []
for name5 in item5:
    if name5.endswith(".jar"):
        newlist5.append(name5)
target_ruleengine = str(newlist5[0]).split('.jar',1)[0]

item6 = os.listdir("/var/lib/jenkins/workspace/product_core-check/core-check/target")
newlist6 = []
for name6 in item6:
    if name6.endswith(".jar"):
        newlist6.append(name6)
target_corecheck = str(newlist6[0]).split('.jar',1)[0]

item7 = os.listdir("/var/lib/jenkins/workspace/product_crm_dubbo/dubbo/target")
newlist7 = []
for name7 in item7:
    if name7.endswith(".jar"):
        newlist7.append(name7)
target_crmdubbo = str(newlist7[0]).split('.jar',1)[0]

item8 = os.listdir("/var/lib/jenkins/workspace/product_event_dubbo/event-dubbo/target")
newlist8 = []
for name8 in item8:
    if name8.endswith(".jar"):
	newlist8.append(name8)
	target_eventdubbo = str(newlist8[0]).split('.jar',1)[0]
###################################################################################
def jenkins_schedule():
            with settings(warn_only=True):
                result = sudo("kill -9 `ps aux | grep tomcat-schedule|grep -v grep|awk \'{print $2}\'`", pty=False, user="hsadmin")
            if result.failed:
                print 'the tomcat-schedule process is not exists'
            else:
                print 'tomcat-schedule is shutdown successing!'
                run('/opt/tomcat-schedule/bin/shutdown.sh')
                run('sleep 10')
            with cd('/opt/tomcat-schedule/webapps/'):
                run('rm -rf ROOT*')
            with lcd('/var/lib/jenkins/workspace/product_hxb-core-schedule/core-schedule/target'):
                put('core-schedule-*.war','/opt/tomcat-schedule/webapps/ROOT.war')
            with cd('/opt/tomcat-schedule/bin'):
                sudo("sh startup.sh", pty=False, user="hsadmin")
def jenkins_match():
            with cd('/opt/core-match'):
                run('cp -rf config lib /backup/core-match/')
                sudo("/opt/core-match/bin/single.sh stop", pty=False, user="hsadmin")
                run('sleep 10')
                run('rm -rf config lib')
            with lcd('/var/lib/jenkins/workspace/product_core-match/core-match/target'):
                put('%s/config' % (target_match),'/opt/core-match/')
                put('%s/lib' % (target_match),'/opt/core-match/')
            with cd('/opt/core-match/bin'):
                sudo("/opt/core-match/bin/single.sh start", pty=False, user="hsadmin")
def jenkins_repay():
    sudo("/opt/core-repay/bin/single.sh stop", pty=False, user="hsadmin")
    run('sleep 5')
    with cd('/opt/core-repay'):
        run('cp -rf config lib /backup/core-repay')
        run('rm -rf config lib')
    with lcd('/var/lib/jenkins/workspace/product_core-repay/core-repay/target'):
        put('%s/config' % (target_repay),'/opt/core-repay/')
        put('%s/lib' % (target_repay),'/opt/core-repay/')
    with cd('/opt/core-repay/bin'):
        sudo("/opt/core-repay/bin/single.sh start", pty=False, user="hsadmin")
def jenkins_retry():
    sudo("/opt/escrow-retry/bin/single.sh stop", pty=False, user="hsadmin")
    with cd('/opt/escrow-retry'):
        run('cp -rf config lib /backup/escrow-retry')
        run('rm -rf config lib')
    with lcd('/var/lib/jenkins/workspace/product_escrow-retry/escrow-retry/target'):
        put('%s/config' % (target_retry),'/opt/escrow-retry')
        put('%s/lib' % (target_retry),'/opt/escrow-retry')
    with cd('/opt/escrow-retry/bin'):
        run('sleep 2')
        sudo("/opt/escrow-retry/bin/single.sh start", pty=False, user="hsadmin")
def jenkins_lend():
        with settings(warn_only=True):
            result = sudo("kill -9 `ps aux | egrep java.*tomcat-lend/.*Bootstrap|grep -v grep|awk \'{print $2}\'`", pty=False, user="hsadmin")
        if result.failed:
            print 'The tomcat-lend is not exists'
        else:
            print 'kill successing'
        run('/opt/tomcat-lend/bin/shutdown.sh')
        run('sleep 5')
        run('/opt/tomcat-lend/bin/shutdown.sh')
        with cd('/opt/tomcat-lend/webapps/'):
            run('cp -rf ROOT /backup/tomcat-lend/')
            run('sudo rm -rf ROOT*')
        with lcd('/var/lib/jenkins/workspace/product_hxb-lend/hxb-lend-api/target'):
            put('hxb-lend-api-*.war','/opt/tomcat-lend/webapps/ROOT.war')
        with cd('/opt/tomcat-lend/bin'):
            sudo("/opt/tomcat-lend/bin/startup.sh", pty=False, user="hsadmin")
def jenkins_mgmt():
        with settings(warn_only=True):
            result = sudo("kill -9 `ps aux | egrep java.*tomcat-mgmt/.*Bootstrap|grep -v grep|awk \'{print $2}\'`", pty=False, user="hsadmin")
        if result.failed:
            print 'The tomcat-mgmt process is not exists'
        else:
            print 'kill success'
        run('/opt/tomcat-mgmt/bin/shutdown.sh')
        with cd('/opt/tomcat-mgmt/webapps'):
            run('cp -rf ROOT /backup/tomcat-mgmt/')
            run('sudo rm -rf ROOT*')
        with lcd('/var/lib/jenkins/workspace/product_hxb-core-mgmt/core-mgmt/target'):
            put('core-mgmt-*.war','/opt/tomcat-mgmt/webapps/ROOT.war')
        with cd('/opt/tomcat-mgmt/bin'):
            sudo("/opt/tomcat-mgmt/bin/startup.sh", pty=False, user="hsadmin")
#nginx for web configuration
def nginx_web_p1():
        sudo("python /scripts/nginx.py web p1", pty=False, user="hsadmin")
        sudo("nginx -s reload", pty=False, user="hsadmin")
def nginx_web_p2():
        sudo("python /scripts/nginx.py web p2", pty=False, user="hsadmin")
def nginx_web_p3():
        sudo("python /scripts/nginx.py web p3", pty=False, user="hsadmin")
        sudo("nginx -s reload", pty=False, user="hsadmin")
def nginx_web_p4():
        sudo("python /scripts/nginx.py web p4", pty=False, user="hsadmin")
        sudo("nginx -s reload", pty=False, user="hsadmin")
#end
#nginx for lend configuration
def nginx_lend_p1():
        sudo("python /scripts/nginx.py lend p1", pty=False, user="hsadmin")
        sudo("nginx -s reload", pty=False, user="hsadmin")
def nginx_lend_p2():
        sudo("python /scripts/nginx.py lend p2", pty=False, user="hsadmin")
def nginx_lend_p3():
        sudo("python /scripts/nginx.py lend p3", pty=False, user="hsadmin")
        sudo("nginx -s reload", pty=False, user="hsadmin")
def nginx_lend_p4():
        sudo("python /scripts/nginx.py lend p4", pty=False, user="hsadmin")
        sudo("nginx -s reload", pty=False, user="hsadmin")
#end
#nginx for oa configuration

def nginx_oa_p1():
        sudo("python /scripts/nginx.py oa p1", pty=False, user="hsadmin")
        sudo("nginx -s reload", pty=False, user="hsadmin")
def nginx_oa_p2():
        sudo("python /scripts/nginx.py oa p2", pty=False, user="hsadmin")
def nginx_oa_p3():
        sudo("python /scripts/nginx.py oa p3", pty=False, user="hsadmin")
        sudo("nginx -s reload", pty=False, user="hsadmin")
def nginx_oa_p4():
        sudo("python /scripts/nginx.py oa p4", pty=False, user="hsadmin")
        sudo("nginx -s reload", pty=False, user="hsadmin")
#end

#nginx for crm configuration
def nginx_crm_p1():
        sudo("python /scripts/nginx.py crm p1", pty=False, user="hsadmin")
        sudo("nginx -s reload", pty=False, user="hsadmin")
def nginx_crm_p2():
        sudo("python /scripts/nginx.py crm p2", pty=False, user="hsadmin")
def nginx_crm_p3():
        sudo("python /scripts/nginx.py crm p3", pty=False, user="hsadmin")
        sudo("nginx -s reload", pty=False, user="hsadmin")
def nginx_crm_p4():
        sudo("python /scripts/nginx.py crm p4", pty=False, user="hsadmin")
        sudo("nginx -s reload", pty=False, user="hsadmin")
#end

def jenkins_web():
        with settings(warn_only=True):
            result = sudo("kill -9 `ps aux | grep tomcat-web|grep -v grep|awk \'{print $2}\'`", pty=False, user="hsadmin")
        if result.failed:
            print 'The tomcat-web process is not exists'
        else:
            print 'kill success'
        with cd('/opt/tomcat-web/bin'):
            sudo("/opt/tomcat-web/bin/shutdown.sh", pty=False, user="hsadmin")
            run('sleep 5')
        with cd('/opt/tomcat-web2/bin'):
            sudo("/opt/tomcat-web2/bin/shutdown.sh", pty=False, user="hsadmin")
            run('sleep 5')
        with cd('/opt'):
            run('cp -rf tomcat-web/webapps/ROOT /backup/tomcat-web1/')
            run('cp -rf tomcat-web2/webapps/ROOT /backup/tomcat-web2/')
            run('rm -rf tomcat-web/webapps/ROOT*')
            run('rm -rf tomcat-web2/webapps/ROOT*')
        with lcd('/var/lib/jenkins/workspace/product_hxb-core-web/core-web/core-web-expose/target'):
            put('core-web-expose-*.war','/opt/tomcat-web/webapps/ROOT.war')
            put('core-web-expose-*.war','/opt/tomcat-web2/webapps/ROOT.war')
        sudo("/opt/tomcat-web/bin/startup.sh", pty=False, user="hsadmin")
        sudo("/opt/tomcat-web2/bin/startup.sh", pty=False, user="hsadmin")

def jenkins_webtest():
        with settings(warn_only=True):
            result = sudo("kill -9 `ps aux | grep tomcat-webtest|grep -v grep|awk \'{print $2}\'`", pty=False, user="hsadmin")
        if result.failed:
            print 'The tomcat-webtest process is not exists'
        else:
            print 'kill success'
        with cd('/opt/tomcat-webtest/bin'):
            sudo("/opt/tomcat-webtest/bin/shutdown.sh", pty=False, user="hsadmin")
        with cd('/opt'):
            run('rm -rf tomcat-webtest/webapps/ROOT*')
        with lcd('/var/lib/jenkins/workspace/product_hxb-core-web/core-web/core-web-expose/target'):
            put('core-web-expose-*.war','/opt/tomcat-webtest/webapps/ROOT.war')
        sudo("/opt/tomcat-webtest/bin/startup.sh", pty=False, user="hsadmin")

def jenkins_gateway():
        with settings(warn_only=True):
            result = sudo("kill -9 `ps aux | egrep java.*tomcat-gateway/.*Bootstrap|grep -v grep|awk \'{print $2}\'`", pty=False, user="hsadmin")
        if result.failed:
            print 'The tomcat-gateway process is not exists'
        else:
            print 'kill success'
        run('/opt/tomcat-gateway/bin/shutdown.sh')
        with cd('/opt/tomcat-gateway/webapps'):
            run('cp -rf ROOT /backup/tomcat-gateway/')
            run('sudo rm -rf ROOT*')
        with lcd('/var/lib/jenkins/workspace/product_escrow-gateway/escrow-gateway/target'):
            put('escrow-gateway-*.war','/opt/tomcat-gateway/webapps/ROOT.war')
        with cd('/opt/tomcat-gateway/bin/'):
            sudo("/opt/tomcat-gateway/bin/startup.sh", pty=False, user="hsadmin")
def jenkins_report():
        with lcd('/var/lib/jenkins/workspace/Product-report-JOB/target'):
            put('hxb-report.war','/opt/workspace-temp/')
            with settings(warn_only=True):
                result = sudo("kill -9 `ps aux | grep tomcat-report/.*Bootstrap|grep -v grep|awk \'{print $2}\'`", pty=False, user="root")
            if result.failed:
                print 'The tomcat-report process is not exists'
            else:
                print 'kill success'
            run('sleep 2')
            run('/opt/tomcat-report/bin/shutdown.sh')
            sudo("rm -rf /upload/report/strategy/normal/*", pty=False, user="hsadmin")
            sudo("rm -rf /upload/report/strategy/batch/*", pty=False, user="hsadmin")
            sudo("rm -rf /upload/report/strategy/template/*", pty=False, user="hsadmin")
        with lcd('/var/lib/jenkins/workspace/Product-report-JOB/upload'):
            put('report','/upload/')
        with cd('/opt/tomcat-report/webapps'):
            run('sudo rm -rf ROOT')
            run('cp /opt/workspace-temp/hxb-report.war /opt/tomcat-report/webapps/ROOT.war')
        with cd('/opt/tomcat-report/bin'):
            run('sleep 2')
            sudo("/opt/tomcat-report/bin/startup.sh", pty=False, user="hsadmin")
def jenkins_mail():
            with cd('/opt/message-mail'):
                run('cp -rf config lib /backup/message-mail/')
                sudo("/opt/message-mail/bin/single.sh stop", pty=False, user="hsadmin")
                run('sleep 5')
                run('rm -rf config lib')
            with lcd('/var/lib/jenkins/workspace/product_core-match/core-match/target/core-match-1.0'):
                put('config','/opt/message-mail/')
                put('lib','/opt/message-mail/')
            with cd('/opt/message-mail/bin'):
                sudo("/opt/message-mail/bin/single.sh start", pty=False, user="hsadmin")
def jenkins_dubbo():
    sudo("/opt/core-dubbo/bin/single.sh stop", pty=False, user="hsadmin")
    run('sleep 5')
    with cd('/opt/core-dubbo'):
        run('cp -rf config lib /backup/core-dubbo')
        run('rm -rf config lib')
    with lcd('/var/lib/jenkins/workspace/product_core-dubbo/core-dubbo/target'):
        put('%s/config' % (target_coredubbo),'/opt/core-dubbo/')
        put('%s/lib' % (target_coredubbo),'/opt/core-dubbo/')
    with cd('/opt/core-dubbo/bin'):
        sudo("/opt/core-dubbo/bin/single.sh start", pty=False, user="hsadmin")
def jenkins_engine():
    sudo("/opt/rule-engine/bin/single.sh stop", pty=False, user="hsadmin")
    run('sleep 5')
    with cd('/opt/rule-engine'):
        run('cp -rf config lib /backup/rule-engine')
        run('rm -rf config lib')
    with lcd('/var/lib/jenkins/workspace/product_rule_engine/ruleengine-service/target'):
        put('%s/config' % (target_ruleengine),'/opt/rule-engine/')
        put('%s/lib' % (target_ruleengine),'/opt/rule-engine/')
    with cd('/opt/rule-engine/bin'):
        sudo("/opt/rule-engine/bin/single.sh start", pty=False, user="hsadmin")
def jenkins_audio():
    with settings(warn_only=True):
            with cd('/opt/message-audio/'):
                sudo("/opt/message-audio/bin/single.sh stop", pty=False)
                run('sleep 2')
                run('rm -rf config lib')
            with lcd('/var/lib/jenkins/workspace/product_message_audio/message-audio/target/message-audio-1.0'):
                put('config','/opt/message-audio/')
                put('lib','/opt/message-audio/')
            with cd('/opt/message-audio/bin'):
                run('sleep 2')
                sudo("/opt/message-audio/bin/single.sh start", pty=False)
def jenkins_check():
    sudo("/opt/core-check/bin/single.sh stop", pty=False, user="hsadmin")
    run('sleep 2')
    with cd('/opt/core-check'):
        run('cp -rf config lib /backup/core-check')
        run('rm -rf config lib')
    with lcd('/var/lib/jenkins/workspace/product_core-check/core-check/target'):
        put('%s/config' % (target_corecheck),'/opt/core-check/')
        put('%s/lib' % (target_corecheck),'/opt/core-check/')
    with cd('/opt/core-check/bin'):
        sudo("/opt/core-check/bin/single.sh start", pty=False, user="hsadmin")

def jenkins_oa():
    with settings(warn_only=True):
        result = sudo("kill -9 `ps aux | egrep java.*tomcat-oa/.*Bootstrap|grep -v grep|awk \'{print $2}\'`", pty=False, user="root")
    if result.failed:
        print 'the tomcat-oa process is not exists'
    else:
        print 'kill success'
    run('sleep 1')
    run('/opt/tomcat-oa/bin/shutdown.sh')
    with cd('/opt/tomcat-oa/webapps'):
        run('sudo rm -rf ROOT')
    with lcd('/var/lib/jenkins/workspace/product_oa/oa-service/target'):
        put('oa-service-*.war','/opt/tomcat-oa/webapps/ROOT.war')
    with cd('/opt/tomcat-oa/bin'):
        sudo("/opt/tomcat-oa/bin/startup.sh", pty=False,user="hsadmin")
def jenkins_cfca():
    with settings(warn_only=True):
        result = sudo("kill -9 `ps aux | grep tomcat-cfcahxb|grep -v grep|awk \'{print $2}\'`", pty=False, user="root")
    if result.failed:
        print 'the tomcat-cfca process is not exists'
    else:
        print 'kill success'
    run('sleep 1')
    run('/opt/tomcat-cfcahxb/bin/shutdown.sh')
    with cd('/opt/tomcat-cfcahxb/webapps'):
        run('sudo rm -rf ROOT*')
    with lcd('/var/lib/jenkins/workspace/product_cfca/cfca-provider/target'):
        put('cfca-provider-*.war','/opt/tomcat-cfcahxb/webapps/ROOT.war')
    with cd('/opt/tomcat-cfcahxb/bin'):
        sudo("/opt/tomcat-cfcahxb/bin/startup.sh", pty=False,user="hsadmin")
def jenkins_crm():
    with settings(warn_only=True):
        result = sudo("kill -9 `ps aux | grep tomcat-crm|grep -v grep|awk \'{print $2}\'`", pty=False, user="root")
    if result.failed:
        print 'the tomcat-crm process is not exists'
    else:
        print 'kill success'
    run('sleep 1')
    run('/opt/tomcat-crm/bin/shutdown.sh')
    with cd('/opt/tomcat-crm/webapps'):
        run('sudo rm -rf ROOT*')
    with lcd('/var/lib/jenkins/workspace/product_crm/admin/target'):
        put('admin-*.war','/opt/tomcat-crm/webapps/ROOT.war')
    with cd('/opt/tomcat-crm/bin'):
        sudo("/opt/tomcat-crm/bin/startup.sh", pty=False,user="hsadmin")
def jenkins_crm_dubbo():
        with settings(warn_only=True):
            sudo("/opt/crm-dubbo/bin/single.sh stop", pty=False, user="hsadmin")
            run('sleep 2')
            with cd('/opt/crm-dubbo/'):
                run('rm -rf config lib bin')
            with lcd('/var/lib/jenkins/workspace/product_crm_dubbo/dubbo/target'):
                put('%s/config' % (target_crmdubbo),'/opt/crm-dubbo')
                put('%s/lib' % (target_crmdubbo),'/opt/crm-dubbo')
                put('%s/bin' % (target_crmdubbo),'/opt/crm-dubbo')
                sudo("chown -R hsadmin:hsadmin /opt/crm-dubbo", pty=False, user="hsadmin")
            with cd('/opt/crm-dubbo/bin'):
                sudo("chmod +x /opt/crm-dubbo/bin/single.sh", pty=False, user="hsadmin")
                sudo("/opt/crm-dubbo/bin/single.sh start", pty=False, user="hsadmin")
def jenkins_stat():
        with settings(warn_only=True):
            result = sudo("kill -9 `ps aux | grep tomcat-stat|grep -v grep|awk \'{print $2}\'`", pty=False, user="hsadmin")
        if result.failed:
            print 'The tomcat-stat process is not exists'
        else:
            print 'kill success'
        with cd('/opt/tomcat-stat/bin'):
            sudo("/opt/tomcat-stat/bin/shutdown.sh", pty=False, user="hsadmin")
            run('sleep 5')
        with cd('/opt'):
            run('rm -rf tomcat-stat/webapps/ROOT*')
        with lcd('/var/lib/jenkins/workspace/product_stat/stat-service/target'):
            put('stat-service-*.war','/opt/tomcat-stat/webapps/ROOT.war')
        sudo("/opt/tomcat-stat/bin/startup.sh", pty=False, user="hsadmin")
def jenkins_datashare():
	sudo("/opt/tomcat-datashare/bin/shutdown.sh", pty=False, user="hsadmin")
        run('sleep 2')
	with cd('/opt/tomcat-datashare/webapps'):
            run('sudo rm -rf ROOT*')
	with lcd('/var/lib/jenkins/workspace/product_datashare/datashare-web/target'):
	    put('data-sharing-web-*.war','/opt/tomcat-datashare/webapps/ROOT.war')
	with cd('/opt/tomcat-datashare/bin'):
	    run('sleep 2')
	sudo("/opt/tomcat-datashare/bin/startup.sh", pty=False, user="hsadmin")

def jenkins_event_dubbo():
        with settings(warn_only=True):
            sudo("/opt/event-dubbo/bin/single.sh stop", pty=False, user="hsadmin")
            run('sleep 2')
	with settings(warn_only=True):
            with cd('/opt/event-dubbo/'):
                run('cp -rf config lib /backup/event-dubbo/')
                run('rm -rf config lib bin')
        with lcd('/var/lib/jenkins/workspace/product_event_dubbo/event-dubbo/target'):
	    with settings(warn_only=True):
                run('mkdir /opt/event-dubbo')
		run('mkdir /opt/event-dubbo/logs')
            put('%s/config' % (target_eventdubbo),'/opt/event-dubbo')
            put('%s/lib' % (target_eventdubbo),'/opt/event-dubbo')
            put('%s/bin' % (target_eventdubbo),'/opt/event-dubbo')
            sudo("chown -R hsadmin:hsadmin /opt/event-dubbo", pty=False, user="hsadmin")
        with cd('/opt/event-dubbo/bin'):
            sudo("chmod +x /opt/event-dubbo/bin/single.sh", pty=False, user="hsadmin")
            sudo("/opt/event-dubbo/bin/single.sh start", pty=False, user="hsadmin")
