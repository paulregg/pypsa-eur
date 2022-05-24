#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 10:49:39 2022

@author: Paul
"""

import shutil

if __name__ == "__main__":
    if "snakemake" not in globals():
        from helper import mock_snakemake

        snakemake = mock_snakemake(
            "scale_load_data",
            simpl="",
            clusters=48,
        )

shutil.copy2(snakemake.input, snakemake.output)
