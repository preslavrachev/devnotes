# Visual Studio Code
## Migrating from IntelliJ/PyCharm

Open `Preferences -> Extensions` or `Preferences-Keymaps`

```
@recommended:keymaps 
```
Search for IntelliJ: You will find [kasecato/vscode-intellij-idea-keybindings](https://github.com/kasecato/vscode-intellij-idea-keybindings)

## Setting up as a Python IDE
### Settings File
Every VS Code project has a `.vscode` directory, which contains a JSON file, called `settings.json`. Whether, you configure your VS Code extensions form their respective UI, or add lines directly to this file, the effect will be the same. This is how a sample `settings.json` file looks like for a particular Python project of mine:

``` json
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "python.linting.flake8Args": ["--max-line-length=88"],
  "python.pythonPath": "path_to_my_project/venv/bin/python",
  "python.formatting.provider": "black",
  "python.unitTest.unittestEnabled": true,
  "python.unitTest.pyTestEnabled": false,
  "python.unitTest.nosetestsEnabled": false
}
```
