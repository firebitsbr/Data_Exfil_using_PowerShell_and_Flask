$URI = Read-Host 'Enter URL'

$File_path = Read-Host 'Enter File Path'

Write-Host "Invoke PowerShell web request"

try{

    $sess = Invoke-WebRequest -Method POST -URI $URI -Infile $File_path
    
    if($sess.StatusCode -eq 200){
            write-host("Success!")
    }
    
    else {
            write-host("Something went wrong")
} 

    Write-Host "done"

    }

catch{

    Write-Host "Failed!!!"

}
