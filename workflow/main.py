"""
The executor is a set of tasks that download the necessary files and executes
some EasyModelAnalysis.jl code that was autogenerated.
"""

from prefect import flow


@flow
def execute_model():
    print("I do nothing!")