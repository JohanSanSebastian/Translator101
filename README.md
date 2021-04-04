![Language](assets/Translator101.png)

# Translator101
![Language](https://img.shields.io/github/languages/top/JohanSanSebastian/Translator101)
![Size](https://img.shields.io/github/languages/code-size/JohanSanSebastian/Translator101)
![Issues](https://img.shields.io/github/issues/JohanSanSebastian/Translator101)
![Size](https://img.shields.io/github/stars/JohanSanSebastian/Translator101?style=social)


Translator101 is a discord bot designed to help connect the community by acting as a bridge between language barriers. It was made using discord.py and has various features like basic translation, live translation etc.

This bot was made as part of a project for LHD : Share 2021.

## Basic Setup and Help
![Setup](https://media.giphy.com/media/iNUg8YByIcve1HJigH/giphy.gif)
![Setup](https://media.giphy.com/media/j0LxYSDiReiTMyfG0m/giphy.gif)

## Translate feature
![Translate](https://media.giphy.com/media/LYjA1ISX7ulKJ4GpSi/giphy.gif)

## Live Translate feature
![Live](https://media.giphy.com/media/nisoS2Z6eoXEhIXrHm/giphy.gif)

## Self-Hosting
1. Firstly, install all the necessary libraries from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

2. You are free to self-host the bot. To self-host the bot just change the name of the bot in `line 29` from `Translator101` to whatever you would like to.

```python
client.name = 'Translator101' # Change This
```

3. You can change the prefix of the bot by changing the prefix declared in the `command_prefix` variable in `line 17` to whatever you would like.

```python
command_prefix = '!' # Change this to your preferred prefix
```

4. To run the bot you also need to make a file called `config.py` and make a variable in it called `token` and set it to your bot token.

```python
token = "Your_Bot_Token" # Add the token here
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
