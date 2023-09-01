import subprocess



comando_ps ='''
                $URL="192.168.5.200"
                $PATH="C:\Sidesys\InicioBotonera\PRUEBAS"
                $Server="192.168.104.93"
                $DS = Invoke-Sqlcmd -ServerInstance $Server -Username "SOF" -Password "SOF" -Query "SELECT    DISTINCT 
                DTE.OrganizationCode,
                DTE.DTECode, 
                DTE.NetId,
                DTE.InstanceCode,
				ORG.OrganizationDes  
                FROM         [STE].[dbo].ProcessTemplate T WITH(NOLOCK)
                INNER JOIN [STE].[dbo].DTEProcessTemplate DPT WITH(NOLOCK)
                    ON (T.OrganizationCode = DPT.OrganizationCode
                    AND    T.SectionId = DPT.SectionId
                    AND    T.ProcessTemplateId = DPT.ProcessTemplateId)
                    INNER JOIN [STE].[dbo].[DTE] WITH(NOLOCK)
                    ON (DTE.OrganizationCode = DPT.OrganizationCode
                    AND    [STE].[dbo].DTE.DTECode = DPT.DTECode
                        --filtro por puestos
                    AND    [STE].[dbo].DTE.ViewTypeCode = 2) --1 = consola, 2 = totem, 3= nodo
                INNER JOIN [STE].[dbo].AbstractSectionDetail ASeD WITH(NOLOCK)
                    ON (ASeD.OrganizationCode = DPT.OrganizationCode
                    AND ASeD.SectionId = DPT.SectionId)
					INNER JOIN [STE].[dbo].Organization ORG WITH(NOLOCK)
					ON (ORG.OrganizationCode = DPT.OrganizationCode)
                 WHERE     --plantillas activas
                    T.Active = 1" -As DataSet 
                $DS.Tables[0].Rows | ForEach-Object{
                if ([System.IO.Directory]::Exists("$PATH\$($_['OrganizationDes'])") -eq $false) 
                {
                    New-Item -Path $PATH\$($_['OrganizationDes']) -ItemType Directory
                }
                if ([System.IO.Directory]::Exists("$PATH\$($_['OrganizationDes'])\$($_['InstanceCode'])") -eq $false)
                {
                    New-Item -Path $PATH\$($_['OrganizationDes'])\$($_['InstanceCode']) -ItemType Directory
                }

                Out-File -FilePath $PATH\$($_['OrganizationDes'])\$($_['InstanceCode'])\Apertura.bat -InputObject "start chrome.exe --start-fullscreen --new-window --app=http://$URL/STE/node/NodeView.aspx?OrganizationCode=$($_['OrganizationCode'])&DTECode=$($_['DTECode'])&InstanceCode=$($_['InstanceCode']) --user-data-dir=c:/test/profile/2 --window-position=1024,0" -Encoding ascii -Width 50
                # $($_['OrganizationCode']),$($_['DTECode']),$($_['NetId']),$($_['InstanceCode'])
                }
                '''

resultado = subprocess.run(["powershell", "-Command", comando_ps], capture_output=True, text=True)
print(resultado)