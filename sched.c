struct _task{
 int ret_id;
 void (*func)(void *);
 int due ;
 int period;
 void *context;
 }task;

//return is task so that i have task handle  of chain scheduling

task * schedule_periodic (int period, worker_routine * workitem, void *context){
  task * mytask;
  int id;
 // give task memory 
  malloc_task() ;  // not defining - just a Stub
  mytask->func = workitem;
  mytask->period = period;
  mytask->due = now() + period;
  mytask->context = context;
  id = schedule (my task.due, myfunc, &mytask); 
  mytask->context = context;
  return mytask; 
  }

/* Function to execute the work item */
 myfunc ( task ** mytask) {
   task *new_task, *cur_task;
   int id, cur_time, diff_time, i = 0, new_due;
   void (*workfunc)(void*) ;
   cur_task =  (task *)*mytask;
  
   int due = cur_task->due;
   workfunc = cur_task->func;
    
   // call the work function 
   workfunc (task->context);

   cur_time = now();
   diff_time =  cur_time - cur_task->due;
   while (diff_time <  ((i+1) * cur_task->period ))
         i++; 
    // to nearest multiple of period
   new_due = (i+1) * cur_task->period ); 

   /* new period is between the next multiple of period */
   cur_task->due =  new_period; // Next due
   cur_task->context =  &cur_task; 
   //cur_function remains same - work item
   release_workitem_handle(cur_task->id); // no need of current handle
   //schedule again
   id =  schedule(new_due, workfunc, cur_task->context);
   cur_task->id = id; // update the id into task structure  - To be used for cancellation
  
  }
   

 
 void cancel_periodic (task *mytask){
      //cancel the task  which is either completed or scheduled
      int cur_id ;
      cur_id= mytask->id; // possible states- SCHEDULED, RUNNING or ALREADY COMPLETED
      if (cancel_scheduled(cur_id)) {
 	   return ; 
       }
      //There should be no previous handles as it is released
      //Only scenario is for current running task
     while(cancel_schedule(cur_id) !=TRUE)
             ; //do nothing - try canceling the task
     free_task();
     return;
     
 }   
