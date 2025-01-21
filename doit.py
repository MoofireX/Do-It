import json
import os

def save_todo(data, dir):
	with open(dir, 'w') as file:
		json.dump(data, file)

def load_todo(dir):
	with open(dir ,'r') as file:
		todo = json.load(file)
		return todo

def ls(directory):
	todo_list = []
	for filename in os.listdir(directory):
		todo_list.append(filename)
	return todo_list		

while True:
	dir = 'todo.json'
	data = {}
	doing = input("Do you want a check off tasks, view your todo list, or do you want to add a task to your list? Say c for check, a for adding, or v for viewing. If you want to exit, press e. ")
	todo_list = ls('.')
	iteratable = 0

	if doing == "a":
	
		tasks = input("What are the tasks you need to do? Seperate multiple tasks with commas. For efficiency and simplicity, do not add spaces between the commas.  ")
		tasks = tasks.split(',')
		print(f"This is the task you have added: {list(tasks)}")
	
		if dir not in todo_list:
			pass
		else:
			iteratable = len(load_todo(dir))
			data = load_todo(dir)
	
		for task in tasks:
			data[str(iteratable)] = task
			iteratable += 1
		save_todo(data, dir)
	elif doing == "c":
		if dir not in todo_list:
			print("Please create a todo list first by entering a, or move the todo_list file into the current directory (the same one doit.py is in.")
		else:
			data = load_todo(dir)
			check = input("Which task would you like to check off? Enter the name of the task exactly. ")
			for task in data:
				if data[task] == check:
					del data[task]
					print("Task successfully checked off!")
					save_todo(data, dir)
					break
				else:
					print("Sorry, that task is not in your list. Please enter the task's name exactly.")
					break
	elif doing == "v":
		view = []
		data = load_todo(dir)
	
		for task in data:
			view.append(data[task])
		print(view)	
	
	elif doing == "e":
		print("Exiting...")
		break

	else:
		print("Please try again and enter either a, c, v, or e.")
