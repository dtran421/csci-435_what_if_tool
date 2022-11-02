"""
wit_code

What-if-tool Code. A Visual Tool for Understanding Machine Learning Models for Software Engineering
"""

__version__ = "0.0.4"
__author__ = 'WM-SEMERU'
__credits__ = 'College of William & Mary'


from .frontend.display import run_server


def WITCode(model: str = "gpt2", dataset: str = "", tokenizer: str = "gpt2") -> None:
    run_server(model, dataset, tokenizer)
