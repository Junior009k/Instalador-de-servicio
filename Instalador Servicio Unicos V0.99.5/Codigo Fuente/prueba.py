import subprocess



comando_ps ='''
                $URL="192.168.5.200"
                $PATH="C:\Sidesys\InicioBotonera\PRUEBAS"
                $Server="192.168.104.93"
                $DS = Invoke-Sqlcmd -ServerInstance $Server -Username "SOF" -Password "SOF" -Query "SELECT TOP (5) *
                FROM [STE].[dbo].[DTE]
                $DS.Tables[0].Rows | ForEach-Object{
                Write-Host $($_['DTECode'])
                }
                '''

resultado = subprocess.run(["powershell", "-Command", comando_ps], capture_output=True, text=True)
print(resultado)