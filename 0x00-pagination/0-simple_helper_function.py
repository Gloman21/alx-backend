#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
     Function that calculates the start and end index of a page based on the
    page number and page size.

    :param page:
    :param page_size:
    :return:
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index