#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact
"""
import argparse
import logging
import wandb
import pandas as pd
import os

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    # artifact_local_path = run.use_artifact(args.input_artifact).file()
    logger.info("Downloading input artifact")
    artifact_local_path = run.use_artifact(args.input_artifact).file()
    df = pd.read_csv(artifact_local_path)
    # Drop outliers
    logger.info("Dropping outliers")
    idx = df['price'].between(args.min_price, args.max_price)
    df = df[idx].copy()
    # Convert last_review to datetime
    logger.info("Fixing formatting errors")
    df['last_review'] = pd.to_datetime(df['last_review'])
    # Save clean data
    logger.info("Saving clean data")
    filename = "clean_sample.csv"
    df.to_csv(filename, index=False)
    # Upload clean data file to W&B
    logger.info("Logging artifact")
    artifact = wandb.Artifact(
        name=args.output_artifact,
        type=args.output_type,
        description=args.output_description
    )
    artifact.add_file(filename)
    run.log_artifact(artifact)
    # Remove the local clean data file
    os.remove(filename)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A very basic data cleaning")


    parser.add_argument(
        "--input_artifact", 
        type=str,
        help="Name for the input artifact",
        required=True
    )

    parser.add_argument(
        "--output_artifact", 
        type=str,
        help="Name for the output artifact",
        required=True
    )

    parser.add_argument(
        "--output_type", 
        type=str,
        help="Type for the output",
        required=True
    )

    parser.add_argument(
        "--output_description", 
        type=str,
        help="Description for the output",
        required=True
    )

    parser.add_argument(
        "--min_price", 
        type=float,
        help="The minimum price",
        required=True
    )

    parser.add_argument(
        "--max_price", 
        type=float,
        help="The maximum price",
        required=True
    )


    args = parser.parse_args()

    go(args)
