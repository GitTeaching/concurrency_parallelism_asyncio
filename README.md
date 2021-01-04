# concurrency_parallelism_asyncio

Multiprocessing, (multi)threading ,and asynchronous programming with asyncio.

The basic types of concurrency available in Python:
- Threading
- Multiprocessing
- Asyncio

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

From : https://www.vinta.com.br/blog/2017/celery-overview-archtecture-and-how-it-works/

<img src="https://vinta-cms.s3.amazonaws.com/media/filer_public/a4/fb/a4fbadbe-6846-4a25-863e-a040accdd69c/results_backend.jpg" width="700px">

<img src="https://miro.medium.com/max/2048/0*HvZk015GZdvL1tyv.png" width="600px">
