from extract import extract
from transform import transform
from load import load
from apscheduler.schedulers.blocking import BlockingScheduler

 
def run_pipeline():

    print("Running ETL...")

    data = extract()

    df = transform(data)

    load(df)

    print("Done")


if __name__ == "__main__":

    scheduler = BlockingScheduler()
    scheduler.add_job(run_pipeline, 'interval', minutes=5)

    print("Scheduler started...")

    scheduler.start()