#include <stdio.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdint.h>
#include <unistd.h>

#define GPIO_BASE_ADDRESS 0xfe200000
#define GPFSEL_OFFSET 0x08
#define GPSET_OFFSET 0x20
#define GPCLR_OFFSET 0x28


int main(int argc, char *argv[])
{
	uint8_t Pin = 42;
	int fd = open("/dev/mem", O_RDWR);
	if (fd == -1)
	{
		printf("Open error!\n");
		return -1;
	}
	void *GPIO_BASE = mmap(0, sysconf(_SC_PAGESIZE), PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO_BASE_ADDRESS);
	close(fd);
	
	if(GPIO_BASE == MAP_FAILED)
	{
		printf("mmap error!\n");
		return -1;
	}
	
	volatile uint32_t *GPFSEL = (uint32_t *)(GPIO_BASE + GPFSEL_OFFSET);
	volatile uint32_t *GPSET = (uint32_t *)(GPIO_BASE + GPSET_OFFSET);
	volatile uint32_t *GPCLR = (uint32_t *)(GPIO_BASE + GPCLR_OFFSET);
	*GPFSEL = (*GPFSEL & ~((uint32_t)7 << (3*(Pin%10)))) | ((uint32_t)1) << (3 * (Pin %10));
	for(uint8_t i=0; i<10; i++)
	{
		*GPCLR = ((uint32_t)1) << Pin %32;
		sleep(1);
		*GPSET = ((uint32_t)1) << Pin %32;
		sleep(1);
	}
	*GPCLR = ((uint32_t)1) << Pin%32;
	if(munmap(GPIO_BASE, sysconf(_SC_PAGESIZE)) == -1){
		printf("munmap Error!\n");
		return -1;
	}
	return 0;
}
