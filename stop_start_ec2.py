import boto3
import boto.ec2
import sys

#key_id = input("please give key_id of your aws_access_key_id :-  ")
#access_key = input ("please type or paste aws_secret_access_key here :-  ")

#region = input("Enter the region :- ")
#instance_ids = input("Enter the instance_ids :- ")

# specify AWS keys
auth = {"aws_access_key_id": "key_id","aws_secret_access_key":"access_key"}

def main():
    # read arguments from the command line and 
    # check whether at least two elements were entered
    if len(sys.argv) < 2:
	    print("Usage: python aws.py {start|stop}\n")
	    sys.exit(0)
    else:
	    action = sys.argv[1] 

    if action == "start":
	    startInstance()
    elif action == "stop":
    	stopInstance()
    else:
    	print ("Usage: python aws.py {start|stop}\n")

def stopInstance():
    print ("Stopping the instance...")

    try:
        ec2 = boto.ec2.connect_to_region("region", **auth)

    except Exception as e1:
        error1 = "Error1: %s" % str(e1)
        print(error1)
        sys.exit(0)

    try:
         ec2.stop_instances("instance_ids")

    except Exception as e2:
        error2 = "Error2: %s" % str(e2)
        print(error2)
        sys.exit(0)

def startInstance():
    print ("Starting the instance...")

    # change the region if its predefine
    try:
        ec2 = boto.ec2.connect_to_region("region", **auth)

    except Exception as e1:
        error1 = "Error1: %s" % str(e1)
        print(error1)
        sys.exit(0)

    # if its predefine please change instance ID 
    try:
        ec2.start_instances("instance_ids")

    except Exception as e2:
        error2 = "Error2: %s" % str(e2)
        print(error2)
        sys.exit(0) 

    ec2.instances.all()
    print("{0}\nPublic IPv4\n".format(instance.public_ip_address))    

print ("code successfully launchd  ")        

if __name__ == '__main__':
    main()
