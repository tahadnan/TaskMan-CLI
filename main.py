import task_mannager_class
import argparse

parser = argparse.ArgumentParser(description="This is a script that helps you with creating and managing your to-do list.")
parser.add_argument('create',help='IDK')

args = parser.parse_args()

if args.create == 'create':
    print("working")
