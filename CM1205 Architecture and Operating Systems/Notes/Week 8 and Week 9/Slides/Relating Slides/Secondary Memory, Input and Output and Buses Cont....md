---
"Creation:": 2024-04-12 14:28
Modified: 2024-04-12 14:38
tags:
  - Memory
  - Input
  - Output
  - Buses
  - Secondary
---
### Topic: R.A.I.D
#### Overview: 
*Alternative way of splitting a hard drive to increase efficiency and reduce seek time (time to get queried data)*

### Definitions:
- *RAID - Redundant Array of Inexpensive Disks*
- *SLED - Single Large Expensive Disk*
- *Striping - Where data is held on multiple drives*

#### Subtopic 1 - Why was RAID made?
***RAID** was made since the seek time in the early 2010s was not being improved, where it took 4.16ms to retrieve data.*

*Therefore instead of using **SLED**, which is self explanatory, **RAID** is used.*

#### Subtopic 2 - What are the Benefits of RAID?

- *Utilities six different disk organisations called levels*
- *Appears to Operating system as a single disk*
- *Inexpensive, as it only requires the installation of a RAID Controller.*

---

### Topic: The Different Raid Versions
#### Overview: 
*The information relating the the four different versions RAID is set up in the hard disk*

### Definitions:
- *Overhead - the space capacity of memory which is unaccounted for*
- *Data word -* ![[Pasted image 20240412155958.png]]

#### Subtopic 1 - What is RAID 0?

![[Pasted image 20240412144946.png]]

*Above is an example of striping*

*When the system queries a piece of data it will read a block of four consecutive strips, which are all parallel commands.*

###### Benefits:
1. *High data-rate*
2. *Can handle simultaneous requests*

###### Problems:
1. *Poor response for many small sector requests*
2. *No robustness/redundancy to disk failure, reliability is even worse*
	-  *This is due to there being 4 disks that all have the same fail rate.*

#### Subtopic 2 - What is RAID 1?

![[Pasted image 20240412150537.png]]

- *This duplicates the design in RAID 0, but if a drive crashes it can be replaced by copying the backup*

###### Benefits:
1. *The read performance is twice as good*

###### Problems:
1. *The number of disks needed*

#### Subtopic 3 - What is RAID 2?

![[Pasted image 20240412151810.png]]

*Each byte is split into two 4-bit segments then 3 error correction bits are added*

*The hard disk then has to synchronise the arm and rotational position of the 7 drives*

###### Benefits:
1. *Fast, as the it can read/write half a byte each cycle of the arm*
2. *Robust, as the error-correction allows any drive to fail*

###### Problems:
1. *An overhead of 19%*
2. *Hard to synchronise the drives*

#### Subtopic 4 - What is RAID 3?

![[Pasted image 20240412152846.png]]

*This is essentially a simpler version of RAID 2 as it still requires drive synchronisation, but instead only uses the parity drive for error correction*

*For each data word there is a single parity bit which is written to the parity drive, but this only detects errors so how would this help?*
*Well if a drive crashes we know the position of the bad bit.*

###### Benefits:
1. *High data-rate*

###### Problems:
1. *Cannot handle parallel I/O*
2. *The number of I/O requests per second is no better than a single drive*

#### Subtopic 5 - What is RAID 4?

![[Pasted image 20240412173434.png]]

*Like RAID 0, but the strip parity is kept on a separate drive*

###### Benefits:
- *Does not need drive synchronisation*

##### Problems:
- *Poor Performance for small updates*
- *All drives must be ready to re-compute parity, thus having a heavy load leading to a bottle-neck*

### Subtopic 5 - What is RAID 5?

![[Pasted image 20240412173843.png]]

*Like RAID 4, but distribute parity blocks over all drives*

##### Problems:
- *Difficult to reconstruct the contents of the drive if one fails.*

***

### Topic: Solid State Drives and USB
#### Overview: 
*A look into the internals of solid state drives*

### Definitions:
- *NAND flash - A way of organising the chips in memory in a faster way*
- *Tunnelling - A method of moving electrons in and out of cells, which erodes the physical structure of the cell.*
- *FTL- File Translation Layer*

#### Subtopic 1 - How does SSD Memory Work?

*Electrons are stored in the floating gate, which then reads them as either charged or not-charged, **where in NAND flash 0's mean that there is data in the cell*** 

*NAND flash is organised in a grid where the entire layout is referred to as a **block**, while the individual rows make up the grid are called a **page**, as shown below...*

![[Pasted image 20240412174838.png]]

*The SSD storage retains information by trapping electrons inside the memory cells, and controls their movement by using tunnelling.*

##### Problems:
- *Tunnelling leads to:*
	* *An eroded cell meaning some can become useless*
	- *Electrons getting stuck in the cell wall, where their associated negative charges complicates the process of reading and writing.*

#### Subtopic 2 - Read/Write and Erase

*SSDs have on functional limitation which is that they can write data to an empty drive quickly but to rewrite over it takes much longer*

*SSDs can only erase a bunch of data at once, not just a little piece. It's like trying to erase one word on a paper without smudging the ones around it - really tricky! So, to update even a tiny part of your SSD, it has to basically start over with a whole section, which takes more time and energy.*

*If the drive is full and there are no empty pages available, the SSD must then first scan for blocks that are marked for deletion but that have not been deleted yet, then they are erased and written over in their place. This is why SSDs become slower as they age as newer drives are empty and easier to write too.*

#### Subtopic 3 - Write Amplification

*Since SSDs write data to pages but erase data in blocks, the amount of data being written to drive is always larger than the actual data intended to be written.*

<em><span style="color:pink;">If you make a change to a 4KB file, for example, the entire block that 4KB file sits within must be updated and rewritten.</span></em>

*This can be stopped by the Garbage collection...*

#### Subtopic 4 - Garbage Collection

*Garbage collection is a background process that allows a drive to reduce the performance impact of the program/erase cycle, below are the steps of Garbage Collection...*

![[Pasted image 20240412202652.png]]

#### Subtopic 5 - Trim

*When deleting files using Windows OS the files are not deleted immediately, instead they are marked that they can be overwritten. This is why its possible to undelete files.*

*With a traditional Hard drive the OS does not need to pay attention to where data is being written whereas it does matter with SSDs.*

*The TRIM command allow the OS to tell the SSD that it can skip rewriting certain data the next time it performs a block erase, this lowers the total amount of data that the drive writes and increases SSD longevity, since although reads and writes damage the NAND flash, writes do far more damage.*

![[Pasted image 20240412203735.png]]

#### Subtopic 6 - Wear Levelling

*Wear Levelling refers to the practice of ensuring that certain NAND blocks are not written and erased more often than others. While wear levelling increases a drive's life expectancy but actually increases Write Amplification.*

*In order to distribute writes evenly across the disk, it's sometimes necessary to program and erase blocks even though their contents actually have not changed.*

<span style="color:red; font-weight:bold;">A good Wear Levelling algorithm seeks to balance these impacts.</span>

*With the flash memory the FTL keeps track of the writes to the drive and designates the next area that should be written to based on the number of writes occurred in each section.*

#### Subtopic 7 - SSD Controllers

*These controllers have to be very sophisticated since they are working at high speeds and need to be able to handle all the concepts above such as Garbage Collection and Wear Levelling*

![[Pasted image 20240412212604.png]]

![[Pasted image 20240412212610.png]]

***

### Topic: CD ROM
#### Overview: 
*A look into the internals and inner workings of CD ROM

### Definitions:
- *CD - Compact Disc*
- *CD-DA - Compact Disc - Digital Audio*

#### Subtopic 1 - Structure of CD ROM and DVDs

![[Pasted image 20240412212916.png|300]]

*CD ROM uses a small plastic-encapsulated disk that can store data, where information is retrieved by a Laser Beam*

##### Benefits:
- *Can store vast amounts of data as it uses light to record data and is tightly packed*

#### Subtopic 2 - CD Layers

*Whilst the thickness of a CD is around 1.1-1.5mm it consists of four layers*

| **Layer** | **Thickness**                     | **Material**                    |
| --------- | --------------------------------- | ------------------------------- |
| *One*     | *Normally 1.2mm*                  | *Clear Polycarbonate*           |
| *Two*     | <span style="color:red;">?</span> | *Reflective metal*              |
| *Three*   | <span style="color:red;">?</span> | *Protective Material*           |
| *Four*    | <span style="color:red;">?</span> | *A Label or Screened Lettering* |

![[Pasted image 20240412213707.png]]

#### Subtopic 3 - CD Safety

*The Label on the CD is the most vulnerable, whereas any damage on the polycarbonate will most likely go unnoticed.*

#### Subtopic 4 - CD vs Magnetic Media

***Magnetic Media:***
*Surfaces is arranged into concentric circles called "tracks", where in the early days the number of sectors per track is constant for all tracks but now there are a different number of sectors per track.*

![[Pasted image 20240421222424.png]]

***CD:***
*CD's have one single track, which starts at the centre and spirals out to the circumference of the disk, where each sector is of equal size.*

![[Pasted image 20240421222412.png]]

#### Subtopic 5 - CD Data Recording

*Information is recorded on a CD using a series of bumps, which are called "pits". The CD is read from the bottom, through the transparent polycarbonate, where the pits are seen as bumps by the scanning laser. Information on a CD-ROM is stored permanently as pits and lands (flat parts between pits).*

![[Pasted image 20240421223024.png]]

#### Subtopic 6 -How does the CD Drive Work?

*First off a motor rotates the CD, where the rotational speed varies on the sector being read.*

*Then a laser beam is shone onto the surface of the disk, where the light is scattered by the pits and reflected by the lands (this encodes the binary 0s and 1s)*

*After reflection, a light diode picks up the reflected laser light and converts it to digital data*

![[Pasted image 20240421223245.png]]

#### Subtopic 7 - What are the CD File Systems?

_The **ISO-9660** is a base standard with three levels of compliance. Level 1 restricts file names to an 8+3 format and forbids many special characters. Levels 2 and 3 allow longer filenames and deeper directory structures but are not usable on some systems, notably MS-DOS._

_The **Rock Ridge** are extensions to the ISO-9660 file system favored in the Unix world. It lifts file name restrictions and allows Unix-style permissions and special files to be stored on the CD. Machines that don’t support Rock Ridge can still read the files as it’s still an ISO-9660 file system. UNIX systems and the Mac support Rock Ridge, but DOS and Windows currently don’t._

_The **Joliet** is favored in the MS Windows world and allows Unicode characters to be used for all text fields, including file names and the volume name. The disk is readable as ISO-9660, but shows the long filenames under MS Windows._

_The **HFS (Hierarchical File System)** is used by the Macintosh in place of the ISO-9660, making the disk unusable on systems that don’t support HFS._

#### Subtopic 7 - How can CDs become Rewritable (CD-RW)?

*Instead of using of using polycarbonate, polycrystalline is used. Compared to polycarbonate, polycrystalline can be melted and reformed to have the specified pits and lands as need. This allows for up to 1000 rewrites.* 

***

### Topic: DVD
#### Overview: 
*Brief overview of DVDs*

### Definitions:



#### Subtopic 1 - What are DVDs?

*Digital Versatile Disk, formerly known as Digital Video Disks, which are sometimes confused with CDs due to the same physical look, allow for better error correction through the use of logarithms and thus have a more effective use of the track space.*

#### Subtopic 2 - DVD vs CD

***DVD:***
- *DVD uses a tighter track*
- *DVD recorders use a laser with a smaller wave length*
- *DVD has smaller "burns" (pits)*
	- ***All of these allow DVDs to store larger amounts of data.***
- *DVD has Faster Transfer speeds*
- *DVD has higher quality pictures, by using MPEG2*

*Overall DVD is way better...*

#### Subtopic 3 - What is Blue Ray?

*Sometimes known as the future (which is a joke due to a lack of physical storages of data in the modern era).*

*They use a blue laser rather than a red one, which has shorter wavelength, allowing a more accurate focus and therefore smaller pits.*

***

### Topic: Input and Output Devices
#### Overview: 
*An overview of Input and Output devices*

### Definitions:
- *Port - A connection point between a device and the machine*
- *Bus - a set of wires shared by one or more devices*


#### Subtopic 1 - What is a Device Controller?

*It connects the device to the computer's bus and controls the operation of the device*

![[Pasted image 20240427163906.png]]

#### Subtopic 2 - How does Data Transfer between Input and Output Devices?

*A device communicates with a system by sending signal through a cable or through the air.*

![[Pasted image 20240427164031.png]]

#### Subtopic 3 - What is the Difference between Serial and Parallel Data Transfers?

*Serial data is transferred one bit at any time which only uses two cables, whereas parallel data is transferred multiple bits at a time where the interface width refers to the number of parallel wires an interface uses.*

*Universal Serial Bus or USB was designed to:*
- *Allow up to 127 of low to medium speed peripherals to be attached to a PC.*
- *Be Plug and Play*

*USBs use bus architecture which means they have different data from different devices travel accrose thr same cables and use multilevel start topology*

![[Pasted image 20240427164638.png]]

![[Pasted image 20240427164701.png]]

#### Subtopic 4 - What is an I/O Controller?

*A CPU communicates with a controller by using a set of registers for data and control signals, where the CPU executes I/O requests by reading and writing device-control registers*

*A controller typically consists of four registers, which are:*
- *The Status register - Displays the Status of the device*
- *The Command register - Controls the commands from the Host*
- *The Data-in register - Controls the input data from the Host*
- *The Data-out register - Controls the output data from the host*

#### Subtopic 5 - What is I/O Polling?

*This is a simple protocol for interactions between the host and the controller, where the controller indicates its state through the **Busy** bit in the status register and the host actively monitors the status of the device by reading the **Busy** bit in the status register.*

![[Pasted image 20240427180219.png]]

*It is efficient if the controller and device are fast and always ready for service, this normally takes only 3 CPU cycles to poll a service and once the device is polled then the device is ready*

*It is inefficient if a device is not ready, the polling has to be repeated until the device is ready, and it may be more efficient to have the device controller notify the CPU that a device is ready for service (this is an interrupt)*

***

### Topic: Interrupts
#### Overview: 
*Interrupts and their usage in I/O controllers and the CPU*

### Definitions:



#### Subtopic 1 - What is an Interrupt?

*Interrupts allow the CPU to respond to an asynchronous event, and is an efficient way to dispatch to the proper interrupt handler for a device, without first polling all the devices to see which one raised the interrupt*

*There are two interrupts:*
- *Hardware interrupts*
- *Software interrupts (aka traps)*

*There is a wire called the Interrupt request line which is used to signal an interrupt, which when activated signals an interrupt.*

#### Subtopic 2 - What is the Interrupt-driven I/O Cycle?

![[Pasted image 20240427181220.png]]

***

### Topic: CPUs
#### Overview: 
*Some of the CPU components used when communicating with an I/O controller*

### Definitions:



#### Subtopic 1 - What are a CPUs Performance Parameters?

*The number of address lines (m), can address up to $2^m$ addresses*
*The number of data line(n), can read/write n-bit word in a single operation*

#### Subtopic 2 - What is Bus Arbitration?

*What happens if two devices want to use the bus at the same time?*
*Well then the Bus Arbitrator decides who gets the bus in case of a conflict, where there are two types of arbitrators centralised and decentralised.*

#### Subtopic 3 - What is the Difference between Centralised and Decentralised Bus Arbitrators?

***Centralised Arbitration:***

![[Pasted image 20240427181823.png]]

***Decentralised Arbitrator:***

![[Pasted image 20240427181857.png]]
<sup>GREAT LECTURE WHO DOESN'T EVEN CORRECT HIS SLIDES</sup>

[USE THIS INSTEAD]([https://users.cs.fiu.edu/~prabakar/cda4101/Common/notes/ lecture10.html](https://users.cs.fiu.edu/~prabakar/cda4101/Common/notes/lecture10.html))

#### Subtopic 4 - What is the ISA Bus?

*The Industry-Standard Architecture Bus (8.33 Mhz)*

![[Pasted image 20240427182110.png]]

#### Subtopic 5 - What is the PCI Bus?

*The Peripheral Component Interconnect Bus is a substitute for the ISA bus as it is too slow for multimedia applications due to its maximum rate being 16.7 Mb/s*

*Intel created PCI Bus Architecture to deal with the slow speed of ISA Buses as it has 33Mhz or 133 Mb/s and PCI-2 has 66Mhz and 528 Mb/s, but PCI is still not fast enough for a memory bus.*

#### Subtopic 6 - What is PCI-X?

- *PCI-X, short for Peripheral Component Interconnect eXtended, is a computer bus and expansion card standard that enhances the 32-bit PCI Local Bus for higher bandwidth demanded by servers. It is a double-wide version of PCI, running at up to four times the clock speed, but is otherwise similar in electrical implementation and uses the same protocol.*
- *It has been replaced in modern designs by the similar-sounding PCI Express (officially abbreviated as PCIe), with a completely different connector and a very different logical design, being a single narrow but fast serial connection instead of a number of slower connections in parallel.*

***NOT SUMMARISED, JUST COPIED FROM SLIDES***

#### Subtopic 7 - What is PCIe/PCI Express?

- *PCI Express (Peripheral Component Interconnect Express), officially abbreviated as PCIe, is a high-speed serial computer expansion bus standard designed to replace the older PCI, PCI- X, and AGP bus standards. PCIe has numerous improvements over the aforementioned bus standards, including higher maximum system bus throughput, lower I/O pin count and smaller physical footprint, better performance-scaling for bus devices, a more detailed error detection and reporting mechanism (Advanced Error Reporting (AER), and native hot- plug functionality. More recent revisions of the PCIe standard support hardware I/O virtualization.*
- *The PCIe electrical interface is also used in a variety of other standards, most notably ExpressCard, a laptop expansion card interface.*

***NOT SUMMARISED, JUST COPIED FROM SLIDES***

#### Subtopic 8 - What is a SOUTHBRIDGE Controller?

- *The southbridge was one of the two chips in the core logic chipset on a personal computer (PC) motherboard, the other being the northbridge.*
- *The southbridge typically implements the slower capabilities of the motherboard in a northbridge/southbridge chipset computer architecture. In Intel chipset systems, the southbridge is named Input/Output Controller Hub (ICH). AMD, beginning with its Fusion APUs, has given the label FCH, or Fusion Controller Hub, to its southbridge.*
- *The southbridge can usually be distinguished from the northbridge by not being directly connected to the CPU. Rather, the northbridge ties the southbridge to the CPU. Through the use of controller integrated channel circuitry, the northbridge can directly link signals from the I/O units to the CPU for data control and access.*

- *A southbridge chipset handles all of a computer's I/O functions, such as USB, audio, serial, the system BIOS, the ISA bus, the interrupt controller and the IDE channels. Different combinations of Southbridge and Northbridge chips are possible, but these two kinds of chips must be designed to work together.*
- *There is no industry-wide standard for interoperability between different core logic chipset designs. Traditionally, the interface between a northbridge and southbridge was the PCI bus. The main bridging interfaces used now are DMI (Intel) and UMI (AMD).*

![[Pasted image 20240427182711.png]]

![[Pasted image 20240427182724.png]]

***NOT SUMMARISED, JUST COPIED FROM SLIDES***
***