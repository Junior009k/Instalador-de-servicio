"C:\Windows\Microsoft.NET\Framework\v4.0.30319\InstallUtil.exe" -i "C:\Sidesys\Middleware\STE\System\Sidesys.eFlow.PerformanceCounter.dll" obj=localsystem start=auto 
rem sc create servicioeFlow Service binpath="C:\Sidesys\Middleware\STE\bin\Sidesys.Services.ApplicationService.exe" obj=localsystem start=auto 
rem sc create servicioeFlowNode binpath="C:\Sidesys\MiddlewareNode\STE\bin\Sidesys.Services.ApplicationService.exe" obj=localsystem start=auto 

rem por si se quiere configurar 
rem sc config "e-Flow TSS Middleware Service" obj=localsystem start=auto
