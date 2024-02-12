import openai
import typer
from rich.table import Table
import rich
import os

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def __prompt() -> str:
    prompt = typer.prompt('\n¿What do you want to say?')
    if prompt == 'exit':
        exit_ = typer.confirm('Are you sure?')
        if exit_:
            print('Well, ¡Goodbye!')
            raise typer.Abort()
        return __prompt()
    return prompt

def main_function():
    openai.api_key = OPENAI_API_KEY
    rich.print('💬 [bold green]Chat-Gpt[/bold green]')
    table = Table('Command', 'Description')
    table.add_row('exit', 'close the programm')
    table.add_row('new', 'Start a new chat')
    rich.print(table)
    context = {
        'role': 'system',
        'content': 'A usefull assistant'
    }
    messages = [context]
    while True:
        content = __prompt()
        if content == 'new':
            rich.print('New chat started')
            messages = [context]
            __prompt()
        messages.append({'role': 'user', 'content': content})
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo', messages=messages
        )
        response_content = response.choices[0].message.content
        messages.append({'role':'assistant', 'content': response_content})
        rich.print(f"[bold green] [/bold green] [green]{response_content}[/green]")

def run_chatgpt():
    typer.run(main_function)