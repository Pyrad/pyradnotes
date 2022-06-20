# Terminals on Windows Platform



## To disable cursor blinking in Windows Terminal

For bash/zsh

Putting the following at the end of your .bashrc/.zshrc file

```bash
echo -e -n "\e[2 q"
```


For PowerShell

```powershell
Write-Host -NoNewLine "`e[2 q"
```

