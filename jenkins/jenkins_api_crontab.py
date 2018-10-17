#!/usr/bin/python
# encoding:utf8
# date:2017-08-07
#version:v1.0.0
import sys
import jenkins
import os
#获取release最新分支
os.chdir("/opt/hxb-core")
os.system('git pull')
w = os.popen("git branch -a|grep  'release_18[0-9][0-9][0-9][0-9]$'|awk 'BEGIN {FS=\"/\"} END {print $2\"/\"$3}'",'r',1)
new_branch = w.read().replace('\n','')


os.chdir("/opt/hxb-lend")
os.system('git pull')
w = os.popen("git branch -a|grep  'release_18[0-9][0-9][0-9][0-9]$'|awk 'BEGIN {FS=\"/\"} END {print $2\"/\"$3}'",'r',1)
new_lend_branch = w.read().replace('\n','')

master_branch = "origin/master"
lanmao = "origin/lanmao"
newbi = "origin/lanmao_newbie"
newbie = "origin/newbie"
sdk = "origin/loantransfer_planquit"
yuesheng = "origin/stepup_plan"
jiaxiquan = "origin/raise_interest"
lanmao_yuesheng = "origin/lanmao_stepup_plan"
#END

server = jenkins.Jenkins('http://192.168.1.39:8080', username='linux', password='f6801d13b1d66c61a6a6d176bdbf1a9e')
choice = sys.argv[1]


def test26():
    param_web = {"profile": "test26", "branch": newbie, "branch_rule_engine": master_branch, "crm_relay": newbie, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_schedule = {"profile": "test26", "branch": newbie, "branch_rule_engine": master_branch, "message": master_branch, "crm_relay": newbie, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_mgmt = {"profile": "test26", "branch": newbie, "branch_rule_engine": master_branch, "crm_relay": newbie, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_lend = {"profile": "test26", "branch": new_lend_branch, "core_branch": new_branch, "branch_rule_engine": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_repay = {"profile": "test26", "branch": newbie, "branch_rule_engine": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_match = {"profile": "test26", "branch": newbie, "branch_rule_engine": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_stat = {"profile": "test26", "branch": newbie, "branch_rule_engine": master_branch, "stat_branch": master_branch, "crm_relay": newbie, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_rule_engine = {"profile": "test26", "branch": master_branch, "branch_core_rely": newbie}
    param_core_dubbo = {"profile": "test26", "branch": newbie, "branch_rule_engine" : master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_crm = {"profile": "test26", "branch": newbie, "rule_engine_rely" : master_branch, "core_rely" : newbie}
#    param_crm_dubbo = {"profile": "test26", "branch": newbie, "rule_engine_rely" : master_branch}
    param_escrow_retry = {"profile": "test26", "branch": newbie, "branch_rule_engine" : master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_crm_dubbo = {"profile": "test26", "branch": master_branch, "rule_engine_rely" : master_branch}


    job_web = ['TEST-web-JOB']
    job_schedule = ['TEST-schedule-JOB']
    job_mgmt = ['TEST-mgmt-JOB']
    job_lend = ['TEST-hxb-lend-JOB']
    job_repay = ['TEST-core-repay-JOB']
    job_match = ['TEST-core-match-JOB']
    job_stat = ['TEST-stat-JOB']
    job_rule_engine = ['Test-rule-engine-JOB']
    job_core_dubbo = ['Test-core-dubbo-JOB']
    job_crm = ['TEST-crm-JOB']
#    job_crm_dubbo = ['Test-crm-dubbo-JOB']
    job_escrow_retry = ['TEST-escrow-retry-JOB']
    for i1 in job_web:
        server.build_job(i1, parameters=param_web)
    for i2 in job_schedule:
        server.build_job(i2, parameters=param_schedule)
    for i3 in job_mgmt:
        server.build_job(i3, parameters=param_mgmt)
    for i4 in job_lend:
        server.build_job(i4, parameters=param_lend)
    for i5 in job_repay:
        server.build_job(i5, parameters=param_repay)
    for i6 in job_match:
        server.build_job(i6, parameters=param_match)
    for i7 in job_stat:
        server.build_job(i7, parameters=param_stat)
    for i8 in job_rule_engine:
        server.build_job(i8, parameters=param_rule_engine)
    for i9 in job_core_dubbo:
        server.build_job(i9, parameters=param_core_dubbo)
    for i10 in job_crm:
        server.build_job(i10, parameters=param_crm)
#    for i11 in job_crm_dubbo:
#        server.build_job(i11, parameters=param_crm_dubbo)
    for i13 in job_escrow_retry:
        server.build_job(i13, parameters=param_escrow_retry)

def test27():
    param_web = {"profile": "test27", "branch": jiaxiquan, "branch_rule_engine": jiaxiquan, "crm_relay": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_schedule = {"profile": "test27", "branch": jiaxiquan, "branch_rule_engine": jiaxiquan, "message": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_mgmt = {"profile": "test27", "branch": jiaxiquan, "branch_rule_engine": jiaxiquan, "crm_relay": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_lend = {"profile": "test27", "branch": new_lend_branch, "core_branch": jiaxiquan, "branch_rule_engine": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_repay = {"profile": "test27", "branch": jiaxiquan, "branch_rule_engine": jiaxiquan, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_match = {"profile": "test27", "branch": jiaxiquan, "branch_rule_engine": jiaxiquan, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_stat = {"profile": "test27", "branch": new_branch, "branch_rule_engine": jiaxiquan, "stat_branch": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_rule_engine = {"profile": "test27", "branch": jiaxiquan, "branch_core_rely": jiaxiquan}
    param_core_dubbo = {"profile": "test27", "branch": jiaxiquan, "branch_rule_engine" : jiaxiquan, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_crm = {"profile": "test26", "branch": master_branch, "rule_engine_rely" : jiaxiquan, "core_rely" : jiaxiquan}
    param_crm_dubbo = {"profile": "test26", "branch": master_branch, "rule_engine_rely" : jiaxiquan}
    param_escrowcallback = {"profile": "test27", "branch": master_branch, "branch_escrow_sdk" : master_branch}
    param_escrow_retry = {"profile": "test27", "branch": newbie, "branch_rule_engine" : master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_crm_dubbo = {"profile": "test27", "branch": master_branch, "rule_engine_rely" : jiaxiquan}


    job_web = ['TEST-web-JOB']
    job_schedule = ['TEST-schedule-JOB']
    job_mgmt = ['TEST-mgmt-JOB']
    job_lend = ['TEST-hxb-lend-JOB']
    job_repay = ['TEST-core-repay-JOB']
    job_match = ['TEST-core-match-JOB']
    job_stat = ['TEST-stat-JOB']
    job_rule_engine = ['Test-rule-engine-JOB']
    job_core_dubbo = ['Test-core-dubbo-JOB']
    job_crm = ['TEST-crm-JOB']
    job_crm_dubbo = ['Test-crm-dubbo-JOB']
    job_escrowcallback = ['Test-escrowcallback-JOB']
    job_escrow_retry = ['TEST-escrow-retry-JOB']
    for i1 in job_web:
        server.build_job(i1, parameters=param_web)
    for i2 in job_schedule:
        server.build_job(i2, parameters=param_schedule)
    for i3 in job_mgmt:
        server.build_job(i3, parameters=param_mgmt)
    for i4 in job_lend:
        server.build_job(i4, parameters=param_lend)
    for i5 in job_repay:
        server.build_job(i5, parameters=param_repay)
    for i6 in job_match:
        server.build_job(i6, parameters=param_match)
    for i7 in job_stat:
        server.build_job(i7, parameters=param_stat)
    for i8 in job_rule_engine:
        server.build_job(i8, parameters=param_rule_engine)
    for i9 in job_core_dubbo:
        server.build_job(i9, parameters=param_core_dubbo)
    for i10 in job_crm:
        server.build_job(i10, parameters=param_crm)
    for i11 in job_crm_dubbo:
        server.build_job(i11, parameters=param_crm_dubbo)
    for i12 in job_escrowcallback:
        server.build_job(i12, parameters=param_escrowcallback)
    for i13 in job_escrow_retry:
        server.build_job(i13, parameters=param_escrow_retry)

def test28():
    param_web = {"profile": "test28", "branch": new_branch, "branch_rule_engine": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_schedule = {"profile": "test28", "branch": new_branch, "branch_rule_engine": master_branch, "message": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_mgmt = {"profile": "test28", "branch": new_branch, "branch_rule_engine": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_lend = {"profile": "test28", "branch": new_lend_branch, "core_branch": new_branch, "branch_rule_engine": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_repay = {"profile": "test28", "branch": new_branch, "branch_rule_engine": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_match = {"profile": "test28", "branch": new_branch, "branch_rule_engine": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_stat = {"profile": "test28", "branch": new_branch, "branch_rule_engine": master_branch, "stat_branch": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch, "event_rely_branch": master_branch}
    param_rule_engine = {"profile": "test28", "branch": master_branch, "branch_core_rely": new_branch}
    param_core_dubbo = {"profile": "test28", "branch": new_branch, "branch_rule_engine" : master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_crm = {"profile": "test28", "branch": newbie, "rule_engine_rely" : master_branch, "core_rely" : master_branch}
    param_crm_dubbo = {"profile": "test28", "branch": newbie, "rule_engine_rely" : master_branch}
    param_escrowcallback = {"profile": "test28", "branch": master_branch, "branch_escrow_sdk" : sdk}
    param_escrow_retry = {"profile": "test28", "branch": newbie, "branch_rule_engine" : master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_crm_dubbo = {"profile": "test28", "branch": master_branch, "rule_engine_rely" : master_branch}


    job_web = ['TEST-web-JOB']
    job_schedule = ['TEST-schedule-JOB']
    job_mgmt = ['TEST-mgmt-JOB']
    job_lend = ['TEST-hxb-lend-JOB']
    job_repay = ['TEST-core-repay-JOB']
    job_match = ['TEST-core-match-JOB']
    job_stat = ['TEST-stat-JOB']
    job_rule_engine = ['Test-rule-engine-JOB']
    job_core_dubbo = ['Test-core-dubbo-JOB']
    job_crm = ['TEST-crm-JOB']
    job_crm_dubbo = ['Test-crm-dubbo-JOB']
    job_escrowcallback = ['Test-escrowcallback-JOB']
    job_escrow_retry = ['TEST-escrow-retry-JOB']
    for i1 in job_web:
        server.build_job(i1, parameters=param_web)
    for i2 in job_schedule:
        server.build_job(i2, parameters=param_schedule)
    for i3 in job_mgmt:
        server.build_job(i3, parameters=param_mgmt)
    for i4 in job_lend:
        server.build_job(i4, parameters=param_lend)
    for i5 in job_repay:
        server.build_job(i5, parameters=param_repay)
    for i6 in job_match:
        server.build_job(i6, parameters=param_match)
    for i7 in job_stat:
        server.build_job(i7, parameters=param_stat)
    for i8 in job_rule_engine:
        server.build_job(i8, parameters=param_rule_engine)
    for i9 in job_core_dubbo:
        server.build_job(i9, parameters=param_core_dubbo)
    for i10 in job_crm:
        server.build_job(i10, parameters=param_crm)
    for i11 in job_crm_dubbo:
        server.build_job(i11, parameters=param_crm_dubbo)
    for i12 in job_escrowcallback:
        server.build_job(i12, parameters=param_escrowcallback)
    for i13 in job_escrow_retry:
       server.build_job(i13, parameters=param_escrow_retry)




def test29():
    param_web = {"profile": "test29", "branch": new_branch, "branch_rule_engine": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_schedule = {"profile": "test29", "branch": new_branch, "branch_rule_engine": master_branch, "message": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_mgmt = {"profile": "test29", "branch": new_branch, "branch_rule_engine": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_lend = {"profile": "test29", "branch": new_branch, "core_branch": new_branch, "branch_rule_engine": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_repay = {"profile": "test29", "branch": new_branch, "branch_rule_engine": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_match = {"profile": "test29", "branch": new_branch, "branch_rule_engine": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_stat = {"profile": "test29", "branch": new_branch, "branch_rule_engine": master_branch, "stat_branch": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch, "event_rely_branch": master_branch}
    param_rule_engine = {"profile": "test29", "branch": master_branch, "branch_core_rely": new_branch}
    param_core_dubbo = {"profile": "test29", "branch": new_branch, "branch_rule_engine" : master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
#    param_crm = {"profile": "test29", "branch": newbie, "rule_engine_rely" : master_branch, "core_rely" : master_branch}
    param_crm_dubbo = {"profile": "test29", "branch": newbie, "rule_engine_rely" : master_branch}
#    param_escrowcallback = {"profile": "test29", "branch": master_branch, "branch_escrow_sdk" : sdk}
#    param_escrow_retry = {"profile": "test29", "branch": newbie, "branch_rule_engine" : master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_crm_dubbo = {"profile": "test29", "branch": master_branch, "rule_engine_rely" : master_branch}


    job_web = ['TEST-web-JOB']
    job_schedule = ['TEST-schedule-JOB']
    job_mgmt = ['TEST-mgmt-JOB']
    job_lend = ['TEST-hxb-lend-JOB']
    job_repay = ['TEST-core-repay-JOB']
    job_match = ['TEST-core-match-JOB']
    job_stat = ['TEST-stat-JOB']
    job_rule_engine = ['Test-rule-engine-JOB']
    job_core_dubbo = ['Test-core-dubbo-JOB']
    job_crm = ['TEST-crm-JOB']
    job_crm_dubbo = ['Test-crm-dubbo-JOB']
    job_escrowcallback = ['Test-escrowcallback-JOB']
    job_escrow_retry = ['TEST-escrow-retry-JOB']
    for i1 in job_web:
        server.build_job(i1, parameters=param_web)
    for i2 in job_schedule:
        server.build_job(i2, parameters=param_schedule)
    for i3 in job_mgmt:
        server.build_job(i3, parameters=param_mgmt)
    for i4 in job_lend:
        server.build_job(i4, parameters=param_lend)
    for i5 in job_repay:
        server.build_job(i5, parameters=param_repay)
    for i6 in job_match:
        server.build_job(i6, parameters=param_match)
    for i7 in job_stat:
        server.build_job(i7, parameters=param_stat)
    for i8 in job_rule_engine:
        server.build_job(i8, parameters=param_rule_engine)
    for i9 in job_core_dubbo:
        server.build_job(i9, parameters=param_core_dubbo)
#    for i10 in job_crm:
#        server.build_job(i10, parameters=param_crm)
    for i11 in job_crm_dubbo:
        server.build_job(i11, parameters=param_crm_dubbo)
    #  for i12 in job_escrowcallback:
    #      server.build_job(i12, parameters=param_escrowcallback)
    #  for i13 in job_escrow_retry:
    #      server.build_job(i13, parameters=param_escrow_retry)



def test31():
    param_web = {"profile": "test31", "branch": new_branch, "branch_rule_engine": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_schedule = {"profile": "test31", "branch": new_branch, "branch_rule_engine": master_branch, "message": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_mgmt = {"profile": "test31", "branch": new_branch, "branch_rule_engine": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_lend = {"profile": "test31", "branch": new_lend_branch, "core_branch": new_branch, "branch_rule_engine": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_repay = {"profile": "test31", "branch": new_branch, "branch_rule_engine": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_match = {"profile": "test31", "branch": new_branch, "branch_rule_engine": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_stat = {"profile": "test31", "branch": new_branch, "branch_rule_engine": master_branch, "stat_branch": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch, "event_rely_branch": master_branch}
    param_rule_engine = {"profile": "test31", "branch": master_branch, "branch_core_rely": new_branch}
    param_core_dubbo = {"profile": "test31", "branch": new_branch, "branch_rule_engine" : master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_crm = {"profile": "test31", "branch": newbie, "rule_engine_rely" : master_branch, "core_rely" : master_branch}
    param_crm_dubbo = {"profile": "test31", "branch": newbie, "rule_engine_rely" : master_branch}
    param_escrowcallback = {"profile": "test31", "branch": master_branch, "branch_escrow_sdk" : sdk}
    param_escrow_retry = {"profile": "test31", "branch": newbie, "branch_rule_engine" : master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_crm_dubbo = {"profile": "test31", "branch": master_branch, "rule_engine_rely" : master_branch}


    job_web = ['TEST-web-JOB']
    job_schedule = ['TEST-schedule-JOB']
    job_mgmt = ['TEST-mgmt-JOB']
    job_lend = ['TEST-hxb-lend-JOB']
    job_repay = ['TEST-core-repay-JOB']
    job_match = ['TEST-core-match-JOB']
    job_stat = ['TEST-stat-JOB']
    job_rule_engine = ['Test-rule-engine-JOB']
    job_core_dubbo = ['Test-core-dubbo-JOB']
    job_crm = ['TEST-crm-JOB']
    job_crm_dubbo = ['Test-crm-dubbo-JOB']
    job_escrowcallback = ['Test-escrowcallback-JOB']
    job_escrow_retry = ['TEST-escrow-retry-JOB']
    for i1 in job_web:
        server.build_job(i1, parameters=param_web)
    for i2 in job_schedule:
        server.build_job(i2, parameters=param_schedule)
    for i3 in job_mgmt:
        server.build_job(i3, parameters=param_mgmt)
    for i4 in job_lend:
        server.build_job(i4, parameters=param_lend)
    for i5 in job_repay:
        server.build_job(i5, parameters=param_repay)
    for i6 in job_match:
        server.build_job(i6, parameters=param_match)
    for i7 in job_stat:
        server.build_job(i7, parameters=param_stat)
    for i8 in job_rule_engine:
        server.build_job(i8, parameters=param_rule_engine)
    for i9 in job_core_dubbo:
        server.build_job(i9, parameters=param_core_dubbo)
    for i10 in job_crm:
        server.build_job(i10, parameters=param_crm)
    for i11 in job_crm_dubbo:
        server.build_job(i11, parameters=param_crm_dubbo)
    for i12 in job_escrowcallback:
        server.build_job(i12, parameters=param_escrowcallback)
    for i13 in job_escrow_retry:
       server.build_job(i13, parameters=param_escrow_retry)



def test32():
    param_web = {"profile": "test32", "branch": lanmao_yuesheng, "branch_rule_engine": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
#    param_schedule = {"profile": "test32", "branch": lanmao_yuesheng, "branch_rule_engine": master_branch, "message": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_mgmt = {"profile": "test32", "branch": lanmao_yuesheng, "branch_rule_engine": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_lend = {"profile": "test32", "branch": lanmao_yuesheng, "core_branch": new_branch, "branch_rule_engine": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_repay = {"profile": "test32", "branch": lanmao_yuesheng, "branch_rule_engine": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_match = {"profile": "test32", "branch": lanmao_yuesheng, "branch_rule_engine": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_stat = {"profile": "test32", "branch": lanmao_yuesheng, "branch_rule_engine": master_branch, "stat_branch": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_rule_engine = {"profile": "test32", "branch": master_branch, "branch_core_rely": new_branch}
    param_core_dubbo = {"profile": "test32", "branch": lanmao_yuesheng, "branch_rule_engine" : master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_crm = {"profile": "test32", "branch": master_branch, "rule_engine_rely" : master_branch, "core_rely" : lanmao_yuesheng}
    param_crm_dubbo = {"profile": "test32", "branch": master_branch, "rule_engine_rely" : master_branch}
    param_escrowcallback = {"profile": "test32", "branch": lanmao, "branch_escrow_sdk" : lanmao}
    param_escrow_retry = {"profile": "test32", "branch": lanmao_yuesheng, "branch_rule_engine" : master_branch, "branch_escrow_sdk": lanmao, "branch_escrow":lanmao}
    param_crm_dubbo = {"profile": "test32", "branch": master_branch, "rule_engine_rely" : master_branch}


    job_web = ['TEST-web-JOB']
#    job_schedule = ['TEST-schedule-JOB']
    job_mgmt = ['TEST-mgmt-JOB']
    job_lend = ['TEST-hxb-lend-JOB']
    job_repay = ['TEST-core-repay-JOB']
    job_match = ['TEST-core-match-JOB']
    job_stat = ['TEST-stat-JOB']
    job_rule_engine = ['Test-rule-engine-JOB']
    job_core_dubbo = ['Test-core-dubbo-JOB']
    job_crm = ['TEST-crm-JOB']
    job_crm_dubbo = ['Test-crm-dubbo-JOB']
    job_escrowcallback = ['Test-escrowcallback-JOB']
    job_escrow_retry = ['TEST-escrow-retry-JOB']
    for i1 in job_web:
        server.build_job(i1, parameters=param_web)
#    for i2 in job_schedule:
#        server.build_job(i2, parameters=param_schedule)
    for i3 in job_mgmt:
        server.build_job(i3, parameters=param_mgmt)
    for i4 in job_lend:
        server.build_job(i4, parameters=param_lend)
    for i5 in job_repay:
        server.build_job(i5, parameters=param_repay)
    for i6 in job_match:
        server.build_job(i6, parameters=param_match)
    for i7 in job_stat:
        server.build_job(i7, parameters=param_stat)
    for i8 in job_rule_engine:
        server.build_job(i8, parameters=param_rule_engine)
    for i9 in job_core_dubbo:
        server.build_job(i9, parameters=param_core_dubbo)
    for i10 in job_crm:
        server.build_job(i10, parameters=param_crm)
    for i11 in job_crm_dubbo:
        server.build_job(i11, parameters=param_crm_dubbo)
    for i12 in job_escrowcallback:
        server.build_job(i12, parameters=param_escrowcallback)
    for i13 in job_escrow_retry:
        server.build_job(i13, parameters=param_escrow_retry)



def test34():
    param_web = {"profile": "test34", "branch": newbi, "branch_rule_engine": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_schedule = {"profile": "test34", "branch": newbi, "branch_rule_engine": master_branch, "message": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_mgmt = {"profile": "test34", "branch": newbi, "branch_rule_engine": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_lend = {"profile": "test34", "branch": new_branch, "branch_rule_engine": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_repay = {"profile": "test34", "branch": newbi, "branch_rule_engine": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_match = {"profile": "test34", "branch": newbi, "branch_rule_engine": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_stat = {"profile": "test34", "branch": newbi, "branch_rule_engine": master_branch, "stat_branch": lanmao, "crm_relay": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_rule_engine = {"profile": "test34", "branch": master_branch, "branch_core_rely": newbi}
    param_core_dubbo = {"profile": "test34", "branch": newbi, "branch_rule_engine" : master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_crm = {"profile": "test34", "branch": master_branch, "rule_engine_rely" : master_branch, "core_rely" : lanmao}
    param_crm_dubbo = {"profile": "test34", "branch": master_branch, "rule_engine_rely" : master_branch}
    param_escrowcallback = {"profile": "test34", "branch": lanmao, "branch_escrow_sdk" : lanmao}
    param_escrow_retry = {"profile": "test34", "branch": newbi, "branch_rule_engine" : master_branch, "branch_escrow_sdk": lanmao, "branch_escrow":lanmao}
    param_crm_dubbo = {"profile": "test34", "branch": master_branch, "rule_engine_rely" : master_branch}


    job_web = ['TEST-web-JOB']
    job_schedule = ['TEST-schedule-JOB']
    job_mgmt = ['TEST-mgmt-JOB']
    job_lend = ['TEST-hxb-lend-JOB']
    job_repay = ['TEST-core-repay-JOB']
    job_match = ['TEST-core-match-JOB']
    job_stat = ['TEST-stat-JOB']
    job_rule_engine = ['Test-rule-engine-JOB']
    job_core_dubbo = ['Test-core-dubbo-JOB']
    job_crm = ['TEST-crm-JOB']
    job_crm_dubbo = ['Test-crm-dubbo-JOB']
    job_escrowcallback = ['Test-escrowcallback-JOB']
    job_escrow_retry = ['TEST-escrow-retry-JOB']
    for i1 in job_web:
        server.build_job(i1, parameters=param_web)
    for i2 in job_schedule:
        server.build_job(i2, parameters=param_schedule)
    for i3 in job_mgmt:
        server.build_job(i3, parameters=param_mgmt)
    for i4 in job_lend:
        server.build_job(i4, parameters=param_lend)
    for i5 in job_repay:
        server.build_job(i5, parameters=param_repay)
    for i6 in job_match:
        server.build_job(i6, parameters=param_match)
    for i7 in job_stat:
        server.build_job(i7, parameters=param_stat)
    for i8 in job_rule_engine:
        server.build_job(i8, parameters=param_rule_engine)
    for i9 in job_core_dubbo:
        server.build_job(i9, parameters=param_core_dubbo)
    for i10 in job_crm:
        server.build_job(i10, parameters=param_crm)
    for i11 in job_crm_dubbo:
        server.build_job(i11, parameters=param_crm_dubbo)
    for i12 in job_escrowcallback:
        server.build_job(i12, parameters=param_escrowcallback)
    for i13 in job_escrow_retry:
        server.build_job(i13, parameters=param_escrow_retry)








def test35():
    param_web = {"profile": "test35", "branch": lanmao_yuesheng, "branch_rule_engine": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_schedule = {"profile": "test35", "branch": lanmao_yuesheng, "branch_rule_engine": master_branch, "message": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_mgmt = {"profile": "test35", "branch": lanmao_yuesheng, "branch_rule_engine": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_lend = {"profile": "test35", "branch": lanmao_yuesheng, "branch_rule_engine": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_repay = {"profile": "test35", "branch": lanmao_yuesheng, "branch_rule_engine": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_match = {"profile": "test35", "branch": lanmao_yuesheng, "branch_rule_engine": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_stat = {"profile": "test35", "branch": lanmao_yuesheng, "branch_rule_engine": master_branch, "stat_branch": master_branch, "crm_relay": master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
    param_rule_engine = {"profile": "test35", "branch": master_branch, "branch_core_rely": new_branch}
    param_core_dubbo = {"profile": "test35", "branch": lanmao_yuesheng, "branch_rule_engine" : master_branch, "branch_escrow_sdk": lanmao, "branch_escrow": lanmao}
#    param_crm = {"profile": "test35", "branch": master_branch, "rule_engine_rely" : master_branch, "core_rely" : lanmao_yuesheng}
    param_crm_dubbo = {"profile": "test35", "branch": master_branch, "rule_engine_rely" : master_branch}
    param_escrowcallback = {"profile": "test35", "branch": lanmao, "branch_escrow_sdk" : lanmao_yuesheng}
    param_escrow_retry = {"profile": "test35", "branch": lanmao_yuesheng, "branch_rule_engine" : master_branch, "branch_escrow_sdk": lanmao, "branch_escrow":lanmao}
    param_crm_dubbo = {"profile": "test35", "branch": master_branch, "rule_engine_rely" : master_branch}


    job_web = ['TEST-web-JOB']
    job_schedule = ['TEST-schedule-JOB']
    job_mgmt = ['TEST-mgmt-JOB']
    job_lend = ['TEST-hxb-lend-JOB']
    job_repay = ['TEST-core-repay-JOB']
    job_match = ['TEST-core-match-JOB']
    job_stat = ['TEST-stat-JOB']
    job_rule_engine = ['Test-rule-engine-JOB']
    job_core_dubbo = ['Test-core-dubbo-JOB']
    job_crm = ['TEST-crm-JOB']
    job_crm_dubbo = ['Test-crm-dubbo-JOB']
    job_escrowcallback = ['Test-escrowcallback-JOB']
    job_escrow_retry = ['TEST-escrow-retry-JOB']
    for i1 in job_web:
        server.build_job(i1, parameters=param_web)
    for i2 in job_schedule:
        server.build_job(i2, parameters=param_schedule)
    for i3 in job_mgmt:
        server.build_job(i3, parameters=param_mgmt)
    for i4 in job_lend:
        server.build_job(i4, parameters=param_lend)
    for i5 in job_repay:
        server.build_job(i5, parameters=param_repay)
    for i6 in job_match:
        server.build_job(i6, parameters=param_match)
    for i7 in job_stat:
        server.build_job(i7, parameters=param_stat)
    for i8 in job_rule_engine:
        server.build_job(i8, parameters=param_rule_engine)
    for i9 in job_core_dubbo:
        server.build_job(i9, parameters=param_core_dubbo)
#    for i10 in job_crm:
#        server.build_job(i10, parameters=param_crm)
    for i11 in job_crm_dubbo:
        server.build_job(i11, parameters=param_crm_dubbo)
    for i12 in job_escrowcallback:
        server.build_job(i12, parameters=param_escrowcallback)
    for i13 in job_escrow_retry:
        server.build_job(i13, parameters=param_escrow_retry)

def test36():
    param_web = {"profile": "test36", "branch": yuesheng, "branch_rule_engine": master_branch, "crm_relay": newbie, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_schedule = {"profile": "test36", "branch": yuesheng, "branch_rule_engine": master_branch, "message": master_branch, "crm_relay": newbie, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_mgmt = {"profile": "test36", "branch": yuesheng, "branch_rule_engine": master_branch, "crm_relay": newbie, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_lend = {"profile": "test36", "branch": yuesheng, "core_branch": yuesheng, "branch_rule_engine": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_repay = {"profile": "test36", "branch": yuesheng, "branch_rule_engine": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_match = {"profile": "test36", "branch": yuesheng, "branch_rule_engine": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_stat = {"profile": "test36", "branch": yuesheng, "branch_rule_engine": master_branch, "stat_branch": yuesheng, "crm_relay": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch, "event_rely_branch": master_branch}
    param_rule_engine = {"profile": "test36", "branch": master_branch, "branch_core_rely": new_branch}
    param_core_dubbo = {"profile": "test36", "branch": yuesheng, "branch_rule_engine" : master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_crm = {"profile": "test36", "branch": newbie, "rule_engine_rely" : master_branch, "core_rely" : newbie}
    param_crm_dubbo = {"profile": "test36", "branch": newbie, "rule_engine_rely" : master_branch}
    param_escrowcallback = {"profile": "test36", "branch": master_branch, "branch_escrow_sdk" : sdk}
    param_escrow_retry = {"profile": "test36", "branch": newbie, "branch_rule_engine" : master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_crm_dubbo = {"profile": "test36", "branch": master_branch, "rule_engine_rely" : master_branch}


    job_web = ['TEST-web-JOB']
    job_schedule = ['TEST-schedule-JOB']
    job_mgmt = ['TEST-mgmt-JOB']
    job_lend = ['TEST-hxb-lend-JOB']
    job_repay = ['TEST-core-repay-JOB']
    job_match = ['TEST-core-match-JOB']
    job_stat = ['TEST-stat-JOB']
    job_rule_engine = ['Test-rule-engine-JOB']
    job_core_dubbo = ['Test-core-dubbo-JOB']
    job_crm = ['TEST-crm-JOB']
    job_crm_dubbo = ['Test-crm-dubbo-JOB']
    job_escrowcallback = ['Test-escrowcallback-JOB']
    job_escrow_retry = ['TEST-escrow-retry-JOB']
    for i1 in job_web:
        server.build_job(i1, parameters=param_web)
    for i2 in job_schedule:
        server.build_job(i2, parameters=param_schedule)
    for i3 in job_mgmt:
        server.build_job(i3, parameters=param_mgmt)
    for i4 in job_lend:
        server.build_job(i4, parameters=param_lend)
    for i5 in job_repay:
        server.build_job(i5, parameters=param_repay)
    for i6 in job_match:
        server.build_job(i6, parameters=param_match)
    for i7 in job_stat:
        server.build_job(i7, parameters=param_stat)
    for i8 in job_rule_engine:
        server.build_job(i8, parameters=param_rule_engine)
    for i9 in job_core_dubbo:
        server.build_job(i9, parameters=param_core_dubbo)
    for i10 in job_crm:
        server.build_job(i10, parameters=param_crm)
    for i11 in job_crm_dubbo:
        server.build_job(i11, parameters=param_crm_dubbo)
    for i12 in job_escrowcallback:
        server.build_job(i12, parameters=param_escrowcallback)
    for i13 in job_escrow_retry:
        server.build_job(i13, parameters=param_escrow_retry)

def test37():
    param_web = {"profile": "test37", "branch": yuesheng, "branch_rule_engine": master_branch, "crm_relay": newbie, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_schedule = {"profile": "test37", "branch": yuesheng, "branch_rule_engine": master_branch, "message": master_branch, "crm_relay": newbie, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_mgmt = {"profile": "test37", "branch": yuesheng, "branch_rule_engine": master_branch, "crm_relay": newbie, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_lend = {"profile": "test37", "branch": yuesheng, "core_branch": yuesheng, "branch_rule_engine": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_repay = {"profile": "test37", "branch": yuesheng, "branch_rule_engine": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_match = {"profile": "test37", "branch": yuesheng, "branch_rule_engine": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_stat = {"profile": "test37", "branch": yuesheng, "branch_rule_engine": master_branch, "stat_branch": yuesheng, "crm_relay": master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch, "event_rely_branch": master_branch}
    param_rule_engine = {"profile": "test37", "branch": master_branch, "branch_core_rely": new_branch}
    param_core_dubbo = {"profile": "test37", "branch": yuesheng, "branch_rule_engine" : master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_crm = {"profile": "test37", "branch": newbie, "rule_engine_rely" : master_branch, "core_rely" : newbie}
    param_crm_dubbo = {"profile": "test37", "branch": newbie, "rule_engine_rely" : master_branch}
    param_escrowcallback = {"profile": "test37", "branch": master_branch, "branch_escrow_sdk" : sdk}
    param_escrow_retry = {"profile": "test37", "branch": newbie, "branch_rule_engine" : master_branch, "branch_escrow_sdk": sdk, "branch_escrow": master_branch}
    param_crm_dubbo = {"profile": "test37", "branch": master_branch, "rule_engine_rely" : master_branch}


    job_web = ['TEST-web-JOB']
    job_schedule = ['TEST-schedule-JOB']
    job_mgmt = ['TEST-mgmt-JOB']
    job_lend = ['TEST-hxb-lend-JOB']
    job_repay = ['TEST-core-repay-JOB']
    job_match = ['TEST-core-match-JOB']
    job_stat = ['TEST-stat-JOB']
    job_rule_engine = ['Test-rule-engine-JOB']
    job_core_dubbo = ['Test-core-dubbo-JOB']
    job_crm = ['TEST-crm-JOB']
    job_crm_dubbo = ['Test-crm-dubbo-JOB']
    job_escrowcallback = ['Test-escrowcallback-JOB']
    job_escrow_retry = ['TEST-escrow-retry-JOB']
    for i1 in job_web:
        server.build_job(i1, parameters=param_web)
    for i2 in job_schedule:
        server.build_job(i2, parameters=param_schedule)
    for i3 in job_mgmt:
        server.build_job(i3, parameters=param_mgmt)
    for i4 in job_lend:
        server.build_job(i4, parameters=param_lend)
    for i5 in job_repay:
        server.build_job(i5, parameters=param_repay)
    for i6 in job_match:
        server.build_job(i6, parameters=param_match)
    for i7 in job_stat:
        server.build_job(i7, parameters=param_stat)
    for i8 in job_rule_engine:
        server.build_job(i8, parameters=param_rule_engine)
    for i9 in job_core_dubbo:
        server.build_job(i9, parameters=param_core_dubbo)
    for i10 in job_crm:
        server.build_job(i10, parameters=param_crm)
    for i11 in job_crm_dubbo:
        server.build_job(i11, parameters=param_crm_dubbo)
    for i12 in job_escrowcallback:
        server.build_job(i12, parameters=param_escrowcallback)
    for i13 in job_escrow_retry:
        server.build_job(i13, parameters=param_escrow_retry)


if choice == 'test26':
    test26()
elif choice == 'test27':
    test27()
elif choice == 'test28':
    test28()
elif choice == 'test29':
    test29()
elif choice == 'test31':
    test31()
elif choice == 'test32':
    test32()
elif choice == 'test34':
    test34()
elif choice == 'test35':
    test35()
elif choice == 'test36':
    test36()
elif choice == 'test37':
    test37()
else:
    print 'Please input your choice'
