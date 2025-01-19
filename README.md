# TaskMan CLI

<div align="center">

[![TaskMan - Your Personal Task Manager](https://img.shields.io/badge/TaskMan-Your%20Personal%20Task%20Manager-blue?style=for-the-badge&logo=python&logoColor=white)](https://github.com/tahadnan/To-do-list-manager)

[![PyPI version](https://badge.fury.io/py/ttask-manager.svg)](https://badge.fury.io/py/ttask-manager)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

## 🗃️ Archival Notice

This repository has been archived. Original Taskman-CLI was in a separate repository than the Taskman-CLI-PyPi package, just as an exercise to get comfortable with packaging. I have gotten enough experience now and will be working exclusively on the Taskman-CLI-PyPi repository. As such this repository won't be updated anymore and any further development will take place in the repository Taskman-CLI-PyPi.

You are welcome to check the [Taskman-CLI-PyPi](https://github.com/tahadnan/TaskMan-CLI-PyPi) repository for further improvements and releases.

## 📝 Description

TaskMan CLI is a powerful and user-friendly task management application built with Python. It offers a seamless command-line interface for efficiently managing your daily tasks, helping you boost productivity and stay organized.

## ✨ Features

- 📌 **Add Tasks**: Easily add new tasks to your to-do list with optional priority levels
- 🗑️ **Remove Tasks**: Remove tasks from your to-do list
- ✅ **Mark Tasks as Completed**: Move tasks to a "done" list when completed
- 👀 **View Current State**: See all your tasks, both pending and completed
- 🧹 **Clear Lists**: Clean up your to-do and done lists with a single command
- 💾 **Save on Exit**: Option to save your tasks when exiting the application
- 🔄 **Load on Start**: Your previously saved tasks are automatically loaded when you start the application
- 📊 **Generate Reports**: Create daily task reports to track your productivity
- 🔢 **Priority Levels**: Assign priority levels (high, medium, low) to your tasks

## 🚀 Installation

1. Ensure you have Python 3.6+ installed on your system.
2. Clone the repo and cd into it:

```bash
git clone https://github.com/tahadnan/TaskMan-CLI.git
cd TaskMan-CLI
```
3. Install required libraries (It's better to use a [Virtual Environment](https://realpython.com/python-virtual-environments-a-primer/)):
```bash
pip install -r requirements.txt
```
**(P.S: I'm using Linux, so some commands may differ slightly. Please take this into consideration.)**

## 🛠️ Usage

1. After installation, you can start TaskMan CLI by running:

```bash
python3 main.py
```

2. Once launched, you'll see the TaskMan welcome screen. Type `help` to see available commands:

```
TaskMan > help
```

3. Use the various commands to manage your tasks. Here are some examples:

```
TaskMan > add Buy groceries:high | Call mom | Finish report:low
TaskMan > list-todo
TaskMan > mark-as-done Buy groceries
TaskMan > list-both
```

## 📚 Available Commands

- `add [task1] | [task2] | ...`: Add one or more tasks
  - Format: task:priority (e.g., "Buy groceries:high")
- `remove [task1] | [task2] | ...`: Remove one or more tasks
- `mark-as-done / mad [task1]...`: Mark one or more tasks as completed
- `list-both / lb`: Show all tasks (to-do and done)
- `list-todo / ltd`: Show pending tasks
- `list-done / ld`: Show completed tasks
- `clear-todo / cltd`: Clear all pending tasks
- `clear-done / cld`: Clear all completed tasks
- `reset`: Clear all tasks (both to-do and done)
- `report [name]`: Generate a report (optional custom name)
- `save`: Manually save current state to file
- `help`: Show the help message
- `clear / Ctrl+l`: Clear the screen
- `exit`: Exit the program (prompts to save tasks)

## 💡 Tips

- Use the up and down arrow keys to navigate through your command history.
- TaskMan supports auto-completion. Start typing a command and press Tab to complete it.
- When exiting, you'll be prompted to save your tasks. This ensures you don't lose any changes.
- Your saved tasks are automatically loaded when you start the application.
- You can assign priorities to tasks: high, medium (default), or low.

## 🤝 Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please make sure to update tests as appropriate.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the ZTM Python course by Andrei Neagoie
- Built with love using Python and prompt_toolkit

---

<div align="center">

Made with ❤️ by [Taha Adnan](https://github.com/tahadnan)

</div>
