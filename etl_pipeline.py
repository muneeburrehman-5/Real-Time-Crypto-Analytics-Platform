from extract import extract
from transform import transform
from load import load
from database import create_table


def run_pipeline():

    print("Running ETL...")

    create_table()

    data = extract()

    df = transform(data)

    load(df)

    print("Done")


if __name__ == "__main__":

    run_pipeline()