ngajimba@ngajimba-HP-EliteBook-820-G3:~$ sftp c7868dd693d0@c7868dd693d0.f2a7c461.alx-cod.online
c7868dd693d0@c7868dd693d0.f2a7c461.alx-cod.online's password: 
Connected to c7868dd693d0.f2a7c461.alx-cod.online.
sftp> ls
4-empty                        RSA-Factoring-Challenge        alx-higher_level_programming   alx-low_level_programming      alx-pre_course                 alx-system_engineering-devops  
alx-zero_day                   bin                            boot                           dev                            etc                            home                           
lib                            lib32                          lib64                          libx32                         media                          mnt                            
monty                          new_monty_directory            opt                            printf                         proc                           root                           
run                            sbin                           simple_shell                   so_cool                        srv                            sys                            
tmp                            usr                            var                            
sftp> cd alx-system_engineering-devops 
sftp> ls
0x00-shell_basics                     0x01-shell_permissions                0x02-shell_redirections               0x03-shell_variables_expansions       README.md                             
command_line_for_the_win              
sftp> cd command_line_for_the_win  
sftp> ls
0-first_9_tasks.png  1-next_9_tasks.png   2-next_9_tasks.png   README.md            
sftp> put /home/ngajimba/Pictures/1-next_9_tasks.png
Uploading /home/ngajimba/Pictures/1-next_9_tasks.png to /alx-system_engineering-devops/command_line_for_the_win/1-next_9_tasks.png
/home/ngajimba/Pictures/1-next_9_tasks.png                                                                                                                  100%  225KB  91.6KB/s   00:02    
sftp> put /home/ngajimba/Pictures/2-next_9_tasks.png
Uploading /home/ngajimba/Pictures/2-next_9_tasks.png to /alx-system_engineering-devops/command_line_for_the_win/2-next_9_tasks.png
/home/ngajimba/Pictures/2-next_9_tasks.png                                                                                                                  100%  225KB  20.7KB/s   00:10    
sftp> put /home/ngajimba/Pictures/README.md
Uploading /home/ngajimba/Pictures/README.md to /alx-system_engineering-devops/command_line_for_the_win/README.md
/home/ngajimba/Pictures/README.md                                                                                                                           100%  189KB  41.7KB/s   00:04    
sftp> ls
0-first_9_tasks.png  1-next_9_tasks.png   2-next_9_tasks.png   README.md            
sftp> ls
0-first_9_tasks.png  1-next_9_tasks.png   2-next_9_tasks.png   README.md            
sftp> put /home/ngajimba/Pictures/README.md


