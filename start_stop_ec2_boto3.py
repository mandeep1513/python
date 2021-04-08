import boto3
import sys
import os 
import time

def get_ec2_con_for_give_region(my_region):
    ec2_con_re=boto3.resource('ec2',region_name=my_region)
    return ec2_con_re
def list_instances_on_myregion(ec2_con_re):
    for each in ec2_con_re.instances.all():
        print (each.id)
def get_instant_state(ec2_con_re,in_id):
    for each in ec2_con_re.instances.filter(Filters=[{'Name':'instance-id','values':[in_id]}]):
        pr_st=each.state['Name']
    return pr_st
def start_instance(ec2_con_re,in_id):
    if pr_st== 'running':
            print ("instance is already running")
    else:
            for each in ec2_con_re.instances.filter(Filters=[{'Name':'instance-id','values':[in_id]}]):
                    each.start()
                    print("please wait it is going to start, once if is is started the we let you know")
                    each.wait_until_running()
                    print("now it is running")
    return None
def stop_instance(ec2_con_re,ub_id):
    pr_st=get_instant_state(ec2_con_re,in_id)
    if pr_st=="stopped":
            print("instaces is already stopped")
    else:
            for each in ec2_con_re.instances.filter(Filters=[{'Name':'instance-id','values':[in_id]}]):
                    each.stop()
                    print("instances stoped")
    return
def Thank_you():
    print("\n\n *Thank you for using this script*")
    return None                    
#print(" code run successfully ")                                    	
