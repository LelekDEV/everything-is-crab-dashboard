## Project

The project focuses on the ability to save images of the game: [Everything is Crab: The Animal Evolution Roguelite](https://store.steampowered.com/app/3526710/Everything_is_Crab_The_Animal_Evolution_Roguelite).

After each run you gain the ability to "photograph" your creature alongside it's displayed stats. I thought it would be nice to create a kind of dashboard that allows you to see all of them side by side in an aesthetically pleasing way.

### Key notes:

- the code doesn't have a lot of safeguards, if any of the paths doesn't match or files don't exists (for instance, you don't have the game), the site will simply not work
- in the worst case scenario, you will see a blank site with just the background (though I haven't tested that), some errors could be visible by inspecting but I suspect not a lot, especially if/why python scripts failed
- everything code related you might need is written in form of comments at the top of source files

## Setup

First and foremost, you need to obviously own a copy of the game and take some pictures (or at least setup a directory with the same file structure as the game creates). Then you can (somewhat) conveniently update the path to yours in `consts.json` (the default path on Windows is `%USERPROFILE%\Pictures\Everything is Crab`, but you need to provide an absolute one with the disk label e.g. C:/Users/...).

If you want to run the dashboard for yourself, you need to have some way of hosting an HTTP server with PHP included.

If you're on Windows I suggest [XAMPP](https://www.apachefriends.org/index.html), unfortunetly I won't provide a step by step guide on how to set it up, but if you have mediocre knowledge in the field and access to the internet you should succeed.

The only thing I want to mention is how to create a *virtual host* for easy dashboard access. For example, that's my apache vhost configuration:
```
<VirtualHost *:80>
    
    ServerName crabthegame.local
    
    DocumentRoot "ABSOLUTE_PATH_TO_THE_PROJCET_HERE_WITHOUT_TRAILING_SLASH"
    
    <Directory "ABSOLUTE_PATH_TO_THE_PROJCET_HERE_WITHOUT_TRAILING_SLASH">
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
        Allow from all
    </Directory>

</VirtualHost>
```

I have it saved in `C:\xampp\apache\conf\vhosts\crabthegame.local.conf` (created `vhosts` myself) and linked it in the main config file likewise (`C:\xampp\apache\conf\httpd.conf`):
```
# Custom created vhosts
Include conf/vhosts/*.conf
```

Though, if you wish you may put the whole thing in the main file as well. On Windows don't forget to append your site name to the host file (`C:\Windows\System32\drivers\etc\hosts`, requires admin privileges to write):
```
127.0.0.1	crabthegame.local
```

## Finally - the dashboard

On my current setup, the site of the project looks like this:

![preview of the dashboard](preview.gif)
