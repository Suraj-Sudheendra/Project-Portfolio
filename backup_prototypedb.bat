@ECHO OFF
robocopy "S:\Shared\Prototype Database" "\\active-nas02\Backup\Access DB" "Active Exhaust Database.mdb" /mt /z /b >> "enter log file name".txt
echo Logged time = %time% %date% >> "enter log file name".txt

