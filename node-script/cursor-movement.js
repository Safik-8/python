const { execFile } = require("child_process");

const powerShellCode = `
Add-Type @"
using System;
using System.Runtime.InteropServices;

public class MouseMove {
  [DllImport("user32.dll")]
  public static extern bool SetCursorPos(int X, int Y);
}
"@

Start-Sleep -Seconds 3

[MouseMove]::SetCursorPos(200, 200)
Start-Sleep -Milliseconds 700
[MouseMove]::SetCursorPos(800, 200)
Start-Sleep -Milliseconds 700
[MouseMove]::SetCursorPos(800, 600)
Start-Sleep -Milliseconds 700
[MouseMove]::SetCursorPos(200, 600)
`;

execFile("powershell.exe", ["-NoProfile", "-Command", powerShellCode], (error) => {
  if (error) console.error("Could not move cursor:", error.message);
});
