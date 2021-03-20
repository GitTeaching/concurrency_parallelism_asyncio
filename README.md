# concurrency_parallelism_asyncio

Multiprocessing, (multi)threading ,and asynchronous programming with **asyncio** and **Celery**.

Python Event-Driven architecture using **RabbitMQ** and **pika**.

### The basic types of concurrency available in Python:
- Multithreading
- Multiprocessing
- Asyncio

Quick Recap

-Sync: Blocking operations.

-Async: Non blocking operations.

-Concurrency: Making progress together.

-Parallelism: Making progress in parallel.


Parallelism implies Concurrency. But Concurrency doesn’t always mean Parallelism.

### Python Multithreading vs. Multiprocessing

"If your code is IO bound, both **multiprocessing** and **multithreading** in Python will work for you. Multiprocessing is a easier to just drop in than threading but has a higher memory overhead. If your code is CPU bound, multiprocessing is most likely going to be the better choice—especially if the target machine has multiple cores or CPUs. For web applications, and when you need to scale the work across multiple machines, **RQ library** is going to be better for you." shorturl.at/ejnz1

### Some readings / References:

#### - Threading / Multiprocessing :

Speed Up Your Python Program With Concurrency : https://realpython.com/python-concurrency/

#### - Asyncio :

Coroutines and tasks : https://docs.python.org/fr/3/library/asyncio-task.html

Event loop : https://docs.python.org/fr/3/library/asyncio-eventloop.html

Python Asyncio: Basic Fundamentals : https://dev.to/v_it_aly/asyncio-basic-fundamentals-4i5m

Async programming in Python with asyncio : https://dev.to/welldone2094/async-programming-in-python-with-asyncio-12dl

Speed Up Your Python Program With Concurrency : https://realpython.com/python-concurrency/

Asynchronous Python for Web Development : https://stackabuse.com/asynchronous-python-for-web-development/

Async IO en Python: une solution complète : https://www.codeflow.site/fr/article/async-io-python#_un_programme_complet_demandes_asynchrones


#### - Celery :

Celery Docs : https://docs.celeryproject.org/en/stable/index.html

Celery Tutorial: A Must-Learn Technology for Python Developers : https://medium.com/swlh/python-developers-celery-is-a-must-learn-technology-heres-how-to-get-started-578f5d63fab3

Setting up a task queue using Celery and RabbitMQ : https://medium.com/@krishnadey30/setting-up-a-task-queue-using-celery-and-rabbitmq-e73f8fd15de0

Celery: an overview of the architecture and how it works : https://www.vinta.com.br/blog/2017/celery-overview-archtecture-and-how-it-works/

Celery in the wild: tips and tricks to run async tasks in the real world : https://www.vinta.com.br/blog/2018/celery-wild-tips-and-tricks-run-async-tasks-real-world/

Dealing with resource-consuming (Time + Memory) tasks on Celery : https://www.vinta.com.br/blog/2018/dealing-resource-consuming-tasks-celery/

Celery tasks Checklist : https://devchecklists.com/celery-tasks-checklist/

How to Use Celery and RabbitMQ with Django : https://simpleisbetterthancomplex.com/tutorial/2017/08/20/how-to-use-celery-with-django.html

---------------------------------------------------------------------------------------------------------------------------------

<img src="https://miro.medium.com/max/810/1*t_oCyHBstMnF8WpZ67pKTg.jpeg">

<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--d28fU0gK--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/eduzmp4zt3898xz5dfia.jpeg" width="500px">

###### Python GIL - Global Interpreter Lock :
<img src="https://miro.medium.com/max/3400/1*FEQjLh2j-8nO-eOJdbxbuA.png" width="700px">

#### From : https://realpython.com/python-concurrency/
<table class="table table-hover">
<thead>
<tr>
<th>Concurrency Type</th>
<th>Switching Decision</th>
<th>Number of Processors</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pre-emptive multitasking (<code>threading</code>)</td>
<td>The operating system decides when to switch tasks external to Python.</td>
<td>1</td>
</tr>
<tr>
<td>Cooperative multitasking (<code>asyncio</code>)</td>
<td>The tasks decide when to give up control.</td>
<td>1</td>
</tr>
<tr>
<td>Multiprocessing (<code>multiprocessing</code>)</td>
<td>The processes all run at the same time on different processors.</td>
<td>Many</td>
</tr>
</tbody>
</table>

#### From https://leimao.github.io/blog/Python-Concurrency-High-Level/: 

<table class="tg">
<thead>
  <tr>
    <th class="tg-uzvj">Concurrency Type</th>
    <th class="tg-uzvj">Features</th>
    <th class="tg-uzvj">Use Criteria</th>
    <th class="tg-uzvj">Metaphor</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-9wq8">Multiprocessing</td>
    <td class="tg-9wq8">Multiple processes, high CPU utilization.</td>
    <td class="tg-9wq8">CPU-bound</td>
    <td class="tg-9wq8"><span style="font-weight:400;font-style:normal">We have ten kitchens, ten chefs, ten dishes to cook.</span></td>
  </tr>
  <tr>
    <td class="tg-9wq8">Threading</td>
    <td class="tg-9wq8">Single process, multiple threads, pre-emptive multitasking, OS decides task switching.</td>
    <td class="tg-9wq8">Fast I/O-bound</td>
    <td class="tg-9wq8"><span style="font-weight:400;font-style:normal">We have one kitchen, ten chefs, ten dishes to cook. The kitchen is crowded when the ten chefs are present together.</span></td>
  </tr>
  <tr>
    <td class="tg-9wq8">AsyncIO</td>
    <td class="tg-9wq8">Single process, single thread, cooperative multitasking, tasks cooperatively decide switching.</td>
    <td class="tg-9wq8">Slow I/O-bound</td>
    <td class="tg-9wq8"><span style="font-weight:400;font-style:normal">We have one kitchen, one chef, ten dishes to cook. </span></td>
  </tr>
</tbody>
</table>


From : https://www.vinta.com.br/blog/2017/celery-overview-archtecture-and-how-it-works/

<img src="https://vinta-cms.s3.amazonaws.com/media/filer_public/a4/fb/a4fbadbe-6846-4a25-863e-a040accdd69c/results_backend.jpg" width="600px">

<img src="https://miro.medium.com/max/2048/0*HvZk015GZdvL1tyv.png" width="700px">
