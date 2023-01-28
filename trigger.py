import psutil
import platform
import os
CURRENT_PLATFORM = platform.system().upper()
partitions = psutil.disk_partitions(all=True)

def get_cryptomator_volumes():

    #Need to list Fuse/WebDAV volumes mounts and iterate through it
        #example OSX macFuse:  sdiskpart(device='Cryptomator@macfuse0', mountpoint='/Volumes/test', fstype='macfuse', opts='rw,sync,nosuid', maxfile=255, maxpath=1024)
        #example OSX WebDAV: sdiskpart(device='http://localhost:42427/sq5q-0UyuwBL/test3/', mountpoint='/Volumes/test3', fstype='webdav', opts='rw,noexec,nosuid', maxfile=255, maxpath=1024)
        #example Linux: sdiskpart(device='fusefs-851974781', mountpoint='/home/<USER>/.local/share/Cryptomator/mnt/testlinuxvault', fstype='fuse.fusefs-851974781', opts='rw,nosuid,nodev,relatime,user_id=1000,group_id=1000', maxfile=254, maxpath=4096)
    
    #iterate over list and find the mount in OSX if mounted with macFuse
    if CURRENT_PLATFORM.startswith( 'DARWIN' ):
        for p in partitions:
            if p.device.startswith('Cryptomator'):
                print (p.mountpoint)
                #can use diskutil or umount -f
                os.system('diskutil unmount force ' + p.mountpoint)

         #port number of WebDav used by Cryptomator, default port 42427
           elif p.device.find('42427') != -1:
                print (p.mountpoint)
                os.system('diskutil unmount force ' + p.mountpoint)

    #iterate over list and find mount for Linux    
    elif CURRENT_PLATFORM.startswith( 'LINUX' ):
        for p in partitions:
            if p.mountpoint.find('Cryptomator') != -1:
                print (p.mountpoint)
                #TODO
                #must be root to unmount fuse disk
                os.system('umount -f ' + p.mountpoint)

    #TODO Windows
    #elif CURRENT_PLATFORM.startswith( 'WIN'):

get_cryptomator_volumes()
