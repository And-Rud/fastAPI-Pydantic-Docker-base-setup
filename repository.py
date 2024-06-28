#using pattern repository that working with db how with collections of objects
from sqlalchemy import select
from database import TaskTable, new_session
from schemas import STaskAdd, STask


class TaskRepository():
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskTable(**task_dict)
            #add changes
            session.add(task)
            #send changes without transaction
            await session.flush()
            #send changes to db
            await session.commit()
            return  task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskTable)
            #executed query req to db
            result = await session.execute(query)
            task_model = result.scalars().all()
            task_schemas = [STask.model_validate(task.__dict__) for task in task_model]
            return task_schemas
