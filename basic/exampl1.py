from prefect import task, Flow, Task, Parameter


@task
def say_hello():
    print("Hello, world!")


@task
def say_hi(name: str) -> None:
    print("Hi, {}!".format(name))


class AddTask(Task):

    def __init__(self, default: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = default

    def run(self, x: int, y: int = None) -> int:
        if y is None:
            y = self.default
        return x + y


# initialize the task instance
add = AddTask(default=1)

with Flow("My first flow!") as flow:
    task_name = Parameter('flow_name')
    say_hello()
    say_hi(task_name)
    first_result = add(1, y=2)
    second_result = add(x=first_result, y=100)

state = flow.run(flow_name="pengfei")

# parameter feature can map the workflow parameter to task parameter