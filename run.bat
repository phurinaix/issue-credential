@ECHO OFF
set venv_dir="D:\Blockchain\Blockcerts\cert-issuer"
cmd /k "cd %venv_dir%\venv\Scripts & activate & cert-issuer -c %venv_dir%\conf.ini & git add %venv_dir%\data\blockchain_certificates\ & git commit -m \"update\" & git push"
PAUSE