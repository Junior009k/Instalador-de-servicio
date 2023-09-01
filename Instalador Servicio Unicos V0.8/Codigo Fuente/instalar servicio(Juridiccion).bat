rem "C:\Windows\Microsoft.NET\Framework\v4.0.30319\InstallUtil.exe" -i "C:\Sidesys\Middleware\STE\System\Sidesys.eFlow.PerformanceCounter.dll" obj=localsystem start=auto 
sc create "e-Flow Juridiccion Inmobiliaria Middleware2" binpath="C:\Entorno\JurisdiccionInmobiliaria\Middleware\STE\bin\Sidesys.Services.ApplicationService.exe" obj=localsystem start=auto 
rem sc create pruebaeFlowNode binpath="C:\Sidesys\MiddlewareNode\STE\bin\Sidesys.Services.ApplicationService.exe" obj=localsystem start=auto 

rem por si se quiere configurar 
rem sc config "e-Flow TSS Middleware Service" obj=localsystem start=auto
