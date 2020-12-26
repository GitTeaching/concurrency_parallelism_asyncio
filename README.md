# concurrency_parallelism_asyncio
Multiprocessing, (multi)threading ,and asynchronous programming with asyncio.

#### Some readings :

Coroutines and tasks : https://docs.python.org/fr/3/library/asyncio-task.html

Python Asyncio: Basic Fundamentals : https://dev.to/v_it_aly/asyncio-basic-fundamentals-4i5m

Async programming in Python with asyncio : https://dev.to/welldone2094/async-programming-in-python-with-asyncio-12dl

Speed Up Your Python Program With Concurrency : https://realpython.com/python-concurrency/

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
