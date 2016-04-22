/*
 *  Swap threading
 *
 **/

#include <unistd.h>
#include <sys/types.h>
#include <errno.h>      /* Errors */
#include <stdio.h>      /* Input/Output */
#include <stdlib.h>     /* General Utilities */
#include <pthread.h>    /* POSIX Threads */
#include <string.h>     /* String handling */

/* Global memory information */
#define SWAP_THRESHOLD 20
#define TOTAL_FREE_HUGEPAGE 100
pthread_mutex_t mcount;
pthread_cond_t mcount_threshold;

/*Declare: Consume memory from the pool */
void get_memory_from_pool ( void *ptr );

/*Declare: Return memory into the pool by swapping FIFO */
void put_memory_into_pool ( void *ptr );


typedef struct mem_info
{
	int thread_no;
    int mem_count;
} meminfo;

void init_mem_info(struct mem_info * m) {
   m->mem_count =  TOTAL_FREE_HUGEPAGE ;
}

int main()
{
    pthread_t maint, swapt;  /* thread variables */
    meminfo mems;
    
    /* Initialize mutex and condition variable objects */
    pthread_mutex_init(&mcount, NULL);
    pthread_cond_init (&mcount_threshold, NULL);

    /* init memory initial memory count */
    init_mem_info(&mems);

    /* Create main and swap threads */
    pthread_create (&maint, NULL, (void *) &get_memory_from_pool, (void *) &mems);


    /*Swap thread */
    pthread_create (&swapt, NULL, (void *) &put_memory_into_pool, (void *) &mems);

    pthread_join(maint, NULL);
    pthread_join(swapt, NULL);
              
    /*destroying mutex and condition variable */
    pthread_mutex_destroy(&mcount);
    pthread_cond_destroy(&mcount_threshold);

    /* exit */  
    exit(0);
} /* main() */

/**
 * Main thread which consumes the memory
 *
**/
void get_memory_from_pool ( void *ptr )
{
    meminfo *get_mem;
    get_mem = (meminfo *) ptr;

    while (get_mem ->mem_count  > SWAP_THRESHOLD ) {
      pthread_mutex_lock (&mcount);
      /* keep using memory till it is below threshold */
      get_mem->mem_count--;

      if(get_mem->mem_count == SWAP_THRESHOLD ){
    	  pthread_cond_signal(&mcount_threshold);
      }
      pthread_mutex_unlock (&mcount);
    }
    /* printf thread info */
	printf("%s(): Thread %d says %d \n", __func__, get_mem->thread_no, get_mem->mem_count);

    pthread_exit(0); /* exit */
}

/*
 * This is SWAP thread which should be invoked when
 * threshold  for the invocation is reached to the
 */
void put_memory_into_pool ( void *ptr )
{
	meminfo *get_mem;
	get_mem = (meminfo *) ptr;
    
	pthread_mutex_lock (&mcount);
	while (get_mem->mem_count > SWAP_THRESHOLD ){
		pthread_cond_wait(&mcount_threshold, &mcount);

	}
	get_mem->mem_count = get_mem->mem_count+5;
	pthread_mutex_unlock (&mcount);

	/* printf thread info */
	printf("%s(): Thread %d says %d \n", __func__, get_mem->thread_no, get_mem->mem_count);
    
    pthread_exit(0); /* exit */
}


