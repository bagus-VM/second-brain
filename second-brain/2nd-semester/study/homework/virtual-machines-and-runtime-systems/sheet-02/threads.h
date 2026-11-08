#ifndef _THREADS_H
#define _THREADS_H

void init(void (*)(void), int withTimer);
void new_thread(void (*)(void));
void schedule(void);

#endif
