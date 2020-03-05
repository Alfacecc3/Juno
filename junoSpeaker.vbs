Set objFileToRead = CreateObject("Scripting.FileSystemObject").OpenTextFile("C:\Users\Administrator\Desktop\Juno2V01\textoutForTxtmkr.txt",1)
strFileText = objFileToRead.ReadAll()
objFileToRead.Close
Set objFileToWrite = Nothing

Dim message, sapi
Set sapi=CreateObject("sapi.spvoice")
sapi.Speak strFileText