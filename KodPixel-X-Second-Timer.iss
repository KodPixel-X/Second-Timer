[Setup]
AppName=KodPixel-X-Second-Timer-Setup
AppVersion=0.7
AppVerName=0.7 Beta 2
DefaultDirName={pf}\KodPixel-X-Second-Timer
OutputBaseFilename=KodPixel-X-Timer-Setup
Compression=lzma
PrivilegesRequired=admin

[Files]
Source: "C:\KodPixel-X-Second-Timer.exe"; DestDir: "{app}"
Source: "C:\KodPixel-X-Second-Timer.ico"; DestDir: "{app}"

[Icons]
Name: "{group}\KodPixel-X-Timer-Second"; Filename: "{app}\KodPixel-X-Timer-Second.exe"
Name: "{userdesktop}\KodPixel-X-Timer-Second"; Filename: "{app}\KodPixel-X-Timer-Second.exe"

[Tasks]
Name: desktopicon; Description: "Create a desktop icon"; GroupDescription: "Additional icons"; Flags: unchecked

[Run]
Filename: "{app}\KodPixel-X-Timer-Second.exe"; Description: "Launch KodPixel-X-Timer-Second"; Flags: nowait postinstall skipifsilent
