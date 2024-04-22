#include <stdio.h>
#include <string.h>
#include <signal.h>
#include <sys/time.h>

void timer_handler(int signum)
{
	static int count = 0;
	static int countdown = 100;
	struct timeval ts;
	
	count++;
	if(countdown>=0){
	printf("Counting down: %d\n", countdown);
	countdown--;
	}
	gettimeofday(&ts, NULL);
	printf("%ld.%06ld: timer expired %d times \n", ts.tv_sec, ts.tv_usec, count);
}

int main()
{
	struct sigaction sa;
	struct itimerval timer;
	
	memset(&sa, 0, sizeof(sa));
	sa.sa_handler = &timer_handler;
	sigaction(SIGVTALRM, &sa, NULL);
	
	timer.it_value.tv_sec = 0;
	timer.it_value.tv_usec = 500000;
	
	timer.it_interval.tv_sec = 0;
	timer.it_interval.tv_usec = 500000;
	
	setitimer(ITIMER_VIRTUAL, &timer, NULL);
	
	while(1);
	
	
}
