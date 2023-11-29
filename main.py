from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from contextlib import asynccontextmanager
import uvicorn

counter = 1


def job_counter():
    global counter
    print('cron job: call you https requests here...')
    counter = counter + 1


@asynccontextmanager
async def lifespan(_: FastAPI):
    print('app started....')
    scheduler = BackgroundScheduler()
    scheduler.add_job(id="job1", func=job_counter, trigger='cron', second='*/2')
    scheduler.start()
    yield
    print('app stopped...')
    scheduler.shutdown(wait=False)


app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run("main:app")
