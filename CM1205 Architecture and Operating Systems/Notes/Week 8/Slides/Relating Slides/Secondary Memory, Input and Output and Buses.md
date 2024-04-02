
### How are Hard Disc Structures?

![[Pasted image 20240325151604.png]]


### What are the Five layers of the File System?

1. Physical Layer
	- *The drive itself*
2. *File System Layer (Partition Information)*
3. *Data Layer (where the data is stored)*
	- *Blocks and Clusters*
4. *Metadata Layer*
	- *Structure information (EXT2/3, FAT, NTFS)*
5. *File Name Layer*
	- *Name of the file*


### What is the Physical Structure of the Hard Disc?

*A disc is divided into many concentric circles called "tracks", where each track is subdivided into segments called "sectors"*

![[Pasted image 20240325152352.png]]

#### How are Early Hard Discs compared to Hard Discs now?

*The number of sectors per track is the same in all tracks, so the outer sectors are larger than the inners, but have the same capacity.*

*Whereas Nowadays,*
![[Pasted image 20240325152613.png]]
![[Pasted image 20240325152625.png]]


### What is Data Recording?

- *An electric current flows through a coil of wire, where a magnetic field is produced which is used to magnetise the coating of iron oxide on a floppy disk. A varying electrical current, the signal is passed through the coil and the variations are "recorded" on the disk.*
![[Pasted image 20240325153150.png]]
![[Pasted image 20240325153203.png]]
![[Pasted image 20240325153210.png]]
![[Pasted image 20240325153217.png]]
![[Pasted image 20240325153229.png]]


### What is DATA Organisation?

- *The data layer is the reason for having a file system as this is where file data is saved, file systems typically use 512-byte sectors. Where for efficiency, consecutive sectors are organised and allocated together into a data unit where typically data unit names depend on the file system:*

1. *FAT & NTFS uses **clusters***
2. *UNIX (FFS and EXT2FS) uses **blocks***


### What are Clusters?

- *Data units (sectors) of a disk must be addressed, which units belong to which file, which units are free and which units are damaged (bad sectors).*
- *Disks having large capacity, allocating one sector as a unit would make the addressing table too large, therefore we combine sectors and create clusters.*
- *Clusters represent the smallest amount of disk space that can be allocated, where the smaller the cluster size, the more efficient the disk space usage. But the larger the addressing table.*
- *The number of sectors per cluster a file system uses is stored in the Boot Record.*


### What are Partitions (DOS-based)?

![[Pasted image 20240325163056.png]]

#### What are Extended Partitions?

![[Pasted image 20240325163118.png]]

#### What are the Partition Table contents?

![[Pasted image 20240325163300.png]]

#### What are the Common Types of Partitions?

![[Pasted image 20240325163334.png]]

### What is the Master Boot Record (MBR)?

![[Pasted image 20240325163143.png]]
![[Pasted image 20240325163207.png]]


### What are Boot Sectors (Boot Record)?

![[Pasted image 20240325163401.png]]
![[Pasted image 20240325163416.png]]


### What are DOS or Window Formatted Disks?

![[Pasted image 20240325163438.png]]
![[Pasted image 20240325163448.png]]


### What is FAT?

![[Pasted image 20240325163528.png]]![[Pasted image 20240325163540.png]]

#### What are the Disadvantages of Fat?

![[Pasted image 20240325163600.png]]
![[Pasted image 20240325163610.png]]

#### What is the FAT Directory Entry (Metadata Area)?

![[Pasted image 20240325163744.png]]

### What is the Data Layer?

![[Pasted image 20240325163630.png]]


### What is the HDD Data Transfer Speed?

![[Pasted image 20240325163803.png]]![[Pasted image 20240325163809.png]]